# Change History for epa.json (Part 34)

### Changes from 31606f9 to dd2190f (Part 24/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c69db231-4e1e-4850-9542-db5ab075ddd3}",
+            "issued": "2019-07-29",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -241453,46 +241472,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-29",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Park Access by Block Group"
         },
-            "identifier": "{c69db231-4e1e-4850-9542-db5ab075ddd3}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{49681807-1c43-45e1-9f40-b9520af03c35}",
+            "issued": "2019-07-29",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -241506,46 +241525,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-29",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Proximity to Parks"
         },
-            "identifier": "{49681807-1c43-45e1-9f40-b9520af03c35}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{83ddd113-0d1e-484f-b1c0-c651b3c6b58d}",
+            "issued": "2019-09-11",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -241563,46 +241582,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-09-11",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{83ddd113-0d1e-484f-b1c0-c651b3c6b58d}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-09-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d38cc89c-c279-41c7-b6c2-cc751328eea2}",
+            "issued": "2019-08-23",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -241620,46 +241639,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-23",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{d38cc89c-c279-41c7-b6c2-cc751328eea2}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{fc58b1aa-d26c-422f-bda4-1a138411a00f}",
+            "issued": "2019-08-14",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241679,46 +241698,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-14",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{fc58b1aa-d26c-422f-bda4-1a138411a00f}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4d67486d-6fe3-472e-a78e-13a531b56e8c}",
+            "issued": "2019-08-14",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241738,46 +241757,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-14",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{4d67486d-6fe3-472e-a78e-13a531b56e8c}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{902b49e4-373c-4df3-a380-9102a7bd6151}",
+            "issued": "2019-08-15",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241797,46 +241816,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-15",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{902b49e4-373c-4df3-a380-9102a7bd6151}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-15",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7bf19972-2fae-46ba-b7ad-e123d7fac270}",
+            "issued": "2019-08-14",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241856,46 +241875,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-14",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{7bf19972-2fae-46ba-b7ad-e123d7fac270}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{61f07a6b-ce92-4ad2-bf79-513f02c797bc}",
+            "issued": "2019-08-13",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241916,46 +241935,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-13",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{61f07a6b-ce92-4ad2-bf79-513f02c797bc}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{13fa8d47-f240-4cab-9cea-bc1e9b716394}",
+            "issued": "2019-08-13",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241973,46 +241992,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-13",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{13fa8d47-f240-4cab-9cea-bc1e9b716394}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0167e588-f339-4ff8-bd38-2f3cb4453848}",
+            "issued": "2019-07-18",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -242028,46 +242047,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-18",
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{0167e588-f339-4ff8-bd38-2f3cb4453848}",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This dataset represents the percentage of land area that is classified as forest land cover, modified forest land cover, and natural land cover using the 2006 National Land Cover Dataset (NLCD) for each Watershed Boundary Dataset (WBD)12-digit hydrological unit (HUC) in the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Land Cover for the Conterminous United States",
-            "description": "This dataset represents the percentage of land area that is classified as forest land cover, modified forest land cover, and natural land cover using the 2006 National Land Cover Dataset (NLCD) for each Watershed Boundary Dataset (WBD)12-digit hydrological unit (HUC) in the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2CC9F8FC-0FFF-43A6-A5C4-C55F1D070DEF}",
+            "issued": "2013-03-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242145,46 +242164,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-03-01",
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2006-01-01/2006-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Land Cover for the Conterminous United States"
         },
-            "identifier": "{2CC9F8FC-0FFF-43A6-A5C4-C55F1D070DEF}",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2006-01-01/2006-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-03-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas hybrid Cropland Data Layer (CDL) - 2011 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2011 Land Cover by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas hybrid Cropland Data Layer (CDL) - 2011 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ee057db8-dc92-4171-9566-e7e8cfd0cb26}",
+            "issued": "2016-04-28",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242250,46 +242269,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-04-28",
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
+            "title": "EnviroAtlas - 2011 Land Cover by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{ee057db8-dc92-4171-9566-e7e8cfd0cb26}",
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
-            "issued": "2016-04-28",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area in estimated floodplains that is classified as natural, forest, shrubland, wetland, developed, low intensity developed, medium intensity developed, high intensity developed, agriculture, pasture, cropland, and rangeland land cover for each 12-digit hydrologic unit code (HUC) in the conterminous United States. Land cover is defined using the EnviroAtlas hybrid Cropland Data Layer (CDL) - 2016 National Land Cover Dataset (NLCD). Floodplains were defined using the EnviroAtlas FEMA_RF_Blend dataset dated 3/25/2019. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 2016 Floodplain Land Cover Proportions for the Conterminous United States",
-            "description": "This EnviroAtlas dataset represents the percentage of land area in estimated floodplains that is classified as natural, forest, shrubland, wetland, developed, low intensity developed, medium intensity developed, high intensity developed, agriculture, pasture, cropland, and rangeland land cover for each 12-digit hydrologic unit code (HUC) in the conterminous United States. Land cover is defined using the EnviroAtlas hybrid Cropland Data Layer (CDL) - 2016 National Land Cover Dataset (NLCD). Floodplains were defined using the EnviroAtlas FEMA_RF_Blend dataset dated 3/25/2019. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5a535ea3-0e87-4331-b083-906954bfae16}",
+            "issued": "2020-04-27",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242352,46 +242371,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-04-27",
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
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2016 Floodplain Land Cover Proportions for the Conterminous United States"
         },
-            "identifier": "{5a535ea3-0e87-4331-b083-906954bfae16}",
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
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-04-27",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover as well as those labeled tundra, shrubland, herbaceous, and perennial snow/ice using the 2016 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in Alaska. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2016 Land Cover Proportions by 12-digit HUC for Alaska",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover as well as those labeled tundra, shrubland, herbaceous, and perennial snow/ice using the 2016 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in Alaska. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9335d1c9-a5e3-4c44-a498-9cd597afd515}",
+            "issued": "2020-05-28",
             "keyword": [
                 "Ecosystem Services",
                 "Wetlands",
@@ -242409,46 +242428,46 @@
                 "Alaska",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-05-28",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgment of the EPA would be appreciated.",
+            "spatial": "-179.229655487448, 51.1568278424693, 179.856674735386, 71.4395725901531",
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2016 Land Cover Proportions by 12-digit HUC for Alaska"
         },
-            "identifier": "{9335d1c9-a5e3-4c44-a498-9cd597afd515}",
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
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgment of the EPA would be appreciated.",
-            "spatial": "-179.229655487448, 51.1568278424693, 179.856674735386, 71.4395725901531",
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-05-28",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas ). The EnviroAtlas One Meter-scale Urban Land Cover (MULC) Data were generated individually for each EnviroAtlas community. Source imagery varies by community. Land cover classes mapped also vary by community and include the following: water, impervious surfaces, soil and barren land, trees, shrub, grass and herbaceous, agriculture, orchards, woody wetlands, and emergent wetlands. Accuracy assessments were completed for each community's classification. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas One Meter Resolution Urban Land Cover Data (2008-2012) Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas ). The EnviroAtlas One Meter-scale Urban Land Cover (MULC) Data were generated individually for each EnviroAtlas community. Source imagery varies by community. Land cover classes mapped also vary by community and include the following: water, impervious surfaces, soil and barren land, trees, shrub, grass and herbaceous, agriculture, orchards, woody wetlands, and emergent wetlands. Accuracy assessments were completed for each community's classification. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{adf673a0-11b4-40d6-befd-8bf75b370cba}",
+            "issued": "2016-10-05",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242526,46 +242545,48 @@
                 "Paterson, NJ",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-10-05",
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
+            "temporal": "2008-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas One Meter Resolution Urban Land Cover Data (2008-2012) Web Service"
         },
-            "identifier": "{adf673a0-11b4-40d6-befd-8bf75b370cba}",
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
-            "temporal": "2008-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, and developed land cover using the 2019 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in the conterminous United States.\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2019 Land Cover Proportions by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, and developed land cover using the 2019 National Land Cover Dataset (NLCD) for each 12-digit hydrologic unit code (HUC) in the conterminous United States.\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "ee057db8-dc92-4171-9566-e7e8cfd0cb26",
+            "issued": "2021-11-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242631,46 +242652,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-11-16",
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
+            "temporal": "2019-01-01T00:00:00/2019-12-31T00:00:00",
+            "title": "EnviroAtlas - 2019 Land Cover Proportions by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "ee057db8-dc92-4171-9566-e7e8cfd0cb26",
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
-            "temporal": "2019-01-01T00:00:00/2019-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-11-16",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas composite of the 2005-2011 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in Hawaii. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2005-2011 Land Cover by 12-digit HUC for Hawaii",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas composite of the 2005-2011 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in Hawaii. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{171946bd-a3e2-47ad-93d3-7aae866d9cf8}",
+            "issued": "2019-08-01",
             "keyword": [
                 "Ecosystem Services",
                 "Wetlands",
@@ -242688,46 +242707,46 @@
                 "Water",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-01",
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
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2005-2011 Land Cover by 12-digit HUC for Hawaii"
         },
