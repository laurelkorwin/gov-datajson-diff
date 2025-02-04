# Change History for epa.json (Part 38)

### Changes from 31606f9 to dd2190f (Part 28/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{05b8fc4d-1112-4002-a4ab-17c3350161a0}",
+            "issued": "2019-04-18",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -283114,46 +283133,46 @@
                 "Transportation",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{05b8fc4d-1112-4002-a4ab-17c3350161a0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 2975 block groups in the Washington, DC Metro region. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 2975 block groups in the Washington, DC Metro region. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ea617eb5-4ce8-4300-9849-a95131d0f3f4}",
+            "issued": "2019-05-17",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -283172,46 +283191,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-05-17",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Ecosystem Services by Block Group"
         },
-            "identifier": "{ea617eb5-4ce8-4300-9849-a95131d0f3f4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-05-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this commmunity, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this commmunity, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{369170cc-ab2e-4647-b04a-5338ea2536f1}",
+            "issued": "2019-06-10",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283227,46 +283246,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Land Cover by Block Group"
         },
-            "identifier": "{369170cc-ab2e-4647-b04a-5338ea2536f1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Washington DC EnviroAtlas Meter-scale Urban Land Cover (MULC) dataset comprises an area of 5423.43 km2 encompassing the entire area of Washington DC, and portions of the state of Maryland and state of Virginia. These MULC data and maps were derived from 1-m pixel, four-band (red, green, blue, and infrared light) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) as well as ancillary data (e.g., Lidar, National Wetlands Inventory [NWI], cropland, land parcels, power lines, building footprints). Eight land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Trees/Forest, Grass/Herbaceous, Agriculture, Woody Wetlands and Emergent Wetlands. Wetlands were delineated using the state wide wetlands data from National Wetlands Inventory (NWI) layer updated on October 15, 2018 (https://www.fws.gov/wetlands/Data/State-Downloads.html ). An analysis of 600 completely random and 111 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 85.4% and an overall fuzzy user's accuracy (RIGHT) of 91.5% within the census block group boundary (see confusion matrices below). These data were developed as part of the Chesapeake Bay High-Resolution Land Cover Project, a cooperative agreement between the Chesapeake Conservancy and the National Park Service, funded through an interagency agreement with the Environmental Protection Agency (EPA). The Chesapeake Conservancy, under the direction of Margaret Markham, created the initial statewide 1-meter land cover data. EPA added agriculture and wetlands taken from ancillary data sources. See detailed processing steps and workflow below. This dataset was produced by the Chesapeake Conservancy, the National Park Service, and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Washington DC -- Meter-Scale Urban Land Cover (MULC) Data (2013-2014)",
-            "description": "The Washington DC EnviroAtlas Meter-scale Urban Land Cover (MULC) dataset comprises an area of 5423.43 km2 encompassing the entire area of Washington DC, and portions of the state of Maryland and state of Virginia. These MULC data and maps were derived from 1-m pixel, four-band (red, green, blue, and infrared light) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) as well as ancillary data (e.g., Lidar, National Wetlands Inventory [NWI], cropland, land parcels, power lines, building footprints). Eight land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Trees/Forest, Grass/Herbaceous, Agriculture, Woody Wetlands and Emergent Wetlands. Wetlands were delineated using the state wide wetlands data from National Wetlands Inventory (NWI) layer updated on October 15, 2018 (https://www.fws.gov/wetlands/Data/State-Downloads.html ). An analysis of 600 completely random and 111 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 85.4% and an overall fuzzy user's accuracy (RIGHT) of 91.5% within the census block group boundary (see confusion matrices below). These data were developed as part of the Chesapeake Bay High-Resolution Land Cover Project, a cooperative agreement between the Chesapeake Conservancy and the National Park Service, funded through an interagency agreement with the Environmental Protection Agency (EPA). The Chesapeake Conservancy, under the direction of Margaret Markham, created the initial statewide 1-meter land cover data. EPA added agriculture and wetlands taken from ancillary data sources. See detailed processing steps and workflow below. This dataset was produced by the Chesapeake Conservancy, the National Park Service, and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6bb22dd7-3087-40b4-8969-a12a8bebe625}",
+            "issued": "2019-04-11",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -283293,46 +283312,46 @@
                 "Agriculture",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-11",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.9714930, 38.355362, -76.645805, 39.430352",
+            "temporal": "2013-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Washington DC -- Meter-Scale Urban Land Cover (MULC) Data (2013-2014)"
         },
-            "identifier": "{6bb22dd7-3087-40b4-8969-a12a8bebe625}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.9714930, 38.355362, -76.645805, 39.430352",
-            "temporal": "2013-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ebc3b294-81b0-4728-b6df-c31cbd5803c1}",
+            "issued": "2019-04-16",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -283350,46 +283369,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{ebc3b294-81b0-4728-b6df-c31cbd5803c1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{db8fc412-4fd9-441b-b937-3f105d7dd26b}",
+            "issued": "2019-04-16",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -283408,46 +283427,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{db8fc412-4fd9-441b-b937-3f105d7dd26b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{97502339-ee5e-4937-994a-1ae638481f2b}",
+            "issued": "2019-04-29",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -283462,46 +283481,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Park Access by Block Group"
         },
-            "identifier": "{97502339-ee5e-4937-994a-1ae638481f2b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{438426b8-1ff5-4c75-9d09-4be8645d4229}",
+            "issued": "2019-04-29",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -283515,46 +283534,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Proximity to Parks"
         },
-            "identifier": "{438426b8-1ff5-4c75-9d09-4be8645d4229}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1f3b92dd-ff2b-48fd-b8f4-782f97009fba}",
+            "issued": "2019-04-18",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -283572,46 +283591,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{1f3b92dd-ff2b-48fd-b8f4-782f97009fba}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b266040b-0b4e-4bf8-87e4-e5cda3f272b7}",
+            "issued": "2019-04-18",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -283629,46 +283648,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{b266040b-0b4e-4bf8-87e4-e5cda3f272b7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1afa2a39-6a58-4788-af4a-48d30c0ba9ab}",
+            "issued": "2019-04-10",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283688,46 +283707,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{1afa2a39-6a58-4788-af4a-48d30c0ba9ab}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{249f594d-68ec-44a7-87ca-fd32731470d6}",
+            "issued": "2019-04-10",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283747,46 +283766,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{249f594d-68ec-44a7-87ca-fd32731470d6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{195b598c-4176-4bba-89cc-25f7ad1e7ad8}",
+            "issued": "2019-04-16",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283806,46 +283825,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{195b598c-4176-4bba-89cc-25f7ad1e7ad8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3894f10b-3f41-4df8-870a-719beb83030d}",
+            "issued": "2019-04-10",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283865,46 +283884,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{3894f10b-3f41-4df8-870a-719beb83030d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7c563b9c-9efa-4fae-aa70-d3679dfc81ca}",
+            "issued": "2019-04-10",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283925,46 +283944,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{7c563b9c-9efa-4fae-aa70-d3679dfc81ca}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c465704f-18a2-4268-94b1-798d10eb2efa}",
+            "issued": "2019-04-16",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -283982,46 +284001,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{c465704f-18a2-4268-94b1-798d10eb2efa}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e7a1aab9-567f-4dc6-9fe9-9c1cc0da8ade}",
+            "issued": "2019-04-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284037,46 +284056,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{e7a1aab9-567f-4dc6-9fe9-9c1cc0da8ade}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains Land Cover data by Wetness Index for each Watershed Boundary Dataset (WBD) 12-Digit Hydrologic Unit Code (HUC-12) of the conterminous United States, based on the National Land Cover Database (NLCD) from 2011, the December 30, 2009 Soil Survey Geographic (SSURGO) Database, and the USDA's Cropland Data Layer (CDL) data from 2011. The dataset includes the percentages of each HUC-12 belonging to several land cover groups that are on land with a Wetness Index greater than 550 (WET550). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Land Cover in Areas of High Water Accumulation in 2011 for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains Land Cover data by Wetness Index for each Watershed Boundary Dataset (WBD) 12-Digit Hydrologic Unit Code (HUC-12) of the conterminous United States, based on the National Land Cover Database (NLCD) from 2011, the December 30, 2009 Soil Survey Geographic (SSURGO) Database, and the USDA's Cropland Data Layer (CDL) data from 2011. The dataset includes the percentages of each HUC-12 belonging to several land cover groups that are on land with a Wetness Index greater than 550 (WET550). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{012F301F-3DE4-4195-BB53-AFA5215B7F59}",
+            "issued": "2017-05-05",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -284142,46 +284161,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-05-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2006-01-01/2006-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Land Cover in Areas of High Water Accumulation in 2011 for the Conterminous United States"
         },
-            "identifier": "{012F301F-3DE4-4195-BB53-AFA5215B7F59}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2006-01-01/2006-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-05-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1 block group in Woodbine, Iowa. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1 block group in Woodbine, Iowa. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B80563B5-28CD-49F8-A3A5-1F99FC6CC5D1}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -284201,46 +284220,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-10-26",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - BenMAP Results by Block Group"
         },
-            "identifier": "{B80563B5-28CD-49F8-A3A5-1F99FC6CC5D1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Woodbine, IA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Woodbine, IA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B77B0C12-7ED7-42E5-8242-80BE0118D556}",
+            "issued": "2014-07-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284253,46 +284272,46 @@
                 "Environmental Atlas",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Block Groups"
         },
-            "identifier": "{B77B0C12-7ED7-42E5-8242-80BE0118D556}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-04-30/2014-04-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3F96AA99-82AA-4009-AE9B-E9C3D8848FC8}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -284309,46 +284328,46 @@
                 "Boundaries",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-31",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Woodbine, IA - Demographics by Block Group"
         },
-            "identifier": "{3F96AA99-82AA-4009-AE9B-E9C3D8848FC8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-31",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Woodbine, IA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Woodbine, IA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0F97C852-2BD1-4BC7-8B8F-24F2E550142E}",
+            "issued": "2014-05-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284361,46 +284380,46 @@
                 "Boundaries",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2013-04-30/2013-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Atlas Area Boundary"
         },
-            "identifier": "{0F97C852-2BD1-4BC7-8B8F-24F2E550142E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2013-04-30/2013-04-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-05-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/research/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/research/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5F3D2255-6EC8-437A-9DA5-82025680ED34}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -284415,46 +284434,46 @@
                 "Environmental Atlas",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{5F3D2255-6EC8-437A-9DA5-82025680ED34}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2015-03-24/2015-03-24",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Water use in the EnviroAtlas-defined study area is estimated at 64 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Water use in the EnviroAtlas-defined study area is estimated at 64 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{71AC4E10-EF6E-4361-A639-457F935A7B86}",
+            "issued": "2014-10-28",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -284474,46 +284493,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-28",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{71AC4E10-EF6E-4361-A639-457F935A7B86}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-10-28",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{309723EA-AE33-4E78-A9E5-E7BE548DB8B8}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -284529,46 +284548,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-04",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{309723EA-AE33-4E78-A9E5-E7BE548DB8B8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{810a1616-3c48-4780-bd69-a1f7b7baec14}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -284592,46 +284611,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-07-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.7416, 41.71539, -95.6722, 41.78347",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{810a1616-3c48-4780-bd69-a1f7b7baec14}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.7416, 41.71539, -95.6722, 41.78347",
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-07-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, and Agriculture. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, and Agriculture. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{49097AF8-2E87-4A0A-BA54-BEC1D8CB7AD1}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284646,46 +284665,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2015-03-20/2015-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Greenspace Proximity Gradient"
         },
-            "identifier": "{49097AF8-2E87-4A0A-BA54-BEC1D8CB7AD1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2015-03-20/2015-03-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F691D4AD-6BDA-496A-9D6F-87DCBA6242B1}",
+            "issued": "2014-09-16",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284701,46 +284720,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-09-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Historic Places by Census Block Group"
         },
-            "identifier": "{F691D4AD-6BDA-496A-9D6F-87DCBA6242B1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-09-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{33B9ED81-B266-4278-A608-33557AEA8A23}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -284754,46 +284773,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2015-03-25/2015-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Impervious Proximity Gradient"
         },
-            "identifier": "{33B9ED81-B266-4278-A608-33557AEA8A23}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2015-03-25/2015-03-25",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4E7173AD-5D8E-426A-9431-67FE34833523}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -284808,46 +284827,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.73864, 41.71377, -95.67509, 41.78499",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{4E7173AD-5D8E-426A-9431-67FE34833523}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.73864, 41.71377, -95.67509, 41.78499",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1 block group in Woodbine, Iowa. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for this block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1 block group in Woodbine, Iowa. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for this block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{65C2EF79-BEDB-4021-8D93-BD162E06FF7A}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -284866,46 +284885,46 @@
                 "Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Ecosystem Services by Block Group"
         },
-            "identifier": "{65C2EF79-BEDB-4021-8D93-BD162E06FF7A}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6A323828-C19B-4D2C-848D-2636825B1744}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -284922,46 +284941,46 @@
                 "Environmental Atlas",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-31",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Land Cover by Block Group"
         },
-            "identifier": "{6A323828-C19B-4D2C-848D-2636825B1744}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The EnviroAtlas Woodbine, IA Meter-Scale Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from Late Summer 2011 at 1 m spatial resolution. Six land cover classes were mapped: water, impervious surfaces (dark and light), soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment using a completely random sampling of 600 samples yielded an overall user's accuracy (MAX) of 87.03% and an overall fuzzy user's accuracy (RIGHT) of 90.23% using a minimum mapping unit of 9 pixels (3x3 pixel window). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Woodbine. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Woodbine, IA -- Meter-Scale Urban Land Cover (MULC) Data (2011)",
-            "description": "The EnviroAtlas Woodbine, IA Meter-Scale Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from Late Summer 2011 at 1 m spatial resolution. Six land cover classes were mapped: water, impervious surfaces (dark and light), soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment using a completely random sampling of 600 samples yielded an overall user's accuracy (MAX) of 87.03% and an overall fuzzy user's accuracy (RIGHT) of 90.23% using a minimum mapping unit of 9 pixels (3x3 pixel window). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Woodbine. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F5ED8E1B-8772-4082-A38B-89810D7C7BA3}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -284984,46 +285003,46 @@
                 "Iowa",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-88.473227, 30.144425, -84.888246, 35.008028",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Woodbine, IA -- Meter-Scale Urban Land Cover (MULC) Data (2011)"
         },
-            "identifier": "{F5ED8E1B-8772-4082-A38B-89810D7C7BA3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.473227, 30.144425, -84.888246, 35.008028",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{79DDF0BC-FBA4-4DA8-9CA8-BE6158C41F86}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -285041,46 +285060,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Near Road Tree Buffer"
         },
-            "identifier": "{79DDF0BC-FBA4-4DA8-9CA8-BE6158C41F86}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1A94C72E-9AF7-42BC-B739-DD72BCF6476C}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -285100,46 +285119,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Near Road Block Group Summary"
         },
-            "identifier": "{1A94C72E-9AF7-42BC-B739-DD72BCF6476C}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3DE7818E-F39B-4DB4-B24B-70D7FEC46723}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -285154,46 +285173,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Park Access by Block Group"
         },
-            "identifier": "{3DE7818E-F39B-4DB4-B24B-70D7FEC46723}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2015-10-01/2015-10-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{667D6539-13C6-45A2-BD5B-80108BAA5213}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Woodbine",
                 "Ecosystem Services",
@@ -285207,46 +285226,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Proximity to Parks"
         },
-            "identifier": "{667D6539-13C6-45A2-BD5B-80108BAA5213}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-08-20/2014-08-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-01-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{004E8C87-72EB-4A62-8AD3-333BCD795656}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -285264,46 +285283,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{004E8C87-72EB-4A62-8AD3-333BCD795656}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-02",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2F091ED2-8A69-47AA-82B5-75A5A4FFABE4}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -285321,46 +285340,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-08-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{2F091ED2-8A69-47AA-82B5-75A5A4FFABE4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-08-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7336D0A4-C8A4-4EF5-B3CD-EC94226E8B2E}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285380,46 +285399,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{7336D0A4-C8A4-4EF5-B3CD-EC94226E8B2E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A3B80653-E19F-45E8-94CE-C5B8861586DA}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285439,46 +285458,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-04",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{A3B80653-E19F-45E8-94CE-C5B8861586DA}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CAB72188-28B8-46FC-B476-BEB10AD62571}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285498,46 +285517,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{CAB72188-28B8-46FC-B476-BEB10AD62571}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{82528C2A-1E86-4BB4-B18D-CB15FEBF3AF6}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285557,46 +285576,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-04",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{82528C2A-1E86-4BB4-B18D-CB15FEBF3AF6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ABB74299-424B-428A-9DCA-016278A632DA}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285617,46 +285636,46 @@
                 "Drinking Water",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-31",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-05-02/2014-05-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{ABB74299-424B-428A-9DCA-016278A632DA}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-05-02/2014-05-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1F599CEC-5D47-4BDF-938A-317B2533E85F}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -285674,46 +285693,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-31",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
+            "temporal": "2014-06-20/2014-06-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{1F599CEC-5D47-4BDF-938A-317B2533E85F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71539, -95.67220, 41.78347",
-            "temporal": "2014-06-20/2014-06-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Woodbine, IA - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5629722b-a45c-43af-bd95-949ac32a69bc}",
+            "issued": "2017-05-31",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -285729,46 +285748,46 @@
                 "Human Well-being",
                 "Woodbine, IA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-05-31",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-95.74160, 41.71534, -95.67220, 41.78342",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Woodbine, IA - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{5629722b-a45c-43af-bd95-949ac32a69bc}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-95.74160, 41.71534, -95.67220, 41.78342",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-05-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the annual average potential wind energy resource in kilowatt hours per square meter per day for each 12-digit Hydrologic Unit (HUC). It was produced using data from the National Renewable Energy Laboratory (NREL). These estimates represent wind resources at a 10 meter height above surface. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WoodbineIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Annual average potential wind energy resource by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset shows the annual average potential wind energy resource in kilowatt hours per square meter per day for each 12-digit Hydrologic Unit (HUC). It was produced using data from the National Renewable Energy Laboratory (NREL). These estimates represent wind resources at a 10 meter height above surface. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7717f3ed-6ab2-4465-b36b-03040c1f2eaf}",
+            "issued": "2016-06-13",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -285830,46 +285849,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2001-01-01/2001-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Annual average potential wind energy resource by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{7717f3ed-6ab2-4465-b36b-03040c1f2eaf}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2001-01-01/2001-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-06-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Hydrologically Connected Zone (HCZ) Mask was determined using grid analysis to combine surface water features in the United States from three datasets: First, the surface water features from the 2011 CDL-NLCD. The CDL-NLCD, which was developed by the EnviroAtlas team, is a hybrid of the 2011 CDL produced by the National Agricultural Statistics Service (NASS) and the 2011 NLCD produced by the Multi-Resolution Land Characteristics Consortium. Features included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95). Second, the flowline and waterbody features as represented in the catseed grid from the National Hydrography Dataset (NHD) Plus version 2.1, downloaded June 18, 2013. Third, all areas contiguous to surface water that also have a wetness index value of 550 or greater. The wetness index, also known as the compound topographic index (CTI), is a steady state wetness index. It is commonly used to quantify topographic control on hydrological processes. The combination of these three datasets represents the Hydrologically Connected Zone. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/National/ConterminousUS/",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Watershed Index Online Hydrologically Connected Zone Mask for the Conterminous United States",
-            "description": "The Hydrologically Connected Zone (HCZ) Mask was determined using grid analysis to combine surface water features in the United States from three datasets: First, the surface water features from the 2011 CDL-NLCD. The CDL-NLCD, which was developed by the EnviroAtlas team, is a hybrid of the 2011 CDL produced by the National Agricultural Statistics Service (NASS) and the 2011 NLCD produced by the Multi-Resolution Land Characteristics Consortium. Features included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95). Second, the flowline and waterbody features as represented in the catseed grid from the National Hydrography Dataset (NHD) Plus version 2.1, downloaded June 18, 2013. Third, all areas contiguous to surface water that also have a wetness index value of 550 or greater. The wetness index, also known as the compound topographic index (CTI), is a steady state wetness index. It is commonly used to quantify topographic control on hydrological processes. The combination of these three datasets represents the Hydrologically Connected Zone. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cc8c85ea-1944-40f8-8513-ce7ad82fe4a7}",
+            "issued": "2016-11-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -285934,46 +285953,48 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-11-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Watershed Index Online Hydrologically Connected Zone Mask for the Conterminous United States"
         },
-            "identifier": "{cc8c85ea-1944-40f8-8513-ce7ad82fe4a7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains information about 303(d) impairments by 12-digit HUC. It uses data that was originally compiled for the Watershed Index Online (WSIO) Version 2.4, released August 31, 2022. \n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).\t\t",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/National/ConterminousUS/",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://www.epa.gov/wsio/wsio-indicator-data-library"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Watershed Index Online (WSIO) Indicator Data Tables - Impaired Waters by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about 303(d) impairments by 12-digit HUC. It uses data that was originally compiled for the Watershed Index Online (WSIO) Version 2.4, released August 31, 2022. \n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).\t\t",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "DD6EC4E5-6435-47B7-A6D1-2FD38431C875",
+            "issued": "2023-08-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286035,46 +286056,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-08-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment (CPHEA), EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-128.007244, 22.868654, -65.25485, 51.64959",
+            "temporal": "2022-08-31T00:00:00/2022-08-31T00:00:00",
+            "title": "EnviroAtlas - Watershed Index Online (WSIO) Indicator Data Tables - Impaired Waters by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "DD6EC4E5-6435-47B7-A6D1-2FD38431C875",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-128.007244, 22.868654, -65.25485, 51.64959",
-            "temporal": "2022-08-31T00:00:00/2022-08-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2023-08-30",
+            "description": "The Riparian Zone Mask represents surface water in the United States and its estimated riparian zone. These areas were determined using grid analysis of an approximate 100 meter buffer placed around the combined surface water features of the Cropland Data Layer-National Land Cover Dataset 2011 (CDL-NLCD) and the 1:100,000 scale National Hydrography Dataset (NHD) Plus version 2. Features from CDL-NLCD included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95). The combination of these two datasets and all cells with a distance of 108 meters or less from surface water are included in the Riparian Zone (RZ). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/wsio/wsio-indicator-data-library"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/National/ConterminousUS/",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Watershed Index Online Riparian Zone Mask for the Conterminous United States",
-            "description": "The Riparian Zone Mask represents surface water in the United States and its estimated riparian zone. These areas were determined using grid analysis of an approximate 100 meter buffer placed around the combined surface water features of the Cropland Data Layer-National Land Cover Dataset 2011 (CDL-NLCD) and the 1:100,000 scale National Hydrography Dataset (NHD) Plus version 2. Features from CDL-NLCD included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95). The combination of these two datasets and all cells with a distance of 108 meters or less from surface water are included in the Riparian Zone (RZ). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6b37a605-0e72-48be-915e-7f9d09fb9ff2}",
+            "issued": "2016-11-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286139,46 +286158,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-11-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Watershed Index Online Riparian Zone Mask for the Conterminous United States"
         },
-            "identifier": "{6b37a605-0e72-48be-915e-7f9d09fb9ff2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This data layer represents all surface water features in the United States. This grid was created by combining water features identified in two sources, the Cropland Data Layer-National Land Cover Database (CDL-NLCD), and the National Hydrography Dataset (NHD Plus version 2.1). First, the surface water features were extracted from the 2011 CDL-NLCD. The CDL-NLCD, which was developed by the EnviroAtlas team, is a hybrid of the 2011 CDL produced by the National Agricultural Statistics Service (NASS) and the 2011 NLCD produced by the Multi-Resolution Land Characteristics Consortium. Features included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95).The second source used was the flowline and waterbody features as represented in the catseed grid from the NHD Plus version 2.1, downloaded June 18, 2013. The combination of these two datasets represents surface water and is referred to as the 'Water Mask.' This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/National/ConterminousUS/",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Watershed Index Online Water Mask for the Conterminous United States",
-            "description": "This data layer represents all surface water features in the United States. This grid was created by combining water features identified in two sources, the Cropland Data Layer-National Land Cover Database (CDL-NLCD), and the National Hydrography Dataset (NHD Plus version 2.1). First, the surface water features were extracted from the 2011 CDL-NLCD. The CDL-NLCD, which was developed by the EnviroAtlas team, is a hybrid of the 2011 CDL produced by the National Agricultural Statistics Service (NASS) and the 2011 NLCD produced by the Multi-Resolution Land Characteristics Consortium. Features included are 'Open Water' (code 11), 'Woody Wetlands' (code 90) and 'Emergent Herbaceous Wetlands' (code 95).The second source used was the flowline and waterbody features as represented in the catseed grid from the NHD Plus version 2.1, downloaded June 18, 2013. The combination of these two datasets represents surface water and is referred to as the 'Water Mask.' This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas and the Watershed Index Online (WSIO). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4651b523-0d9f-4165-adb7-7e82c64e384d}",
+            "issued": "2016-11-18",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286243,46 +286262,43 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-11-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Watershed Index Online Water Mask for the Conterminous United States"
         },
-            "identifier": "{4651b523-0d9f-4165-adb7-7e82c64e384d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-11-18",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danelle Lobdell",
+                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            },
+            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized Environmental Quality Index (EQI), and an index for each of the associated domains (air, water, land, built environment, and sociodemographic environment). Indices are at the county level for all counties in the United States. Indices are at the county level for all counties in the United States for 2000-2005.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/National/ConterminousUS/",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/NHEERL/EQI"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "USEPA Environmental Quality Index (EQI) and Associated Domain Indices by County for the United States 2000-2005 Original",
-            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized Environmental Quality Index (EQI), and an index for each of the associated domains (air, water, land, built environment, and sociodemographic environment). Indices are at the county level for all counties in the United States. Indices are at the county level for all counties in the United States for 2000-2005.",
+            ],
+            "identifier": "53AE6A65-E2C4-4B84-B012-66BC473F5C04",
+            "issued": "2016-06-22",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286347,41 +286363,41 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Danelle Lobdell",
-                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2000-01-01T00:00:00/2005-12-31T00:00:00",
+            "title": "USEPA Environmental Quality Index (EQI) and Associated Domain Indices by County for the United States 2000-2005 Original"
         },