-            "identifier": "{171946bd-a3e2-47ad-93d3-7aae866d9cf8}",
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
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas version of the 2010 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in Puerto Rico. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2010 Land Cover by 12-digit HUC for Puerto Rico",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas version of the 2010 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in Puerto Rico. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1135eb39-a3b0-4477-9dd4-cd27250b98a9}",
+            "issued": "2019-07-31",
             "keyword": [
                 "Puerto Rico",
                 "Ecosystem Services",
@@ -242745,46 +242764,46 @@
                 "Water",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-31",
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
+            "spatial": "-67.951455, 17.926837, -65.221033, 18.516091",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2010 Land Cover by 12-digit HUC for Puerto Rico"
         },
-            "identifier": "{1135eb39-a3b0-4477-9dd4-cd27250b98a9}",
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
-            "spatial": "-67.951455, 17.926837, -65.221033, 18.516091",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas version of the 2012 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in US Virgin Islands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2012 Land Cover by 12-digit HUC for US Virgin Islands",
-            "description": "This EnviroAtlas dataset represents the percentage of land area that is classified as natural, forest, wetland, agricultural, natural, and developed land cover using the EnviroAtlas version of the 2012 Coastal Change Analysis Program (C-CAP) land cover dataset for each 12-digit hydrologic unit code (HUC) in US Virgin Islands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{040d23b2-a650-4109-af06-1d817d1dce1a}",
+            "issued": "2019-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Wetlands",
@@ -242802,46 +242821,46 @@
                 "Water",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-31",
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
+            "spatial": "-65.085831, 17.673736, -64.565191, 18.414889",
+            "temporal": "2012-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2012 Land Cover by 12-digit HUC for US Virgin Islands"
         },
-            "identifier": "{040d23b2-a650-4109-af06-1d817d1dce1a}",
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
-            "spatial": "-65.085831, 17.673736, -64.565191, 18.414889",
-            "temporal": "2012-01-01/2012-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream catchments of stream confluences for 2001. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence catchments for the Conterminous United States - 2001",
-            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream catchments of stream confluences for 2001. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8bab7af0-6419-477b-a478-eb6ecafe92df}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -242901,46 +242920,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence catchments for the Conterminous United States - 2001"
         },
-            "identifier": "{8bab7af0-6419-477b-a478-eb6ecafe92df}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream watersheds of stream confluences for 2001. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence watersheds for the Conterminous United States - 2001",
-            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream watersheds of stream confluences for 2001. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f5363f4b-d7c7-46bf-aec5-9719ace0760a}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243000,46 +243019,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence watersheds for the Conterminous United States - 2001"
         },
-            "identifier": "{f5363f4b-d7c7-46bf-aec5-9719ace0760a}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream catchments of stream confluences for 2011. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence catchments for the Conterminous United States - 2011",
-            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream catchments of stream confluences for 2011. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{be7bfc47-773d-4fb4-84f1-92b5cb1c6d39}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243099,46 +243118,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence catchments for the Conterminous United States - 2011"
         },
-            "identifier": "{be7bfc47-773d-4fb4-84f1-92b5cb1c6d39}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream watersheds of stream confluences for 2011. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence watersheds for the Conterminous United States - 2011",
-            "description": "This EnviroAtlas dataset contains land cover proportions for the upstream watersheds of stream confluences for 2011. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a0a4f4e5-ca68-4d75-8674-b0788ba6daa2}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243198,46 +243217,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover attributes for stream confluence watersheds for the Conterminous United States - 2011"
         },
-            "identifier": "{a0a4f4e5-ca68-4d75-8674-b0788ba6daa2}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains changes in land cover proportions between 2001 and 2011 for the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover change for stream confluence catchments for the Conterminous United States - 2001 to 2011",
-            "description": "This EnviroAtlas dataset contains changes in land cover proportions between 2001 and 2011 for the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{77e8cbbf-7c97-4e77-a07a-d8415f2f44a5}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243297,46 +243316,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover change for stream confluence catchments for the Conterminous United States - 2001 to 2011"
         },
-            "identifier": "{77e8cbbf-7c97-4e77-a07a-d8415f2f44a5}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains changes in land cover proportions between 2001 and 2011 for the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover change for stream confluence watersheds for the Conterminous United States - 2001 to 2011",
-            "description": "This EnviroAtlas dataset contains changes in land cover proportions between 2001 and 2011 for the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cb209db7-1dfc-4385-93c6-e049a1e06adf}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243396,46 +243415,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-09-01",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-125.00, 24.52, -66.95, 49.37",
+            "temporal": "2015-01-21/2015-01-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Land cover change for stream confluence watersheds for the Conterminous United States - 2001 to 2011"
         },
-            "identifier": "{cb209db7-1dfc-4385-93c6-e049a1e06adf}",
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
-            "spatial": "-125.00, 24.52, -66.95, 49.37",
-            "temporal": "2015-01-21/2015-01-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-09-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains data on the mean livestock manure application to cultivated crop and hay/pasture lands by 12-digit Hydrologic Unit (HUC) in 2006. Livestock manure inputs to cultivated crop and hay/pasture lands were estimated using county-level estimates of recoverable animal manure from confined feeding operations compiled for 2007. Recoverable manure is defined as manure that is collected, stored, and available for land application from confined feeding operations. County-scale data on livestock populations -- needed to calculate manure inputs -- were only available for the year 2007 from the USDA Census of Agriculture (http://www.agcensus.usda.gov/index.php). We acquired county-level data describing total farm-level inputs (kg N/yr) of recoverable manure to individual counties in 2007 from the International Plant Nutrition Institute (IPNI) Nutrient Geographic Information System (NuGIS; http://www.ipni.net/nugis). These data were converted to per area rates (kg N/ha/yr) of manure N inputs by dividing the total N input by the land area (ha) of combined cultivated crop and hay/pasture (agricultural) lands within a county as determined from county-level summarization of the 2006 NLCD. We distributed county-specific, per area N inputs rates to cultivated crop and hay/pasture lands (30 x 30 m pixels) within the corresponding county. Manure data described here represent an average input to a typical agricultural land type within a county, i.e., they are not specific to individual crop types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Manure application to agricultural lands from confined animal feeding operations by 12-digit HUC for the Conterminous United States, 2006",
-            "description": "This EnviroAtlas dataset contains data on the mean livestock manure application to cultivated crop and hay/pasture lands by 12-digit Hydrologic Unit (HUC) in 2006. Livestock manure inputs to cultivated crop and hay/pasture lands were estimated using county-level estimates of recoverable animal manure from confined feeding operations compiled for 2007. Recoverable manure is defined as manure that is collected, stored, and available for land application from confined feeding operations. County-scale data on livestock populations -- needed to calculate manure inputs -- were only available for the year 2007 from the USDA Census of Agriculture (http://www.agcensus.usda.gov/index.php). We acquired county-level data describing total farm-level inputs (kg N/yr) of recoverable manure to individual counties in 2007 from the International Plant Nutrition Institute (IPNI) Nutrient Geographic Information System (NuGIS; http://www.ipni.net/nugis). These data were converted to per area rates (kg N/ha/yr) of manure N inputs by dividing the total N input by the land area (ha) of combined cultivated crop and hay/pasture (agricultural) lands within a county as determined from county-level summarization of the 2006 NLCD. We distributed county-specific, per area N inputs rates to cultivated crop and hay/pasture lands (30 x 30 m pixels) within the corresponding county. Manure data described here represent an average input to a typical agricultural land type within a county, i.e., they are not specific to individual crop types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0A4E7DDE-5F54-4DB5-8688-6AB2B1C8AFE5}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243500,46 +243519,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-07",
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
+            "title": "EnviroAtlas - Manure application to agricultural lands from confined animal feeding operations by 12-digit HUC for the Conterminous United States, 2006"
         },
-            "identifier": "{0A4E7DDE-5F54-4DB5-8688-6AB2B1C8AFE5}",
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
-            "issued": "2015-05-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas national map displays the application rate of phosphorus (P) as manure on croplands in the conterminous United States (excluding Hawaii and Alaska) for the year 2012 by 12-digit HUC. These data are based on county-level data on P as recoverable manure from concentrated animal feeding operations (CAFOs) from the International Plant Nutrition Institute (IPNI) and cropland area from the USGS's U.S. conterminous wall-to-wall anthropogenic land use trends (NWALT) 2012 land cover data. These are thus not actual application rates but rather estimated rates based on the production of recoverable manure and the amount of agricultural lands close by. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phosphorus application as manure for 2012 by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas national map displays the application rate of phosphorus (P) as manure on croplands in the conterminous United States (excluding Hawaii and Alaska) for the year 2012 by 12-digit HUC. These data are based on county-level data on P as recoverable manure from concentrated animal feeding operations (CAFOs) from the International Plant Nutrition Institute (IPNI) and cropland area from the USGS's U.S. conterminous wall-to-wall anthropogenic land use trends (NWALT) 2012 land cover data. These are thus not actual application rates but rather estimated rates based on the production of recoverable manure and the amount of agricultural lands close by. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1b54f913-4e36-482a-a670-69f19786a048}",
+            "issued": "2016-10-28",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243602,46 +243621,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-10-28",
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
+            "temporal": "2012-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phosphorus application as manure for 2012 by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{1b54f913-4e36-482a-a670-69f19786a048}",
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
-            "temporal": "2012-01-01/2012-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-28",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset includes the total number of recreational days per year demanded by people ages 18 and over for migratory bird hunting by location in the contiguous United States. These values are based on 2010 population distribution, 2011 U.S. Fish and Wildlife Service (FWS) Fish, Hunting, and Wildlife-Associated Recreation (FHWAR) survey data, and 2011 U.S. Department of Agriculture (USDA) Forest Service National Visitor Use Monitoring program data, and have been summarized by 12-digit hydrologic unit code (HUC). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Migratory Bird Hunting Recreation Demand by 12-Digit HUC in the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes the total number of recreational days per year demanded by people ages 18 and over for migratory bird hunting by location in the contiguous United States. These values are based on 2010 population distribution, 2011 U.S. Fish and Wildlife Service (FWS) Fish, Hunting, and Wildlife-Associated Recreation (FHWAR) survey data, and 2011 U.S. Department of Agriculture (USDA) Forest Service National Visitor Use Monitoring program data, and have been summarized by 12-digit hydrologic unit code (HUC). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{bf7112ad-58f7-40c4-9343-e70ab97f8af2}",
+            "issued": "2016-06-13",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243705,46 +243724,46 @@
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Migratory Bird Hunting Recreation Demand by 12-Digit HUC in the Conterminous United States"
         },