-            "identifier": "53AE6A65-E2C4-4B84-B012-66BC473F5C04",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2000-01-01T00:00:00/2005-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-22",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danelle Lobdell",
+                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            },
+            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized non-transformed variables chosen to represent the Air, Water, Land, Built, and Sociodemographic Domains of the total environment. This does not represent the final variables for the EQI. The Transformed dataset was used to create the EQI. This dataset is for information purposes only for those who want to see the original non-transformed variables.Six criteria air pollutants and 81 hazardous air pollutants are included in this dataset. Data sources are the EPA's Air Quality system (https://www.epa.gov/ttn/airs/airsaqs/) and the National-scale Air Toxics Assessment (https://www.epa.gov/nata/). Variables are average pollutant concentrations or emissions for 2000-2005 at the county level for all counties in the United States. Data on water impairment, waste permits, beach closures, domestic water source, deposition for 9 pollutants, drought status, and 60 chemical contaminants. Data sources are the EPA's WATERS (Watershed Assessment, Tracking and Environmental ResultS) Database (https://www.epa.gov/waters/), the U.S. Geological Survey Estimates of Water Use in the U.S. for 2000 and 2005 (https://water.usgs.gov/watuse/), the National Atmospheric Deposition Program (http://nadp.sws.uiuc.edu/), the U.S. Drought Monitor Data (http://droughtmonitor.unl.edu/), and the EPA's National Contaminant Occurrence Database (https://water.epa.gov/scitech/datait/databases/drink/ncod/databases-index.cfm). Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States. Data represents traffic safety, public transportation, road type, the business environment and public housing. Data sources are the Dun and Bradstreet North American Industry Classification System (NAICS) codes; Topologically Integrated Geographic Encoding and Referencing (TIGER); Fatality Annual Reporting System (FARS); and Housing and Urban Development (HUD) data. This dataset contains the finalized variables chosen to represent the sociodemographic domain of the total environment. Data represents socioeconomic and crime conditions. Data sources are the United States Census and the Federal Bureau of Investigation Uniform Crime Reports. Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/NHEERL/EQI"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "USEPA Environmental Quality Index (EQI) - Air, Water, Land, Built, and Sociodemographic Domains Non-Transformed Variables Dataset as Input for the 2000-2005 USEPA EQI, by County for the United States",
-            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized non-transformed variables chosen to represent the Air, Water, Land, Built, and Sociodemographic Domains of the total environment. This does not represent the final variables for the EQI. The Transformed dataset was used to create the EQI. This dataset is for information purposes only for those who want to see the original non-transformed variables.Six criteria air pollutants and 81 hazardous air pollutants are included in this dataset. Data sources are the EPA's Air Quality system (https://www.epa.gov/ttn/airs/airsaqs/) and the National-scale Air Toxics Assessment (https://www.epa.gov/nata/). Variables are average pollutant concentrations or emissions for 2000-2005 at the county level for all counties in the United States. Data on water impairment, waste permits, beach closures, domestic water source, deposition for 9 pollutants, drought status, and 60 chemical contaminants. Data sources are the EPA's WATERS (Watershed Assessment, Tracking and Environmental ResultS) Database (https://www.epa.gov/waters/), the U.S. Geological Survey Estimates of Water Use in the U.S. for 2000 and 2005 (https://water.usgs.gov/watuse/), the National Atmospheric Deposition Program (http://nadp.sws.uiuc.edu/), the U.S. Drought Monitor Data (http://droughtmonitor.unl.edu/), and the EPA's National Contaminant Occurrence Database (https://water.epa.gov/scitech/datait/databases/drink/ncod/databases-index.cfm). Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States. Data represents traffic safety, public transportation, road type, the business environment and public housing. Data sources are the Dun and Bradstreet North American Industry Classification System (NAICS) codes; Topologically Integrated Geographic Encoding and Referencing (TIGER); Fatality Annual Reporting System (FARS); and Housing and Urban Development (HUD) data. This dataset contains the finalized variables chosen to represent the sociodemographic domain of the total environment. Data represents socioeconomic and crime conditions. Data sources are the United States Census and the Federal Bureau of Investigation Uniform Crime Reports. Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States.",
+            ],
+            "identifier": "6C622625-F820-47AA-9838-C4762AA1B916",
+            "issued": "2013-05-21",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286447,41 +286463,41 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Danelle Lobdell",
-                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2000-01-01T00:00:00/2005-12-31T00:00:00",
+            "title": "USEPA Environmental Quality Index (EQI) - Air, Water, Land, Built, and Sociodemographic Domains Non-Transformed Variables Dataset as Input for the 2000-2005 USEPA EQI, by County for the United States"
         },
-            "identifier": "6C622625-F820-47AA-9838-C4762AA1B916",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2000-01-01T00:00:00/2005-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2013-05-21",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danelle Lobdell",
+                "hasEmail": "mailto:lobdell.danelle@epa.gov"
+            },
+            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized transformed variables chosen to represent the Air, Water, Land, Built, and Sociodemographic Domains of the total environment.Six criteria air pollutants and 81 hazardous air pollutants are included in this dataset. Data sources are the EPA's Air Quality system (https://www.epa.gov/ttn/airs/airsaqs/) and the National-scale Air Toxics Assessment (https://www.epa.gov/nata/). Variables are average pollutant concentrations or emissions for 2000-2005 at the county level for all counties in the United States. Data on water impairment, waste permits, beach closures, domestic water source, deposition for 9 pollutants, drought status, and 60 chemical contaminants. Data sources are the EPA's WATERS (Watershed Assessment, Tracking and Environmental ResultS) Database (https://www.epa.gov/waters/), the U.S. Geological Survey Estimates of Water Use in the U.S. for 2000 and 2005 (https://water.usgs.gov/watuse/), the National Atmospheric Deposition Program (http://nadp.sws.uiuc.edu/), the U.S. Drought Monitor Data (http://droughtmonitor.unl.edu/), and the EPA's National Contaminant Occurrence Database (https://water.epa.gov/scitech/datait/databases/drink/ncod/databases-index.cfm). Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States. Data represents traffic safety, public transportation, road type, the business environment and public housing. Data sources are the Dun and Bradstreet North American Industry Classification System (NAICS) codes; Topologically Integrated Geographic Encoding and Referencing (TIGER); Fatality Annual Reporting System (FARS); and Housing and Urban Development (HUD) data. This dataset contains the finalized variables chosen to represent the sociodemographic domain of the total environment. Data represents socioeconomic and crime conditions. Data sources are the United States Census and the Federal Bureau of Investigation Uniform Crime Reports. Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/NHEERL/EQI"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "USEPA Environmental Quality Index (EQI) - Air, Water, Land, Built, and Sociodemographic Domains Transformed Variables Dataset as Input for the 2000-2005 USEPA EQI, by County for the United States",
-            "description": "The US Environmental Protection Agency's (EPA) National Health and Environmental Effects Research Laboratory (NHEERL) in the Environmental Public Health Division (EPHD) is currently engaged in research aimed at developing a measure that estimates overall environmental quality at the county level for the United States. This work is being conducted as an effort to learn more about how various environmental factors simultaneously contribute to health disparities in low-income and minority populations, and to better estimate the total environmental and social context to which humans are exposed. This dataset contains the finalized transformed variables chosen to represent the Air, Water, Land, Built, and Sociodemographic Domains of the total environment.Six criteria air pollutants and 81 hazardous air pollutants are included in this dataset. Data sources are the EPA's Air Quality system (https://www.epa.gov/ttn/airs/airsaqs/) and the National-scale Air Toxics Assessment (https://www.epa.gov/nata/). Variables are average pollutant concentrations or emissions for 2000-2005 at the county level for all counties in the United States. Data on water impairment, waste permits, beach closures, domestic water source, deposition for 9 pollutants, drought status, and 60 chemical contaminants. Data sources are the EPA's WATERS (Watershed Assessment, Tracking and Environmental ResultS) Database (https://www.epa.gov/waters/), the U.S. Geological Survey Estimates of Water Use in the U.S. for 2000 and 2005 (https://water.usgs.gov/watuse/), the National Atmospheric Deposition Program (http://nadp.sws.uiuc.edu/), the U.S. Drought Monitor Data (http://droughtmonitor.unl.edu/), and the EPA's National Contaminant Occurrence Database (https://water.epa.gov/scitech/datait/databases/drink/ncod/databases-index.cfm). Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States. Data represents traffic safety, public transportation, road type, the business environment and public housing. Data sources are the Dun and Bradstreet North American Industry Classification System (NAICS) codes; Topologically Integrated Geographic Encoding and Referencing (TIGER); Fatality Annual Reporting System (FARS); and Housing and Urban Development (HUD) data. This dataset contains the finalized variables chosen to represent the sociodemographic domain of the total environment. Data represents socioeconomic and crime conditions. Data sources are the United States Census and the Federal Bureau of Investigation Uniform Crime Reports. Variables are calculated for the time period from 2000-2005 at the county level for all counties in the United States.",
+            ],
+            "identifier": "7F1AAA3A-4950-490B-B809-EB49F77D55DB",
+            "issued": "2013-05-21",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286547,41 +286563,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Danelle Lobdell",
-                "hasEmail": "mailto:lobdell.danelle@epa.gov"
-            },
-            "identifier": "7F1AAA3A-4950-490B-B809-EB49F77D55DB",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2000-01-01T00:00:00/2005-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2013-05-21",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/NHEERL/EQI"
-                }
-            ]
+            "title": "USEPA Environmental Quality Index (EQI) - Air, Water, Land, Built, and Sociodemographic Domains Transformed Variables Dataset as Input for the 2000-2005 USEPA EQI, by County for the United States"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_CERCLIS",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to the Comprehensive Environmental Response, Compensation, and Liability Information System (CERCLIS) non-NPL sites. Superfund is a program administered by the EPA to locate, investigate, and clean up the worst hazardous waste sites throughout the United States. Before Superfund, Americans were less aware of how dumping chemical wastes might affect public health and the environment. Hazardous wastes were often left in the open, where they seeped into the ground, flowed into rivers and lakes, and contaminated soil and groundwater. Consequently, where these practices were intensive or continuous, there were uncontrolled or abandoned hazardous waste sites. These sites include abandoned warehouses, manufacturing facilities, processing plants, and landfills. Citizen concern about the extent of this problem prompted Congress in 1980 to establish the Superfund Program to eliminate the health and environmental threats posed by hazardous waste sites. EPA administers the Superfund program in cooperation with individual states and tribal governmentsFRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to CERCLIS non-NPL facilities once the CERCLIS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{06B40E9D-A0F0-4A3A-AEBD-BD700142B343}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286655,36 +286666,36 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{06B40E9D-A0F0-4A3A-AEBD-BD700142B343}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_CERCLIS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_CHEMICALS",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith PE PLS",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
+            "distribution": [],
+            "identifier": "{63A40686-4333-4851-A227-3ED77D3BC6BC}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Permits",
                 "Puerto Rico",
@@ -286704,36 +286715,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information, Office of Information Collection"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David G. Smith PE PLS",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{63A40686-4333-4851-A227-3ED77D3BC6BC}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_CHEMICALS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_CONTACTS",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith PE PLS",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
+            "distribution": [],
+            "identifier": "{65DCD2EA-2456-4DE3-922D-653AF327631E}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Permits",
                 "Puerto Rico",
@@ -286753,36 +286764,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information, Office of Information Collection"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David G. Smith PE PLS",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{65DCD2EA-2456-4DE3-922D-653AF327631E}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_CONTACTS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_FRP",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This dataset contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to Facility Response Plan (FRP) in the Oil database. These facilities are subject to the requirements to prevent and respond to oil spills. FRP facilities are referred to as substantial harm facilities due to the quantities of oil stored and facility characteristics. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to Oil FRP facilities once the Oil data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{A7068618-9332-489C-9B1D-22070ECF90B1}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -286856,44 +286867,44 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{A7068618-9332-489C-9B1D-22070ECF90B1}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_FRP"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_NAICS",
-            "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
-            "keyword": [
-                "Permits",
-                "Puerto Rico",
-                "Air",
-                "Compliance",
-                "Environment",
-                "Virgin Islands",
-                "ESF3",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith PE PLS",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
+            "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
+            "distribution": [],
+            "identifier": "{F55608E8-3CDE-41AE-AC77-1ED1C914F5A2}",
+            "issued": "2016-06-29",
+            "keyword": [
+                "Permits",
+                "Puerto Rico",
+                "Air",
+                "Compliance",
+                "Environment",
+                "Virgin Islands",
+                "ESF3",
                 "Washington DC",
                 "Cleanup",
                 "American Samoa",
@@ -286905,36 +286916,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information, Office of Information Collection"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David G. Smith PE PLS",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{F55608E8-3CDE-41AE-AC77-1ED1C914F5A2}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_NAICS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_RCRATSD",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to the Risk Management Plan (RMP) database. RMP stores the risk management plans reported by companies that handle, manufacture, use, or store certain flammable or toxic substances, as required under section 112(r) of the Clean Air Act (CAA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RMP facilities once the RMP data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{2A6E0E49-4523-4E26-A2BF-D5DDADE44B86}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287008,36 +287019,36 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{2A6E0E49-4523-4E26-A2BF-D5DDADE44B86}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_RCRATSD"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_RMP",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to the Risk Management Plan (RMP) database. RMP stores the risk management plans reported by companies that handle, manufacture, use, or store certain flammable or toxic substances, as required under section 112(r) of the Clean Air Act (CAA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RMP facilities once the RMP data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{53BA24E6-BED1-4B47-88DF-C2565E6B052B}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287111,36 +287122,36 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{53BA24E6-BED1-4B47-88DF-C2565E6B052B}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_RMP"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_SIC",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith PE PLS",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
+            "distribution": [],
+            "identifier": "{E6F93D2C-28C6-4B52-B748-89E8BDC90D27}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Permits",
                 "Puerto Rico",
@@ -287160,36 +287171,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information, Office of Information Collection"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David G. Smith PE PLS",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{E6F93D2C-28C6-4B52-B748-89E8BDC90D27}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_SIC"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_STATE_ID",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith PE PLS",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "To improve public health and the environment, the United States Environmental Protection Agency (USEPA) collects information about facilities, sites, or places subject to environmental regulation or of environmental interest.",
+            "distribution": [],
+            "identifier": "{C0DF0FC5-AD75-4DED-936A-D162F8E46B76}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Permits",
                 "Puerto Rico",
@@ -287209,36 +287220,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information, Office of Information Collection"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David G. Smith PE PLS",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{C0DF0FC5-AD75-4DED-936A-D162F8E46B76}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_STATE_ID"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_TRI",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to the Toxic Release Inventory (TRI) System. TRI is a publicly available EPA database reported annually by certain covered industry groups, as well as federal facilities. It contains information about more than 650 toxic chemicals that are being used, manufactured, treated, transported, or released into the environment, and includes information about waste management and pollution prevention activities. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TRI facilities once the TRI data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{AF7F710A-53FC-4F63-8A92-F35A6A050ED4}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287312,36 +287323,36 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{AF7F710A-53FC-4F63-8A92-F35A6A050ED4}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_TRI"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_TSCA",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that link to the Toxic Substances Control Act (TSCA) System. The TSCA database supports the Toxic Substances Control Act (TSCA) of 1976, which provides EPA with authority to require reporting, record-keeping and testing requirements, and restrictions relating to chemical substances and/or mixtures. Certain substances are generally excluded from TSCA, including, among others, food, drugs, cosmetics and pesticides. TSCA addresses the production, importation, use, and disposal of specific chemicals including polychlorinated biphenyls (PCBs), asbestos, radon and lead-based paint.FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TSCA facilities once the TSCA data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "epa-facility-registry-service-frs-er-tsca",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287414,36 +287425,36 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "epa-facility-registry-service-frs-er-tsca",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): ER_TSCA"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_WTP",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of Waste Water Treatment Plant facilities that link to the National Pollutant Discharge Elimination System (NPDES) module of the Integrated Compliance Information System (ICIS). ICIS tracks NPDES surface water permits issued under the Clean Water Act. Under NPDES, all facilities that discharge pollutants from any point source into waters of the United States are required to obtain a permit. The permit will likely contain limits on what can be discharged, impose monitoring and reporting requirements, and include other provisions to ensure that the discharge does not adversely affect water quality. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES facilities once the ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{60031F80-ED67-487C-84E0-ACE941870463}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287520,35 +287531,35 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
+            "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
+            "temporal": "2020-12-12/2020-12-12",
+            "title": "EPA Facility Registry Service (FRS): ER_WTP"
         },
-            "identifier": "{60031F80-ED67-487C-84E0-ACE941870463}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
-            "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ER_WWTP_NPDES",
             "description": "This web feature service contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of Waste Water Treatment Plant facilities that link to the National Pollutant Discharge Elimination System (NPDES) module of the Integrated Compliance Information System (ICIS). ICIS tracks NPDES surface water permits issued under the Clean Water Act. Under NPDES, all facilities that discharge pollutants from any point source into waters of the United States are required to obtain a permit. The permit will likely contain limits on what can be discharged, impose monitoring and reporting requirements, and include other provisions to ensure that the discharge does not adversely affect water quality. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES facilities once the ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "{4B0291A7-26C8-4EC0-A525-1F8A33A9998C}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -287625,35 +287636,35 @@
                 "Contaminant",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Headquarters"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
+            "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
+            "temporal": "2020-12-12/2020-12-12",
+            "title": "EPA Facility Registry Service (FRS): ER_WWTP_NPDES"
         },
-            "identifier": "{4B0291A7-26C8-4EC0-A525-1F8A33A9998C}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
-            "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): FRS_ESF10",
             "description": "This web service contains the following layers: RMP, TRI, FRP, RCRATSD, CERCLIS, TSCA, and E-PLAN facilities and their associated CONTACTS, CHEMICALS, NAIP, SIC, and STATE IDs information. Layers are drawn at scale of 1: 18,489,297 and lower. Data used to create this web service are available as a separate download at the Secondary Linkage listed above. Full FGDC metadata records for each layer may be found by clicking the layer name in the web service table of contents (available through the online link provided above) and viewing the layer description. Data Dictionary available: https://ordsext.epa.gov/FLA/www3/ESF10_Supplemental_Metadata.docx",
+            "distribution": [],
+            "identifier": "{EF4A2554-B797-4604-ABAD-C9660E2AD749}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Sites",
                 "Permits",
@@ -287669,36 +287680,36 @@
                 "Cleanup",
                 "ESF10"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "{EF4A2554-B797-4604-ABAD-C9660E2AD749}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): FRS_ESF10"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): FRS_ESF3",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This web service contains the following layers: WWTP -NPDES and WTP. The WWTP-NPDES facilties have associated CONTACTS, NAIP, SIC, and STATE IDs information. Layers are drawn at a scale of 1: 2311162.217155 and larger. Data used to create this web service are available as a separate download at the Secondary Linkage listed above. Full FGDC metadata records for each layer may be found by clicking the layer name in the web service table of contents (available through the online link provided above) and viewing the layer description.",
+            "distribution": [],
+            "identifier": "{B4A867A5-89B2-4B39-BF64-5A5AD206F298}",
+            "issued": "2016-06-29",
             "keyword": [
                 "Sites",
                 "Permits",
@@ -287713,35 +287724,47 @@
                 "Facilities",
                 "Cleanup"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2020-12-12/2020-12-12",
+            "title": "EPA Facility Registry Service (FRS): FRS_ESF3"
         },
-            "identifier": "{B4A867A5-89B2-4B39-BF64-5A5AD206F298}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "irregular",
-            "issued": "2016-06-29",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ACRES",
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=becec3456e414008ab77b26b640331a8",
             "description": "This web feature service consists of location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of sites that link to the Assessment Cleanup and Redevelopment Exchange System (ACRES). ACRES stores information reported by EPA Brownfields grant recipients on Brownfields properties assessed or cleaned up with grant funding, as well as information on Targeted Brownfields Assessments (TBA) performed by EPA Regions. The Facility Registry Service (FRS) identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS facilities that link to Brownfields sites once the ACRES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-acres",
+                    "title": "EDG Open Data site with Clip N Ship capability"
+                }
+            ],
+            "identifier": "34D8A6B2-A49F-4AD6-94C1-7CD3678B1E2C",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -287755,48 +287778,42 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-170.681866, -14.281981, 145.80274, 71.274721",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): ACRES"
         },
-            "identifier": "34D8A6B2-A49F-4AD6-94C1-7CD3678B1E2C",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-170.681866, -14.281981, 145.80274, 71.274721",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=becec3456e414008ab77b26b640331a8",
-            "issued": "2020-01-09",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
             },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Air Quality System (AQS). The AQS contains ambient air pollution data collected by EPA, State, Local, and Tribal air pollution control agencies from thousands of monitoring stations. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to monitoring stations once the AQS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-acres"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): AIRS_AQS",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Air Quality System (AQS). The AQS contains ambient air pollution data collected by EPA, State, Local, and Tribal air pollution control agencies from thousands of monitoring stations. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to monitoring stations once the AQS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "AAA8828C-7469-4F7D-A8CC-167E9437A646",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -287811,42 +287828,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-159.366715, 17.727472, -64.789403, 70.293892",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): AIRS_AQS"
         },
-            "identifier": "AAA8828C-7469-4F7D-A8CC-167E9437A646",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-159.366715, 17.727472, -64.789403, 70.293892",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=bc42cd5b45da4893a0cfbe599a5cb21b",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to dischargers of air pollutants from the Integrated Compliance Information System for Air (AIR). ICIS-Air (AIR) \u2013 AIR is the modernization of the Air Facility System (AFS) into the Integrated Compliance Information System (ICIS).  AIR contains enforcement, compliance, and permit data for stationary sources of air pollution regulated by the EPA, State, and Local air pollution agencies. A facility is classified as a Major Discharger if: a) Actual or potential emissions are above the applicable major source thresholds, or  b) Actual or potential controlled emissions > 100 tons/year as per Alabama power decision, or c) Unregulated pollutant actual or potential controlled emissions > 100 tons/year as per Alabama power decision. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to ICIS-Air (AIR) major facilities once the ICIS-Air (AIR) data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
-                }
-            ]
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): AIR_MAJOR",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to dischargers of air pollutants from the Integrated Compliance Information System for Air (AIR). ICIS-Air (AIR) \u2013 AIR is the modernization of the Air Facility System (AFS) into the Integrated Compliance Information System (ICIS).  AIR contains enforcement, compliance, and permit data for stationary sources of air pollution regulated by the EPA, State, and Local air pollution agencies. A facility is classified as a Major Discharger if: a) Actual or potential emissions are above the applicable major source thresholds, or  b) Actual or potential controlled emissions > 100 tons/year as per Alabama power decision, or c) Unregulated pollutant actual or potential controlled emissions > 100 tons/year as per Alabama power decision. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to ICIS-Air (AIR) major facilities once the ICIS-Air (AIR) data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-air-major",
+                    "title": "EDG Open Data site with Clip N Ship capability"
+                }
+            ],
+            "identifier": "860B8794-0C8A-4A28-9002-D9B9B4F84316",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -287860,48 +287883,48 @@
                 "Cleanup",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.659, -14.270919, 174.107672, 71.292071",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): AIR_MAJOR"
         },
-            "identifier": "860B8794-0C8A-4A28-9002-D9B9B4F84316",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.659, -14.270919, 174.107672, 71.292071",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=bc42cd5b45da4893a0cfbe599a5cb21b",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=2ec5c12c263c45b9a800f48666bdf4f2",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Integrated Compliance Information System for Air (AIR). ICIS-Air (AIR) \u2013 AIR is the modernization of the Air Facility System (AFS) into the Integrated Compliance Information System (ICIS).  AIR contains enforcement, compliance, and permit data for stationary sources of air pollution regulated by the EPA, State, and Local air pollution agencies. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS facilities that link to ICIS-Air (AIR) facilities once the ICIS-Air (AIR) data has been fully integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-air-major"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-air",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): AIR",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Integrated Compliance Information System for Air (AIR). ICIS-Air (AIR) \u2013 AIR is the modernization of the Air Facility System (AFS) into the Integrated Compliance Information System (ICIS).  AIR contains enforcement, compliance, and permit data for stationary sources of air pollution regulated by the EPA, State, and Local air pollution agencies. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS facilities that link to ICIS-Air (AIR) facilities once the ICIS-Air (AIR) data has been fully integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "97CE920F-62F3-4029-B64E-2AC73C4C1485",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -287914,48 +287937,42 @@
                 "Cleanup",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.659, 13.3039, 174.107672, 71.35589",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): AIR"
         },
-            "identifier": "97CE920F-62F3-4029-B64E-2AC73C4C1485",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.659, 13.3039, 174.107672, 71.35589",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=2ec5c12c263c45b9a800f48666bdf4f2",
-            "issued": "2020-01-09",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
             },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Bureau of Indian Affairs (BIA) school data on Indian land. The BIA is responsible for the administration and management of 55.7 million acres of land held in trust by the United States for American Indians, Indian Tribes, and Alaska natives and provides education services to approximately 48,000 Indian students. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to the BIA school facilities once the BIA Indian School dataset has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-air"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): BIA",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Bureau of Indian Affairs (BIA) school data on Indian land. The BIA is responsible for the administration and management of 55.7 million acres of land held in trust by the United States for American Indians, Indian Tribes, and Alaska natives and provides education services to approximately 48,000 Indian students. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to the BIA school facilities once the BIA Indian School dataset has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "554CA3B1-8C32-4D05-A4CE-9313AE80C346",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -287969,42 +287986,42 @@
                 "Cleanup",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-124.6377, 26.32613, -67.04015, 48.846135",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): BIA"
         },
-            "identifier": "554CA3B1-8C32-4D05-A4CE-9313AE80C346",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-124.6377, 26.32613, -67.04015, 48.846135",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Base Realignment and Closure (BRAC) facilities. BRAC is a process used to close excess military installations and realign the total asset inventory in order to save money on operations and maintenance. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that are classified as BRAC. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): BRAC",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Base Realignment and Closure (BRAC) facilities. BRAC is a process used to close excess military installations and realign the total asset inventory in order to save money on operations and maintenance. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that are classified as BRAC. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "0A386875-326D-4673-958E-92FD28326890",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288018,41 +288035,41 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.646252, 13.41605, 144.685097, 63.900543",
+            "title": "EPA Facility Registry Service (FRS): BRAC"
         },
-            "identifier": "0A386875-326D-4673-958E-92FD28326890",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.646252, 13.41605, 144.685097, 63.900543",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Clean Air Markets Division Business System (CAMDBS). Administered by the EPA Clean Air Markets Division, within the Office of Air and Radiation, CAMDBS supports the implementation of market-based air pollution control programs, including the Acid Rain Program and regional programs designed to reduce the transport of ozone. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to CAMDBS facilities once the CAMDBS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): CAMDBS",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Clean Air Markets Division Business System (CAMDBS). Administered by the EPA Clean Air Markets Division, within the Office of Air and Radiation, CAMDBS supports the implementation of market-based air pollution control programs, including the Acid Rain Program and regional programs designed to reduce the transport of ozone. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to CAMDBS facilities once the CAMDBS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "73E943CD-F370-4569-9E3A-69890321799F",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288066,42 +288083,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-158.107306, 17.943889, -66.1489, 63.855545",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): CAMDBS"
         },