-            "identifier": "{bf7112ad-58f7-40c4-9343-e70ab97f8af2}",
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
-            "temporal": "2010-01-01/2010-01-01",
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
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as background in this dataset; waterbodies are separated from the natural land cover classes and included in the analysis with the developed land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as background and 1-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as background in this dataset; waterbodies are separated from the natural land cover classes and included in the analysis with the developed land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{70f7ee8e-55f6-4a28-ade3-2c174a0a3673}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243811,46 +243830,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as background and 1-pixel edge width for the conterminous United States"
         },
-            "identifier": "{70f7ee8e-55f6-4a28-ade3-2c174a0a3673}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as background in this dataset; waterbodies are separated from the natural land cover classes and included in the analysis with the developed land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as background and 3-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as background in this dataset; waterbodies are separated from the natural land cover classes and included in the analysis with the developed land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{be798475-6ba2-47a1-9a24-fd2fc637ce26}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -243917,46 +243936,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as background and 3-pixel edge width for the conterminous United States"
         },
-            "identifier": "{be798475-6ba2-47a1-9a24-fd2fc637ce26}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as foreground in this dataset; waterbodies are included with core natural areas and included in the analysis with the natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as foreground and 1-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as foreground in this dataset; waterbodies are included with core natural areas and included in the analysis with the natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0337e623-728c-4961-8d8b-eb0b4fc47152}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -244023,46 +244042,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as foreground and 1-pixel edge width for the conterminous United States"
         },
-            "identifier": "{0337e623-728c-4961-8d8b-eb0b4fc47152}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as foreground in this dataset; waterbodies are included with core natural areas and included in the analysis with the natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as foreground and 3-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as foreground in this dataset; waterbodies are included with core natural areas and included in the analysis with the natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{12036d85-1cef-4b3e-a416-bc79a80a729c}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -244129,46 +244148,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as foreground and 3-pixel edge width for the conterminous United States"
         },
-            "identifier": "{12036d85-1cef-4b3e-a416-bc79a80a729c}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as missing in this dataset; waterbodies are masked out and not included in the analysis with the development and natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as missing and 1-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as missing in this dataset; waterbodies are masked out and not included in the analysis with the development and natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b7ddc7a5-8cc6-45e6-b3ca-87488c5dbb21}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -244235,46 +244254,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as missing and 1-pixel edge width for the conterminous United States"
         },
-            "identifier": "{b7ddc7a5-8cc6-45e6-b3ca-87488c5dbb21}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as missing in this dataset; waterbodies are masked out and not included in the analysis with the development and natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - MSPA connectivity with water as missing and 3-pixel edge width for the conterminous United States",
-            "description": "This EnviroAtlas dataset categorizes land cover into structural elements (e.g. core, edge, connector, etc.). It depicts core areas of natural land cover, core fragmentation, and patterns of connectivity among core patches. Water is treated as missing in this dataset; waterbodies are masked out and not included in the analysis with the development and natural land cover classes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7c43e58b-1beb-44f1-b0a2-483628029e63}",
+            "issued": "2017-03-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -244341,46 +244360,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-17",
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
+            "title": "EnviroAtlas - MSPA connectivity with water as missing and 3-pixel edge width for the conterminous United States"
         },
-            "identifier": "{7c43e58b-1beb-44f1-b0a2-483628029e63}",
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
-            "issued": "2017-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,772 block groups in Minneapolis/St. Paul, Minnesota. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Anoka, Dakota, Hennepin, and Ramsey Counties, MN. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,772 block groups in Minneapolis/St. Paul, Minnesota. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Anoka, Dakota, Hennepin, and Ramsey Counties, MN. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4089d659-8cc2-4271-8bbd-8c340c850e7c}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -244400,46 +244419,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - BenMAP Results by Block Group"
         },
-            "identifier": "{4089d659-8cc2-4271-8bbd-8c340c850e7c}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Minneapolis/St. Paul, MN EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Minneapolis/St. Paul, MN EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{51d5fa04-aff5-4a79-bfc5-f77522d16eb5}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -244452,46 +244471,46 @@
                 "Environmental Atlas",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Block Groups"
         },
-            "identifier": "{51d5fa04-aff5-4a79-bfc5-f77522d16eb5}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{765ebdd9-3713-4974-a82a-e0af4c68626a}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -244508,46 +244527,46 @@
                 "Boundaries",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Demographics by Block Group"
         },
-            "identifier": "{765ebdd9-3713-4974-a82a-e0af4c68626a}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Minneapolis/St. Paul, MN EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Minneapolis/St. Paul, MN EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{32f4aeed-fb97-4601-bd05-0bcadf475857}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -244560,46 +244579,46 @@
                 "Boundaries",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - EnviroAtlas Community Boundary"
         },
-            "identifier": "{32f4aeed-fb97-4601-bd05-0bcadf475857}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "enviroatlas-minneapolis-st-paul-mn-tree-cover-configuration-and-connectivity",
+            "issued": "2017-05-30",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -244614,46 +244633,46 @@
                 "Environmental Atlas",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-05-30",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "enviroatlas-minneapolis-st-paul-mn-tree-cover-configuration-and-connectivity",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-05-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD or GPCD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential water use reporting in the EnviroAtlas-defined study area is available through the Minnesota Geospatial Commons website. Within the Minneapolis/St Paul study area, there are 45 estimates from 2005 ranging from 42 to 167 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD or GPCD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential water use reporting in the EnviroAtlas-defined study area is available through the Minnesota Geospatial Commons website. Within the Minneapolis/St Paul study area, there are 45 estimates from 2005 ranging from 42 to 167 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6c29143a-e955-4afe-8401-faac49609d73}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -244673,46 +244692,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{6c29143a-e955-4afe-8401-faac49609d73}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community,green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community,green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{be696d31-3343-41b2-9a19-6b143be1e914}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -244728,46 +244747,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{be696d31-3343-41b2-9a19-6b143be1e914}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d67a5058-671b-4bf8-bf21-a14730588ff4}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -244791,46 +244810,46 @@
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{d67a5058-671b-4bf8-bf21-a14730588ff4}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{55c524a1-74e6-4c01-877a-19fcf1e2da60}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -244845,46 +244864,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Green Space Proximity Gradient"
         },
-            "identifier": "{55c524a1-74e6-4c01-877a-19fcf1e2da60}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7d1bd4ce-8f34-4979-bbb8-9f86788092f7}",
+            "issued": "2016-09-30",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -244900,46 +244919,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-30",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Historic Places by Census Block Group"
         },
-            "identifier": "{7d1bd4ce-8f34-4979-bbb8-9f86788092f7}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{51dbd196-bd1b-4343-baed-7be94cf72e6d}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -244953,46 +244972,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Impervious Proximity Gradient"
         },
-            "identifier": "{51dbd196-bd1b-4343-baed-7be94cf72e6d}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ea532fdb-df76-4c5b-afcf-2af27d5b5e10}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -245007,46 +245026,46 @@
                 "Transportation",
                 "Human Well-being"
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{ea532fdb-df76-4c5b-afcf-2af27d5b5e10}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,772 block groups in Minneapolis/St. Paul, Minnesota. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,772 block groups in Minneapolis/St. Paul, Minnesota. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{344cacad-db43-49d0-8704-236f39b6adbf}",
+            "issued": "2016-09-07",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -245065,46 +245084,46 @@
                 "Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-07",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Ecosystem Services by Block Group"
         },
-            "identifier": "{344cacad-db43-49d0-8704-236f39b6adbf}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, agriculture, and wetlands. In this community, forest is defined as Trees and Forest and Woody Wetlands.and green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, agriculture, and wetlands. In this community, forest is defined as Trees and Forest and Woody Wetlands.and green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{df80151d-710a-4ded-8d1d-98831b178eec}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245120,46 +245139,46 @@
                 "Environmental Atlas",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Land Cover by Block Group"
         },