-            "identifier": "73E943CD-F370-4569-9E3A-69890321799F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-158.107306, 17.943889, -66.1489, 63.855545",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=e64c3fd66010469abc42a77a2b428ed4",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Emission Inventory System (EIS). The Emission Inventory System (EIS) maintains an inventory of large stationary sources and voluntarily-reported smaller sources of air point pollution emitters. It contains information about facility sites and their physical location, emission units, emission processes, release points, control approaches, and regulations. Facility inventory data are kept separate from the emissions data and have stable identifiers to improve continuity from year to year and to help identify duplicate or missing facilities. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.  Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
-                }
-            ]
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): EIS",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Emission Inventory System (EIS). The Emission Inventory System (EIS) maintains an inventory of large stationary sources and voluntarily-reported smaller sources of air point pollution emitters. It contains information about facility sites and their physical location, emission units, emission processes, release points, control approaches, and regulations. Facility inventory data are kept separate from the emissions data and have stable identifiers to improve continuity from year to year and to help identify duplicate or missing facilities. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.  Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-eis",
+                    "title": "EDG Open Data site with Clip N Ship capability"
+                }
+            ],
+            "identifier": "405C0D1B-6530-48F3-960F-D40EBC6E5518",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288115,48 +288138,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.659, 17.7003, 174.113589, 71.292071",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): EIS"
         },
-            "identifier": "405C0D1B-6530-48F3-960F-D40EBC6E5518",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.659, 17.7003, 174.113589, 71.292071",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=e64c3fd66010469abc42a77a2b428ed4",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=cdff193a3e3743a5bc770e2743f215b3",
+            "description": "This downloadable data package consists of location and facility identification information from EPA's Facility Registry Service (FRS) for all sites that are available in the FRS individual feature layers. The layers comprise the FRS major program databases, including: Assessment Cleanup and Redevelopment Exchange System (ACRES) : brownfields sites ; Air Facility System (AFS) : stationary sources of air pollution ; ICIS-AIR (AIR) : stationary sources of air pollution;  Bureau of Indian Affairs (BIA) : schools data on Indian land; Base Realignment and Closure (BRAC) facilities; Clean Air Markets Division Business System (CAMDBS) :  market-based air pollution control programs;  Comprehensive Environmental Response, Superfund Enterprise Management System (SEMS): hazardous waste sites; Integrated Compliance Information System (ICIS) : integrated enforcement and compliance information; National Compliance Database (NCDB) : Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) and the Toxic Substances Control Act (TSCA); National Pollutant Discharge Elimination System (NPDES) module of ICIS : NPDES surface water permits; Radiation Information Database (RADINFO) : radiation and radioactivity facilities; RACT/BACT/LAER Clearinghouse (RBLC) : best available air pollution technology requirements; Resource Conservation and Recovery Act Information System (RCRAInfo) : tracks generators, transporters, treaters, storers, and disposers of hazardous waste; Toxic Release Inventory (TRI) : certain industries that use, manufacture, treat, or transport more than 650 toxic chemicals; Emission Inventory System (EIS) : inventory of large stationary sources and voluntarily-reported smaller sources of air point pollution emitters; countermeasure (SPCC) and facility response plan (FRP) subject facilities; Electronic Greenhouse Gas Reporting Tool (E-GGRT) : large greenhouse gas emitters; Emissions and; Generation Resource Integrated Database (EGRID) : power plants. The Facility Registry Service (FRS) identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the FRS facilities that link to the programs listed above once the program data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.  Included in this package are a file geodatabase, Esri ArcMap map document and an XML file of this metadata record.  Full FGDC metadata records for each layer are contained in the database.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-eis"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/facility-registry-service-frs-interests",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Facility Interests Dataset Download",
-            "description": "This downloadable data package consists of location and facility identification information from EPA's Facility Registry Service (FRS) for all sites that are available in the FRS individual feature layers. The layers comprise the FRS major program databases, including: Assessment Cleanup and Redevelopment Exchange System (ACRES) : brownfields sites ; Air Facility System (AFS) : stationary sources of air pollution ; ICIS-AIR (AIR) : stationary sources of air pollution;  Bureau of Indian Affairs (BIA) : schools data on Indian land; Base Realignment and Closure (BRAC) facilities; Clean Air Markets Division Business System (CAMDBS) :  market-based air pollution control programs;  Comprehensive Environmental Response, Superfund Enterprise Management System (SEMS): hazardous waste sites; Integrated Compliance Information System (ICIS) : integrated enforcement and compliance information; National Compliance Database (NCDB) : Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) and the Toxic Substances Control Act (TSCA); National Pollutant Discharge Elimination System (NPDES) module of ICIS : NPDES surface water permits; Radiation Information Database (RADINFO) : radiation and radioactivity facilities; RACT/BACT/LAER Clearinghouse (RBLC) : best available air pollution technology requirements; Resource Conservation and Recovery Act Information System (RCRAInfo) : tracks generators, transporters, treaters, storers, and disposers of hazardous waste; Toxic Release Inventory (TRI) : certain industries that use, manufacture, treat, or transport more than 650 toxic chemicals; Emission Inventory System (EIS) : inventory of large stationary sources and voluntarily-reported smaller sources of air point pollution emitters; countermeasure (SPCC) and facility response plan (FRP) subject facilities; Electronic Greenhouse Gas Reporting Tool (E-GGRT) : large greenhouse gas emitters; Emissions and; Generation Resource Integrated Database (EGRID) : power plants. The Facility Registry Service (FRS) identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the FRS facilities that link to the programs listed above once the program data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.  Included in this package are a file geodatabase, Esri ArcMap map document and an XML file of this metadata record.  Full FGDC metadata records for each layer are contained in the database.",
+            ],
+            "identifier": "01AB5777-E768-4088-9817-C186F297970B",
+            "issued": "2020-01-09",
             "keyword": [
                 "AZURITE",
                 "BRAC",
@@ -288249,48 +288272,48 @@
                 "OK-FMS",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, 13.27111, 145.72, 71.301199",
+            "temporal": "2020-04-08T00:00:00/2020-04-08T00:00:00",
+            "title": "EPA Facility Registry Service (FRS): Facility Interests Dataset Download"
         },
-            "identifier": "01AB5777-E768-4088-9817-C186F297970B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, 13.27111, 145.72, 71.301199",
-            "temporal": "2020-04-08T00:00:00/2020-04-08T00:00:00",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=cdff193a3e3743a5bc770e2743f215b3",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=a117d02cdbfc4bcbad5abb7c9bf94982",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Integrated Compliance Information System (ICIS). When complete, ICIS will provide a database that will contain integrated enforcement and compliance information across most of EPA's programs. The vision for ICIS is to replace EPA's independent databases that contain enforcement data with a single repository for that information. Currently, ICIS contains all Federal Administrative and Judicial enforcement actions and a subset of the Permit Compliance System (PCS), which supports the National Pollutant Discharge Elimination System (NPDES). ICIS exchanges non-sensitive enforcement/compliance activities, non-sensitive formal enforcement actions and NPDES information with FRS. This web feature service contains the enforcement/compliance activities and formal enforcement action related facilities; the NPDES facilities are contained in the PCS_NPDES web feature service. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to ICIS non-sensitive enforcement/compliance activities and formal enforcement actions once the ICIS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/facility-registry-service-frs-interests"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-icis",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): ICIS",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Integrated Compliance Information System (ICIS). When complete, ICIS will provide a database that will contain integrated enforcement and compliance information across most of EPA's programs. The vision for ICIS is to replace EPA's independent databases that contain enforcement data with a single repository for that information. Currently, ICIS contains all Federal Administrative and Judicial enforcement actions and a subset of the Permit Compliance System (PCS), which supports the National Pollutant Discharge Elimination System (NPDES). ICIS exchanges non-sensitive enforcement/compliance activities, non-sensitive formal enforcement actions and NPDES information with FRS. This web feature service contains the enforcement/compliance activities and formal enforcement action related facilities; the NPDES facilities are contained in the PCS_NPDES web feature service. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to ICIS non-sensitive enforcement/compliance activities and formal enforcement actions once the ICIS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "03D8D923-4B65-42D8-9745-E7A929E7F437",
+            "issued": "2020-03-13",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288304,48 +288327,42 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-03-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.646252, -14.340156, 174.107672, 71.35589",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): ICIS"
         },
-            "identifier": "03D8D923-4B65-42D8-9745-E7A929E7F437",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.646252, -14.340156, 174.107672, 71.35589",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=a117d02cdbfc4bcbad5abb7c9bf94982",
-            "issued": "2020-03-13",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
             },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the National Compliance Database (NCDB). The NCDB supports implementation of the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) and the Toxic Substances Control Act (TSCA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NCDB facilities once the NCDB data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-icis"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): NCDB",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the National Compliance Database (NCDB). The NCDB supports implementation of the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) and the Toxic Substances Control Act (TSCA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NCDB facilities once the NCDB data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "38EA07F7-F499-477E-AD38-2F21068D3DBA",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288359,42 +288376,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-179.3, -14.322328, 174.107672, 71.35589",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): NCDB"
         },
-            "identifier": "38EA07F7-F499-477E-AD38-2F21068D3DBA",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-179.3, -14.322328, 174.107672, 71.35589",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=dcbc597562f34a7bb55dce6ce8a4c19a",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that are Clean Water Act (CWA) National Pollutant Discharge Elimination System (NPDES) dischargers of pollutants into waters of the United States. These facilities are tracked in the NPDES module of the Integrated Compliance Information System (ICIS). For Publicly Owned Treatment Works (POTWs), Major dischargers include all facilities with design flows equal to or greater than one million gallons per day, or serve a population of 10,000 or more, or cause significant water quality impacts. Non-POTW discharges are classified as Major facilities on the basis of the number of points accumulated using a Rating worksheet, which evaluates the significance of a facility using several criteria, including toxic pollutant potential, flow volume, and water quality factors such as impairment of the receiving water or proximity of the discharge to coastal waters. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES Major Facilities once the  ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
-                }
-            ]
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): NPDES_MAJOR",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that are Clean Water Act (CWA) National Pollutant Discharge Elimination System (NPDES) dischargers of pollutants into waters of the United States. These facilities are tracked in the NPDES module of the Integrated Compliance Information System (ICIS). For Publicly Owned Treatment Works (POTWs), Major dischargers include all facilities with design flows equal to or greater than one million gallons per day, or serve a population of 10,000 or more, or cause significant water quality impacts. Non-POTW discharges are classified as Major facilities on the basis of the number of points accumulated using a Rating worksheet, which evaluates the significance of a facility using several criteria, including toxic pollutant potential, flow volume, and water quality factors such as impairment of the receiving water or proximity of the discharge to coastal waters. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES Major Facilities once the  ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html.",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-npdes-major",
+                    "title": "EDG Open Data site with Clip N Ship capability"
+                }
+            ],
+            "identifier": "C8E8427A-7ECD-4B74-80CB-917B055EF516",
+            "issued": "2015-05-20",
             "keyword": [
                 "020:072",
                 "Remediation",
@@ -288411,48 +288434,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-170.722611, -14.340156, 145.75, 70.490861",
+            "temporal": "2015-05-20/2015-05-20",
+            "title": "EPA Facility Registry Service (FRS): NPDES_MAJOR"
         },
-            "identifier": "C8E8427A-7ECD-4B74-80CB-917B055EF516",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-170.722611, -14.340156, 145.75, 70.490861",
-            "temporal": "2015-05-20/2015-05-20",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=dcbc597562f34a7bb55dce6ce8a4c19a",
-            "issued": "2015-05-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=56eac669cfbf4b529c067a65a3c559b5",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the the National Pollutant Discharge Elimination System (NPDES) module of the Integrated Compliance Information System (ICIS). This tracks NPDES surface water permits issued under the Clean Water Act. This system is being incrementally replaced by the NPDES module of ICIS. Under NPDES, all facilities that discharge pollutants from any point source into waters of the United States are required to obtain a permit. The permit will likely contain limits on what can be discharged, impose monitoring and reporting requirements, and include other provisions to ensure that the discharge does not adversely affect water quality. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES facilities once the ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-npdes-major"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-npdes",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): NPDES",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the the National Pollutant Discharge Elimination System (NPDES) module of the Integrated Compliance Information System (ICIS). This tracks NPDES surface water permits issued under the Clean Water Act. This system is being incrementally replaced by the NPDES module of ICIS. Under NPDES, all facilities that discharge pollutants from any point source into waters of the United States are required to obtain a permit. The permit will likely contain limits on what can be discharged, impose monitoring and reporting requirements, and include other provisions to ensure that the discharge does not adversely affect water quality. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to NPDES facilities once the ICIS-NPDES data has been integrated into the FRS database. Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html.",
+            ],
+            "identifier": "518DA394-2CCB-4C54-8BA8-4C0BBDCE5DAF",
+            "issued": "2015-05-20",
             "keyword": [
                 "020:072",
                 "Estuary",
@@ -288472,48 +288495,42 @@
                 "Contaminant",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-177.8945, -14.356083, 174.107672, 71.57521",
+            "temporal": "2015-05-20/2015-05-20",
+            "title": "EPA Facility Registry Service (FRS): NPDES"
         },
-            "identifier": "518DA394-2CCB-4C54-8BA8-4C0BBDCE5DAF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-177.8945, -14.356083, 174.107672, 71.57521",
-            "temporal": "2015-05-20/2015-05-20",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=56eac669cfbf4b529c067a65a3c559b5",
-            "issued": "2015-05-20",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
             },
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Radiation Information Database (RADINFO). RADINFO contains information about facilities that are regulated by EPA for radiation and radioactivity. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RADINFO facilities once the RADINFO data has been integrated into the FRS database.  Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-npdes"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RADINFO",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Radiation Information Database (RADINFO). RADINFO contains information about facilities that are regulated by EPA for radiation and radioactivity. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RADINFO facilities once the RADINFO data has been integrated into the FRS database.  Additional information on FRS is available at the EPA website http://www.epa.gov/enviro/html/fii/index.html",
+            ],
+            "identifier": "FDD134A9-07C4-4268-9E72-3B6702D1BB35",
+            "issued": "2015-04-23",
             "keyword": [
                 "Exposure",
                 "020:072",
@@ -288529,92 +288546,42 @@
                 "Facilities",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-04-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
-            },
-            "identifier": "FDD134A9-07C4-4268-9E72-3B6702D1BB35",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-157.960222, 21.351472, -70.73626, 47.948611",
             "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2015-04-23",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
-                }
-            ]
+            "title": "EPA Facility Registry Service (FRS): RADINFO"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RBLC",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the RACT/BACT/LAER Clearinghouse (RBLC). The RBLC database contains case-specific information on the air pollution technologies that have been required to reduce the emission of air pollutions from stationary sources. RACT, or Reasonably Available Control Technology, is required on existing sources in areas that are not meeting national ambient air quality standards. BACT, or Best Available Control Technology, is required on major new or modified sources in clean areas. LAER, or Lowest Achievable Emission Rate, is required on major new or modified sources in non-attainment areas. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RBLC facilities once the RBLC data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
-            "keyword": [
-                "020:072",
-                "Air",
-                "Remediation",
-                "Compliance",
-                "Environment",
-                null,
-                "Cleanup",
-                "geospatial",
-                "Regulatory",
-                "Facilities",
-                "Drinking Water",
-                "United States"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2020-01-09",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRS Support",
                 "hasEmail": "mailto:FRS_Support@epa.gov"
             },
-            "identifier": "27AB3010-377B-42CD-BDC3-5F7DE886C21A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-166.555224, 17.707752, -64.755978, 70.333333",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the RACT/BACT/LAER Clearinghouse (RBLC). The RBLC database contains case-specific information on the air pollution technologies that have been required to reduce the emission of air pollutions from stationary sources. RACT, or Reasonably Available Control Technology, is required on existing sources in areas that are not meeting national ambient air quality standards. BACT, or Best Available Control Technology, is required on major new or modified sources in clean areas. LAER, or Lowest Achievable Emission Rate, is required on major new or modified sources in non-attainment areas. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RBLC facilities once the RBLC data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA_ACTIVE",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of active hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to active RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
+            ],
+            "identifier": "27AB3010-377B-42CD-BDC3-5F7DE886C21A",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288629,48 +288596,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-166.555224, 17.707752, -64.755978, 70.333333",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RBLC"
         },
-            "identifier": "C87CF92B-5310-44AC-B860-F3F2AC580A1B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, -14.2866, 144.89736, 71.292591",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=e79a618517704831ad2ef4f61987dabf",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of active hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to active RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-active"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-active",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA_INACTIVE",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to inactive RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "C87CF92B-5310-44AC-B860-F3F2AC580A1B",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288685,48 +288652,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, -14.2866, 144.89736, 71.292591",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA_ACTIVE"
         },
-            "identifier": "90F8C808-347B-48EE-87FF-76A92FC027C7",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.635369, -14.2769, 144.806428, 71.289822",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=a00411926ca541de8df4c4cb60da3126",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to inactive RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-inactive"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-inactive",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA_LQG",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo) and are classified as hazardous waste large quantity generators (LQG). RCRAInfo is EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984. It tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste. A LQG generates: \n1,000 kg or more of hazardous waste during any calendar month; or More than 1 kg of acutely hazardous waste during any calendar month; or More than 100 kg of any residue or contaminated soil, waste or other debris resulting from the cleanup of a spill, into or on any land or water, of acutely hazardous waste during any calendar month; or 1 kg or less of acutely hazardous waste during any calendar month, and accumulate more than 1 kg of acutely hazardous waste at any time; or 100 kg or less of any residue or contaminated soil, waste or other debris resulting from the cleanup of a spill, into or on any land or water, of acutely hazardous waste during any calendar month, and accumulated more than 100 kg of that material at any time. \nFRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste LQGs once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs\n\t\t\t",
+            ],
+            "identifier": "90F8C808-347B-48EE-87FF-76A92FC027C7",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288741,48 +288708,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.635369, -14.2769, 144.806428, 71.289822",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA_INACTIVE"
         },
-            "identifier": "5AEE57F3-3298-4B0C-A67F-091E35CA1215",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-170.6666, -14.2666, 144.89736, 66.899817",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=1616e854060642b58cd8e33fa6f91b8f",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo) and are classified as hazardous waste large quantity generators (LQG). RCRAInfo is EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984. It tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste. A LQG generates: \n1,000 kg or more of hazardous waste during any calendar month; or More than 1 kg of acutely hazardous waste during any calendar month; or More than 100 kg of any residue or contaminated soil, waste or other debris resulting from the cleanup of a spill, into or on any land or water, of acutely hazardous waste during any calendar month; or 1 kg or less of acutely hazardous waste during any calendar month, and accumulate more than 1 kg of acutely hazardous waste at any time; or 100 kg or less of any residue or contaminated soil, waste or other debris resulting from the cleanup of a spill, into or on any land or water, of acutely hazardous waste during any calendar month, and accumulated more than 100 kg of that material at any time. \nFRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste LQGs once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs\n\t\t\t",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "downloadURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-lqg"
+                    "downloadURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-lqg",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
+            ],
+            "identifier": "5AEE57F3-3298-4B0C-A67F-091E35CA1215",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288797,48 +288764,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-170.6666, -14.2666, 144.89736, 66.899817",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA_LQG"
         },
-            "identifier": "B036E7A0-FF40-4AE2-831D-D012B2B8763F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, -14.2866, 144.89736, 71.292591",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=5770ebcca752418fb892bdb6a8baf0c2",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of hazardous waste facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA_TRANS",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo) and are transporters of hazardous waste.  RCRAInfo is EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984. It tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste transporters once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "B036E7A0-FF40-4AE2-831D-D012B2B8763F",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288853,54 +288820,55 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, -14.2866, 144.89736, 71.292591",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA"
         },
-            "identifier": "B63C851D-D10C-4AF4-9B6C-22377E9AAFC8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-166.553836, 13.419606, 144.833761, 71.289088",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=3f69dcc7ba35403483d190f3f80e4c06",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo) and are transporters of hazardous waste.  RCRAInfo is EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Hazardous and Solid Waste Amendments (HSWA) of 1984. It tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste transporters once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-trans"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-trans",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RCRA_TSD",
-            "description": "This web feature service contains location and facility identification information from e Hazardous EPA's Facility Registry Service (FRS) for the subset of Hazardous Waste Treatment, Storage, and Disposal (TSD) facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  A TSD Facility performs one or more of the following functions: \nTreatment: Any method, technique, or process, including neutralization, designed to change the physical, chemical or biological character or composition of any hazardous waste so as to neutralize such waste, or so as to recover energy or material resources from the waste, or so as to render such waste non-hazardous, or less hazardous; safer to transport, store or dispose of; or amenable for recovery, amenable for storage, or reduced in volume. \nStorage: The holding of hazardous waste for a temporary period, at the end of which the hazardous waste is treated, disposed of, or stored elsewhere. \nDisposal: The discharge, deposit, injection, dumping, spilling, leaking, or placing of any solid waste or hazardous waste into or on any land or water so that such solid waste or hazardous waste or any constituent thereof may enter the environment or be emitted into the air or discharged into any waters, including groundwaters. \nFRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste TSD facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs\n\t\t\t",
+            ],
+            "identifier": "B63C851D-D10C-4AF4-9B6C-22377E9AAFC8",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
                 "Remediation",
                 "Compliance",
                 "Environment",
+                null,
                 "Cleanup",
                 "geospatial",
                 "Regulatory",
@@ -288908,48 +288876,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-166.553836, 13.419606, 144.833761, 71.289088",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA_TRANS"
         },
-            "identifier": "720A41F5-B170-4EF4-BBF1-F1CA9ADFCE02",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-158.11379, 13.419444, 144.89736, 61.25833",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=0b30c57359194330bb89c9b3cf9c0bd5",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from e Hazardous EPA's Facility Registry Service (FRS) for the subset of Hazardous Waste Treatment, Storage, and Disposal (TSD) facilities that link to the Resource Conservation and Recovery Act Information System (RCRAInfo). EPA's comprehensive information system in support of the Resource Conservation and Recovery Act (RCRA) of 1976 and the Solid Waste Amendments (HSWA) of 1984, RCRAInfo tracks many types of information about generators, transporters, treaters, storers, and disposers of hazardous waste.  A TSD Facility performs one or more of the following functions: \nTreatment: Any method, technique, or process, including neutralization, designed to change the physical, chemical or biological character or composition of any hazardous waste so as to neutralize such waste, or so as to recover energy or material resources from the waste, or so as to render such waste non-hazardous, or less hazardous; safer to transport, store or dispose of; or amenable for recovery, amenable for storage, or reduced in volume. \nStorage: The holding of hazardous waste for a temporary period, at the end of which the hazardous waste is treated, disposed of, or stored elsewhere. \nDisposal: The discharge, deposit, injection, dumping, spilling, leaking, or placing of any solid waste or hazardous waste into or on any land or water so that such solid waste or hazardous waste or any constituent thereof may enter the environment or be emitted into the air or discharged into any waters, including groundwaters. \nFRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RCRAInfo hazardous waste TSD facilities once the RCRAInfo data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs\n\t\t\t",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-tsd"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rcra-tsd",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): RMP",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Risk Management Plan (RMP) System. The Risk Management Plan (RMP) database stores the risk management plans reported by companies that handle, manufacture, use, or store certain flammable or toxic substances, as required under section 112(r) of the Clean Air Act (CAA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RMP facilities once the RMP data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "720A41F5-B170-4EF4-BBF1-F1CA9ADFCE02",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -288963,48 +288931,48 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-158.11379, 13.419444, 144.89736, 61.25833",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): RCRA_TSD"
         },
-            "identifier": "epa-facility-registry-service-frs-rmp",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-170.686791, -14.270809, 144.783, 70.490861",
-            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
-            "accrualPeriodicity": "R/P1M",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=3c8a335f4b5243a188fd75472459e567",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Risk Management Plan (RMP) System. The Risk Management Plan (RMP) database stores the risk management plans reported by companies that handle, manufacture, use, or store certain flammable or toxic substances, as required under section 112(r) of the Clean Air Act (CAA). FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to RMP facilities once the RMP data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rmp"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-rmp",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): SEMS",
-            "description": "This data provides location and attribute information on Facilities regulated under the Superfund Enterprise Management System (SEMS). The Superfund Enterprise Management System (SEMS) integrates multiple legacy systems (e.g., CERCLIS, ICTS, SDMS) into a comprehensive tracking and reporting tool, providing data on the inventory of active and archived hazardous waste sites evaluated by the Superfund program. It contains sites that are either proposed to be, or are on, the National Priorities List (NPL) as well as sites that are in the screening and assessment phase for possible inclusion on the NPL. The data provided in this service are obtained from EPA's Facility Registry Service (FRS).  The FRS is an integrated source of comprehensive (air, water, and waste) environmental information about facilities, sites or places. This service connects directly to the FRS database to provide this data as a feature service.  FRS creates high-quality, accurate, and authoritative facility identification records through rigorous verification and management procedures that incorporate information from program national systems, state master facility records, data collected from EPA's Central Data Exchange registrations and data management personnel. Additional Information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "epa-facility-registry-service-frs-rmp",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -289018,55 +288986,54 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-170.686791, -14.270809, 144.783, 70.490861",
+            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
+            "title": "EPA Facility Registry Service (FRS): RMP"
         },
-            "identifier": "AF434DAD-D23E-4AEB-95C3-C0663F3DDB6A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, -14.3601, 151.78372, 70.328874",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=7dd2b44b4cfc4f75b034a7bbe86c0a60",
-            "issued": "2020-01-09",
+            "description": "This data provides location and attribute information on Facilities regulated under the Superfund Enterprise Management System (SEMS). The Superfund Enterprise Management System (SEMS) integrates multiple legacy systems (e.g., CERCLIS, ICTS, SDMS) into a comprehensive tracking and reporting tool, providing data on the inventory of active and archived hazardous waste sites evaluated by the Superfund program. It contains sites that are either proposed to be, or are on, the National Priorities List (NPL) as well as sites that are in the screening and assessment phase for possible inclusion on the NPL. The data provided in this service are obtained from EPA's Facility Registry Service (FRS).  The FRS is an integrated source of comprehensive (air, water, and waste) environmental information about facilities, sites or places. This service connects directly to the FRS database to provide this data as a feature service.  FRS creates high-quality, accurate, and authoritative facility identification records through rigorous verification and management procedures that incorporate information from program national systems, state master facility records, data collected from EPA's Central Data Exchange registrations and data management personnel. Additional Information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-sems"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-sems",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): SEMS_NPL",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that are listed on the Superfund National Priorities List (NPL). The NPL lists national priorities among the known releases or threatened releases of hazardous substances, pollutants, or contaminants throughout the United States. The NPL is recorded in the Superfund Enterprise Management System (SEMS), which serves as a comprehensive tracking and reporting tool, providing data on the inventory of active and archived hazardous waste sites evaluated by the Superfund program. It contains sites that are either proposed to be, or are on, the National Priorities List (NPL) as well as sites that are in the screening and assessment phase for possible inclusion on the NPL.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that are listed on the Superfund NPL once the SEMS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "AF434DAD-D23E-4AEB-95C3-C0663F3DDB6A",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
                 "Remediation",
                 "Compliance",
                 "Environment",