-            "identifier": "{df80151d-710a-4ded-8d1d-98831b178eec}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Minneapolis-St. Paul, MN EnviroAtlas Meter-scale Urban Land Cover (MULC) data were generated from four-band (red, green, blue, and near infrared) aerial photography provided by the United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP). The NAIP imagery for the state of Minnesota was collected during the summer and fall of 2010. Lidar data and relevant ancillary datasets contributed to the classification. Eight land cover types were classified: water, impervious surface, soil and barren land, trees and forest, grass and herbaceous, agriculture, woody wetland, and emergent wetland. An accuracy assessment of 644 completely random and 62 stratified random photointerpreted reference points yielded an overall User's Accuracy of 83 percent. The boundary of this data layer is delineated by the US Census Bureau's 2010 Urban Statistical Area for Minneapolis-St. Paul, MN plus a 1-km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Minneapolis/St. Paul, MN -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The Minneapolis-St. Paul, MN EnviroAtlas Meter-scale Urban Land Cover (MULC) data were generated from four-band (red, green, blue, and near infrared) aerial photography provided by the United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP). The NAIP imagery for the state of Minnesota was collected during the summer and fall of 2010. Lidar data and relevant ancillary datasets contributed to the classification. Eight land cover types were classified: water, impervious surface, soil and barren land, trees and forest, grass and herbaceous, agriculture, woody wetland, and emergent wetland. An accuracy assessment of 644 completely random and 62 stratified random photointerpreted reference points yielded an overall User's Accuracy of 83 percent. The boundary of this data layer is delineated by the US Census Bureau's 2010 Urban Statistical Area for Minneapolis-St. Paul, MN plus a 1-km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8e426180-b263-48b0-ac28-514adc076f03}",
+            "issued": "2016-12-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -245182,46 +245201,46 @@
                 "Minneapolis/St. Paul, MN",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-12-05",
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
+            "spatial": "-93.7854091301, 44.5899921157, -92.9610329068, 45.3094922328",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Minneapolis/St. Paul, MN -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{8e426180-b263-48b0-ac28-514adc076f03}",
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
-            "spatial": "-93.7854091301, 44.5899921157, -92.9610329068, 45.3094922328",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-12-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees and Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees and Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1a723653-0eb5-48c5-ad15-23617b2edb42}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -245239,46 +245258,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Near Road Tree Buffer"
         },
-            "identifier": "{1a723653-0eb5-48c5-ad15-23617b2edb42}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees and Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees and Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2009f5bc-e4e3-46d8-87fc-96a4bec9a387}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -245297,46 +245316,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Near Road Block Group Summary"
         },
-            "identifier": "{2009f5bc-e4e3-46d8-87fc-96a4bec9a387}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{985471ae-f8b6-4f35-a510-7b62087159f2}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -245351,46 +245370,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Park Access by Block Group"
         },
-            "identifier": "{985471ae-f8b6-4f35-a510-7b62087159f2}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6a46d7c8-a344-4d19-a111-0c96a2fda15f}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -245404,46 +245423,46 @@
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Proximity to Parks"
         },
-            "identifier": "{6a46d7c8-a344-4d19-a111-0c96a2fda15f}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2011-01-01/2011-01-01",
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
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees and Forest, Grass and Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dd9a9138-6a1b-41db-af48-a19d833b4d23}",
+            "issued": "2016-10-06",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -245461,46 +245480,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-10-06",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{dd9a9138-6a1b-41db-af48-a19d833b4d23}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees and Forest and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees and Forest and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{99987de2-b31a-43db-ac6d-117180e04d51}",
+            "issued": "2016-10-06",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -245518,46 +245537,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-10-06",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{99987de2-b31a-43db-ac6d-117180e04d51}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees and Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees and Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3dd12d45-b77b-44de-bbe9-101e0b44acd7}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245577,46 +245596,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{3dd12d45-b77b-44de-bbe9-101e0b44acd7}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2df6ed65-b315-4c17-9e51-40fe581aa4ad}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245636,46 +245655,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{2df6ed65-b315-4c17-9e51-40fe581aa4ad}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees and Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees and Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f7ae2e8b-8979-4ad2-b14c-98bec47c91ac}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245695,46 +245714,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{f7ae2e8b-8979-4ad2-b14c-98bec47c91ac}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c3e91c42-8c59-469b-8d1b-fcfed11c3fc7}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245754,46 +245773,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{c3e91c42-8c59-469b-8d1b-fcfed11c3fc7}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees and Forest and Woody Wetlands. and vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees and Forest and Woody Wetlands. and vegetated cover is defined as Trees and Forest, Grass and Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{547a3d12-8fcf-4bfb-92ed-9275745390b1}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245814,46 +245833,46 @@
                 "Drinking Water",
                 "Minnesota"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{547a3d12-8fcf-4bfb-92ed-9275745390b1}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, forest is defined as Trees and Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, forest is defined as Trees and Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e20621c1-27e9-4fb4-8cee-035302ec42c9}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -245871,46 +245890,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{e20621c1-27e9-4fb4-8cee-035302ec42c9}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e26fbd82-c372-4e86-aefd-8955df3da84f}",
+            "issued": "2016-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -245926,46 +245945,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-09-09",
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
+            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Minneapolis/St. Paul, MN - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{e26fbd82-c372-4e86-aefd-8955df3da84f}",
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
-            "spatial": "-93.772509, 44.601617, -92.974149, 45.297876",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 703 block groups in Memphis, Tennessee. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MinneapolisStPaulMN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 703 block groups in Memphis, Tennessee. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6A87D03C-3810-49C1-AC70-57B22625C328}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -245985,46 +246004,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - BenMAP Results by Block Group"
         },
-            "identifier": "{6A87D03C-3810-49C1-AC70-57B22625C328}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "9999-01-01/9999-01-01",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Memphis, TN EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Memphis, TN EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7C471986-A8AD-4299-AB8E-16B98B6BDC3E}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246037,46 +246056,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2013-11-05/2013-11-05",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Block Groups"
         },
-            "identifier": "{7C471986-A8AD-4299-AB8E-16B98B6BDC3E}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2013-11-05/2013-11-05",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FA170F4C-1230-488F-8B5C-B04583D69259}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -246093,46 +246112,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Memphis, TN - Demographics by Block Group"
         },
-            "identifier": "{FA170F4C-1230-488F-8B5C-B04583D69259}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Memphis, TN EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Memphis, TN EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CE000148-3663-4A52-B98C-4069BB693CFF}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246145,46 +246164,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2013-10-24/2013-10-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - EnviroAtlas Community Boundary"
         },
-            "identifier": "{CE000148-3663-4A52-B98C-4069BB693CFF}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2013-10-24/2013-10-24",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). Forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). Forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "enviroatlas-memphis-tn-tree-cover-configuration-and-connectivity-water-background",
+            "issued": "2017-05-30",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -246199,46 +246218,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-05-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-03-03/2015-03-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "enviroatlas-memphis-tn-tree-cover-configuration-and-connectivity-water-background",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-03-03/2015-03-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-05-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential water use in the EnviroAtlas-defined study area is estimated at between 81 and 100 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential water use in the EnviroAtlas-defined study area is estimated at between 81 and 100 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{009DC293-238A-45BD-8404-3FD20B9126CC}",
+            "issued": "2015-02-24",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -246258,46 +246277,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-02-24",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{009DC293-238A-45BD-8404-3FD20B9126CC}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-02-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C6586DCF-066A-4F59-9088-1F37742B518C}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -246313,46 +246332,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-20/2015-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{C6586DCF-066A-4F59-9088-1F37742B518C}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-20/2015-07-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7fc02bf1-9a32-4d74-a3e0-e0d1ea4e115b}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -246376,46 +246395,46 @@
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.385504",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{7fc02bf1-9a32-4d74-a3e0-e0d1ea4e115b}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.385504",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{754C27D5-C0EA-41B1-9B45-6E00EAEFC526}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246430,46 +246449,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Green Space Proximity Gradient"
         },
-            "identifier": "{754C27D5-C0EA-41B1-9B45-6E00EAEFC526}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{EB00218A-48CD-4215-910D-0E9134027520}",
+            "issued": "2015-11-20",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246485,46 +246504,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-20",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Historic Places by Census Block Group"
         },
-            "identifier": "{EB00218A-48CD-4215-910D-0E9134027520}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8D2851A7-E783-49F8-A0C6-9B1AD784411B}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246538,46 +246557,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Impervious Proximity Gradient"
         },
-            "identifier": "{8D2851A7-E783-49F8-A0C6-9B1AD784411B}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9C5E1317-F07D-4CEF-935A-A494E0BE7A7F}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -246592,46 +246611,46 @@
                 "Transportation",
                 "Human Well-being"
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.385504",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{9C5E1317-F07D-4CEF-935A-A494E0BE7A7F}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.385504",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 703 block groups in Memphis, Tennessee. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 703 block groups in Memphis, Tennessee. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E1D73F82-A206-4AF7-9658-A1CFFD6154EC}",
+            "issued": "2015-12-01",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -246650,46 +246669,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-01",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Ecosystem Services by Block Group"
         },
-            "identifier": "{E1D73F82-A206-4AF7-9658-A1CFFD6154EC}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, agriculture, and wetlands. Forest is defined as Trees & Forest and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, agriculture, and wetlands. Forest is defined as Trees & Forest and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{80A22622-4B2C-4C27-843D-F0B7E3610F02}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -246706,46 +246725,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-20/2015-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Land Cover by Block Group"
         },