-                null,
                 "Cleanup",
                 "geospatial",
                 "Regulatory",
@@ -289074,158 +289041,159 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, -14.3601, 151.78372, 70.328874",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): SEMS"
         },
-            "identifier": "50A945A1-1874-4874-9786-995A0E2C097B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, -14.3601, 145.75, 64.823",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1M",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=29c2d40eda9c4734bafa450d4d596c2f",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that are listed on the Superfund National Priorities List (NPL). The NPL lists national priorities among the known releases or threatened releases of hazardous substances, pollutants, or contaminants throughout the United States. The NPL is recorded in the Superfund Enterprise Management System (SEMS), which serves as a comprehensive tracking and reporting tool, providing data on the inventory of active and archived hazardous waste sites evaluated by the Superfund program. It contains sites that are either proposed to be, or are on, the National Priorities List (NPL) as well as sites that are in the screening and assessment phase for possible inclusion on the NPL.  FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that are listed on the Superfund NPL once the SEMS data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-sems-npl"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-sems-npl",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): SSTS",
-            "description": "This data provides location and attribute information on Facilities regulated under the Section Seven Tracking System (SSTS). SSTS tracks the registration of all pesticide-producing establishments and tracks annually the types and amounts of pesticides, active ingredients, and related devices that are produced, sold, or distributed. The data provided in this service are obtained from EPA's Facility Registry Service (FRS).  The FRS is an integrated source of comprehensive (air, water, and waste) environmental information about facilities, sites or places. This service connects directly to the FRS database to provide this data as a feature service.  FRS creates high-quality, accurate, and authoritative facility identification records through rigorous verification and management procedures that incorporate information from program national systems, state master facility records, data collected from EPA's Central Data Exchange registrations and data management personnel. Additional Information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "50A945A1-1874-4874-9786-995A0E2C097B",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
+                "Remediation",
                 "Compliance",
                 "Environment",
+                null,
                 "Cleanup",
                 "geospatial",
                 "Regulatory",
-                "Pesticides",
                 "Facilities",
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, -14.3601, 145.75, 64.823",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): SEMS_NPL"
         },
-            "identifier": "9DD37820-C590-438E-B99C-A55E5B3BEC12",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.6525, -14.3601, 151.78372, 70.328874",
-            "temporal": "2020-11-17/2020-11-17",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=25cd6f11a64f490484275bb4cd821506",
-            "issued": "2020-01-09",
+            "description": "This data provides location and attribute information on Facilities regulated under the Section Seven Tracking System (SSTS). SSTS tracks the registration of all pesticide-producing establishments and tracks annually the types and amounts of pesticides, active ingredients, and related devices that are produced, sold, or distributed. The data provided in this service are obtained from EPA's Facility Registry Service (FRS).  The FRS is an integrated source of comprehensive (air, water, and waste) environmental information about facilities, sites or places. This service connects directly to the FRS database to provide this data as a feature service.  FRS creates high-quality, accurate, and authoritative facility identification records through rigorous verification and management procedures that incorporate information from program national systems, state master facility records, data collected from EPA's Central Data Exchange registrations and data management personnel. Additional Information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-ssts"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-ssts",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): TRI",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Toxic Release Inventory (TRI) System. TRI is a publicly available EPA database reported annually by certain covered industry groups, as well as federal facilities. It contains information about more than 650 toxic chemicals that are being used, manufactured, treated, transported, or released into the environment, and includes information about waste management and pollution prevention activities. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TRI facilities once the TRI data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "9DD37820-C590-438E-B99C-A55E5B3BEC12",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
-                "Remediation",
                 "Compliance",
                 "Environment",
                 "Cleanup",
                 "geospatial",
                 "Regulatory",
+                "Pesticides",
                 "Facilities",
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.6525, -14.3601, 151.78372, 70.328874",
+            "temporal": "2020-11-17/2020-11-17",
+            "title": "EPA Facility Registry Service (FRS): SSTS"
         },
-            "identifier": "epa-facility-registry-service-frs-tri",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-176.634509, -14.321981, 174.107672, 70.293892",
-            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
-            "accrualPeriodicity": "R/P1M",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=de71cdcedc924aca86af4f838744fce7",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Toxic Release Inventory (TRI) System. TRI is a publicly available EPA database reported annually by certain covered industry groups, as well as federal facilities. It contains information about more than 650 toxic chemicals that are being used, manufactured, treated, transported, or released into the environment, and includes information about waste management and pollution prevention activities. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TRI facilities once the TRI data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-tri"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-tri",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): TSCA",
-            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Toxic Substances Control Act (TSCA) Chemical Substance Inventory System. Section 8 (b) of the Toxic Substances Control Act (TSCA) requires EPA to compile, keep current and publish a list of each chemical substance that is manufactured or processed, including imports, in the United States for uses under TSCA. Also called the \"TSCA Inventory\" or simply \"the Inventory,\" it plays a central role in the regulation of most industrial chemicals in the United States. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TSCA facilities once the TSCA data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            ],
+            "identifier": "epa-facility-registry-service-frs-tri",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -289239,48 +289207,91 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRS Support",
-                "hasEmail": "mailto:FRS_Support@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-176.634509, -14.321981, 174.107672, 70.293892",
+            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
+            "title": "EPA Facility Registry Service (FRS): TRI"
         },
-            "identifier": "epa-facility-registry-service-frs-tsca",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-162.855492, 17.7102, -1.986133, 70.324114",
-            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
-            "accrualPeriodicity": "R/P1M",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRS Support",
+                "hasEmail": "mailto:FRS_Support@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=3c8a335f4b5243a188fd75472459e567",
-            "issued": "2020-01-09",
+            "description": "This web feature service contains location and facility identification information from EPA's Facility Registry Service (FRS) for the subset of facilities that link to the Toxic Substances Control Act (TSCA) Chemical Substance Inventory System. Section 8 (b) of the Toxic Substances Control Act (TSCA) requires EPA to compile, keep current and publish a list of each chemical substance that is manufactured or processed, including imports, in the United States for uses under TSCA. Also called the \"TSCA Inventory\" or simply \"the Inventory,\" it plays a central role in the regulation of most industrial chemicals in the United States. FRS identifies and geospatially locates facilities, sites or places subject to environmental regulations or of environmental interest. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities. This data set contains the subset of FRS integrated facilities that link to TSCA facilities once the TSCA data has been integrated into the FRS database. Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped File Geodatabase",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.amazonaws.com/OMS/FRS/FRS_Interests_Download.zip",
+                    "title": "Zipped File Geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EDG Open Data site with Clip N Ship capability",
-                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-tsca"
+                    "accessURL": "https://edg-epa.hub.arcgis.com/datasets/epa-facility-registry-service-frs-tsca",
+                    "title": "EDG Open Data site with Clip N Ship capability"
                 }
-            ]
+            ],
+            "identifier": "epa-facility-registry-service-frs-tsca",
+            "issued": "2020-01-09",
+            "keyword": [
+                "020:072",
+                "Air",
+                "Remediation",
+                "Compliance",
+                "Environment",
+                "Cleanup",
+                "geospatial",
+                "Regulatory",
+                "Facilities",
+                "Drinking Water",
+                "United States"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
+            },
+            "rights": "licenseUnrestricted",
+            "spatial": "-162.855492, 17.7102, -1.986133, 70.324114",
+            "temporal": "2020-11-17T00:00:00/2020-11-17T00:00:00",
+            "title": "EPA Facility Registry Service (FRS): TSCA"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Oil Capacity ",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EPA GIS Agency Central Support",
+                "hasEmail": "mailto:esrisupport@epa.gov"
+            },
             "description": "This dataset contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that are active oil facilities.  It includes aboveground Oil storage containers and buried Oil storage containers. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.   Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "19657FFD-AD12-42EC-A9BB-4DB51130E03C",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -289357,36 +289368,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EPA GIS Agency Central Support",
-                "hasEmail": "mailto:esrisupport@epa.gov"
-            },
-            "identifier": "19657FFD-AD12-42EC-A9BB-4DB51130E03C",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): Oil Capacity "
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Oil Compliance Activity ",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EPA GIS Agency Central Support",
+                "hasEmail": "mailto:esrisupport@epa.gov"
+            },
             "description": "This dataset contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that contain Oil compliance inspection activities for all active Oil facilities. It includes inspection start date, end date and outcome information. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.   Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "9435C4C0-7F1A-49E1-BDB4-075FE90638FA",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -289463,36 +289474,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EPA GIS Agency Central Support",
-                "hasEmail": "mailto:esrisupport@epa.gov"
-            },
-            "identifier": "9435C4C0-7F1A-49E1-BDB4-075FE90638FA",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): Oil Compliance Activity "
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Oil Discharge History",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EPA GIS Agency Central Support",
+                "hasEmail": "mailto:esrisupport@epa.gov"
+            },
             "description": "This dataset contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that are active oil facilities. It contains Oil incidents information for all active Oil facilities. It includes incident cause, type, location and volume. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.   Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "0F10E744-36AB-416A-AE99-BACDD67536C6",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -289569,36 +289580,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EPA GIS Agency Central Support",
-                "hasEmail": "mailto:esrisupport@epa.gov"
-            },
-            "identifier": "0F10E744-36AB-416A-AE99-BACDD67536C6",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): Oil Discharge History"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): FRP",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Geospatial Support Team",
+                "hasEmail": "mailto:geoservices@epa.gov"
+            },
             "description": "This dataset contains location and facility identification information from EPA's Facility Registry System (FRS) for the subset of facilities that are active oil facilities subject to FRP. It includes FRP id, harm/determination category, OSRO, and harm factors,  Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.   Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "5559DF41-944C-45F7-9E18-7CF0BBB165B5",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -289675,36 +289686,36 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Geospatial Support Team",
-                "hasEmail": "mailto:geoservices@epa.gov"
-            },
-            "identifier": "5559DF41-944C-45F7-9E18-7CF0BBB165B5",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): FRP"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): OIL OSRO",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Geospatial Support Team",
+                "hasEmail": "mailto:geoservices@epa.gov"
+            },
             "description": "This dataset contains OSRO information from EPA's Facility Registry System (FRS) for the subset of facilities that are active oil facilities subject to FRP. Using vigorous verification and data management procedures, FRS integrates facility data from EPA's national program systems, other federal agencies, and State and tribal master facility records and provides EPA with a centrally managed, single source of comprehensive and authoritative information on facilities.   Additional information on FRS is available at the EPA website https://www.epa.gov/enviro/facility-registry-service-frs.",
+            "distribution": [],
+            "identifier": "5559DF41-944C-45F7-9E18-7CF0BBB165B5",
+            "issued": "2016-06-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -289781,87 +289792,85 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Research Triangle Park"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Geospatial Support Team",
-                "hasEmail": "mailto:geoservices@epa.gov"
-            },
-            "identifier": "5559DF41-944C-45F7-9E18-7CF0BBB165B5",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-170.6855, -14.2738, 144.783, 64.997222",
             "temporal": "2020-12-12/2020-12-12",
-            "accrualPeriodicity": "R/P1M",
-            "issued": "2016-06-29",
-            "distribution": []
+            "title": "EPA Facility Registry Service (FRS): OIL OSRO"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Power Plants",
-            "description": "This GIS dataset contains data on power plants, based on the Energy Information Administration's EIA-860 dataset and supplemented with data from EPA's Facility Registry Service (FRS) compiled from various EPA programs.",
-            "keyword": [
-                "020:072",
-                "Facilities",
-                "geospatial",
-                "United States"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2025-01-26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Smith",
                 "hasEmail": "mailto:smith.davidg@epa.gov"
             },
-            "identifier": "87DA7478-01F7-4706-877C-356C048085F4",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-166.479506, 18.9742, -68.147222, 67.08798",
-            "accrualPeriodicity": "R/P1W",
             "describedBy": "https://www.epa.gov/frs/frs-physical-data-model",
+            "description": "This GIS dataset contains data on power plants, based on the Energy Information Administration's EIA-860 dataset and supplemented with data from EPA's Facility Registry Service (FRS) compiled from various EPA programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Zipped file geodatabase",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OEI/FRS/FRS_PowerPlants.zip"
+                    "downloadURL": "https://edg.epa.gov/data/Public/OEI/FRS/FRS_PowerPlants.zip",
+                    "title": "Zipped file geodatabase"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Web Map Service",
                     "accessURL": "https://geodata.epa.gov/arcgis/rest/services/OEI/FRS_PowerPlants/MapServer",
-                    "description": "ArcGIS Server Map/Feature Service"
+                    "description": "ArcGIS Server Map/Feature Service",
+                    "title": "Web Map Service"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Homepage",
-                    "accessURL": "https://www.epa.gov/frs"
+                    "accessURL": "https://www.epa.gov/frs",
+                    "title": "Homepage"
                 }
-            ]
+            ],
+            "identifier": "87DA7478-01F7-4706-877C-356C048085F4",
+            "keyword": [
+                "020:072",
+                "Facilities",
+                "geospatial",
+                "United States"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2025-01-26",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
+            },
+            "spatial": "-166.479506, 18.9742, -68.147222, 67.08798",
+            "title": "EPA Facility Registry Service (FRS): Power Plants"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Wastewater Treatment Plants",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "description": "This GIS dataset contains data on wastewater treatment plants, based on EPA's Facility Registry Service (FRS) and NPDES, along with Clean Watersheds Needs Survey (CWNS) and other data sources.",
+            "distribution": [],
+            "identifier": "\n\t",
             "keyword": [
                 "020:072",
                 "Surface Water",
@@ -289876,32 +289885,32 @@
                 "Contaminant",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2025-01-26",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
+            "spatial": "-176.646252, -14.340056, 174.107672, 71.323851",
+            "title": "EPA Facility Registry Service (FRS): Wastewater Treatment Plants"
         },
-            "identifier": "\n\t",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-176.646252, -14.340056, 174.107672, 71.323851",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Facility Registry Service (FRS): Wastewater Treatment Plants",
             "description": "This GIS dataset contains data on wastewater treatment plants, based on EPA's Facility Registry Service (FRS) and NPDES, along with Clean Watersheds Needs Survey (CWNS) and other data sources.",
+            "distribution": [],
+            "identifier": "\n",
             "keyword": [
                 "020:072",
                 "Surface Water",
@@ -289916,110 +289925,119 @@
                 "Contaminant",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-05-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Environmental Information"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
+            "spatial": "-176.646252, -14.340056, 145.75, 71.323851",
+            "title": "EPA Facility Registry Service (FRS): Wastewater Treatment Plants"
         },
-            "identifier": "\n",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-176.646252, -14.340056, 145.75, 71.323851",
-            "distribution": []
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Access to Jobs and Workers via Transit - Download",
-            "description": "A collection of performance indicators and regional benchmarks for consistently comparing neighborhoods (census block groups) across the US in regards to their accessibility to jobs or workers via public transit service. Accessibility was modeled by calculating total travel time between block group centroids inclusive of walking to/from transit stops, wait times, and transfers. Block groups that can be accessed in 45 minutes or less from the origin block group are considered accessible. Indicators reflect public transit service in December 2012 and employment/worker counts in 2010. Coverage is limited to census block groups within metropolitan regions served by transit agencies who share their service data in a standardized format called GTFS.",
-            "modified": "2014-03-19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John V. Thomas",
                 "hasEmail": "mailto:thomas.john@epa.gov"
             },
-            "identifier": "{8E9DDDA1-1F38-44F0-9114-CD81DC15019A}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "description": "A collection of performance indicators and regional benchmarks for consistently comparing neighborhoods (census block groups) across the US in regards to their accessibility to jobs or workers via public transit service. Accessibility was modeled by calculating total travel time between block group centroids inclusive of walking to/from transit stops, wait times, and transfers. Block groups that can be accessed in 45 minutes or less from the origin block group are considered accessible. Indicators reflect public transit service in December 2012 and employment/worker counts in 2010. Coverage is limited to census block groups within metropolitan regions served by transit agencies who share their service data in a standardized format called GTFS.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OP/SLD/SLD_trans45.zip",
+                    "title": "Download"
+                }
             ],
+            "identifier": "{8E9DDDA1-1F38-44F0-9114-CD81DC15019A}",
+            "issued": "2014-03-19",
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2014-03-19",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
+            },
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014-03-19",
-            "language": "en-us",
             "theme": "transportation",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OP/SLD/SLD_trans45.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Access to Jobs and Workers via Transit - Download"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Access to Jobs and Workers via Transit - Service",
-            "description": "A collection of performance indicators and regional benchmarks for consistently comparing neighborhoods (census block groups) across the US in regards to their accessibility to jobs or workers via public transit service. Accessibility was modeled by calculating total travel time between block group centroids inclusive of walking to/from transit stops, wait times, and transfers. Block groups that can be accessed in 45 minutes or less from the origin block group are considered accessible. Indicators reflect public transit service in December 2012 and employment/worker counts in 2010. Coverage is limited to census block groups within metropolitan regions served by transit agencies who share their service data in a standardized format called GTFS.",
-            "modified": "2014-03-19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
-            },
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John V. Thomas",
                 "hasEmail": "mailto:thomas.john@epa.gov"
             },
-            "identifier": "{09649C32-7B39-4690-BFFB-88B250F6DF1B}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "description": "A collection of performance indicators and regional benchmarks for consistently comparing neighborhoods (census block groups) across the US in regards to their accessibility to jobs or workers via public transit service. Accessibility was modeled by calculating total travel time between block group centroids inclusive of walking to/from transit stops, wait times, and transfers. Block groups that can be accessed in 45 minutes or less from the origin block group are considered accessible. Indicators reflect public transit service in December 2012 and employment/worker counts in 2010. Coverage is limited to census block groups within metropolitan regions served by transit agencies who share their service data in a standardized format called GTFS.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/SLD_Trans45/MapServer",
+                    "title": "Download"
+                }
             ],
+            "identifier": "{09649C32-7B39-4690-BFFB-88B250F6DF1B}",
+            "issued": "2014-03-19",
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2014-03-19",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
+            },
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014-03-19",
-            "language": "en-us",
             "theme": "transportation",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/SLD_Trans45/MapServer",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Access to Jobs and Workers via Transit - Service"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Jobs within a 30-minute transit ride - Download",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John V. Thomas",
+                "hasEmail": "mailto:thomas.john@epa.gov"
+            },
             "description": "A collection of performance indicators for consistently comparing neighborhoods (census block groups) across the US in regards to their accessibility to jobs or workers via public transit service. Accessibility was modeled by calculating total travel time between block group centroids inclusive of walking to/from transit stops, wait times, and transfers. Block groups that can be accessed in 30 minutes or less from the origin block group are considered accessible. Indicators reflect public transit service in December 2012 and employment/worker counts in 2010. Coverage is limited to census block groups within metropolitan regions served by transit agencies who share their service data in a standardized format called GTFS. All variable names refer to variables in EPA's Smart Location Database. For instance EmpTot10_sum summarizes total employment (EmpTot10) in block groups that are reachable within a 30-minute transit and walking commute. See Smart Location Database User Guide for full variable descriptions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OP/SLD/SLD_trans30.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{1B762BFE-5C63-4CA7-81FC-5A7371295A61}",
+            "issued": "2014-03-19",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -290075,71 +290093,71 @@
                 "Transportation",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-03-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John V. Thomas",
-                "hasEmail": "mailto:thomas.john@epa.gov"
-            },
-            "identifier": "{1B762BFE-5C63-4CA7-81FC-5A7371295A61}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014-03-19",
-            "language": "en-us",
             "theme": "transportation",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OP/SLD/SLD_trans30.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Jobs within a 30-minute transit ride - Download"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Jobs Within a 30-minute Transit and Walking Commute",
-            "description": "Jobs Within a 30-minute Transit and Walking Commute",
-            "modified": "2021-10-26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "EPA Data Publishing Organization"
-            },
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EPA Data Publisher",
                 "hasEmail": "mailto:edg@epa.gov"
             },
+            "description": "Jobs Within a 30-minute Transit and Walking Commute",
+            "distribution": [],
             "identifier": "{781BDD8F-2BF4-4072-86E9-FA67BC6C5E8B}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021-10-26",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "EPA Data Publishing Organization"
+            },
             "spatial": "-178.443606, 21.199241, -69.858861, 48.657839",
-            "distribution": []
+            "title": "Jobs Within a 30-minute Transit and Walking Commute"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "NGBS: Points for Smart Location Practices",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Thomas",
+                "hasEmail": "mailto:thomas.john@epa.gov"
+            },
             "description": "These map layers present the number of National Green Building Standard points awarded for a project site or lot\u2019s relative walkability, and accessibility to jobs via transit or within a 45-minute drive. This map presents information on the following criteria included in the 2020 National Green Building Standard: \u2022 Section 405.6(7) - Points for sites located in census block groups with above-average transit access to employment. (See variable D5b in Smart Location Database Technical Documentation and User Guide (2014) for background) \u2022 Section 405.6(8) - Points for sites located in census block groups with above-average access to employment within a 45-minute drive (See variable D5a in Smart Location Database Technical Documentation and User Guide (2014) for background on methods) \u2022 Section 501.2(4) - Points for lots located in census block groups with above-average neighborhood walkability (See National Walkability Index for background on methods) \u2022 Section 11.501.2(3) - Points for lots located in census block groups with above-average neighborhood walkability (See National Walkability Index for background on methods) Using data available through EPA\u2019s Smart Location Database and National Walkability Index, relative walkability and accessibility to jobs via transit or within a 45-minute drive for census block groups were calculated and ranked into quartile groups. The regional comparison was made by considering the score of each individual census block group as a ratio of the average score of the county in which it is located. Those block groups with scores in the highest two quartiles nationally are eligible for NGBS points per the Sections noted above. Details on methodologies and datasets includes in the Smart Location Database and National Walkability Index can be found here: https://www.epa.gov/smartgrowth/smart-location-mapping#SLD",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/NGBS/MapServer",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{D551F0CD-7781-4CD5-8692-06AFB931B3D0}",
+            "issued": "2018-11-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -290202,45 +290220,52 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Thomas",
-                "hasEmail": "mailto:thomas.john@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-180.000000, 2.969871, 180.000000, 90.000000",
+            "temporal": "2006-01-01/2013-01-01",
+            "theme": "health",
+            "title": "NGBS: Points for Smart Location Practices"
         },
-            "identifier": "{D551F0CD-7781-4CD5-8692-06AFB931B3D0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-180.000000, 2.969871, 180.000000, 90.000000",
-            "temporal": "2006-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2018-11-07",
-            "language": "en-us",
-            "theme": "health",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John V. Thomas",
+                "hasEmail": "mailto:thomas.john@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/smartgrowth/smart-location-mapping",
+            "description": "A large body of research has demonstrated that land use and urban form can have a significant effect on transportation outcomes. People who live and/or work in compact neighborhoods with a walkable street grid and easy access to public transit, jobs, stores, and services are more likely to have several transportation options to meet their everyday needs. As a result, they can choose to drive less, which reduces their emissions of greenhouse gases and other pollutants compared to people who live and work in places that are not location efficient. Walking, biking, and taking public transit can also save people money and improve their health by encouraging physical activity.\n\nThe Smart Location Database summarizes several demographic, employment, and built environment variables for every census block group (CBG) in the United States. The database includes indicators of the commonly cited \u201cD\u201d variables shown in the transportation research literature to be related to travel behavior.  The Ds include residential and employment density, land use diversity, design of the built environment, access to destinations, and distance to transit. SLD variables can be used as inputs to travel demand models, baseline data for scenario planning studies, and combined into composite indicators characterizing the relative location efficiency of CBG within U.S. metropolitan regions.\n\nThis update features the most recent geographic boundaries (2019 Census Block Groups) and new and expanded sources of data used to calculate variables. Entirely new variables have been added and the methods used to calculate some of the SLD variables have changed.\n\nMore information on the National Walkability index: https://www.epa.gov/smartgrowth/smart-location-mapping\nMore information on the Smart Location Calculator: https://www.slc.gsa.gov/slc/\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/NGBS/MapServer",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/SLD/SmartLocationDatabaseV3.zip"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Smart Location Database",
-            "description": "A large body of research has demonstrated that land use and urban form can have a significant effect on transportation outcomes. People who live and/or work in compact neighborhoods with a walkable street grid and easy access to public transit, jobs, stores, and services are more likely to have several transportation options to meet their everyday needs. As a result, they can choose to drive less, which reduces their emissions of greenhouse gases and other pollutants compared to people who live and work in places that are not location efficient. Walking, biking, and taking public transit can also save people money and improve their health by encouraging physical activity.\n\nThe Smart Location Database summarizes several demographic, employment, and built environment variables for every census block group (CBG) in the United States. The database includes indicators of the commonly cited \u201cD\u201d variables shown in the transportation research literature to be related to travel behavior.  The Ds include residential and employment density, land use diversity, design of the built environment, access to destinations, and distance to transit. SLD variables can be used as inputs to travel demand models, baseline data for scenario planning studies, and combined into composite indicators characterizing the relative location efficiency of CBG within U.S. metropolitan regions.\n\nThis update features the most recent geographic boundaries (2019 Census Block Groups) and new and expanded sources of data used to calculate variables. Entirely new variables have been added and the methods used to calculate some of the SLD variables have changed.\n\nMore information on the National Walkability index: https://www.epa.gov/smartgrowth/smart-location-mapping\nMore information on the Smart Location Calculator: https://www.slc.gsa.gov/slc/\n",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/SmartLocationDatabase/MapServer"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv"
+                }
+            ],
+            "identifier": "33514B4C-54F2-464A-BCC7-35F441B7E21A",
+            "issued": "2013-07-09",
             "keyword": [
                 "020:072",
                 "Human",
@@ -290250,50 +290275,44 @@
                 "Transportation",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-07-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Policy, Office of Sustainable Communities"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John V. Thomas",
-                "hasEmail": "mailto:thomas.john@epa.gov"
-            },
-            "identifier": "33514B4C-54F2-464A-BCC7-35F441B7E21A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2010/2010",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/smartgrowth/smart-location-mapping",
-            "issued": "2013-07-09",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/SLD/SmartLocationDatabaseV3.zip"
+            "title": "Smart Location Database"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OA/SmartLocationDatabase/MapServer"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Thomas",
+                "hasEmail": "mailto:thomas.john@epa.gov"
             },