-            "identifier": "{80A22622-4B2C-4C27-843D-F0B7E3610F02}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-20/2015-07-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Memphis, TN EnviroAtlas One Meter-scale Urban Land Cover (MULC) dataset comprises 2,733 km2 around the city of Memphis, surrounding towns, and rural areas. These leaf-on LC data and maps were derived from 1-m pixel, four-band (red, green, blue, and near-infrared) aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) on four dates in 2012: June 15, June 18, June 21 and June 23, and one date in 2013: July 12. Three separate LiDAR (Light Detection and Ranging) data sets collected on February 19, 2009 - August 2, 2010, December 1-2, 2011 and January 23-24, 2012 were integrated for Shelby Co., TN, Crittenden Co., AR, and DeSoto Co, MS. Five MULC classes were mapped directly from the NAIP and LiDAR data: Water, Impervious, Soil, Trees, and Grass/Herbaceous. Agriculture was derived from USDA Common Land Unit (CLU) data. Woody and emergent wetlands were copied from existing National Wetlands Inventory (NWI) data. Analysis of a random sampling of 612 photo-interpreted land cover reference points yielded an overall users accuracy of 86.9%. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Memphis, Tennessee -- Meter-Scale Urban Land Cover (MULC) Data (2012)",
-            "description": "The Memphis, TN EnviroAtlas One Meter-scale Urban Land Cover (MULC) dataset comprises 2,733 km2 around the city of Memphis, surrounding towns, and rural areas. These leaf-on LC data and maps were derived from 1-m pixel, four-band (red, green, blue, and near-infrared) aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) on four dates in 2012: June 15, June 18, June 21 and June 23, and one date in 2013: July 12. Three separate LiDAR (Light Detection and Ranging) data sets collected on February 19, 2009 - August 2, 2010, December 1-2, 2011 and January 23-24, 2012 were integrated for Shelby Co., TN, Crittenden Co., AR, and DeSoto Co, MS. Five MULC classes were mapped directly from the NAIP and LiDAR data: Water, Impervious, Soil, Trees, and Grass/Herbaceous. Agriculture was derived from USDA Common Land Unit (CLU) data. Woody and emergent wetlands were copied from existing National Wetlands Inventory (NWI) data. Analysis of a random sampling of 612 photo-interpreted land cover reference points yielded an overall users accuracy of 86.9%. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{61C69E94-1EB4-42B7-8C56-4D064C05243E}",
+            "issued": "2015-12-03",
             "keyword": [
                 "Ecosystem Services",
                 "Wetlands",
@@ -246765,46 +246784,46 @@
                 "Environmental Atlas",
                 "Biophysical"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-03",
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
+            "spatial": "-90.324550, 34.714780, -89.624648, 35.402557",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Memphis, Tennessee -- Meter-Scale Urban Land Cover (MULC) Data (2012)"
         },
-            "identifier": "{61C69E94-1EB4-42B7-8C56-4D064C05243E}",
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
-            "spatial": "-90.324550, 34.714780, -89.624648, 35.402557",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9DBB7006-B86C-43B7-8531-38F8D3E229A3}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -246823,46 +246842,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-19",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Near Road Tree Buffer"
         },
-            "identifier": "{9DBB7006-B86C-43B7-8531-38F8D3E229A3}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{30C8C193-233A-4FEA-81BF-159F22B7CC9B}",
+            "issued": "2014-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -246881,46 +246900,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-07",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Near Road Block Group Summary"
         },
-            "identifier": "{30C8C193-233A-4FEA-81BF-159F22B7CC9B}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B553C7FE-2F39-49F3-8CA2-FF7DF6765FC3}",
+            "issued": "2015-12-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246935,46 +246954,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-01",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Park Access by Block Group"
         },
-            "identifier": "{B553C7FE-2F39-49F3-8CA2-FF7DF6765FC3}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-10-01/2015-10-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BBF52A70-DCCF-4DB6-ACDE-82A321A03F8C}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -246988,46 +247007,46 @@
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-20/2015-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Proximity to Parks"
         },
-            "identifier": "{BBF52A70-DCCF-4DB6-ACDE-82A321A03F8C}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-20/2015-07-20",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{EA4CAD62-CB0F-4B5F-B76D-60786EFC240F}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -247045,46 +247064,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{EA4CAD62-CB0F-4B5F-B76D-60786EFC240F}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BE552E7A-A789-4AA9-ADF9-234109C6517E}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -247102,46 +247121,46 @@
                 "Trees",
                 "Human Well-being"
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
-            },
-            "identifier": "{BE552E7A-A789-4AA9-ADF9-234109C6517E}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
             "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-08-07",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
-        },
+            "title": "EnviroAtlas - Memphis, TN - Estimated Percent Tree Cover Along Walkable Roads"
+        },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - 15m Riparian Buffer Forest Cover",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
             "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. Forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{86CB334C-C74F-4B42-BE2F-28BBEDB764CE}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247161,46 +247180,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{86CB334C-C74F-4B42-BE2F-28BBEDB764CE}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{52B6F298-50DD-404B-91DB-11ACA93CF798}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247220,46 +247239,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{52B6F298-50DD-404B-91DB-11ACA93CF798}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. Forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. Forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D46AD66D-EF29-4CDD-AFDB-C2D6AD09372D}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247279,46 +247298,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-08",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{D46AD66D-EF29-4CDD-AFDB-C2D6AD09372D}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AACB2A04-8675-43BC-81E6-EACBEB8ABCCD}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247338,46 +247357,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-21/2015-07-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{AACB2A04-8675-43BC-81E6-EACBEB8ABCCD}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-21/2015-07-21",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. Forest is defined as Trees & Forest and Woody Wetlands. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. Forest is defined as Trees & Forest and Woody Wetlands. Vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2CE454EA-9382-4375-881A-96FA485296D3}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247398,46 +247417,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-07-20/2015-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{2CE454EA-9382-4375-881A-96FA485296D3}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-07-20/2015-07-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7869ADB1-85CF-4D5A-B989-36DFC1C3919A}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -247455,46 +247474,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{7869ADB1-85CF-4D5A-B989-36DFC1C3919A}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-10-01/2015-10-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Memphis, TN - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B5D1624C-90C3-4050-AF0C-258153B6BC48}",
+            "issued": "2015-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -247510,46 +247529,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-30",
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
+            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Memphis, TN - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{B5D1624C-90C3-4050-AF0C-258153B6BC48}",
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
-            "spatial": "-90.319154, 34.732073, -89.628181, 35.402340",
-            "temporal": "2015-10-01/2015-10-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,175 block groups in Milwaukee, Wisconsin. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Milwaukee, Ozaukee, Washington, and Waukesha Counties, WI. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MemphisTN",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,175 block groups in Milwaukee, Wisconsin. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Milwaukee, Ozaukee, Washington, and Waukesha Counties, WI. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{57730CE3-F739-41E7-BF53-F98834151778}",
+            "issued": "2017-08-04",
             "keyword": [
                 "Exposure",
                 "Milwaukee, WI",
@@ -247569,46 +247588,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-08-04",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - BenMAP Results by Block Group"
         },
-            "identifier": "{57730CE3-F739-41E7-BF53-F98834151778}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-08-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Milwaukee, WI EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Milwaukee, WI EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BA0816D2-0CE1-4B05-A89F-C4041D24DD48}",
+            "issued": "2017-11-17",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -247621,46 +247640,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-17",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Census Block Groups"
         },
-            "identifier": "{BA0816D2-0CE1-4B05-A89F-C4041D24DD48}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A780D52C-AB37-4DF2-A141-94D3DB292249}",
+            "issued": "2017-11-17",
             "keyword": [
                 "Milwaukee, WI",
                 "Human",
@@ -247677,46 +247696,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-17",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Milwaukee, WI - Demographics by Block Group"
         },
-            "identifier": "{A780D52C-AB37-4DF2-A141-94D3DB292249}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-17",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Milwaukee, WI EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Milwaukee, WI EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{34B78FAB-9584-4B84-ADA8-116628366799}",
+            "issued": "2017-11-17",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -247729,46 +247748,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-17",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - EnviroAtlas Community Boundary"
         },
-            "identifier": "{34B78FAB-9584-4B84-ADA8-116628366799}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{743BCDE5-141B-414F-B85B-1E9C16B08EA5}",
+            "issued": "2019-11-12",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -247784,46 +247803,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-12",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{743BCDE5-141B-414F-B85B-1E9C16B08EA5}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Oversight of water utilities at the state level is handled by the Public Service Commission of Wisconsin. Within the Milwaukee boundary, there are 30 service providers with 2008-2012 estimates ranging from 39 to 74 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Oversight of water utilities at the state level is handled by the Public Service Commission of Wisconsin. Within the Milwaukee boundary, there are 30 service providers with 2008-2012 estimates ranging from 39 to 74 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{12033935-1ABA-4D77-89B0-914E40EE5A83}",
+            "issued": "2014-10-31",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -247843,46 +247862,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-31",
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
+            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{12033935-1ABA-4D77-89B0-914E40EE5A83}",
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
-            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-10-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1D52E6B0-9540-4CCA-8234-F8742790648E}",
+            "issued": "2017-11-17",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -247898,46 +247917,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-17",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{1D52E6B0-9540-4CCA-8234-F8742790648E}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ac91e0d3-8299-43f5-af11-90b03bde21cd}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -247961,46 +247980,46 @@
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
+            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{ac91e0d3-8299-43f5-af11-90b03bde21cd}",
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
-            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9AEF0BAA-8C8D-49BD-A6FD-0CA4FCBC159B}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248015,46 +248034,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Green Space Proximity Gradient"
         },
-            "identifier": "{9AEF0BAA-8C8D-49BD-A6FD-0CA4FCBC159B}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3F8A9526-1D4D-4321-B122-06F2202EB7FD}",
+            "issued": "2014-08-26",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248070,46 +248089,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-26",
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
+            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Historic Places by Census Block Group"
         },
-            "identifier": "{3F8A9526-1D4D-4321-B122-06F2202EB7FD}",
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
-            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9E570625-171E-4C99-805A-CB693059A067}",
+            "issued": "2017-11-21",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248123,46 +248142,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-21",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Impervious Proximity Gradient"
         },
-            "identifier": "{9E570625-171E-4C99-805A-CB693059A067}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{991BCB95-1624-4102-95D5-6B1E382F5C12}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248177,46 +248196,46 @@
                 "Transportation",
                 "Human Well-being"
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{991BCB95-1624-4102-95D5-6B1E382F5C12}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,175 block groups in Milwaukee, Wisconsin. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,175 block groups in Milwaukee, Wisconsin. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{EE017535-9D3C-43E7-89B1-AE908F209B64}",
+            "issued": "2017-08-04",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248235,46 +248254,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-08-04",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Ecosystem Services by Block Group"
         },
-            "identifier": "{EE017535-9D3C-43E7-89B1-AE908F209B64}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-08-04",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{104F9776-1473-4B41-A8F3-15C80EF50879}",
+            "issued": "2017-11-17",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248290,46 +248309,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-17",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Land Cover by Block Group"
         },
-            "identifier": "{104F9776-1473-4B41-A8F3-15C80EF50879}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The EnviroAtlas Milwaukee, WI Meter Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from Late Summer 2010 at 1 meter spatial scale. Eight land cover classes were mapped: water, impervious surfaces (dark and light), soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, agriculture, and wetlands (woody and emergent). An accuracy assessment yielded an overall user's accuracy (MAX) of 76.2 percent and a fuzzy user's accuracy (RIGHT) of 85.5 (see Overview section). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Milwaukee. This dataset was produced by Oneida Total Integrated Enterprises (OTIE), its subcontractor, the University of Arkansas Center for Advanced Spatial Technologies (CAST), and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Meter-Scale Urban Land Cover Data (MULC) Data (2010)",
-            "description": "The EnviroAtlas Milwaukee, WI Meter Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from Late Summer 2010 at 1 meter spatial scale. Eight land cover classes were mapped: water, impervious surfaces (dark and light), soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, agriculture, and wetlands (woody and emergent). An accuracy assessment yielded an overall user's accuracy (MAX) of 76.2 percent and a fuzzy user's accuracy (RIGHT) of 85.5 (see Overview section). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Milwaukee. This dataset was produced by Oneida Total Integrated Enterprises (OTIE), its subcontractor, the University of Arkansas Center for Advanced Spatial Technologies (CAST), and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9780F143-C78D-4FB6-91C1-DDCDCAE30EBE}",
+            "issued": "2017-03-14",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -248352,46 +248371,46 @@
                 "Agriculture",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-14",
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
+            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Meter-Scale Urban Land Cover Data (MULC) Data (2010)"
         },
-            "identifier": "{9780F143-C78D-4FB6-91C1-DDCDCAE30EBE}",
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
-            "spatial": "-88.54936, 42.84283, -87.79614, 43.44913",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F66406EC-DE10-4BB8-B948-8B7E7B487ABE}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248409,46 +248428,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{F66406EC-DE10-4BB8-B948-8B7E7B487ABE}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{24A7E9CD-EF30-4381-A1C6-6248298304B1}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248467,46 +248486,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{24A7E9CD-EF30-4381-A1C6-6248298304B1}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AE21A127-D4ED-415F-BC4C-D3CD3117E35C}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248521,46 +248540,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
-            },
-            "identifier": "{AE21A127-D4ED-415F-BC4C-D3CD3117E35C}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
             "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Park Access by Block Group"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E0EC8E26-0688-4EC5-8611-BF300054820E}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248574,46 +248593,46 @@
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Proximity to Parks"
         },
-            "identifier": "{E0EC8E26-0688-4EC5-8611-BF300054820E}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2011-01-01/2011-01-01",
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
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1F0F363E-147B-4253-8912-0EBF54D548FC}",
+            "issued": "2017-11-21",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248631,46 +248650,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-21",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{1F0F363E-147B-4253-8912-0EBF54D548FC}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{922381C1-009A-4EC6-AAE8-7809AE0B23D7}",
+            "issued": "2017-11-21",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248688,46 +248707,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-21",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{922381C1-009A-4EC6-AAE8-7809AE0B23D7}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6D35F1D5-7301-494C-BFE2-6A1446810ADC}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248747,46 +248766,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{6D35F1D5-7301-494C-BFE2-6A1446810ADC}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5426CC75-0953-4BC9-86F3-B96DFB6DA661}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248806,46 +248825,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{5426CC75-0953-4BC9-86F3-B96DFB6DA661}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{52EEA142-035E-48F4-981F-9EA4F3279F9B}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248865,46 +248884,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{52EEA142-035E-48F4-981F-9EA4F3279F9B}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7DD7C43B-E15A-43C1-94CD-91512F22E89E}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248924,46 +248943,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{7DD7C43B-E15A-43C1-94CD-91512F22E89E}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. Vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. Vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{88E6AD36-C6D1-4C64-BFFE-EC5CCE916CC4}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -248984,46 +249003,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{88E6AD36-C6D1-4C64-BFFE-EC5CCE916CC4}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C2C6C515-654B-4C2F-9917-594D7E920A67}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -249041,46 +249060,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{C2C6C515-654B-4C2F-9917-594D7E920A67}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Milwaukee, WI - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{92BF58F3-6820-466B-8980-EDCDBB70A81E}",
+            "issued": "2017-11-20",
             "keyword": [
                 "Milwaukee, WI",
                 "Ecosystem Services",
@@ -249096,46 +249115,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-20",
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
+            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Milwaukee, WI - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{92BF58F3-6820-466B-8980-EDCDBB70A81E}",
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
-            "spatial": "-88.53393, 42.83492, -87.80415, 43.4568",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by 2010 counties. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/MilwaukeeWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by County - 2014",
-            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by 2010 counties. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
+            ],
+            "identifier": "{52db5976-973e-4a7f-8650-d483cbc2ee12}",
+            "issued": "2019-08-15",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -249207,46 +249226,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-15",
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
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by County - 2014"
         },
-            "identifier": "{52db5976-973e-4a7f-8650-d483cbc2ee12}",
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
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-15",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by state. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
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
-            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by State - 2014",
-            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by state. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
+            ],
+            "identifier": "{01a2f8ab-4d84-455c-a1f2-6b5f91346b09}",
+            "issued": "2019-08-15",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -249318,46 +249337,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-15",
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
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by State - 2014"
         },
-            "identifier": "{01a2f8ab-4d84-455c-a1f2-6b5f91346b09}",
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
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-15",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by 2010 U.S. Census Tract. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
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
-            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by Census Tract - 2014",
-            "description": "These layers are a selection of the National Air Toxics Assessment (NATA) 2014 estimates of ambient concentrations and health-effect results by 2010 U.S. Census Tract. The Environmental Protection Agency (EPA) developed NATA as a screening tool to identify potential health risks from toxic air pollutants for further study. Please see NATA's website (https://www.epa.gov/national-air-toxics-assessment) for information about using NATA. This dataset is based on data from 2014 NATA, which was produced by the US EPA to estimate health risks from toxic air pollutants. It was modified for incorporation into the Compare my Area tool. The NATA results are available as downloadable data from https://www.epa.gov/national-air-toxics-assessment/2014-nata-assessment-results.",
+            ],
+            "identifier": "{99b1d6d6-cdf2-4c19-ba63-fdb8f11eafdb}",
+            "issued": "2019-08-15",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -249429,46 +249448,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-15",
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
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Selected National Air Toxics Assessment Results by Census Tract - 2014"
         },
-            "identifier": "{99b1d6d6-cdf2-4c19-ba63-fdb8f11eafdb}",
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
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-15",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains the percentage of small, medium, and large natural areas for each Watershed Boundary Dataset (WBD) 12-Digit Hydrologic Unit Code (HUC-12) of the conterminous United States that is considered Natural based on the National Land Cover Database (NLCD). The percentage of natural area is by size class: Small is <500 acres, Medium is 500-25,000 acres, and Large is > 25,000 acres. Natural land cover combines NLCD-CDL 63, 83, 87, 111, 112, 131, 141, 142, 143, 151, 152, 171, 190, 195. This dataset was produced by the Tetra Tech, Inc. to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Percent Large, Medium, and Small Natural Areas for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains the percentage of small, medium, and large natural areas for each Watershed Boundary Dataset (WBD) 12-Digit Hydrologic Unit Code (HUC-12) of the conterminous United States that is considered Natural based on the National Land Cover Database (NLCD). The percentage of natural area is by size class: Small is <500 acres, Medium is 500-25,000 acres, and Large is > 25,000 acres. Natural land cover combines NLCD-CDL 63, 83, 87, 111, 112, 131, 141, 142, 143, 151, 152, 171, 190, 195. This dataset was produced by the Tetra Tech, Inc. to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B803EDB7-3BE0-4ADF-870C-2EB9733310AE}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -249530,46 +249549,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-07",
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
+            "title": "EnviroAtlas - Percent Large, Medium, and Small Natural Areas for the Conterminous United States"
         },