+            "describedBy": "https://geodata.epa.gov/arcgis/rest/services/OA/WalkabilityIndex/MapServer",
+            "description": "The Walkability Index dataset characterizes every Census 2019 block group in the U.S. based on its relative walkability. Walkability depends upon characteristics of the built environment that influence the likelihood of walking being used as a mode of travel. The Walkability Index is based on the EPA's previous data product, the Smart Location Database (SLD). Block group data from the SLD was the only input into the Walkability Index, and consisted of four variables from the SLD weighted in a formula to create the new Walkability Index. This dataset shares the SLD's block group boundary definitions from Census 2019. The methodology describing the process of creating the Walkability Index can be found in the documents located at https://edg.epa.gov/EPADataCommons/public/OA/WalkabilityIndex.zip. You can also learn more about the Smart Location Database at https://www.epa.gov/smartgrowth/smart-location-mapping.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/WalkabilityIndex.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Walkability Index",
-            "description": "The Walkability Index dataset characterizes every Census 2019 block group in the U.S. based on its relative walkability. Walkability depends upon characteristics of the built environment that influence the likelihood of walking being used as a mode of travel. The Walkability Index is based on the EPA's previous data product, the Smart Location Database (SLD). Block group data from the SLD was the only input into the Walkability Index, and consisted of four variables from the SLD weighted in a formula to create the new Walkability Index. This dataset shares the SLD's block group boundary definitions from Census 2019. The methodology describing the process of creating the Walkability Index can be found in the documents located at https://edg.epa.gov/EPADataCommons/public/OA/WalkabilityIndex.zip. You can also learn more about the Smart Location Database at https://www.epa.gov/smartgrowth/smart-location-mapping.",
+            ],
+            "identifier": "{251AFDD9-23A7-4068-9B27-A3048A7E6012}",
+            "issued": "2021-05-13",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -290361,92 +290380,92 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-05-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Sustainable Communities"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Thomas",
-                "hasEmail": "mailto:thomas.john@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-180.000000, 2.969871, 180.000000, 90.000000",
+            "temporal": "2019-01-01/9999-01-01",
+            "theme": "health",
+            "title": "Walkability Index"
         },
-            "identifier": "{251AFDD9-23A7-4068-9B27-A3048A7E6012}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-180.000000, 2.969871, 180.000000, 90.000000",
-            "temporal": "2019-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://geodata.epa.gov/arcgis/rest/services/OA/WalkabilityIndex/MapServer",
-            "issued": "2021-05-13",
-            "language": "en-us",
-            "theme": "health",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Stitt",
+                "hasEmail": "mailto:stitt.brian@epa.gov"
+            },
+            "describedBy": "https://www.airnow.gov/index.cfm?action=flag_program.index",
+            "description": "This map service contains participants in EPA's Air Quality Flags Program. The map service also includes the current day's AQI forecast for each participant in the program. The Air Quality Flag Program alerts organizations to the local air quality forecast and helps them to take actions to protect people\u2019s health, including those with asthma. Here's how it works: each day your organization raises a flag that corresponds to how clean or polluted the air is. The color of the flag matches EPA's Air Quality Index (AQI): green, yellow, orange, red, and purple. On unhealthy days, your organization can use this information to adjust physical activities to help reduce exposure to air pollution, while still keeping people active.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/OA/WalkabilityIndex.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://epa.maps.arcgis.com/home/item.html?id=6346986ac0e84a41b54fb51273c48dbc",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Air Quality Flags Program, U.S., 2017, EPA/OAR/OAQPS/OID",
-            "description": "This map service contains participants in EPA's Air Quality Flags Program. The map service also includes the current day's AQI forecast for each participant in the program. The Air Quality Flag Program alerts organizations to the local air quality forecast and helps them to take actions to protect people\u2019s health, including those with asthma. Here's how it works: each day your organization raises a flag that corresponds to how clean or polluted the air is. The color of the flag matches EPA's Air Quality Index (AQI): green, yellow, orange, red, and purple. On unhealthy days, your organization can use this information to adjust physical activities to help reduce exposure to air pollution, while still keeping people active.",
+            ],
+            "identifier": "{7ecec25d-2a8a-47f9-8773-dc8227bbf0d7}",
+            "issued": "2017-04-20",
             "keyword": [
                 "geospatial",
                 "Facilities",
                 "Air",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-04-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Stitt",
-                "hasEmail": "mailto:stitt.brian@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-160.193232, 25.993468, -71.032651, 62.650404",
+            "temporal": "2017-04-20/2017-04-20",
+            "theme": "environment",
+            "title": "Air Quality Flags Program, U.S., 2017, EPA/OAR/OAQPS/OID"
         },
-            "identifier": "{7ecec25d-2a8a-47f9-8773-dc8227bbf0d7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-160.193232, 25.993468, -71.032651, 62.650404",
-            "temporal": "2017-04-20/2017-04-20",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.airnow.gov/index.cfm?action=flag_program.index",
-            "issued": "2017-04-20",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:Cakir.Halil@epa.gov"
+            },
+            "describedBy": "https://www3.epa.gov/airdata/",
+            "description": "This GIS dataset contains points which depict air quality monitors within EPA's Air Quality System (AQS) monitoring network. This dataset is updated weekly to reflect the most recent changes in the monitoring network. The monitors are generally operated by State, local, and tribal air pollution control agencies using procedures specified by the U.S. EPA. These agencies collect the data, quality assure it, and then submit it to the EPA Air Quality System (AQS). The GIS dataset includes monitor information and links to download historic air quality data at each monitor.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://epa.maps.arcgis.com/home/item.html?id=6346986ac0e84a41b54fb51273c48dbc",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Air Quality System (AQS) Monitoring Network, EPA OAR OAQPS",
-            "description": "This GIS dataset contains points which depict air quality monitors within EPA's Air Quality System (AQS) monitoring network. This dataset is updated weekly to reflect the most recent changes in the monitoring network. The monitors are generally operated by State, local, and tribal air pollution control agencies using procedures specified by the U.S. EPA. These agencies collect the data, quality assure it, and then submit it to the EPA Air Quality System (AQS). The GIS dataset includes monitor information and links to download historic air quality data at each monitor.",
+            ],
+            "identifier": "{7BF467D5-A5D7-427B-B896-5674A15B55B4}",
+            "issued": "2015-11-18",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -290512,46 +290531,38 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:Cakir.Halil@epa.gov"
-            },
-            "identifier": "{7BF467D5-A5D7-427B-B896-5674A15B55B4}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-167.803765955, -7.795760124, -58.461724639, 85.322212718",
             "temporal": "2015-11-18/2015-11-18",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www3.epa.gov/airdata/",
-            "issued": "2015-11-18",
-            "language": "en-us",
             "theme": "climatologyMeteorologyAtmosphere",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Air Quality System (AQS) Monitoring Network, EPA OAR OAQPS"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "All Landfills in LMOP Database with Coordinates",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lauren Aepli",
+                "hasEmail": "mailto:lmop@epa.gov"
+            },
             "description": "Feature layer published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows landfills listed in the LMOP Database having latitude and longitude coordinates. Data from the LMOP Database are available at  https://www.epa.gov/lmop/lmop-landfill-and-project-database.",
+            "distribution": [],
+            "identifier": "ea5b52b8ac864cbabc57143b7a1f012e",
+            "issued": "2022-12-12",
             "keyword": [
                 "Air",
                 "Energy",
@@ -290563,36 +290574,36 @@
                 "Sustainability",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-12-12",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Landfill Methane Outreach Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lauren Aepli",
-                "hasEmail": "mailto:lmop@epa.gov"
-            },
-            "identifier": "ea5b52b8ac864cbabc57143b7a1f012e",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-180, -90, 180, 90",
             "temporal": "1994-12-01/2022-08-31",
-            "accrualPeriodicity": "R/P3M",
-            "issued": "2022-12-12",
-            "distribution": []
+            "title": "All Landfills in LMOP Database with Coordinates"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Reported Neuroinvasive Cases of West Nile Virus by State, 2002\u20132023",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Air and Radiation",
+                "hasEmail": "mailto:climateindicators@epa.gov"
+            },
             "description": "This map shows the average annual incidence of neuroinvasive West Nile virus disease in each state, which is calculated as the average number of new cases per 100,000 people per year from 2002 to 2023. The map is based on cases that local and state health departments report to CDC\u2019s national disease tracking system. Neuroinvasive cases are those that affect the brain or cause neurologic dysfunction. For more information: www.epa.gov/climate-indicators",
+            "distribution": [],
+            "identifier": "C756F1ED-4735-46E0-98E1-FBE71BE31726",
+            "issued": "2024-12-23",
             "keyword": [
                 "020:033",
                 "Environment",
@@ -290600,33 +290611,31 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Air and Radiation",
-                "hasEmail": "mailto:climateindicators@epa.gov"
+            "title": "Reported Neuroinvasive Cases of West Nile Virus by State, 2002\u20132023"
         },
-            "identifier": "C756F1ED-4735-46E0-98E1-FBE71BE31726",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "accrualPeriodicity": "irregular",
-            "issued": "2024-12-23",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EPA Data Publisher",
+                "hasEmail": "mailto:edg@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Frequency of Flooding Along U.S. Coasts, 2014\u20132023 Versus 1950\u20131959",
             "description": "This map shows the average number of days per year in which coastal waters rose above the local threshold for minor flooding at 33 sites along the U.S. coast. Each small bar graph compares the first decade of widespread measurements (the 1950s in orange) with the most recent decade (the 2010s in purple). For more information: www.epa.gov/climate-indicators",
+            "distribution": [],
+            "identifier": "frequency-of-flooding-along-u-s-coasts-2014-2023-versus-1950-1959",
             "keyword": [
                 "Other Documents",
                 "Coastal",
@@ -290635,31 +290644,38 @@
                 "Indicator",
                 "Climate"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EPA Data Publishing Organization"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EPA Data Publisher",
-                "hasEmail": "mailto:edg@epa.gov"
+            "title": "Frequency of Flooding Along U.S. Coasts, 2014\u20132023 Versus 1950\u20131959"
         },
-            "identifier": "frequency-of-flooding-along-u-s-coasts-2014-2023-versus-1950-1959",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Average Change in Drought (Five-Year SPEI) in the Contiguous 48 States, 1900\u20132020",
+            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
             "description": "This map shows how drought conditions have changed across the contiguous 48 states from 1900 to 2020. The data are showed for small regions called climate divisions, as defined by the National Oceanic and Atmospheric Administration. Blue areas represent increased moisture; brown areas represent a decrease or drier conditions. For more information: https://www.epa.gov/climatechange/science/indicators.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Drought/MapServer"
+                }
+            ],
+            "identifier": "AAAABAA4-3B0E-401E-AFF4-DA5B51988428",
             "keyword": [
                 "020:033",
                 "Downloadable Data",
@@ -290671,40 +290687,40 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-06-17",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-124.733174, 24.54394, -66.950005, 49.384359",
+            "title": "Average Change in Drought (Five-Year SPEI) in the Contiguous 48 States, 1900\u20132020"
         },
-            "identifier": "AAAABAA4-3B0E-401E-AFF4-DA5B51988428",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-124.733174, 24.54394, -66.950005, 49.384359",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kong Chiu",
+                "hasEmail": "mailto: chiu.kong@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/geospatial/",
+            "description": "This is a coverage shapefile of geologic basin boundaries which are used by EPA's Greenhouse Gas Reporting Program. For onshore production, the \"facility\" includes all emissions associated with wells owned or operated by a single company in a specific hydrocarbon producing basin (as defined by the geologic provinces published by the American Association of Petroleum Geologists). This layer is limited to the contiguous United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Drought/MapServer"
+                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAP/Basins_Shapefile.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Geologic Basin Boundaries (Basins_GHGRP) GIS Layer",
-            "description": "This is a coverage shapefile of geologic basin boundaries which are used by EPA's Greenhouse Gas Reporting Program. For onshore production, the \"facility\" includes all emissions associated with wells owned or operated by a single company in a specific hydrocarbon producing basin (as defined by the geologic provinces published by the American Association of Petroleum Geologists). This layer is limited to the contiguous United States.",
+            ],
+            "identifier": "19F20B68-AEBC-4A16-A59B-BFF5ECB5EEED",
+            "issued": "2017-01-18",
             "keyword": [
                 "020:033",
                 "boundaries",
@@ -290713,41 +290729,37 @@
                 "Facilities",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-01-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kong Chiu",
-                "hasEmail": "mailto: chiu.kong@epa.gov"
-            },
-            "identifier": "19F20B68-AEBC-4A16-A59B-BFF5ECB5EEED",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-126.73828125, 24.5271348226, -62.05078125, 50.0641917367",
             "temporal": "2017-01-18/2017-01-18",
-            "describedBy": "https://www.epa.gov/geospatial/",
-            "issued": "2017-01-18",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAP/Basins_Shapefile.zip"
-                }
-            ]
+            "title": "Geologic Basin Boundaries (Basins_GHGRP) GIS Layer"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in Glacier Surface Area in Glacier National Park, 1966\u20132015",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This map shows the change in surface area of all 37 named glaciers in Glacier National Park for 1966, 1998, 2005, and 2015. The glacier footprints for four different years are laid on top of each other: 2015 is red, 2005 and 1998 are shades of orange, and 1966 is yellow.",
+            "distribution": [],
+            "identifier": "68C2F591-D80C-44B7-8BBC-E3231FC27B7A",
+            "issued": "2018-08-22",
             "keyword": [
                 "020:033",
                 "Montana",
@@ -290756,37 +290768,40 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-08-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "68C2F591-D80C-44B7-8BBC-E3231FC27B7A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-114.475516, 48.233688, -113.241977, 49.000971",
             "temporal": "1966-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2018-08-22",
-            "distribution": []
+            "title": "Change in Glacier Surface Area in Glacier National Park, 1966\u20132015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in Growing Degree Days in the Contiguous 48 States, 1948\u20132020",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
             "description": "This map shows trends in the total number of growing degree days per year at 305 weather stations . The color and size of the symbols represent percent change between 1948 and 2020, based on the long-term average rate of change. For more information: https://www.epa.gov/climatechange/science/indicators.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/GrowingDegreeDays/MapServer"
+                }
+            ],
+            "identifier": "1D491D99-DB00-4B86-BA56-89836ABBF382",
             "keyword": [
                 "020:033",
                 "Downloadable Data",
@@ -290798,39 +290813,35 @@
                 "United States",
                 "Degree-Day"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-06-17",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-124.3539, 26.1019, -70.1564, 48.9672",
+            "title": "Change in Growing Degree Days in the Contiguous 48 States, 1948\u20132020"
         },
-            "identifier": "1D491D99-DB00-4B86-BA56-89836ABBF382",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-124.3539, 26.1019, -70.1564, 48.9672",
-            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/GrowingDegreeDays/MapServer"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Length of Growing Season, 1895\u20132023",
             "description": "This indicator looks at the impact of temperature on the length of the growing season in the contiguous 48 states, as well as trends in the timing of spring and fall frosts. For more information: https://www.epa.gov/climate-indicators.",
+            "distribution": [],
+            "identifier": "45AAE510-4FFB-425E-BEB5-F3D4AEADA536",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -290838,36 +290849,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
-            },
-            "identifier": "45AAE510-4FFB-425E-BEB5-F3D4AEADA536",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-178.217598, 18.921786, -66.969271, 71.406235",
             "temporal": "1895-01-01/2024-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Length of Growing Season, 1895\u20132023"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Heating and Cooling Degree Day by State, 1960\u20132023 Versus 1895\u20131959",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This indicator shows how heating and cooling degree days have changed by state, based on a comparison of the first 65 years of available data (1895\u20131959) with the most recent 64 years (1960\u20132023). For more information: https://www.epa.gov/climate-indicators.   ",
+            "distribution": [],
+            "identifier": "FC1C4D7D-2782-4562-BCF1-975D26D41EA9",
+            "issued": "2019-11-09",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -290875,37 +290887,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
-            },
-            "identifier": "FC1C4D7D-2782-4562-BCF1-975D26D41EA9",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-157.867, 21.3067, -71.0517, 47.60264",
             "temporal": "1950-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2019-11-09",
-            "distribution": []
+            "title": "Heating and Cooling Degree Day by State, 1960\u20132023 Versus 1895\u20131959"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Average Rate of Heat-Related Hospitalizations in 23 States, 2001-2010",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This map shows the 2001\u20132010 average rate of hospitalizations classified as \u201cheat-related\u201d by medical professionals in 23 states that participate in CDC\u2019s hospitalization tracking program. Rates are based on hospital discharge records for May 1 to September 30 of every year. Rates have been age-adjusted to account for differences in the population distribution over time and between states\u2014for example, if one state has a higher proportion of older adults than another. For more information: www.epa.gov/climatechange/science/indicators",
+            "distribution": [],
+            "identifier": "44B8B369-65B5-4B0A-B064-FF2C45C9A17D",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -290913,37 +290925,41 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "44B8B369-65B5-4B0A-B064-FF2C45C9A17D",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-124.73277, 24.956376, -66.969271, 49.37173",
             "temporal": "2001-01-01/2010-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Average Rate of Heat-Related Hospitalizations in 23 States, 2001-2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Heat Wave Characteristics in 50 Large U.S. Cities, 1961\u20132023",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-indicators",
             "description": "These maps show changes in the number of heat waves per year (frequency); the average length of heat waves in days (duration); the number of days between the first and last heat wave of the year (season length); and how hot the heat waves were, compared with the local temperature threshold for defining a heat wave (intensity). These data were analyzed from 1961 to 2023 for 50 large metropolitan areas. The size of each circle indicates the rate of change per decade. Solid-color circles represent cities where the trend was statistically significant. For more information: www.epa.gov/climate-indicators",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/HeatWaves/MapServer"
+                }
+            ],
+            "identifier": "0F13EBA6-F622-4F85-B33B-654FB80A45C1",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -290959,39 +290975,35 @@
                 "Cities",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "spatial": "\n                    ",
+            "title": "Heat Wave Characteristics in 50 Large U.S. Cities, 1961\u20132023"
         },
-            "identifier": "0F13EBA6-F622-4F85-B33B-654FB80A45C1",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "\n                    ",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/HeatWaves/MapServer"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Change in Unusually Hot and Cold Temperatures in the Contiguous 48 States, 1948\u20132023",
+            "describedBy": "https://www.epa.gov/climate-indicators",
             "description": "This map shows trends in unusually hot and cold temperatures at individual weather stations that have operated consistently since 1948. In this case, the term \u201cunusually hot\u201d refers to a daily maximum temperature that is hotter than the 95th percentile temperature during the 1948\u20132023 period. Thus, the maximum temperature on a particular day at a particular station would be considered \u201cunusually hot\u201d if it falls within the warmest 5 percent of measurements at that station during the 1948\u20132023 period. The map shows changes in the total number of days per year that were hotter than the 95th percentile. Red upward-pointing symbols show where these unusually hot days are becoming more common. Blue downward-pointing symbols show where unusually hot days are becoming less common. For more information: www.epa.gov/climate-indicators.",
+            "distribution": [],
+            "identifier": "2C064546-969B-4D3E-9883-939761B6C782",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -290999,37 +291011,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
-            },
-            "identifier": "2C064546-969B-4D3E-9883-939761B6C782",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-124.3539, 24.555, -66.9919, 48.9994",
             "temporal": "1948-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Change in Unusually Hot and Cold Temperatures in the Contiguous 48 States, 1948\u20132023"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in Ice Thaw Dates for Selected U.S. Lakes, 1905-2019",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-indicators",
             "description": "This figure shows the change in the \"ice-off\" date, or date of ice thawing and breakup, for 14 U.S. lakes during the period from 1905 to 2019. All of the lakes have red circles with negative numbers, which represent earlier thaw dates. Larger circles indicate larger changes. For more information: www.epa.gov/climatechange/science/indicators",
+            "distribution": [],
+            "identifier": "50E386A3-7770-4487-A4D9-693F8FC76924",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -291037,37 +291049,36 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "50E386A3-7770-4487-A4D9-693F8FC76924",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-95.93333, 42.57, -69.47917, 46.81",
             "temporal": "1905-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Change in Ice Thaw Dates for Selected U.S. Lakes, 1905-2019"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in Summer Surface Water Temperatures of North American Lakes, 1985-2009",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MIke Kolian",
+                "hasEmail": "mailto:climateindicators@epa.gov"
+            },
             "description": "This map shows the total change in the average July\u2013September surface water temperatures in 34 North American lakes from 1985 to 2009, as measured by satellites. Red circles represent warming; blue circles represent cooling. Larger circles indicate larger changes. Circles with black borders represent lakes where the trend was statistically significant.",
+            "distribution": [],
+            "identifier": "3DC9350E-F673-4683-9F72-0775A7416D9A",
+            "issued": "2018-08-22",
             "keyword": [
                 "Air",
                 "020:033",
@@ -291077,77 +291088,36 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-08-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Atmospheric Programs, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "MIke Kolian",
-                "hasEmail": "mailto:climateindicators@epa.gov"
-            },
-            "identifier": "3DC9350E-F673-4683-9F72-0775A7416D9A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-160.52, 33.23, -60.79, 66.47",
             "temporal": "None/2009-01-01T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2018-08-22",
-            "distribution": []
+            "title": "Change in Summer Surface Water Temperatures of North American Lakes, 1985-2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Landfill Gas Energy Projects and Landfills in LMOP Database",
-            "description": "Web map published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows currently operational landfill gas energy projects and landfills listed in the LMOP Database having latitude and longitude coordinates. Data for operational projects are provided in 4 layers by Project Type Category (electricity, direct use, RNG pipeline injection, and RNG local use). Data for landfills are provided in 3 layers by Landfill Category (candidate, with project, and other). LMOP defines a candidate landfill as one that is accepting waste or has been closed for five years or less, has at least one million tons of waste, and does not have an operational, under-construction, or planned project; candidate landfills can also be designated based on actual interest in the site. The map also incorporates environmental justice (EJ) demographic layers and Tribal data layers, so that users can identify these areas as they review landfill and project locations.Data from the LMOP Database are available at https://www.epa.gov/lmop/lmop-landfill-and-project-database. EJScreen is available at https://www.epa.gov/ejscreen. The Tribal layer data are available at https://geopub.epa.gov/arcgis/rest/services/EMEF/Tribal/MapServer.",
-            "keyword": [
-                "Air",
-                "Energy",
-                "Environment",
-                "Waste",
-                "Climate Change",
-                "020:000",
-                "geospatial",
-                "Sustainability",
-                "United States"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2022-12-12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US EPA Landfill Methane Outreach Program"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lauren Aepli",
                 "hasEmail": "mailto:lmop@epa.gov"
             },
+            "description": "Web map published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows currently operational landfill gas energy projects and landfills listed in the LMOP Database having latitude and longitude coordinates. Data for operational projects are provided in 4 layers by Project Type Category (electricity, direct use, RNG pipeline injection, and RNG local use). Data for landfills are provided in 3 layers by Landfill Category (candidate, with project, and other). LMOP defines a candidate landfill as one that is accepting waste or has been closed for five years or less, has at least one million tons of waste, and does not have an operational, under-construction, or planned project; candidate landfills can also be designated based on actual interest in the site. The map also incorporates environmental justice (EJ) demographic layers and Tribal data layers, so that users can identify these areas as they review landfill and project locations.Data from the LMOP Database are available at https://www.epa.gov/lmop/lmop-landfill-and-project-database. EJScreen is available at https://www.epa.gov/ejscreen. The Tribal layer data are available at https://geopub.epa.gov/arcgis/rest/services/EMEF/Tribal/MapServer.",
+            "distribution": [],
             "identifier": "cfb50984b19d463f89082489a1a61558",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-156.4744, -4.2302, -26.6599, 58.0698",
-            "temporal": "1994-12-01/2022-08-31",
-            "accrualPeriodicity": "R/P3M",
             "issued": "2022-12-12",
-            "distribution": []
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Map of Landfill Gas Energy Projects and Landfills in LMOP Database for Homepage",
-            "description": "Web map published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows currently operational landfill gas energy projects and landfills listed in the LMOP Database having latitude and longitude coordinates. Data for operational projects are provided in 4 layers by Project Type Category (electricity, direct use, RNG pipeline injection, and RNG local use). Data from the LMOP Database are available at https://www.epa.gov/lmop/lmop-landfill-and-project-database.",
             "keyword": [
                 "Air",
                 "Energy",
@@ -291159,36 +291129,78 @@
                 "Sustainability",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-12-12",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA Landfill Methane Outreach Program"
             },
-            "contactPoint": {
+            "rights": "licenseUnrestricted",
+            "spatial": "-156.4744, -4.2302, -26.6599, 58.0698",
+            "temporal": "1994-12-01/2022-08-31",
+            "title": "Landfill Gas Energy Projects and Landfills in LMOP Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lauren Aepli",
                 "hasEmail": "mailto:lmop@epa.gov"
             },
+            "description": "Web map published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows currently operational landfill gas energy projects and landfills listed in the LMOP Database having latitude and longitude coordinates. Data for operational projects are provided in 4 layers by Project Type Category (electricity, direct use, RNG pipeline injection, and RNG local use). Data from the LMOP Database are available at https://www.epa.gov/lmop/lmop-landfill-and-project-database.",
+            "distribution": [],
             "identifier": "cbdcda405d514c94abf45e797205967a",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "issued": "2022-12-12",
+            "keyword": [
+                "Air",
+                "Energy",
+                "Environment",
+                "Waste",
+                "Climate Change",
+                "020:000",
+                "geospatial",
+                "Sustainability",
+                "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2022-12-12",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US EPA Landfill Methane Outreach Program"
+            },
             "rights": "licenseUnrestricted",
             "spatial": "-156.4744, -4.2302, -26.6599, 58.0698",
             "temporal": "1994-12-01/2022-08-31",
-            "accrualPeriodicity": "R/P3M",
-            "issued": "2022-12-12",
-            "distribution": []
+            "title": "Map of Landfill Gas Energy Projects and Landfills in LMOP Database for Homepage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in First Leaf and Bloom Dates Between 1951\u20131960 and 2014\u20132023",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-change",
             "description": "This indicator shows modeled trends in lilac and honeysuckle first leaf dates at weather stations across the contiguous 48 states. This map compares the average first leaf date during two 10-year periods, developed using data from the USA National Phenology Network. Blue circles represent later leaf dates, and red circles represent earlier. For more information:  https://www.epa.gov/climate-indicators",
+            "distribution": [],
+            "identifier": "7E337966-74D0-4EF3-99DD-B7FB46EBFD2",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -291196,37 +291208,36 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
-            },
-            "identifier": "7E337966-74D0-4EF3-99DD-B7FB46EBFD2",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-124.4, 25.92, -67.4, 49",
             "temporal": "1951-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climate-change",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Change in First Leaf and Bloom Dates Between 1951\u20131960 and 2014\u20132023"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Operational Landfill Gas Energy Projects with Coordinates",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lauren Aepli",
+                "hasEmail": "mailto:lmop@epa.gov"
+            },
             "description": "Feature layer published by the U.S. EPA Landfill Methane Outreach Program (LMOP) that shows currently operational landfill gas energy projects in the United States. Data from the LMOP Database are available at https://www.epa.gov/lmop/lmop-landfill-and-project-database.",