-            "identifier": "{B803EDB7-3BE0-4ADF-870C-2EB9733310AE}",
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
-            "issued": "2015-05-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This web service includes layers depicting EnviroAtlas national metrics mapped at the 12-digit HUC within the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas National Layers Master Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This web service includes layers depicting EnviroAtlas national metrics mapped at the 12-digit HUC within the conterminous United States. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{fe643065-3153-46a5-8c5e-b9cc3ede39ff}",
+            "issued": "2017-02-21",
             "keyword": [
                 "Connecticut",
                 "Modeling",
@@ -249686,46 +249705,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-02-21",
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
+            "title": "EnviroAtlas National Layers Master Web Service"
         },
-            "identifier": "{fe643065-3153-46a5-8c5e-b9cc3ede39ff}",
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
-            "issued": "2017-02-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the native freshwater aquatic biodiversity by 12-digit HUC (subwatershed) for the conterminous United States. It includes amphibians, fish, mollusks, decapods, and turtles. The metrics are: total species richness; count of threatened and endangered species; a rarity index; and a native vulnerability index. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Native Freshwater Aquatic Biodiversity by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset describes the native freshwater aquatic biodiversity by 12-digit HUC (subwatershed) for the conterminous United States. It includes amphibians, fish, mollusks, decapods, and turtles. The metrics are: total species richness; count of threatened and endangered species; a rarity index; and a native vulnerability index. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{63eab210-e5bc-4e7c-bb6d-15dfae09b2ec}",
+            "issued": "2018-05-24",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -249791,46 +249810,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-05-24",
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
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Native Freshwater Aquatic Biodiversity by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{63eab210-e5bc-4e7c-bb6d-15dfae09b2ec}",
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
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-05-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset includes analysis by NatureServe of species that are Imperiled (G1/G2) or Listed under the U.S. Endangered Species Act (ESA) by 12-digit Hydrologic Units (HUCs). The analysis results are for use and publication by both the LandScope America website and by the EnviroAtlas. Results are provided for the total number of Aquatic Associated G1-G2/ESA species, the total number of Wetland Associated G1-G2/ESA species, the total number of Terrestrial Associated G1-G2/ESA species, and the total number of Unknown Habitat Association G1-G2/ESA species in each HUC12. NatureServe is a non-profit organization dedicated to developing and providing information about the world's plants, animals, and ecological communities. NatureServe works in partnership with 82 independent Natural Heritage programs and Conservation Data Centers that gather scientific information on rare species and ecosystems in the United States, Latin America, and Canada (the Natural Heritage Network). NatureServe is a leading source for biodiversity information that is essential for effective conservation action. This dataset was produced by NatureServe to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - NatureServe Analysis of Imperiled or Federally Listed Species by HUC-12 for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes analysis by NatureServe of species that are Imperiled (G1/G2) or Listed under the U.S. Endangered Species Act (ESA) by 12-digit Hydrologic Units (HUCs). The analysis results are for use and publication by both the LandScope America website and by the EnviroAtlas. Results are provided for the total number of Aquatic Associated G1-G2/ESA species, the total number of Wetland Associated G1-G2/ESA species, the total number of Terrestrial Associated G1-G2/ESA species, and the total number of Unknown Habitat Association G1-G2/ESA species in each HUC12. NatureServe is a non-profit organization dedicated to developing and providing information about the world's plants, animals, and ecological communities. NatureServe works in partnership with 82 independent Natural Heritage programs and Conservation Data Centers that gather scientific information on rare species and ecosystems in the United States, Latin America, and Canada (the Natural Heritage Network). NatureServe is a leading source for biodiversity information that is essential for effective conservation action. This dataset was produced by NatureServe to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9E49350E-728C-4B75-90B5-A2A2A62C019E}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -249899,46 +249918,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-07",
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
+            "spatial": "-128.02839229, 17.673736, -64.565191, 71.439573",
+            "temporal": "2011-10-14/2011-10-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - NatureServe Analysis of Imperiled or Federally Listed Species by HUC-12 for the Conterminous United States"
         },
-            "identifier": "{9E49350E-728C-4B75-90B5-A2A2A62C019E}",
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
-            "spatial": "-128.02839229, 17.673736, -64.565191, 71.439573",
-            "temporal": "2011-10-14/2011-10-14",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 128 block group in New Bedford, Massachusetts. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 128 block group in New Bedford, Massachusetts. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6FD091EA-47E1-4D4F-AE1F-F3335F200E50}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Massachusetts",
@@ -249958,46 +249977,46 @@
                 "New Bedford",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - BenMAP Results by Block Group"
         },
-            "identifier": "{6FD091EA-47E1-4D4F-AE1F-F3335F200E50}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
+            "description": "This EnviroAtlas dataset is the base layer for the New Bedford, MA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the New Bedford, MA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{476514A6-7569-463B-B06C-15B41C485E29}",
+            "issued": "2014-01-01",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250010,46 +250029,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Block Groups"
         },
-            "identifier": "{476514A6-7569-463B-B06C-15B41C485E29}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-01-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E4EFA84E-DBE2-4957-982E-F925B9FFEDCF}",
+            "issued": "2014-01-01",
             "keyword": [
                 "Massachusetts",
                 "Human",
@@ -250066,46 +250085,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - New Bedford, MA - Demographics by Block Group"
         },
-            "identifier": "{E4EFA84E-DBE2-4957-982E-F925B9FFEDCF}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the New Bedford, MA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the New Bedford, MA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CF310BFF-73E9-4084-AEA8-04E6A444DB09}",
+            "issued": "2013-10-24",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250118,46 +250137,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-10-24",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Atlas Area Boundary"
         },
-            "identifier": "{CF310BFF-73E9-4084-AEA8-04E6A444DB09}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-10-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7230F45E-5C9A-4A81-A4CC-A554F820A5E6}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250172,46 +250191,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{7230F45E-5C9A-4A81-A4CC-A554F820A5E6}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential Gallons per Capita per Day (RGPCD) in the EnviroAtlas-defined study area is available through the Commonwealth of Massachusetts' (mass.gov). Within the New Bedford boundary, there are five service providers with 2008-2013 estimates ranging from 45 to 76 GPD.This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Residential Gallons per Capita per Day (RGPCD) in the EnviroAtlas-defined study area is available through the Commonwealth of Massachusetts' (mass.gov). Within the New Bedford boundary, there are five service providers with 2008-2013 estimates ranging from 45 to 76 GPD.This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{300C9AEE-CE7E-4BA4-858F-62E5DDB4EC8B}",
+            "issued": "2014-10-27",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250231,46 +250250,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-27",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{300C9AEE-CE7E-4BA4-858F-62E5DDB4EC8B}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-10-27",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3F227FB6-AA78-4025-AB29-FDF90E146983}",
+            "issued": "2014-02-24",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250286,48 +250305,48 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-02-24",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2013-12-31/2013-12-31",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{3F227FB6-AA78-4025-AB29-FDF90E146983}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2013-12-31/2013-12-31",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-02-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
-            "keyword": [
-                "Ecosystem Services",
+            ],
+            "identifier": "{f149b8f3-9116-4ad3-aba6-e8f8464c3973}",
+            "issued": "2017-07-19",
+            "keyword": [
+                "Ecosystem Services",
                 "Hazards",
                 "Land Cover",
                 "Ecosystem",
@@ -250349,46 +250368,46 @@
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{f149b8f3-9116-4ad3-aba6-e8f8464c3973}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{61266EC3-8065-4FA6-BA62-7AAAE2CE7FA3}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250403,46 +250422,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2015-03-19/2015-03-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Greenspace Proximity Gradient"
         },
-            "identifier": "{61266EC3-8065-4FA6-BA62-7AAAE2CE7FA3}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2015-03-19/2015-03-19",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{271EEB8C-EBB8-4513-835B-E86D3CE47D56}",
+            "issued": "2014-09-16",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250458,46 +250477,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Historic Places by Census Block Group"
         },
-            "identifier": "{271EEB8C-EBB8-4513-835B-E86D3CE47D56}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D7C6E530-7E8A-4CC4-A206-0FB27D793695}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250511,46 +250530,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2015-03-25/2015-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Impervious Proximity Gradient"
         },
-            "identifier": "{D7C6E530-7E8A-4CC4-A206-0FB27D793695}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{89E0CE0B-DAEE-430E-A8E4-C486B3FD803F}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -250565,46 +250584,46 @@
                 "Transportation",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{89E0CE0B-DAEE-430E-A8E4-C486B3FD803F}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 128 block group in New Bedford, Massachusetts. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 128 block group in New Bedford, Massachusetts. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2370BB5A-1E9D-4505-9E67-6285DE5630BD}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250623,46 +250642,46 @@
                 "Climate",
                 "Water"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Ecosystem Services by Block Group"
         },
-            "identifier": "{2370BB5A-1E9D-4505-9E67-6285DE5630BD}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2010-01-01/2010-01-01",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and wetlands. Forest is a combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and wetlands. Forest is a combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CFA7B8FC-B211-410D-B0C1-9A6A1CEB5429}",
+            "issued": "2014-02-24",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250679,46 +250698,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-02-24",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-09/2014-01-09",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Land Cover by Block Group"
         },