+            "distribution": [],
+            "identifier": "d840ee5e49af490fbadec3a59372e645",
+            "issued": "2022-12-12",
             "keyword": [
                 "Air",
                 "Energy",
@@ -291238,36 +291249,40 @@
                 "Sustainability",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-12-12",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA Landfill Methane Outreach Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lauren Aepli",
-                "hasEmail": "mailto:lmop@epa.gov"
-            },
-            "identifier": "d840ee5e49af490fbadec3a59372e645",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-180, -90, 180, 90",
             "temporal": "1994-12-01/2022-08-31",
-            "accrualPeriodicity": "R/P3M",
-            "issued": "2022-12-12",
-            "distribution": []
+            "title": "Operational Landfill Gas Energy Projects with Coordinates"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in Permafrost Temperatures in Alaska, 1978-2023",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Air and Radiation",
+                "hasEmail": "mailto:climateindicators@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
             "description": "This map shows the change in permafrost temperature per decade for long-term borehole sites in Alaska. As the circles get larger, the rate of warming per decade increases. The blue circle represents a cooling trend. For more information: https://www.epa.gov/climatechange/science/indicators.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Permafrost/MapServer"
+                }
+            ],
+            "identifier": "D644FD2F-5555-4AB4-9A8D-B32FB8CF56EE",
             "keyword": [
                 "020:033",
                 "Melt",
@@ -291279,39 +291294,40 @@
                 "Thaw",
                 "Alaska"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Air and Radiation",
-                "hasEmail": "mailto:climateindicators@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-156.6615, 62.1669, -143.6285, 71.309",
+            "title": "Change in Permafrost Temperatures in Alaska, 1978-2023"
         },
-            "identifier": "D644FD2F-5555-4AB4-9A8D-B32FB8CF56EE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-156.6615, 62.1669, -143.6285, 71.309",
-            "describedBy": "https://www.epa.gov/climatechange/science/indicators",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-change",
+            "description": "This indicator shows the rate of change in total annual precipitation in different parts of the United States since the early 20th century (since 1901 for the contiguous 48 states and 1925 for Alaska). The data are shown for climate divisions, as defined by the National Oceanic and Atmospheric Administration. For more information: www.epa.gov/climate-indicators",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Permafrost/MapServer"
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/US_Precipitation/MapServer"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Precipitation, 1901\u20132023",
-            "description": "This indicator shows the rate of change in total annual precipitation in different parts of the United States since the early 20th century (since 1901 for the contiguous 48 states and 1925 for Alaska). The data are shown for climate divisions, as defined by the National Oceanic and Atmospheric Administration. For more information: www.epa.gov/climate-indicators",
+            ],
+            "identifier": "BDD5DD12-4942-41A6-B47D-9C2459F28A0A",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -291326,39 +291342,35 @@
                 "Precipitation",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Atmospheric Programs, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "rights": "licenseUnrestricted",
+            "title": "U.S. Precipitation, 1901\u20132023"
         },
-            "identifier": "BDD5DD12-4942-41A6-B47D-9C2459F28A0A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-change",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/US_Precipitation/MapServer"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Change in Ragweed Pollen Season, 1995-2015",
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This figure shows how the length of ragweed pollen season changed at 11 locations in the central United States and Canada between 1995 and 2015. Data were provided by Dr. Lewis Ziska of the U.S. Department of Agriculture, Agricultural Research Service. Red circles represent a longer pollen season; the blue circle represents a shorter season. Larger circles indicate larger changes. For more information: www.epa.gov/climatechange/science/indicators",
+            "distribution": [],
+            "identifier": "8A53C09B-FAE2-419C-88EC-154EE3198792",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "Air",
@@ -291367,37 +291379,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "8A53C09B-FAE2-419C-88EC-154EE3198792",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-106.647675, 30.632711, -89.401244, 52.134392",
             "temporal": "1995-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Change in Ragweed Pollen Season, 1995-2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Change in the Magnitude of River Flooding in the United States, 1965-2015",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This figure shows changes in the size and frequency of flooding events in rivers and streams in the United States between 1965 and 2015. Blue upward-pointing symbols show locations where floods have become larger; brown downward-pointing symbols show locations where floods have become smaller. Data were analyzed by Louise Slater and Gabriele Villarini at the University of Iowa. For more information: www.epa.gov/climatechange/science/indicators",
+            "distribution": [],
+            "identifier": "E8C38173-E457-463C-BEAC-80ACCB5FB29E",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "Air",
@@ -291406,37 +291418,41 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "E8C38173-E457-463C-BEAC-80ACCB5FB29E",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-159.61998, 18.032464, -66.032387, 64.902374",
             "temporal": "1965-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Change in the Magnitude of River Flooding in the United States, 1965-2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Relative Sea Level Change Along U.S. Coasts, 1960-2023",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-change",
             "description": "This map shows the change in relative sea level at 72 locations along the U.S. Coasts from 1960 - 2023. Arrows pointing up indicate an increase in sea level height (in inches) over time and arrows pointing down, a decrease. The different color and size of the arrows represent the amount of change in the height. For more information: www.epa.gov/climate-indicators",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/SeaLevel/MapServer"
+                }
+            ],
+            "identifier": "BF03ABEF-97B4-4AE6-9346-BDC11C300693",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -291447,39 +291463,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Atmospheric Programs, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "rights": "licenseUnrestricted",
+            "title": "Relative Sea Level Change Along U.S. Coasts, 1960-2023"
         },
-            "identifier": "BF03ABEF-97B4-4AE6-9346-BDC11C300693",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-change",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "description": "Full Metadata These maps show the total change in the average seasonal temperature for each of the contiguous 48 states from 1896 to 2023, in degrees Fahrenheit. Total change in temperature was calculated from the long-term average rate of change. The three-month seasons are defined as follows: winter (December, January, February), spring (March, April, May), summer (June, July, August), and fall (September, October, November). For more information: www.epa.gov/climate-indicators",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/SeaLevel/MapServer"
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/SeasonalTemperature/MapServer"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Change in Seasonal Temperature by State 1896-2023",
-            "description": "Full Metadata These maps show the total change in the average seasonal temperature for each of the contiguous 48 states from 1896 to 2023, in degrees Fahrenheit. Total change in temperature was calculated from the long-term average rate of change. The three-month seasons are defined as follows: winter (December, January, February), spring (March, April, May), summer (June, July, August), and fall (September, October, November). For more information: www.epa.gov/climate-indicators",
+            ],
+            "identifier": "98D2EA35-78A1-47C8-AA5D-EC9301A70A1E",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -291491,37 +291505,40 @@
                 "Seasons",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Atmospheric Programs, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "rights": "licenseUnrestricted",
+            "title": "Change in Seasonal Temperature by State 1896-2023"
         },
-            "identifier": "98D2EA35-78A1-47C8-AA5D-EC9301A70A1E",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Air and Radiation",
+                "hasEmail": "mailto:climateindicators@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
+            "description": "This indicator shows the average rate of change in total snowfall from 1930 to 2007 at 419 weather stations in the contiguous 48 states. Blue circles represent increased snowfall; red circles represent a decrease. This indicator also shows the percentage change in winter snow-to-precipitation ratio from 1949 to 2024 at 170 weather stations in the contiguous 48 states. This ratio measures what percentage of total winter precipitation falls in the form of snow. A decrease (red circle) indicates that more precipitation is falling in the form of rain instead of snow. Blue circles indicate more precipitation is falling in the form of snow instead of rain. For more information: https://www.epa.gov/climate-indicators.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/SeasonalTemperature/MapServer"
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Snowfall_Indicators/MapServer"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Change in Snowfall",
-            "description": "This indicator shows the average rate of change in total snowfall from 1930 to 2007 at 419 weather stations in the contiguous 48 states. Blue circles represent increased snowfall; red circles represent a decrease. This indicator also shows the percentage change in winter snow-to-precipitation ratio from 1949 to 2024 at 170 weather stations in the contiguous 48 states. This ratio measures what percentage of total winter precipitation falls in the form of snow. A decrease (red circle) indicates that more precipitation is falling in the form of rain instead of snow. Blue circles indicate more precipitation is falling in the form of snow instead of rain. For more information: https://www.epa.gov/climate-indicators.",
+            ],
+            "identifier": "9BAE40D8-2B7E-42E4-82B3-01076FB7129C",
+            "issued": "2016-08-02",
             "keyword": [
                 "Air",
                 "020:033",
@@ -291532,42 +291549,41 @@
                 "Precipitation",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Air and Radiation",
-                "hasEmail": "mailto:climateindicators@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-124.37, 31.95, -69.72, 48.98",
+            "temporal": "1930-01-01/2007-01-01",
+            "title": "Change in Snowfall"
         },
-            "identifier": "9BAE40D8-2B7E-42E4-82B3-01076FB7129C",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-124.37, 31.95, -69.72, 48.98",
-            "temporal": "1930-01-01/2007-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2016-08-02",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-indicators",
+            "description": "This indicator shows trends in snowpack amounts as well as change in peak date of annual snowpack at measurement sites in the western United States. For more information: www.epa.gov/climate-indicators",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Snowfall_Indicators/MapServer"
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Snowpack/MapServer"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Trends in Amount and Timing of Snowpack in the Western United States",
-            "description": "This indicator shows trends in snowpack amounts as well as change in peak date of annual snowpack at measurement sites in the western United States. For more information: www.epa.gov/climate-indicators",
+            ],
+            "identifier": "7D04F8A8-947C-457A-9628-BF74FA5CEB97",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -291579,39 +291595,34 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "spatial": "\n                    ",
+            "title": "Trends in Amount and Timing of Snowpack in the Western United States"
         },
-            "identifier": "7D04F8A8-947C-457A-9628-BF74FA5CEB97",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "\n                    ",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Snowpack/MapServer"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "USEPA",
+                "hasEmail": "mailto:climateindicators@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Average Temperatures in the Southwestern United States, 2000\u20132023 Versus Long-Term Average",
+            "describedBy": "https://www.epa.gov/climate-indicators",
             "description": "This indicator shows how the average air temperature from 2000 to 2023 has differed from the long-term average (1895 - 2023). To provide more detailed information, each state has been divided into climate divisions, which are zones that share similar climate features. For more information: https://www.epa.gov/climate-indicators.",
+            "distribution": [],
+            "identifier": "E06B9849-A8D5-4A92-9D3F-3DDF86E925BB",
+            "issued": "2019-11-18",
             "keyword": [
                 "Meteorology",
                 "020:033",
@@ -291625,35 +291636,36 @@
                 "Climatology",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "USEPA",
-                "hasEmail": "mailto:climateindicators@epa.gov"
+            "spatial": "-124.409721, 31.332178, -102.041486, 42.009519",
+            "temporal": "1895-01-01T00:00:00/2023-12-31T00:00:00",
+            "title": "Average Temperatures in the Southwestern United States, 2000\u20132023 Versus Long-Term Average"
         },
-            "identifier": "E06B9849-A8D5-4A92-9D3F-3DDF86E925BB",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-124.409721, 31.332178, -102.041486, 42.009519",
-            "temporal": "1895-01-01T00:00:00/2023-12-31T00:00:00",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "issued": "2019-11-18",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Streamflow in the United States, 1940\u20132022",
+            "describedBy": "https://www.epa.gov/climate-indicators",
             "description": "This map shows percentage changes in the minimum annual rate of water carried by rivers and streams across the country, based on the long-term rate of change from 1940 to 2022. For more information: https://www.epa.gov/climate-indicators.",
+            "distribution": [],
+            "identifier": "0599E344-4682-479D-9334-78FE576E2881",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -291661,37 +291673,37 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
-            },
-            "identifier": "0599E344-4682-479D-9334-78FE576E2881",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-159.61998, 20.80686, -68.30596, 55.3916",
             "temporal": "1940-01-01/2014-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climate-indicators",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Streamflow in the United States, 1940\u20132022"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Changes in Stream Water Temperatures in the Chesapeake Bay Region, 1960-2014",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kolian",
+                "hasEmail": "mailto:kolian.michael@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climatechange",
             "description": "This map shows the changes in stream water temperatures in the Chesapeake Bay region from 1960 to 2014. Blue circles represent cooling trends in stream water temperatures, and red circles represent warming trends in stream water temperatures. Data were analyzed by Mike Kolian of EPA in partnership with John Jastram and Karen Rice of the U.S. Geological Survey. For more information: www.epa.gov/climatechange/science/indicators",
+            "distribution": [],
+            "identifier": "E3CB0878-2DAD-4783-BA92-0B3049FF13DF",
+            "issued": "2016-08-02",
             "keyword": [
                 "020:033",
                 "geospatial",
@@ -291699,37 +291711,41 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kolian",
-                "hasEmail": "mailto:kolian.michael@epa.gov"
-            },
-            "identifier": "E3CB0878-2DAD-4783-BA92-0B3049FF13DF",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-82.296, 36.717, -75.117, 41.997",
             "temporal": "1960-01-01/2014-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://www.epa.gov/climatechange",
-            "issued": "2016-08-02",
-            "distribution": []
+            "title": "Changes in Stream Water Temperatures in the Chesapeake Bay Region, 1960-2014"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Temperature, 1901\u20132023",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-change",
             "description": "This indicator shows how annual average air temperatures have changed in different parts of the United States since the early 20th century (since 1901 for the contiguous 48 states and 1925 for Alaska). The data are shown for climate divisions, as defined by the National Oceanic and Atmospheric Administration. For more information: www.epa.gov/climate-indicators",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/US_Temperature/MapServer"
+                }
+            ],
+            "identifier": "CFC1A18F-778F-44C5-A691-57781C0D95F0",
             "keyword": [
                 "020:072",
                 "Other Documents",
@@ -291744,39 +291760,39 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Atmospheric Programs, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "rights": "licenseUnrestricted",
+            "title": "U.S. Temperature, 1901\u20132023"
         },
-            "identifier": "CFC1A18F-778F-44C5-A691-57781C0D95F0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-change",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lisa Bacanskas",
+                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/climate-indicators",
+            "description": "This indicator tracks the extent and severity of wildfires in the United States. One map shows the average annual burned acreage by state, while the other map shows the change in annual burned acreage by state between 1984-2002 and 2003-2021. For more information: www.epa.gov/climate-indicators",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/US_Temperature/MapServer"
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Wildfires/MapServer"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wildfires, 1984\u20132021",
-            "description": "This indicator tracks the extent and severity of wildfires in the United States. One map shows the average annual burned acreage by state, while the other map shows the change in annual burned acreage by state between 1984-2002 and 2003-2021. For more information: www.epa.gov/climate-indicators",
+            ],
+            "identifier": "50995AB9-C7F4-4163-8E9A-E8470083C429",
             "keyword": [
                 "020:072",
                 "Wildfires",
@@ -291788,39 +291804,41 @@
                 "Climate",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-06-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lisa Bacanskas",
-                "hasEmail": "mailto:bacanskas.lisa@epa.gov"
+            "spatial": "\n                    ",
+            "title": "Wildfires, 1984\u20132021"
         },
-            "identifier": "50995AB9-C7F4-4163-8E9A-E8470083C429",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "\n                    ",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/climate-indicators",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "description": "This downloadable package contains the following layers: Mandatory Class 1 Federal Area polygons in the United States. Included in this package are a file geodatabase, Esri ArcMap map document and an XML file of this metadata record. This dataset was developed by EPA's Office of Air Quality Planning and Standards (OAQPS) based on features originating from several data sources, including USEPA, USFS, USFWS, NPS and BIA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OAR_OAP/Wildfires/MapServer"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/OAR/OAQPS/Class1/Class1Areas.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mandatory Class 1 Federal Areas Download Package",
-            "description": "This downloadable package contains the following layers: Mandatory Class 1 Federal Area polygons in the United States. Included in this package are a file geodatabase, Esri ArcMap map document and an XML file of this metadata record. This dataset was developed by EPA's Office of Air Quality Planning and Standards (OAQPS) based on features originating from several data sources, including USEPA, USFS, USFWS, NPS and BIA.",
+            ],
+            "identifier": "mandatory-class-1-federal-areas-download-package",
+            "issued": "2015-09-22",
             "keyword": [
                 "Texas",
                 "California",
@@ -291868,45 +291886,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-09-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-09-22/2015-09-22",
+            "theme": "boundaries",
+            "title": "Mandatory Class 1 Federal Areas Download Package"
         },
-            "identifier": "mandatory-class-1-federal-areas-download-package",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-09-22/2015-09-22",
-            "accrualPeriodicity": "irregular",
-            "issued": "2015-09-22",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "description": "This web service contains the following layers: Mandatory Class 1 Federal Area polygons and Mandatory Class 1 Federal Area labels in the United States. The polygon layer draws at all scales. The labels draw at scales greater than or equal to 1:3 million. Data used to create this web service are available as a separate download at the secondary linkage listed above. Full FGDC metadata are available by clicking the layer name in the web service table of contents and clicking the Full Metadata link in the layer description. This dataset was developed by EPA's Office of Air Quality Planning and Standards (OAQPS) based on features originating from several data sources, including USEPA, USFS, USFWS, NPS and BIA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/OAR/OAQPS/Class1/Class1Areas.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mandatory Class 1 Federal Areas Web Service",
-            "description": "This web service contains the following layers: Mandatory Class 1 Federal Area polygons and Mandatory Class 1 Federal Area labels in the United States. The polygon layer draws at all scales. The labels draw at scales greater than or equal to 1:3 million. Data used to create this web service are available as a separate download at the secondary linkage listed above. Full FGDC metadata are available by clicking the layer name in the web service table of contents and clicking the Full Metadata link in the layer description. This dataset was developed by EPA's Office of Air Quality Planning and Standards (OAQPS) based on features originating from several data sources, including USEPA, USFS, USFWS, NPS and BIA.",
+            ],
+            "identifier": "mandatory-class-1-federal-areas-web-service",
+            "issued": "2015-09-22",
             "keyword": [
                 "Texas",
                 "California",
@@ -291954,80 +291972,81 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-09-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
-            },
-            "identifier": "mandatory-class-1-federal-areas-web-service",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-09-22/2015-09-22",
-            "accrualPeriodicity": "irregular",
-            "issued": "2015-09-22",
-            "language": "en-us",
             "theme": "boundaries",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/OAR/OAQPS/Class1/Class1Areas.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Mandatory Class 1 Federal Areas Web Service"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "2012 and 2013 Air Quality Fused Surface for the Conterminous U.S. Map Service",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Stitt",
+                "hasEmail": "mailto:stitt.brian@epa.gov"
+            },
             "description": "This web service contains a polygon layer that depicts fused air quality predictions for 2012, 2013, and 2014 for census tracts in the conterminous United States. Fused air quality predictions (for ozone and PM2.5) are modeled using a Bayesian space-time downscaling fusion model approach described in a series of three published journal papers: 1) (Berrocal, V., Gelfand, A. E. and Holland, D. M. (2012). Space-time fusion under error in computer model output: an application to modeling air quality. Biometrics 68, 837-848; 2) Berrocal, V., Gelfand, A. E. and Holland, D. M. (2010). A bivariate space-time downscaler under space and time misalignment. The Annals of Applied Statistics 4, 1942-1975; and 3) Berrocal, V., Gelfand, A. E., and Holland, D. M. (2010). A spatio-temporal downscaler for output from numerical models. J. of Agricultural, Biological,and Environmental Statistics 15, 176-197) is used to provide daily, predictive PM2.5 (daily average) and O3 (daily 8-hr maximum) surfaces for 2012, 2013, and 2014. Summer (O3) and annual (PM2.5) means calculated and published. The downscaling fusion model uses both air quality monitoring data from the National Air Monitoring Stations/State and Local Air Monitoring Stations (NAMS/SLAMS) and numerical output from the Models-3/Community Multiscale Air Quality (CMAQ). Currently, predictions at the US census tract centroid locations within the 12 km CMAQ domain are archived. Predictions at the CMAQ grid cell centroids, or any desired set of locations could be provided if needed. Predictions are not provided on December 31st of any year because complete daily CMAQ output are not available on those days after conversion of GMT to local eastern time.",
+            "distribution": [],
+            "identifier": "a7fd531c-b6ed-4edd-8b6d-20a28d71270f",
+            "issued": "2016-06-15",
             "keyword": [
                 "020:072",
                 "geospatial",
                 "Air",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-06-15",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Stitt",
-                "hasEmail": "mailto:stitt.brian@epa.gov"
-            },
-            "identifier": "a7fd531c-b6ed-4edd-8b6d-20a28d71270f",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2012-01-01/2014-01-01",
-            "issued": "2016-06-15",
-            "distribution": []
+            "title": "2012 and 2013 Air Quality Fused Surface for the Conterminous U.S. Map Service"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-PM10 (1987 NAAQS)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
             "description": "This web service contains the following layer: PM10 Nonattainment Areas (1987 NAAQS). Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA1987PM10/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www.epa.gov/approved-sips/regional-sip-coordinators. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{F335092D-E644-4967-8226-520172B3097E}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292093,46 +292112,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-PM10 (1987 NAAQS)"
         },
-            "identifier": "{F335092D-E644-4967-8226-520172B3097E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/oar/oaqps/greenbk/regcntct.html",
+            "description": "This web service layer, Carbon Monoxide (1990 NAAQS), displays identified state level areas where carbon monoxide pollution has not met the National Ambient Air Quality Standards (NAAQS) established in 1990 for and have been designated \"nonattainment\u201d areas (NAA)\". Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www.epa.gov/oar/oaqps/greenbk/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/oar/oaqps/greenbk/regcntct.html). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://arcg.is/1Lq9Vp2",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations - Carbon Monoxide (1990 NAAQS) - Web Service Layer",
-            "description": "This web service layer, Carbon Monoxide (1990 NAAQS), displays identified state level areas where carbon monoxide pollution has not met the National Ambient Air Quality Standards (NAAQS) established in 1990 for and have been designated \"nonattainment\u201d areas (NAA)\". Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www.epa.gov/oar/oaqps/greenbk/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/oar/oaqps/greenbk/regcntct.html). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "us-epa-nonattainment-areas-and-designations-carbon-monoxide-1990-naaqs-web-service-layer",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292198,46 +292217,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations - Carbon Monoxide (1990 NAAQS) - Web Service Layer"
         },
-            "identifier": "us-epa-nonattainment-areas-and-designations-carbon-monoxide-1990-naaqs-web-service-layer",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www.epa.gov/oar/oaqps/greenbk/regcntct.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
+            "description": "This web service contains the following layers: Ozone 1997 NAAQS NAA State Level and Ozone 1997 NAAQS NAA National Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA1997Ozone8hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://arcg.is/1Lq9Vp2",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (1997 NAAQS)",
-            "description": "This web service contains the following layers: Ozone 1997 NAAQS NAA State Level and Ozone 1997 NAAQS NAA National Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA1997Ozone8hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{4EF36438-8026-4B6F-863F-62DBD9F9010C}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292303,46 +292322,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (1997 NAAQS)"
         },
-            "identifier": "{4EF36438-8026-4B6F-863F-62DBD9F9010C}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
             "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This web service contains the following layers: PM2.5 Annual 1997 NAAQS State Level and PM2.5 Annual 1997 NAAQS National . It also contains the following tables: maps99.FRED_MAP_VIEWER.%fred_area_map_data and maps99.FRED_MAP_VIEWER.%fred_area_map_view. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA1997PM25Annual/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \u201cattainment\u201d (meeting), \u201cnonattainment\u201d (not meeting), or \u201cunclassifiable\u201d (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-Annual PM2.5 (1997 NAAQS)",
-            "description": "This web service contains the following layers: PM2.5 Annual 1997 NAAQS State Level and PM2.5 Annual 1997 NAAQS National . It also contains the following tables: maps99.FRED_MAP_VIEWER.%fred_area_map_data and maps99.FRED_MAP_VIEWER.%fred_area_map_view. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA1997PM25Annual/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \u201cattainment\u201d (meeting), \u201cnonattainment\u201d (not meeting), or \u201cunclassifiable\u201d (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{8B003F09-7FB4-4D8E-BD27-5B3E6D31899A}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292408,46 +292427,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-Annual PM2.5 (1997 NAAQS)"
         },
-            "identifier": "{8B003F09-7FB4-4D8E-BD27-5B3E6D31899A}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/approved-sips/regional-sip-coordinators",
+            "description": "This web service contains the following layers: PM2.5 24hr 2006 NAAQS State Level and PM2.5 24hr 2006 NAAQS National. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2006PM2524hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-24 Hour PM2.5 (2006 NAAQS)",
-            "description": "This web service contains the following layers: PM2.5 24hr 2006 NAAQS State Level and PM2.5 24hr 2006 NAAQS National. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2006PM2524hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{BB79CB7F-6C4C-4CF3-8DD9-35B5A4718337}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292513,46 +292532,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-24 Hour PM2.5 (2006 NAAQS)"
         },
-            "identifier": "{BB79CB7F-6C4C-4CF3-8DD9-35B5A4718337}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www.epa.gov/approved-sips/regional-sip-coordinators",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
+            "description": "This web service contains the following layers: Lead NAA 2008 NAAQS and Lead NAA Centroids 2008 NAAQS. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2008Lead/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-Lead (2008 NAAQS)",
-            "description": "This web service contains the following layers: Lead NAA 2008 NAAQS and Lead NAA Centroids 2008 NAAQS. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2008Lead/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{BCE9E778-C0CD-4468-8234-F90ACEF43C24}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292618,46 +292637,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-Lead (2008 NAAQS)"
         },
-            "identifier": "{BCE9E778-C0CD-4468-8234-F90ACEF43C24}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
             "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This web service contains the following layers: Ozone 2008 NAAQS NAA State Level and Ozone 2008 NAAQS NAA National Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2008Ozone8hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (2008 NAAQS)",
-            "description": "This web service contains the following layers: Ozone 2008 NAAQS NAA State Level and Ozone 2008 NAAQS NAA National Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2008Ozone8hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{448451DF-30E7-4B29-9A08-B3F7A68870BE}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292723,46 +292742,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (2008 NAAQS)"
         },
-            "identifier": "{448451DF-30E7-4B29-9A08-B3F7A68870BE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
             "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This web service contains the following layer: SO2 2010 NAAQS State Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2010SO21hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-SO2 (2010 NAAQS)",
-            "description": "This web service contains the following layer: SO2 2010 NAAQS State Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2010SO21hour/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{2666B6DA-07AD-4CAA-9DEB-E90798D828B8}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292828,46 +292847,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-SO2 (2010 NAAQS)"
         },
-            "identifier": "{2666B6DA-07AD-4CAA-9DEB-E90798D828B8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
             "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This web service contains the following layer: PM2.5 Annual 2012 NAAQS State Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2012PM25Annual/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-Annual PM2.5 (2012 NAAQS)",
-            "description": "This web service contains the following layer: PM2.5 Annual 2012 NAAQS State Level. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NAA2012PM25Annual/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{09E54579-FD59-4B09-AA3E-46E06D45F123}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -292933,46 +292952,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations-Annual PM2.5 (2012 NAAQS)"
         },
-            "identifier": "{09E54579-FD59-4B09-AA3E-46E06D45F123}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/oar/oaqps/greenbk/regcntct.html",
+            "description": "This web service layer, Ozone 8-hr (2015 standard), displays identified state level areas where ground-level ozone have not met the National Ambient Air Quality Standards (NAAQS) established in 2015 for ground-level ozone and have been designated \"nonattainment\u201d areas (NAA)\". Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www.epa.gov/oar/oaqps/greenbk/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/oar/oaqps/greenbk/regcntct.html). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://arcg.is/1Lq9Vp2",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (2015 NAAQS) - Web Service Layer",
-            "description": "This web service layer, Ozone 8-hr (2015 standard), displays identified state level areas where ground-level ozone have not met the National Ambient Air Quality Standards (NAAQS) established in 2015 for ground-level ozone and have been designated \"nonattainment\u201d areas (NAA)\". Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www.epa.gov/oar/oaqps/greenbk/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/oar/oaqps/greenbk/regcntct.html). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "us-epa-nonattainment-areas-and-designations-8-hour-ozone-2015-naaqs-web-service-layer",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293038,177 +293057,177 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
-            },
-            "identifier": "us-epa-nonattainment-areas-and-designations-8-hour-ozone-2015-naaqs-web-service-layer",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www.epa.gov/oar/oaqps/greenbk/regcntct.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://arcg.is/1Lq9Vp2",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "US EPA Nonattainment Areas and Designations-8 Hour Ozone (2015 NAAQS) - Web Service Layer"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Emissions Inventory, U.S., 2014, EPA/OAR/OAQPS/AQAD",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Stitt",
+                "hasEmail": "mailto:stitt.brian@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/air-emissions-inventories/national-emissions-inventory",
             "description": "This web service contains layers that depict annual emissions for 2014 at the facility and county level for the following criterial pollutants: CO, Lead, NH3, NOx, PM10, PM25, SO2, and VOC. The National Emissions Inventory (NEI) is a comprehensive and detailed estimate of air emissions of criteria pollutants, criteria precursors, and hazardous air pollutants from air emissions sources. The NEI is released every three years based primarily upon data provided by State, Local, and Tribal air agencies for sources in their jurisdictions and supplemented by data developed by the US EPA. The NEI is built using the Emissions Inventory System (EIS) first to collect the data from State, Local, and Tribal air agencies and then to blend that data with other data sources. NEI point sources include emissions estimates for larger sources that are located at a fixed, stationary location. Point sources in the NEI include large industrial facilities and electric power plants, airports, and smaller industrial, non-industrial and commercial facilities. A small number of portable sources such as some asphalt or rock crushing operations are also included. Some states voluntarily also provide facilities such as dry cleaners, gas stations, and livestock facilities, which are otherwise included in the NEI as nonpoint sources. The emissions potential of each facility determines whether that facility should be reported as a point source, according to emissions thresholds set in the Air Emissions Reporting Rule (AERR). NEI Point Sources are all included in the EIS Point Data Category. NEI nonpoint sources include emissions estimates for sources which individually are too small in magnitude to report as point sources. These emissions sources are included in the NEI as a county total or tribal total (for participating tribes). Examples include residential heating, commercial combustion, asphalt paving, and commercial and consumer solvent use. NEI nonpoint sources are all included in the EIS Nonpoint Data Category.",
+            "distribution": [],
+            "identifier": "{76cf8ad6-b57e-420f-9465-9f199a4ad985}",
+            "issued": "2016-04-11",
             "keyword": [
                 "geospatial",
                 "Facilities",
                 "Air",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-04-11",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Stitt",
-                "hasEmail": "mailto:stitt.brian@epa.gov"
-            },
-            "identifier": "{76cf8ad6-b57e-420f-9465-9f199a4ad985}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/air-emissions-inventories/national-emissions-inventory",
-            "issued": "2016-04-11",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": []
+            "title": "National Emissions Inventory, U.S., 2014, EPA/OAR/OAQPS/AQAD"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Emissions Inventory (NEI), Facility-Level, US, 2008, 2011, 2014, EPA OAR, OAPQS",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Stitt",
+                "hasEmail": "mailto:stitt.brian@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/air-emissions-inventories/national-emissions-inventory",
             "description": "This US EPA Office of Air and Radiation, Office of Air Quality Planning and Standards, Air Quality Assessment Division, Air Quality Analysis Group (OAR, OAQPS, AQAD, AQAG) web service contains the following layers created from the 2008, 2011 and 2014 National Emissions Inventory (NEI): All Pollutants, which include hazardous air pollutants (HAPs) and criteria air pollutants (CAPs) Criteria Majors, which include CAP point source emissions \u2265 100 tons per year (except Lead which is \u2265 0.5 tons per year) Criteria Minors, which include CAP point source emissions < 100 tons per year (except Lead which is < 0.5 tons per year). Layers are drawn at all scales. The National Emission Inventory (NEI) is a comprehensive and detailed estimate of air emissions of criteria pollutants, criteria precursors, and hazardous air pollutants from air emissions sources. The NEI is released every three years based primarily upon data provided by State, Local, and Tribal air agencies for sources in their jurisdictions and supplemented by data developed by the US EPA. The NEI is built using the Emissions Inventory System (EIS) first to collect the data from State, Local, and Tribal air agencies and then to blend that data with other data sources. NEI point sources include emissions estimates for larger sources that are located at a fixed, stationary location. Point sources in the NEI include large industrial facilities and electric power plants, airports, and smaller industrial, non-industrial and commercial facilities. A small number of portable sources such as some asphalt or rock crushing operations are also included. Some states voluntarily also provide facilities such as dry cleaners, gas stations, and livestock facilities, which are otherwise included in the NEI as nonpoint sources. The emissions potential of each facility determines whether that facility should be reported as a point source, according to emissions thresholds set in the Air Emissions Reporting Rule (AERR). NEI Point Sources are all included in the EIS Point Data Category. NEI nonpoint sources include emissions estimates for sources which individually are too small in magnitude to report as point sources. These emissions sources are included in the NEI as a county total or tribal total (for participating tribes). Examples include residential heating, commercial combustion, asphalt paving, and commercial and consumer solvent use. NEI nonpoint sources are all included in the EIS Nonpoint Data Category.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/OAR/OAQPS/NEI/NEI_Facility_HAPs_CAPs.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{ec46e614-75cf-48c6-ac5d-2b3050ee9ac5}",
+            "issued": "2017-03-02",
             "keyword": [
                 "geospatial",
                 "Facilities",
                 "Air",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Stitt",
-                "hasEmail": "mailto:stitt.brian@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2008-01-01/2008-01-01",
+            "theme": "environment",
+            "title": "National Emissions Inventory (NEI), Facility-Level, US, 2008, 2011, 2014, EPA OAR, OAPQS"
         },
-            "identifier": "{ec46e614-75cf-48c6-ac5d-2b3050ee9ac5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2008-01-01/2008-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Stitt",
+                "hasEmail": "mailto:stitt.brian@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/air-emissions-inventories/national-emissions-inventory",
-            "issued": "2017-03-02",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This US EPA Office of Air and Radiation, Office of Air Quality Planning and Standards, Air Quality Assessment Division, Air Quality Analysis Group (OAR, OAQPS, AQAD, AQAG) web service contains the following layers created from the 2008, 2011 and 2014 National Emissions Inventory (NEI): Carbon Monoxide (CO), Lead, Ammonia (NH3), Nitrogen Oxides (NOx), Particulate Matter 10 (PM10), Particulate Matter 2.5 (PM2.5), Sulfur Dioxide (SO2), Volatile Organic Compounds (VOC). Each of these layers conatin county level emissions for 2008, 2011, and 2014. Layers are drawn at all scales. The National Emission Inventory (NEI) is a comprehensive and detailed estimate of air emissions of criteria pollutants, criteria precursors, and hazardous air pollutants from air emissions sources. The NEI is released every three years based primarily upon data provided by State, Local, and Tribal air agencies for sources in their jurisdictions and supplemented by data developed by the US EPA. The NEI is built using the Emissions Inventory System (EIS) first to collect the data from State, Local, and Tribal air agencies and then to blend that data with other data sources. NEI point sources include emissions estimates for larger sources that are located at a fixed, stationary location. Point sources in the NEI include large industrial facilities and electric power plants, airports, and smaller industrial, non-industrial and commercial facilities. A small number of portable sources such as some asphalt or rock crushing operations are also included. Some states voluntarily also provide facilities such as dry cleaners, gas stations, and livestock facilities, which are otherwise included in the NEI as nonpoint sources. The emissions potential of each facility determines whether that facility should be reported as a point source, according to emissions thresholds set in the Air Emissions Reporting Rule (AERR). NEI Point Sources are all included in the EIS Point Data Category. NEI nonpoint sources include emissions estimates for sources which individually are too small in magnitude to report as point sources. These emissions sources are included in the NEI as a county total or tribal total (for participating tribes). Examples include residential heating, commercial combustion, asphalt paving, and commercial and consumer solvent use. NEI nonpoint sources are all included in the EIS Nonpoint Data Category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/OAR/OAQPS/NEI/NEI_Facility_HAPs_CAPs.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/OAR/OAQPS/NEI/NEI_County_CAP.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Emissions Inventory (NEI), County-Level, US, 2008, 2011, 2014, EPA OAR, OAPQS",
-            "description": "This US EPA Office of Air and Radiation, Office of Air Quality Planning and Standards, Air Quality Assessment Division, Air Quality Analysis Group (OAR, OAQPS, AQAD, AQAG) web service contains the following layers created from the 2008, 2011 and 2014 National Emissions Inventory (NEI): Carbon Monoxide (CO), Lead, Ammonia (NH3), Nitrogen Oxides (NOx), Particulate Matter 10 (PM10), Particulate Matter 2.5 (PM2.5), Sulfur Dioxide (SO2), Volatile Organic Compounds (VOC). Each of these layers conatin county level emissions for 2008, 2011, and 2014. Layers are drawn at all scales. The National Emission Inventory (NEI) is a comprehensive and detailed estimate of air emissions of criteria pollutants, criteria precursors, and hazardous air pollutants from air emissions sources. The NEI is released every three years based primarily upon data provided by State, Local, and Tribal air agencies for sources in their jurisdictions and supplemented by data developed by the US EPA. The NEI is built using the Emissions Inventory System (EIS) first to collect the data from State, Local, and Tribal air agencies and then to blend that data with other data sources. NEI point sources include emissions estimates for larger sources that are located at a fixed, stationary location. Point sources in the NEI include large industrial facilities and electric power plants, airports, and smaller industrial, non-industrial and commercial facilities. A small number of portable sources such as some asphalt or rock crushing operations are also included. Some states voluntarily also provide facilities such as dry cleaners, gas stations, and livestock facilities, which are otherwise included in the NEI as nonpoint sources. The emissions potential of each facility determines whether that facility should be reported as a point source, according to emissions thresholds set in the Air Emissions Reporting Rule (AERR). NEI Point Sources are all included in the EIS Point Data Category. NEI nonpoint sources include emissions estimates for sources which individually are too small in magnitude to report as point sources. These emissions sources are included in the NEI as a county total or tribal total (for participating tribes). Examples include residential heating, commercial combustion, asphalt paving, and commercial and consumer solvent use. NEI nonpoint sources are all included in the EIS Nonpoint Data Category.",
+            ],
+            "identifier": "{6d0d2bcc-67ed-48ea-8655-361982efd8d9}",
+            "issued": "2017-03-02",
             "keyword": [
                 "geospatial",
                 "Facilities",
                 "Air",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-02",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Stitt",
-                "hasEmail": "mailto:stitt.brian@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2008-01-01/2008-01-01",
+            "theme": "environment",
+            "title": "National Emissions Inventory (NEI), County-Level, US, 2008, 2011, 2014, EPA OAR, OAPQS"
         },
-            "identifier": "{6d0d2bcc-67ed-48ea-8655-361982efd8d9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2008-01-01/2008-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/air-emissions-inventories/national-emissions-inventory",
-            "issued": "2017-03-02",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
+            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
+            "description": "This web service contains the following state level layers:Ozone 8-hr (1997 standard), Ozone 8-hr (2008 standard), Lead (2008 standard), SO2 1-hr (2010 standard), PM2.5 24hr (2006 standard), PM2.5 Annual (1997 standard), PM2.5 Annual (2012 standard), PM10 (1987 standard), and CO (1990 standard). Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/OAR/OAQPS/NEI/NEI_County_CAP.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations",
-            "description": "This web service contains the following state level layers:Ozone 8-hr (1997 standard), Ozone 8-hr (2008 standard), Lead (2008 standard), SO2 1-hr (2010 standard), PM2.5 24hr (2006 standard), PM2.5 Annual (1997 standard), PM2.5 Annual (2012 standard), PM10 (1987 standard), and CO (1990 standard). Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (https://gispub.epa.gov/arcgis/rest/services/OAR_OAQPS/NonattainmentAreas/MapServer) and viewing the layer description. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{6D412E16-523A-4466-AE04-09EAEF7C16F3}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293274,46 +293293,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "US EPA Nonattainment Areas and Designations"
         },
-            "identifier": "{6D412E16-523A-4466-AE04-09EAEF7C16F3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Doug Solomon",
+                "hasEmail": "mailto:solomon.douglas@epa.gov"
+            },
             "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This downloadable data package contains the following state level layers: Ozone 8-hr (1997 standard), Ozone 8-hr (2008 standard), Lead (2008 standard), SO2 1-hr (2010 standard), PM2.5 24hr (2006 standard), PM2.5 Annual (1997 standard), PM2.5 Annual (2012 standard), and PM10 (1987 standard). Included in this package are a file geodatabase and full FGDC metadata records for each layer. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US EPA Nonattainment Areas and Designations - Download Package",
-            "description": "This downloadable data package contains the following state level layers: Ozone 8-hr (1997 standard), Ozone 8-hr (2008 standard), Lead (2008 standard), SO2 1-hr (2010 standard), PM2.5 24hr (2006 standard), PM2.5 Annual (1997 standard), PM2.5 Annual (2012 standard), and PM10 (1987 standard). Included in this package are a file geodatabase and full FGDC metadata records for each layer. These layers identify areas in the U.S. where air pollution levels have not met the National Ambient Air Quality Standards (NAAQS) for criteria air pollutants and have been designated \"nonattainment\u201d areas (NAA)\". The data are updated weekly from an OAQPS internal database. However, that does not necessarily mean the data have changed. The EPA Office of Air Quality Planning and Standards (OAQPS) has set National Ambient Air Quality Standards for six principal pollutants, which are called \"criteria\" pollutants. Under provisions of the Clean Air Act, which is intended to improve the quality of the air we breathe, EPA is required to set National Ambient Air Quality Standards for six common air pollutants. These commonly found air pollutants (also known as \"criteria pollutants\") are found all over the United States. They are particle pollution (often referred to as particulate matter), ground-level ozone, carbon monoxide, sulfur oxides, nitrogen oxides, and lead. For each criteria pollutant, there are specific procedures used for measuring ambient concentrations and for calculating long-term (quarterly or annual) and/or short-term (24-hour) exposure levels. The methods and allowable concentrations vary from one pollutant to another, and within NAAQS revisions for each pollutant. These pollutants can harm your health and the environment, and cause property damage. Of the six pollutants, particle pollution and ground-level ozone are the most widespread health threats. EPA calls these pollutants \"criteria\" air pollutants because it regulates them by developing human health-based and/or environmentally-based criteria (science-based guidelines) for setting permissible levels. The set of limits based on human health is called primary standards. Another set of limits intended to prevent environmental and property damage is called secondary standards. A geographic area that meets or does better than the primary standard is called an attainment area; areas that don't meet the primary standard are called nonattainment areas. In some cases, a designated nonattainment area can include portions of 2, 3, or 4 states rather than falling entirely within a single state. Multi-state areas have had different state portions handled through up to 3 separate EPA regional offices. The actions of EPA and the state governments for separate portions of such areas are not always simultaneous. While some areas have had coordinated action from all related states on the same day, other areas (so-called \"split areas\") have had delays of several months, ranging up to more than 2 years, between different states. EPA must designate areas as meeting (attainment) or not meeting (nonattainment) the standard. A designation is the term EPA uses to describe the air quality in a given area for any of the six common air pollutants (criteria pollutants). After EPA establishes or revises a primary and/or secondary National Ambient Air Quality Standard (NAAQS), the Clean Air Act requires EPA to designate areas as \"attainment\" (meeting), \"nonattainment\" (not meeting), or \"unclassifiable\" (insufficient data) after monitoring data is collected by state, local and tribal governments. Once nonattainment designations take effect, the state and local governments have three years to develop implementation plans outlining how areas will attain and maintain the standards by reducing air pollutant emissions. For further information please refer to: https://www3.epa.gov/airquality/greenbook/index.html. Questions concerning the status of nonattainment areas, their classification and EPA policy should be directed to the appropriate Regional Offices (https://www.epa.gov/approved-sips/regional-sip-coordinators). EPA Headquarters should be contacted only when the Regional Office is unable to answer a question.",
+            ],
+            "identifier": "{6BE1A54B-B777-4306-ACFE-F7730C8F0B6E}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293379,46 +293398,39 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Doug Solomon",
-                "hasEmail": "mailto:solomon.douglas@epa.gov"
-            },
-            "identifier": "{6BE1A54B-B777-4306-ACFE-F7730C8F0B6E}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://www3.epa.gov/airquality/greenbook/index.html",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OAR/OAQPS/NAA.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "US EPA Nonattainment Areas and Designations - Download Package"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US EPA 2014 Ozone Season Review by Core Based Statistical Area",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www.airnow.gov/",
             "description": "This web service contains the following layer: CBSA35_2014OzoneAQI_data. Full FGDC metadata record for this layer may be found by clicking the layer name at the web service endpoint (available through the online link provided above) and viewing the layer description.",
+            "distribution": [],
+            "identifier": "{4A52FB27-153C-449B-AA7D-5C61A968E059}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293484,39 +293496,39 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
-            },
-            "identifier": "{4A52FB27-153C-449B-AA7D-5C61A968E059}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.airnow.gov/",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": []
+            "title": "US EPA 2014 Ozone Season Review by Core Based Statistical Area"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US EPA 2014 Ozone Season Review by City",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www.airnow.gov/",
             "description": "This web service contains the following layer: OzoneReview35Cities_with2000to2014data. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (available through the online link provided above) and viewing the layer description.",
+            "distribution": [],
+            "identifier": "{ED2DFDB7-7520-4F3F-B7AA-61AD4FB841E0}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293582,39 +293594,39 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
-            },
-            "identifier": "{ED2DFDB7-7520-4F3F-B7AA-61AD4FB841E0}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.airnow.gov/",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": []
+            "title": "US EPA 2014 Ozone Season Review by City"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US EPA 2014 Fine Particulate Pollution (PM2.5) Season Review by Core Based Statistical Area",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www.airnow.gov/",
             "description": "This web service contains the following layer: PM25_2014_SesonReview_35CBSA. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (available through the online link provided above) and viewing the layer description.",
+            "distribution": [],
+            "identifier": "{7C15C281-82B2-420D-869A-D150FD91C7DF}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293680,39 +293692,39 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
-            },
-            "identifier": "{7C15C281-82B2-420D-869A-D150FD91C7DF}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.airnow.gov/",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": []
+            "title": "US EPA 2014 Fine Particulate Pollution (PM2.5) Season Review by Core Based Statistical Area"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US EPA 2014 Fine Particulate Pollution (PM2.5) Season Review by City",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Halil Cakir",
+                "hasEmail": "mailto:cakir.halil@epa.gov"
+            },
+            "describedBy": "https://www.airnow.gov/",
             "description": "This web service contains the following layer: PM25Review35Cities_with2000to2014data. Full FGDC metadata records for each layer may be found by clicking the layer name at the web service endpoint (available through the online link provided above) and viewing the layer description.",
+            "distribution": [],
+            "identifier": "{EA2740AD-FC6D-4ECC-9D1F-434ECD213514}",
+            "issued": "2015-07-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -293778,39 +293790,38 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-07-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation-Office of Air Quality Planning and Standards"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Halil Cakir",
-                "hasEmail": "mailto:cakir.halil@epa.gov"
-            },
-            "identifier": "{EA2740AD-FC6D-4ECC-9D1F-434ECD213514}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.airnow.gov/",
-            "issued": "2015-07-01",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": []
+            "title": "US EPA 2014 Fine Particulate Pollution (PM2.5) Season Review by City"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Acute Exposure Guideline Levels Chemical Listing",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ernest Falke",
+                "hasEmail": "mailto:Falke.ernest@Epa.gov"
+            },
             "description": "The Acute Exposure Guideline Levels Chemical Listing provides a complete listing of risk exposure guidelines from rare exposure to certain chemicals.",
+            "distribution": [],
+            "identifier": "{BC3DF16C-9287-454B-92A8-FF7F7788D43D}",
+            "issued": "2014",
             "keyword": [
                 "Exposure",
                 "Health Risks",
@@ -293823,37 +293834,44 @@
                 "Chemicals",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ernest Falke",
-                "hasEmail": "mailto:Falke.ernest@Epa.gov"
-            },
-            "identifier": "{BC3DF16C-9287-454B-92A8-FF7F7788D43D}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180, 18, -66, 72",
             "temporal": "\n                                    /\n                                    ",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014",
             "theme": "environment",
-            "distribution": []
+            "title": "Acute Exposure Guideline Levels Chemical Listing"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Chemicals per Site, 2012",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
             "description": "This layer displays points of per site chemical use extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "chemical-data-release-cdr-chemicals-per-site-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -293919,45 +293937,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Chemicals per Site, 2012"
         },
-            "identifier": "chemical-data-release-cdr-chemicals-per-site-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This data download package contains the following map layers: CDR sites, CDR chemicals, and CDR commercial and industrial submissions. Layers are drawn at all scales. Included in this package are a file geodatabase, Esri ArcMap map document and XML files of this and layer-level metadata records. Full FGDC metadata records for each layer are also contained in the database. This dataset was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OCSPP/CDR_Sites/MapServer",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Reporting (CDR), 2012",
-            "description": "This data download package contains the following map layers: CDR sites, CDR chemicals, and CDR commercial and industrial submissions. Layers are drawn at all scales. Included in this package are a file geodatabase, Esri ArcMap map document and XML files of this and layer-level metadata records. Full FGDC metadata records for each layer are also contained in the database. This dataset was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-reporting-cdr-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294027,45 +294045,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Reporting (CDR), 2012"
         },
-            "identifier": "chemical-data-reporting-cdr-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of submission sites extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://geodata.epa.gov/arcgis/rest/services/OCSPP/CDR_Sites/MapServer",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Sites, 2012",
-            "description": "This layer displays points of submission sites extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-sites-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294131,45 +294149,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Sites, 2012"
         },
-            "identifier": "chemical-data-release-cdr-sites-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of children's products uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Children's Products Uses, 2012",
-            "description": "This layer displays points of children's products uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-childrens-products-uses-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294235,45 +294253,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Children's Products Uses, 2012"
         },
-            "identifier": "chemical-data-release-cdr-childrens-products-uses-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of commercial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Commercial Uses, 2012",
-            "description": "This layer displays points of commercial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-commercial-uses-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294339,45 +294357,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Commercial Uses, 2012"
         },
-            "identifier": "chemical-data-release-cdr-commercial-uses-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of consumer and commercial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Consumer and Commercial Uses, 2012",
-            "description": "This layer displays points of consumer and commercial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-consumer-and-commercial-uses-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294443,45 +294461,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Consumer and Commercial Uses, 2012"
         },
-            "identifier": "chemical-data-release-cdr-consumer-and-commercial-uses-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of consumer uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Consumer Uses, 2012",
-            "description": "This layer displays points of consumer uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-consumer-uses-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294547,45 +294565,45 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2013-06-05/2013-06-05",
+            "theme": "environment",
+            "title": "Chemical Data Release (CDR) Consumer Uses, 2012"
         },