-            "identifier": "{CFA7B8FC-B211-410D-B0C1-9A6A1CEB5429}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-09/2014-01-09",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-02-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The New Bedford, MA Meter-Scale Urban Land Cover (MULC) data were generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution. Imagery was collected in August of 2010. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, woody wetlands and emergent wetlands. An accuracy assessment of 500 completely random and 45 stratified random points yielded an overall user's accuracy (MAX) of 92.3% and an overall fuzzy user's accuracy (RIGHT) of 95.1%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for New Bedford, MA plus a 1 km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- New Bedford, Massachusetts -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The New Bedford, MA Meter-Scale Urban Land Cover (MULC) data were generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution. Imagery was collected in August of 2010. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, woody wetlands and emergent wetlands. An accuracy assessment of 500 completely random and 45 stratified random points yielded an overall user's accuracy (MAX) of 92.3% and an overall fuzzy user's accuracy (RIGHT) of 95.1%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for New Bedford, MA plus a 1 km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{901B707A-F205-4B85-A9C1-8C01DA206E60}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -250741,46 +250760,46 @@
                 "Agriculture",
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
+            "spatial": "-71.108338, 41.540689, -70.770086, 41.894446",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- New Bedford, Massachusetts -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{901B707A-F205-4B85-A9C1-8C01DA206E60}",
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
-            "spatial": "-71.108338, 41.540689, -70.770086, 41.894446",
-            "temporal": "2010-01-01/2010-01-01",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C0D14034-B230-435C-8357-91CF1FC55AA3}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250798,46 +250817,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Near Road Tree Buffer"
         },
-            "identifier": "{C0D14034-B230-435C-8357-91CF1FC55AA3}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5877E839-048D-4578-B7F9-554897C567EC}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250857,46 +250876,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Near Road Block Group Summary"
         },
-            "identifier": "{5877E839-048D-4578-B7F9-554897C567EC}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8C1C9324-A5EB-4256-BCE9-B9133388BBD0}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250911,46 +250930,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Park Access by Block Group"
         },
-            "identifier": "{8C1C9324-A5EB-4256-BCE9-B9133388BBD0}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{15DE4903-7C9D-4F61-9761-53D9904447C1}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -250964,46 +250983,46 @@
                 "New Bedford",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Proximity to Parks"
         },
-            "identifier": "{15DE4903-7C9D-4F61-9761-53D9904447C1}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{233796CF-1DF0-436F-8480-B6C960B57768}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251021,46 +251040,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{233796CF-1DF0-436F-8480-B6C960B57768}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ECA7BDD7-8461-4C97-A406-B52B7B453282}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251078,46 +251097,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{ECA7BDD7-8461-4C97-A406-B52B7B453282}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B299B0C2-7759-4470-86C8-79F5001F6FF2}",
+            "issued": "2014-02-25",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251137,46 +251156,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-02-25",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-14/2014-01-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{B299B0C2-7759-4470-86C8-79F5001F6FF2}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-14/2014-01-14",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-02-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3740370C-C0A4-4F12-A3DB-46A745407D51}",
+            "issued": "2014-01-14",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251196,46 +251215,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-14",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-14/2014-01-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{3740370C-C0A4-4F12-A3DB-46A745407D51}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-14/2014-01-14",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-01-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CD937B20-CB6B-4764-B8A3-32B819CCA1CB}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251255,46 +251274,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-14/2014-01-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{CD937B20-CB6B-4764-B8A3-32B819CCA1CB}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-14/2014-01-14",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4C038D6E-360B-41C8-97C9-F4EB4971E835}",
+            "issued": "2014-01-14",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251314,46 +251333,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-14",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-14/2014-01-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{4C038D6E-360B-41C8-97C9-F4EB4971E835}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-14/2014-01-14",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-01-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D40CC0AB-C73F-4021-9C90-002396318687}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251374,46 +251393,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2012-01-01",
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-01-09/2014-01-09",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{D40CC0AB-C73F-4021-9C90-002396318687}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-01-09/2014-01-09",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{00493E9F-FECB-4B7B-A406-98FD6C26E519}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251431,46 +251450,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-06-19/2014-06-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{00493E9F-FECB-4B7B-A406-98FD6C26E519}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-06-19/2014-06-19",
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
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Bedford, MA - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{980643A8-2DB1-4A8B-B995-C29B010911C4}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Massachusetts",
                 "Ecosystem Services",
@@ -251486,46 +251505,46 @@
                 "Water",
                 "Human Well-being"
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
+            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
+            "temporal": "2014-06-18/2014-06-18",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Bedford, MA - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{980643A8-2DB1-4A8B-B995-C29B010911C4}",
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
-            "spatial": "-71.05506, 41.57308, -70.78054, 41.85484",
-            "temporal": "2014-06-18/2014-06-18",
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
+            "description": "This EnviroAtlas dataset is a summary of total population near major roads without any tree buffer within 12-digit Hydrologic Units (HUC_12), based on the National Land Cover Database 2011 (NLCD 2011) percent tree canopy cover (TCC 2011) dataset. The metric is a measure of potential exposure to particulate matter from exhaust from traffic. Studies have shown that tree buffers can help improve air quality by filtering particulate matter for those living or working near roads. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewBedfordMA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sum of population near roads without tree buffer for the conterminous United States",
-            "description": "This EnviroAtlas dataset is a summary of total population near major roads without any tree buffer within 12-digit Hydrologic Units (HUC_12), based on the National Land Cover Database 2011 (NLCD 2011) percent tree canopy cover (TCC 2011) dataset. The metric is a measure of potential exposure to particulate matter from exhaust from traffic. Studies have shown that tree buffers can help improve air quality by filtering particulate matter for those living or working near roads. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A5DD4702-89C7-4167-93EF-62E114461D33}",
+            "issued": "2017-05-05",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -251590,46 +251609,46 @@
                 "Transportation",
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
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sum of population near roads without tree buffer for the conterminous United States"
         },
-            "identifier": "{A5DD4702-89C7-4167-93EF-62E114461D33}",
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
-            "issued": "2017-05-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 444 block groups in New Haven, Connecticut. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Middlesex and New Haven Counties, CT. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 444 block groups in New Haven, Connecticut. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Middlesex and New Haven Counties, CT. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{079168e9-beb6-4017-b783-5e833c5c8025}",
+            "issued": "2016-12-06",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -251649,46 +251668,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-12-06",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - BenMAP Results by Block Group"
         },
-            "identifier": "{079168e9-beb6-4017-b783-5e833c5c8025}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-12-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the New Haven, CT EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the New Haven, CT EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d12736b2-4c54-4744-92ad-75c7c851038a}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -251700,46 +251719,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Block Groups"
         },
-            "identifier": "{d12736b2-4c54-4744-92ad-75c7c851038a}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b056ed6c-ae88-476c-9d8d-75ed1d7d6f7a}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Human",
@@ -251756,46 +251775,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
-            },
-            "identifier": "{b056ed6c-ae88-476c-9d8d-75ed1d7d6f7a}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency, and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
             "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
             "theme": "boundaries",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
-        },
+            "title": "EnviroAtlas - New Haven, CT - Demographics by Block Group"
+        },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - EnviroAtlas Community Boundary",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
             "description": "This EnviroAtlas dataset shows the boundary of the New Haven, CT EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{799c19d2-9268-48c3-82e2-3d515ca97fea}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -251808,46 +251827,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - EnviroAtlas Community Boundary"
         },
-            "identifier": "{799c19d2-9268-48c3-82e2-3d515ca97fea}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c67a0a5e-8f67-4685-b6c7-851bf21d90f1}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -251862,46 +251881,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency, and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{c67a0a5e-8f67-4685-b6c7-851bf21d90f1}",
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
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency, and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community-level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The South Central Connecticut Regional Water Supply (RWA) estimates domestic water use at 50 GPD and supplies water to the western half of the study area. The U.S. Geological Survey (USGS) estimates publicly and self-supplied domestic water use at 75 GPD for the eastern half of the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community-level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The South Central Connecticut Regional Water Supply (RWA) estimates domestic water use at 50 GPD and supplies water to the western half of the study area. The U.S. Geological Survey (USGS) estimates publicly and self-supplied domestic water use at 75 GPD for the eastern half of the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5f9ef1bf-0ee6-458c-83a1-6f6ad92f969d}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -251921,46 +251940,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{5f9ef1bf-0ee6-458c-83a1-6f6ad92f969d}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c270de37-4f87-4c36-90db-29eab8e7daf4}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -251976,46 +251995,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{c270de37-4f87-4c36-90db-29eab8e7daf4}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{58fc2c21-941a-40f2-b2fc-348447ff850f}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252039,46 +252058,46 @@
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
+            "spatial": "-73.109535, 41.207187, -72.304353, 41.603395",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{58fc2c21-941a-40f2-b2fc-348447ff850f}",
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
-            "spatial": "-73.109535, 41.207187, -72.304353, 41.603395",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4b724510-6500-403d-bb6e-82f7855550ed}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252093,46 +252112,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-21",
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Green Space Proximity Gradient"
         },
-            "identifier": "{4b724510-6500-403d-bb6e-82f7855550ed}",
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
-            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
-            "temporal": "2014-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-21",
-            "language": "en-us",
-            "theme": "environment",
```