-            "identifier": "chemical-data-release-cdr-consumer-uses-2012",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jennifer Connolly",
+                "hasEmail": "mailto:connolly.jennifer@epa.gov"
+            },
+            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=d46156cc921d4b41923c70c280b82458",
+            "description": "The Endangered Species Act (ESA) provides a program for the conservation of threatened and endangered species and the habitats in which they are found. The U.S. Fish and Wildlife Service (USFWS) and the National Marine Fisheries Service of U.S. National Oceanic and Atmospheric Organization (NMFS/NOAA) lead federal implementation of the ESA, though they are supported by other federal agencies, including the U.S. Environmental Protection Agency (US EPA). Section 7 of the ESA directs all Federal agencies to conserve endangered and threatened species and to use their authorities to ensure actions do not jeopardized the further existence of threatened and endangered species or adversely modify designated critical habitats. As part of the Section 7 coordination, federal agencies work with USFWS and NMFS to identify species found within the jurisdiction of the United that could be affected by actions carried out by the agency.    Of note, the US EPA\u2019s Office of Pesticide Programs (OPP) is responsible for ensuring that Agency actions under the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) are in compliance with ESA. OPP determines if ESA-listed species or their designated critical habitat may be affected by pesticide products. Pesticide products that \u201cmay affect\u201d an ESA-listed species or its designated critical habitat may be subject to additional regulation.     Species ranges represent anywhere an individual of the listed species could be found based on the best available information at the time of delineation. As defined in ESA, critical habitat delineates habitat characteristics in specific geographical areas and may be occupied or unoccupied by a threatened or endangered species at the time of listing. These areas must contain physical or biological features essential to conservation of a species and may require special management considerations or protection. Critical habitat may also include areas that are not currently occupied by the species but that may be needed for their recovery. Range areas represent more generalized habitat where species are or could be found based on the best available information. For some species, best available information is based on site specific surveys. For others, it will be historical location information based on political boundaries. These areas are, therefore, less geographically explicit than critical habitat. Consideration of both the species range and critical habitat ensures the conservation of the ecosystems upon which endangered and threatened species depend.    To support EPA\u2019s implementation of ESA, critical habitat and range data for species listed under ESA Section 7 were obtained by the US EPA from the USFWS Environmental Conservation Online System (ECOS) database in November 2020. These data were supplemented with areas provided by NOAA\u2019s National Marine Fisheries Service (NMFS) where NOAA has species authority. For NMFS species not found in either location, a request was made directly to the NMFS scientists. The last download of the species locations occurred in November 2020.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "accessURL": "https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services/Critical_Habitat/FeatureServer",
+                    "title": "EPA GeoPlatform Hosted Feature Service"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Critical Habitat for Endangered Species",
-            "description": "The Endangered Species Act (ESA) provides a program for the conservation of threatened and endangered species and the habitats in which they are found. The U.S. Fish and Wildlife Service (USFWS) and the National Marine Fisheries Service of U.S. National Oceanic and Atmospheric Organization (NMFS/NOAA) lead federal implementation of the ESA, though they are supported by other federal agencies, including the U.S. Environmental Protection Agency (US EPA). Section 7 of the ESA directs all Federal agencies to conserve endangered and threatened species and to use their authorities to ensure actions do not jeopardized the further existence of threatened and endangered species or adversely modify designated critical habitats. As part of the Section 7 coordination, federal agencies work with USFWS and NMFS to identify species found within the jurisdiction of the United that could be affected by actions carried out by the agency.    Of note, the US EPA\u2019s Office of Pesticide Programs (OPP) is responsible for ensuring that Agency actions under the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) are in compliance with ESA. OPP determines if ESA-listed species or their designated critical habitat may be affected by pesticide products. Pesticide products that \u201cmay affect\u201d an ESA-listed species or its designated critical habitat may be subject to additional regulation.     Species ranges represent anywhere an individual of the listed species could be found based on the best available information at the time of delineation. As defined in ESA, critical habitat delineates habitat characteristics in specific geographical areas and may be occupied or unoccupied by a threatened or endangered species at the time of listing. These areas must contain physical or biological features essential to conservation of a species and may require special management considerations or protection. Critical habitat may also include areas that are not currently occupied by the species but that may be needed for their recovery. Range areas represent more generalized habitat where species are or could be found based on the best available information. For some species, best available information is based on site specific surveys. For others, it will be historical location information based on political boundaries. These areas are, therefore, less geographically explicit than critical habitat. Consideration of both the species range and critical habitat ensures the conservation of the ecosystems upon which endangered and threatened species depend.    To support EPA\u2019s implementation of ESA, critical habitat and range data for species listed under ESA Section 7 were obtained by the US EPA from the USFWS Environmental Conservation Online System (ECOS) database in November 2020. These data were supplemented with areas provided by NOAA\u2019s National Marine Fisheries Service (NMFS) where NOAA has species authority. For NMFS species not found in either location, a request was made directly to the NMFS scientists. The last download of the species locations occurred in November 2020.",
+            ],
+            "identifier": "1733ABAE-728C-4951-AA17-A45AD1E7C080",
+            "issued": "2022-10-01",
             "keyword": [
                 "Exposure",
                 "Modeling",
@@ -294607,42 +294625,42 @@
                 "Pesticides",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-10-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Pesticide Programs"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jennifer Connolly",
-                "hasEmail": "mailto:connolly.jennifer@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-179.146415, -14.548618, 179.776438, 74.024896",
+            "title": "Critical Habitat for Endangered Species"
         },
-            "identifier": "1733ABAE-728C-4951-AA17-A45AD1E7C080",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-179.146415, -14.548618, 179.776438, 74.024896",
-            "accrualPeriodicity": "R/P1W",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jennifer Connolly",
+                "hasEmail": "mailto:connolly.jennifer@epa.gov"
+            },
             "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=d46156cc921d4b41923c70c280b82458",
-            "issued": "2022-10-01",
+            "description": "The Endangered Species Act (ESA) provides a program for the conservation of threatened and endangered species and the habitats in which they are found. The U.S. Fish and Wildlife Service (USFWS) and the National Marine Fisheries Service of U.S. National Oceanic and Atmospheric Organization (NMFS/NOAA) lead federal implementation of the ESA, though they are supported by other federal agencies, including the U.S. Environmental Protection Agency (US EPA). Section 7 of the ESA directs all Federal agencies to conserve endangered and threatened species and to use their authorities to ensure actions do not jeopardized the further existence of threatened and endangered species or adversely modify designated critical habitats. As part of the Section 7 coordination, federal agencies work with USFWS and NMFS to identify species found within the jurisdiction of the United that could be affected by actions carried out by the agency.    Of note, the US EPA\u2019s Office of Pesticide Programs (OPP) is responsible for ensuring that Agency actions under the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) are in compliance with ESA. OPP determines if ESA-listed species or their designated critical habitat may be affected by pesticide products. Pesticide products that \u201cmay affect\u201d an ESA-listed species or its designated critical habitat may be subject to additional regulation.     Species ranges represent anywhere an individual of the listed species could be found based on the best available information at the time of delineation. As defined in ESA, critical habitat delineates habitat characteristics in specific geographical areas and may be occupied or unoccupied by a threatened or endangered species at the time of listing. These areas must contain physical or biological features essential to conservation of a species and may require special management considerations or protection. Critical habitat may also include areas that are not currently occupied by the species but that may be needed for their recovery. Range areas represent more generalized habitat where species are or could be found based on the best available information. For some species, best available information is based on site specific surveys. For others, it will be historical location information based on political boundaries. These areas are, therefore, less geographically explicit than critical habitat. Consideration of both the species range and critical habitat ensures the conservation of the ecosystems upon which endangered and threatened species depend.    To support EPA\u2019s implementation of ESA, critical habitat and range data for species listed under ESA Section 7 were obtained by the US EPA from the USFWS Environmental Conservation Online System (ECOS) database in November 2020. These data were supplemented with areas provided by NOAA\u2019s National Marine Fisheries Service (NMFS) where NOAA has species authority. For NMFS species not found in either location, a request was made directly to the NMFS scientists. The last download of the species locations occurred in November 2020.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EPA GeoPlatform Hosted Feature Service",
-                    "accessURL": "https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services/Critical_Habitat/FeatureServer"
+                    "accessURL": "https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services/Critical_Habitat/FeatureServer",
+                    "title": "EPA GeoPlatform Hosted Feature Service"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Endangered Species Range Areas",
-            "description": "The Endangered Species Act (ESA) provides a program for the conservation of threatened and endangered species and the habitats in which they are found. The U.S. Fish and Wildlife Service (USFWS) and the National Marine Fisheries Service of U.S. National Oceanic and Atmospheric Organization (NMFS/NOAA) lead federal implementation of the ESA, though they are supported by other federal agencies, including the U.S. Environmental Protection Agency (US EPA). Section 7 of the ESA directs all Federal agencies to conserve endangered and threatened species and to use their authorities to ensure actions do not jeopardized the further existence of threatened and endangered species or adversely modify designated critical habitats. As part of the Section 7 coordination, federal agencies work with USFWS and NMFS to identify species found within the jurisdiction of the United that could be affected by actions carried out by the agency.    Of note, the US EPA\u2019s Office of Pesticide Programs (OPP) is responsible for ensuring that Agency actions under the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) are in compliance with ESA. OPP determines if ESA-listed species or their designated critical habitat may be affected by pesticide products. Pesticide products that \u201cmay affect\u201d an ESA-listed species or its designated critical habitat may be subject to additional regulation.     Species ranges represent anywhere an individual of the listed species could be found based on the best available information at the time of delineation. As defined in ESA, critical habitat delineates habitat characteristics in specific geographical areas and may be occupied or unoccupied by a threatened or endangered species at the time of listing. These areas must contain physical or biological features essential to conservation of a species and may require special management considerations or protection. Critical habitat may also include areas that are not currently occupied by the species but that may be needed for their recovery. Range areas represent more generalized habitat where species are or could be found based on the best available information. For some species, best available information is based on site specific surveys. For others, it will be historical location information based on political boundaries. These areas are, therefore, less geographically explicit than critical habitat. Consideration of both the species range and critical habitat ensures the conservation of the ecosystems upon which endangered and threatened species depend.    To support EPA\u2019s implementation of ESA, critical habitat and range data for species listed under ESA Section 7 were obtained by the US EPA from the USFWS Environmental Conservation Online System (ECOS) database in November 2020. These data were supplemented with areas provided by NOAA\u2019s National Marine Fisheries Service (NMFS) where NOAA has species authority. For NMFS species not found in either location, a request was made directly to the NMFS scientists. The last download of the species locations occurred in November 2020.",
+            ],
+            "identifier": "AF047E5D-B6AE-4207-9582-33AB848C76E1",
+            "issued": "2022-10-01",
             "keyword": [
                 "Exposure",
                 "Modeling",
@@ -294664,42 +294682,42 @@
                 "Pesticides",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-10-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Pesticide Programs"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jennifer Connolly",
-                "hasEmail": "mailto:connolly.jennifer@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-180.00002, -85.470289, 180.00002, 89.987675",
+            "title": "Endangered Species Range Areas"
         },
-            "identifier": "AF047E5D-B6AE-4207-9582-33AB848C76E1",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "licenseUnrestricted",
-            "spatial": "-180.00002, -85.470289, 180.00002, 89.987675",
-            "accrualPeriodicity": "R/P1W",
-            "describedBy": "https://epa.maps.arcgis.com/home/item.html?id=d46156cc921d4b41923c70c280b82458",
-            "issued": "2022-10-01",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "description": "This layer displays points of industrial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "EPA GeoPlatform Hosted Feature Service",
-                    "accessURL": "https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services/Critical_Habitat/FeatureServer"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Chemical Data Release (CDR) Industrial Uses, 2012",
-            "description": "This layer displays points of industrial uses extracted from the 2012 Chemical Data Reporting (CDR) database. The CDR database contains comprehensive use and exposure information on the most widely used chemicals in the United States. This layer is drawn at all scales and was procured for EPA through the Office of Pollution Prevention and Toxics (OPPT).",
+            ],
+            "identifier": "chemical-data-release-cdr-industrial-uses-2012",
+            "issued": "2013-06-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -294765,45 +294783,38 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-06-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
-            },
-            "identifier": "chemical-data-release-cdr-industrial-uses-2012",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
             "temporal": "2013-06-05/2013-06-05",
-            "accrualPeriodicity": "R/P1Y",
-            "issued": "2013-06-05",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/OCSPP/OPPT/CDR/CDR.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Chemical Data Release (CDR) Industrial Uses, 2012"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Results of Section 4 Chemical Testing",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mark Seltzer",
+                "hasEmail": "mailto:seltzer.mark@epa.gov"
+            },
             "description": "The Toxic Substances Control Act (TSCA) requires that data be developed on the effect of chemical substances and mixtures on health and the environment. This data source collects the applicable test information on these chemicals submitted by external parties.",
+            "distribution": [],
+            "identifier": "{1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D}",
+            "issued": "2014",
             "keyword": [
                 "Criteria Air Pollutants",
                 "Air",
@@ -294817,37 +294828,37 @@
                 "Environmental Media Topics",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Seltzer",
-                "hasEmail": "mailto:seltzer.mark@epa.gov"
-            },
-            "identifier": "{1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180, 18, -66, 72",
             "temporal": "\n                                    /\n                                    ",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014",
             "theme": "environment",
-            "distribution": []
+            "title": "Results of Section 4 Chemical Testing"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Toxic Substances Control Act (TSCA) 8(e) Notices and FYI Submissions",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Toni Krasnic",
+                "hasEmail": "mailto:Krasnic.Toni@epa.gov"
+            },
             "description": "Section 8(e) of the Toxic Substances Control Act (TSCA) requires U.S. chemical manufacturers, importers, processors and distributors to notify EPA within 30 calendar days of new, unpublished information on their chemicals that may lead to a conclusion of substantial risk to human health or to the environment. This data source collects these Section 8(e) notices as well as voluntary submissions (FYI submissions) and organizes them by date.",
+            "distribution": [],
+            "identifier": "{BD105142-CF54-40DF-9135-5AB7513EFE1B}",
+            "issued": "2014",
             "keyword": [
                 "Non-Point Sources of Water Pollution",
                 "Health Risks",
@@ -294863,37 +294874,37 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Toni Krasnic",
-                "hasEmail": "mailto:Krasnic.Toni@epa.gov"
-            },
-            "identifier": "{BD105142-CF54-40DF-9135-5AB7513EFE1B}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180, 18, -66, 72",
             "temporal": "\n                                    /\n                                    ",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014",
             "theme": "environment",
-            "distribution": []
+            "title": "Toxic Substances Control Act (TSCA) 8(e) Notices and FYI Submissions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Toxic Substances Control Act Test Submissions 2.0 (TSCATS 2.0)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Leitzke",
+                "hasEmail": "mailto:Leitzke.John@epa.gov"
+            },
             "description": "The Toxic Substances Control Act Test Submissions 2.0 (TSCATS 2.0) tracks the submissions of health and safety data submitted to the EPA either as required or voluntarily under certain sections of TSCA.",
+            "distribution": [],
+            "identifier": "{2244ADB0-B057-46B2-B1D8-705A08BD732D}",
+            "issued": "2014",
             "keyword": [
                 "Health Risks",
                 "DataFinder",
@@ -294905,37 +294916,38 @@
                 "Life Stages & Populations",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Leitzke",
-                "hasEmail": "mailto:Leitzke.John@epa.gov"
-            },
-            "identifier": "{2244ADB0-B057-46B2-B1D8-705A08BD732D}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180, 18, -66, 72",
             "temporal": "\n                                    /\n                                    ",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014",
             "theme": "environment",
-            "distribution": []
+            "title": "Toxic Substances Control Act Test Submissions 2.0 (TSCATS 2.0)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "TRI Reporting Facilities Map Service",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": " Amanda Roach",
+                "hasEmail": "mailto:roach.amanda@epa.gov"
+            },
+            "describedBy": "https://gispub.epa.gov/arcgis/rest/services/OCSPP/TRI_Reporting_Facilities/MapServer",
             "description": "This map service shows point locations for facilities that submitted TRI reports to EPA during the most recent reporting year. EPA's Locational Reference Table is used for the facility\u2019s latitude and longitude coordinates. Icons on the map are relatively sized based on the sum of all chemical quantities reported as released. The pop-up presents TRI data including facility name, address, industry sector, and total on-site and off-site release amounts as well as identifiers for TRI and FRS programs and a link to a more detailed TRI report. The data refreshes biannually. For more information, refere to the TRI Program Webpages, https://www.epa.gov/toxics-release-inventory-tri-program.",
+            "distribution": [],
+            "identifier": "C05903B3-3F57-43ED-B280-079A3E05414A",
+            "issued": "2020-01-09",
             "keyword": [
                 "020:072",
                 "Air",
@@ -294951,37 +294963,44 @@
                 "Drinking Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Chemical Safety and Pollution Prevention"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": " Amanda Roach",
-                "hasEmail": "mailto:roach.amanda@epa.gov"
-            },
-            "identifier": "C05903B3-3F57-43ED-B280-079A3E05414A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-176.634509, -14.321981, 174.107672, 70.293892",
             "temporal": "2022-07-01T00:00:00/2022-07-01T00:00:00",
-            "accrualPeriodicity": "R/P2Y",
-            "describedBy": "https://gispub.epa.gov/arcgis/rest/services/OCSPP/TRI_Reporting_Facilities/MapServer",
-            "issued": "2020-01-09",
-            "distribution": []
+            "title": "TRI Reporting Facilities Map Service"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "OECA Annual Report 2015 Data Package",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Paul Stey",
+                "hasEmail": "mailto:stey.paul@epa.gov"
+            },
+            "describedBy": "https://archive.epa.gov/epa/sites/production/files/2017-01/documents/enforcement_annual_results_for_fiscal_year_fy_2015.pdf",
             "description": "This downloadable data package shows information on enforcement actions and cases from 2015. They include civil enforcement actions taken by EPA at facilities, criminal cases prosecuted by EPA under federal statutes and the U.S. Criminal Code, and cases in which EPA provided significant support to cases prosecuted under state criminal laws.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/OECA/AnnualResults2015.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{3364B00C-5160-4BC9-AB57-96497D4446E3}",
+            "issued": "2014-12-04",
             "keyword": [
                 "Air",
                 "Energy",
@@ -294993,46 +295012,46 @@
                 "Facilities",
                 "Contaminant"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-12-04",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance-Office of Compliance"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Paul Stey",
-                "hasEmail": "mailto:stey.paul@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2014-12-04/2014-12-04",
+            "theme": "environment",
+            "title": "OECA Annual Report 2015 Data Package"
         },
-            "identifier": "{3364B00C-5160-4BC9-AB57-96497D4446E3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2014-12-04/2014-12-04",
-            "accrualPeriodicity": "R/P1Y",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Paul Stey",
+                "hasEmail": "mailto:stey.paul@epa.gov"
+            },
             "describedBy": "https://archive.epa.gov/epa/sites/production/files/2017-01/documents/enforcement_annual_results_for_fiscal_year_fy_2015.pdf",
-            "issued": "2014-12-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This interactive map shows information on enforcement actions and cases from 2015. They include civil enforcement actions taken by EPA at facilities, criminal cases prosecuted by EPA under federal statutes and the U.S. Criminal Code, and cases in which EPA provided significant support to cases prosecuted under state criminal laws.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/OECA/AnnualResults2015.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OECA Annual Report 2015 Map Service",
-            "description": "This interactive map shows information on enforcement actions and cases from 2015. They include civil enforcement actions taken by EPA at facilities, criminal cases prosecuted by EPA under federal statutes and the U.S. Criminal Code, and cases in which EPA provided significant support to cases prosecuted under state criminal laws.",
+            ],
+            "identifier": "{3F97342C-64EE-491C-A138-54F50D97A890}",
+            "issued": "2014-12-04",
             "keyword": [
                 "Air",
                 "Energy",
@@ -295043,134 +295062,133 @@
                 "Water",
                 "Contaminant"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-12-04",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance-Office of Compliance"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Paul Stey",
-                "hasEmail": "mailto:stey.paul@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2014-12-04/2014-12-04",
+            "theme": "environment",
+            "title": "OECA Annual Report 2015 Map Service"
         },
-            "identifier": "{3F97342C-64EE-491C-A138-54F50D97A890}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
-            "temporal": "2014-12-04/2014-12-04",
-            "accrualPeriodicity": "R/P1Y",
-            "describedBy": "https://archive.epa.gov/epa/sites/production/files/2017-01/documents/enforcement_annual_results_for_fiscal_year_fy_2015.pdf",
-            "issued": "2014-12-04",
-            "language": "en-us",
-            "theme": "environment",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kimberly Chavez",
+                "hasEmail": "mailto:chavez.kimberly@epa.gov"
+            },
+            "description": "This downloadable data package contains the following map layer: An ESRI polygon layer which depicts the boundaries of each US county. It has been joined with a US EPA value-added dataset derived from the 2007 USDA Census of Agriculture. This USDA dataset was procured for EPA through the Office of Water (OW). Included in this package are a shapefile (v. 10.0), Esri ArcMap map document (v. 10.0) and XML files for this record and the layer level metadata.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/OECA/AnnualResults2015.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/OECA/CAFO_Density.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Concentrated Animal Feeding Operations (CAFOs) per County, US, 2013, US EPA",
-            "description": "This downloadable data package contains the following map layer: An ESRI polygon layer which depicts the boundaries of each US county. It has been joined with a US EPA value-added dataset derived from the 2007 USDA Census of Agriculture. This USDA dataset was procured for EPA through the Office of Water (OW). Included in this package are a shapefile (v. 10.0), Esri ArcMap map document (v. 10.0) and XML files for this record and the layer level metadata.",
+            ],
+            "identifier": "concentrated-animal-feeding-operations-cafos-per-county-us-2013-us-epa",
+            "issued": "2013-05-09",
             "keyword": [
                 "Agriculture",
                 "geospatial",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance-Office of Compliance"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kimberly Chavez",
-                "hasEmail": "mailto:chavez.kimberly@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-178.217598, 18.921786, -66.969271, 71.406235",
+            "temporal": "2007-01-01/2007-01-01",
+            "theme": "boundaries",
+            "title": "Concentrated Animal Feeding Operations (CAFOs) per County, US, 2013, US EPA"
         },
-            "identifier": "concentrated-animal-feeding-operations-cafos-per-county-us-2013-us-epa",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-178.217598, 18.921786, -66.969271, 71.406235",
-            "temporal": "2007-01-01/2007-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2013-05-09",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kimberly Chavez",
+                "hasEmail": "mailto:chavez.kimberly@epa.gov"
+            },
+            "description": "This downloadable data package contains the following map layer: An ESRI polygon layer which depicts the boundaries of each US county. It has been joined with a US EPA value-added dataset derived from the 2007 USDA Census of Agriculture. This USDA dataset was procured for EPA through the Office of Water (OW). Included in this package are a shapefile (v. 10.0), Esri ArcMap map document (v. 10.0) and XML files for this record and the layer level metadata.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/OECA/CAFO_Density.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/public/OECA/CAFO_Density.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Concentrated Animal Feeding Operations (CAFOs) per County Downloadable Package, US, 2013, US EPA",
-            "description": "This downloadable data package contains the following map layer: An ESRI polygon layer which depicts the boundaries of each US county. It has been joined with a US EPA value-added dataset derived from the 2007 USDA Census of Agriculture. This USDA dataset was procured for EPA through the Office of Water (OW). Included in this package are a shapefile (v. 10.0), Esri ArcMap map document (v. 10.0) and XML files for this record and the layer level metadata.",
+            ],
+            "identifier": "{A811129F-3796-4940-A3F8-1BC216AF5D15}",
+            "issued": "2013-05-09",
             "keyword": [
                 "Agriculture",
                 "geospatial",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance-Office of Compliance"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kimberly Chavez",
-                "hasEmail": "mailto:chavez.kimberly@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-178.217598, 18.921786, -66.969271, 71.406235",
+            "temporal": "2007-01-01/2007-01-01",
+            "theme": "boundaries",
+            "title": "Concentrated Animal Feeding Operations (CAFOs) per County Downloadable Package, US, 2013, US EPA"
         },
-            "identifier": "{A811129F-3796-4940-A3F8-1BC216AF5D15}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-178.217598, 18.921786, -66.969271, 71.406235",
-            "temporal": "2007-01-01/2007-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2013-05-09",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rebecca Kane",
+                "hasEmail": "mailto:Kane.Rebecca@epa.gov"
+            },
+            "describedBy": "https://echo.epa.gov/arcgis/rest/services/ECHO/Facilities/MapServer",
+            "description": "ECHO provides integrated compliance and enforcement information for about 800,000 regulated facilities nationwide. Its features range from simple to advanced, catering to users who want to conduct broad analyses as well as those who need to perform complex searches. Enforcement and compliance data are available for air emissions, surface water discharges, hazardous waste, and drinking water systems. ECHO includes EPA, state, local and tribal environmental agency compliance and enforcement records that are contained in EPA national databases. ECHO also incorporates many EPA environmental data sets to provide additional context for analyses.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/public/OECA/CAFO_Density.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://echo.epa.gov",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Enforcement and Compliance History Online (ECHO) Facilities",
-            "description": "ECHO provides integrated compliance and enforcement information for about 800,000 regulated facilities nationwide. Its features range from simple to advanced, catering to users who want to conduct broad analyses as well as those who need to perform complex searches. Enforcement and compliance data are available for air emissions, surface water discharges, hazardous waste, and drinking water systems. ECHO includes EPA, state, local and tribal environmental agency compliance and enforcement records that are contained in EPA national databases. ECHO also incorporates many EPA environmental data sets to provide additional context for analyses.",
+            ],
+            "identifier": "enforcement-and-compliance-history-online-echo-facilities",
+            "issued": "2025-01-27",
             "keyword": [
                 "U.S. Census Data",
                 "ATTAINS",
@@ -295209,77 +295227,71 @@
                 "Contaminant",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2025-01-27",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Enforcment and Compliance Assurance"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Rebecca Kane",
-                "hasEmail": "mailto:Kane.Rebecca@epa.gov"
-            },
-            "identifier": "enforcement-and-compliance-history-online-echo-facilities",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-180, -90, 180, 90",
             "temporal": "2025-01-27/2025-01-27",
-            "describedBy": "https://echo.epa.gov/arcgis/rest/services/ECHO/Facilities/MapServer",
-            "issued": "2025-01-27",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://echo.epa.gov",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Enforcement and Compliance History Online (ECHO) Facilities"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "FY2018 Concluded EPA Enforcement Cases Feature Service",
-            "description": "This interactive map shows information on concluded enforcement actions and cases from federal fiscal year (FY) 2018. They include: civil enforcement actions taken by EPA at facilities, criminal cases prosecuted by EPA under federal statutes and the U.S. Criminal Code, and cases in which EPA provided significant support to cases prosecuted under state criminal laws. They do not include: state civil cases or civil cases where EPA provide significant support to a state. The indicators on the map generally mark the location of the site or facility where the violations occurred or were discovered. Data are updated from the EPA program system on a weekly basis.",
-            "keyword": [
-                "EPA ECHO",
-                "geospatial"
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2019-02-04",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Kane",
                 "hasEmail": "mailto:Kane.Rebecca@epa.gov"
             },
+            "description": "This interactive map shows information on concluded enforcement actions and cases from federal fiscal year (FY) 2018. They include: civil enforcement actions taken by EPA at facilities, criminal cases prosecuted by EPA under federal statutes and the U.S. Criminal Code, and cases in which EPA provided significant support to cases prosecuted under state criminal laws. They do not include: state civil cases or civil cases where EPA provide significant support to a state. The indicators on the map generally mark the location of the site or facility where the violations occurred or were discovered. Data are updated from the EPA program system on a weekly basis.",
+            "distribution": [],
             "identifier": "d4db1849d1684a9eab51d2029e96bf45",
-            "accessLevel": "restricted public",
-            "bureauCode": [
-                "020:00"
+            "issued": "2019-02-04",
+            "keyword": [
+                "EPA ECHO",
+                "geospatial"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2019-02-04",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Enforcement and Compliance Assurance"
+            },
             "rights": "license",
             "spatial": "-180, -90, 180, 90",
-            "issued": "2019-02-04",
-            "distribution": []
+            "title": "FY2018 Concluded EPA Enforcement Cases Feature Service"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Demographics for US Census Tracts - 2010 (American Community Survey 2006-2010 Derived Summary Tables)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EPA GIS Agency Central Support",
+                "hasEmail": "mailto:esrisupport@epa.gov"
+            },
+            "describedBy": "https://edg.epa.gov/metadata",
             "description": "This map service displays data derived from the 2006-2010 American Community Survey (ACS). Values derived from the ACS and used for this map service include: Total Population, Population Density (per square mile), Percent Minority, Percent Below Poverty Level, Percent Age (less than 5, less than 18, and greater than 64), Percent Housing Units Built Before 1950, Percent (population) 25 years and over (with less than a High School Degree and with a High School Degree), Percent Linguistically Isolated Households, Population of American Indians and Alaskan Natives, Population of American Indians and Alaskan Natives Below Poverty Level. The map service was created for inclusion in US EPA mapping applications.",
+            "distribution": [],
+            "identifier": "{A767674A-2BFB-4612-B42F-7A80D96002E0}",
+            "issued": "2012-07-19",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -295342,37 +295354,37 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2012-07-19",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
```

