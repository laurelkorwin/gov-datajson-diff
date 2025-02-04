# Change History for epa.json (Part 35)

### Changes from 31606f9 to dd2190f (Part 25/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2c779097-7265-4dc4-b126-b516cbc6113d}",
+            "issued": "2017-03-23",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252148,46 +252167,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-23",
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
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Historic Places by Census Block Group"
         },
-            "identifier": "{2c779097-7265-4dc4-b126-b516cbc6113d}",
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
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{da56ba2a-5ed0-4c61-a30b-03c052efc57e}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252201,46 +252220,46 @@
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
+            "title": "EnviroAtlas - New Haven, CT - Impervious Proximity Gradient"
         },
-            "identifier": "{da56ba2a-5ed0-4c61-a30b-03c052efc57e}",
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
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f39d7d21-064d-4498-9926-743d543bc8f0}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252255,46 +252274,46 @@
                 "Transportation",
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{f39d7d21-064d-4498-9926-743d543bc8f0}",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 444 block groups in New Haven, Connecticut. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New Haven, CT - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 444 block groups in New Haven, Connecticut. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dda504d7-4c92-4456-bd47-9314759d415f}",
+            "issued": "2016-12-06",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252313,46 +252332,46 @@
                 "Climate",
                 "Water"
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
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Ecosystem Services by Block Group"
         },
-            "identifier": "{dda504d7-4c92-4456-bd47-9314759d415f}",
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
-            "issued": "2016-12-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and wetlands. In this community, forest is defined as Trees & Forest and Woody Wetlands and green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and wetlands. In this community, forest is defined as Trees & Forest and Woody Wetlands and green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{209585f0-c5e8-4363-a7a6-b21487675142}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252368,46 +252387,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Land Cover by Block Group"
         },
-            "identifier": "{209585f0-c5e8-4363-a7a6-b21487675142}",
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
+            "description": "The EnviroAtlas New Haven, CT EnviroAtlas Meter-scale Urban Land Cover (MULC) Data were generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial scale acquired on September 25, 2014. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, and grass-herbaceous non-woody vegetation,as well as woody wetlands and emergent herbaceous wetlands. An accuracy assessment of 500 completely random and 50 stratified random photo-interpreted reference points yielded an overall MAX accuracy of 89 percent and an overall RIGHT accuracy of 92 percent. The area mapped is the US Census Bureau's 2010 Urban Statistical Area for New Haven, CT plus a 1 km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Meter-Scale Urban Land Cover Data (2014)",
-            "description": "The EnviroAtlas New Haven, CT EnviroAtlas Meter-scale Urban Land Cover (MULC) Data were generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial scale acquired on September 25, 2014. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, and grass-herbaceous non-woody vegetation,as well as woody wetlands and emergent herbaceous wetlands. An accuracy assessment of 500 completely random and 50 stratified random photo-interpreted reference points yielded an overall MAX accuracy of 89 percent and an overall RIGHT accuracy of 92 percent. The area mapped is the US Census Bureau's 2010 Urban Statistical Area for New Haven, CT plus a 1 km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{66bb3d88-be8d-428e-b137-0a427d0ad41c}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252430,46 +252449,46 @@
                 "Agriculture",
                 "Communities"
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
+            "spatial": "-97.683809, 25.824946, -97.131017, 26.190659",
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Meter-Scale Urban Land Cover Data (2014)"
         },
-            "identifier": "{66bb3d88-be8d-428e-b137-0a427d0ad41c}",
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
-            "spatial": "-97.683809, 25.824946, -97.131017, 26.190659",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4ee24ede-422c-4626-b512-baf728e7318e}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252487,46 +252506,46 @@
                 "Trees",
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
+            "title": "EnviroAtlas - New Haven, CT - Near Road Tree Buffer"
         },
-            "identifier": "{4ee24ede-422c-4626-b512-baf728e7318e}",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6da2bcbb-9802-4312-842c-592ca6188ce6}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252545,46 +252564,46 @@
                 "Trees",
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Near Road Block Group Summary"
         },
-            "identifier": "{6da2bcbb-9802-4312-842c-592ca6188ce6}",
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
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0fc681be-3e94-4f30-aafd-8f658fa4f709}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252599,46 +252618,46 @@
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Park Access by Block Group"
         },
-            "identifier": "{0fc681be-3e94-4f30-aafd-8f658fa4f709}",
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
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9d0bac80-69fc-4649-9131-95f276da0ca0}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252652,46 +252671,46 @@
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
+            "spatial": "-73.086852, 41.231658, -72.331482, 41.578894",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Proximity to Parks"
         },
-            "identifier": "{9d0bac80-69fc-4649-9131-95f276da0ca0}",
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
-            "issued": "2020-01-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a660a9d0-7133-49e8-a5a5-b1862e737ad6}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252709,46 +252728,46 @@
                 "Trees",
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
+            "title": "EnviroAtlas - New Haven, CT - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{a660a9d0-7133-49e8-a5a5-b1862e737ad6}",
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
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, forest is defined as Trees & Forest and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, forest is defined as Trees & Forest and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f8f4bca9-cfa4-4efd-899c-079690b8c708}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252766,46 +252785,46 @@
                 "Trees",
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
+            "title": "EnviroAtlas - New Haven, CT - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{f8f4bca9-cfa4-4efd-899c-079690b8c708}",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7f868866-c5ce-493b-8a5b-a76633ba05fd}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252825,46 +252844,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{7f868866-c5ce-493b-8a5b-a76633ba05fd}",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{555a1fe3-eea3-408e-9c29-99aa9ea99cc8}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252884,46 +252903,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{555a1fe3-eea3-408e-9c29-99aa9ea99cc8}",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{572a5ab3-f384-4483-a5eb-7e5fc8d3947f}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -252943,46 +252962,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{572a5ab3-f384-4483-a5eb-7e5fc8d3947f}",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4fe5d6d6-0b62-4b75-8b82-e6029a65e557}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -253002,46 +253021,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{4fe5d6d6-0b62-4b75-8b82-e6029a65e557}",
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
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees & Forest and Woody Wetlands and vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees & Forest and Woody Wetlands and vegetated cover is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c9ba8d53-fd2b-4271-9a05-bf91113ed58a}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -253062,46 +253081,46 @@
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{c9ba8d53-fd2b-4271-9a05-bf91113ed58a}",
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
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, forest is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, forest is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{803b25fb-a0ad-4cdf-b485-76898a772e99}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -253119,46 +253138,46 @@
                 "Trees",
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{803b25fb-a0ad-4cdf-b485-76898a772e99}",
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
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - New Haven, CT - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1a3a6b78-0b4a-4a8d-a7fd-d1c8e8867037}",
+            "issued": "2017-03-21",
             "keyword": [
                 "Connecticut",
                 "Ecosystem Services",
@@ -253174,46 +253193,46 @@
                 "Water",
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New Haven, CT - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{1a3a6b78-0b4a-4a8d-a7fd-d1c8e8867037}",
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
+            "description": "This EnviroAtlas web service contains layers depicting NHD Version 2.1 Plus flowlines and waterbodies for the conterminous United States. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewHavenCT",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - NHDPlus V2 Flowlines and Waterbodies Web Service - Conterminous United States",
-            "description": "This EnviroAtlas web service contains layers depicting NHD Version 2.1 Plus flowlines and waterbodies for the conterminous United States. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{19adbf65-443a-4289-bcc1-e43d871d1765}",
+            "issued": "2017-02-22",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -253286,46 +253305,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-02-22",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of Forest Trends' Ecosystem Marketplace would be app",
+            "spatial": "-124.859953, 24.512240, -66.885441, 49.384487",
+            "temporal": "2015-02-02/2015-02-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - NHDPlus V2 Flowlines and Waterbodies Web Service - Conterminous United States"
         },
-            "identifier": "{19adbf65-443a-4289-bcc1-e43d871d1765}",
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
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of Forest Trends' Ecosystem Marketplace would be app",
-            "spatial": "-124.859953, 24.512240, -66.885441, 49.384487",
-            "temporal": "2015-02-02/2015-02-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-02-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service contains layers depicting hydrologic unit boundary layers and labels for the Subregion level (4-digit HUCs), Subbasin level (8-digit HUCs), and Subwatershed level (12-digit HUCs) for the conterminous United States. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - NHDPlus V2 Hydrologic Unit Boundaries Web Service - Conterminous United States",
-            "description": "This EnviroAtlas web service contains layers depicting hydrologic unit boundary layers and labels for the Subregion level (4-digit HUCs), Subbasin level (8-digit HUCs), and Subwatershed level (12-digit HUCs) for the conterminous United States. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e69d8d1f-6f58-498b-a18a-eb544c571537}",
+            "issued": "2017-02-22",
             "keyword": [
                 "Connecticut",
                 "Kansas",
@@ -253405,46 +253424,46 @@
                 "Subregion",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-02-22",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of Forest Trends' Ecosystem Marketplace would be app",
+            "spatial": "-124.859953, 24.512240, -66.885441, 49.384487",
+            "temporal": "2015-02-02/2015-02-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - NHDPlus V2 Hydrologic Unit Boundaries Web Service - Conterminous United States"
         },
-            "identifier": "{e69d8d1f-6f58-498b-a18a-eb544c571537}",
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
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of Forest Trends' Ecosystem Marketplace would be app",
-            "spatial": "-124.859953, 24.512240, -66.885441, 49.384487",
-            "temporal": "2015-02-02/2015-02-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-02-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a digital hydrologic unit boundary layer to the Subwatershed (12-digit) 6th level for the conterminous United States, based on the January 6, 2015 NHDPlus V2 WBD (Watershed Boundary Dataset) Snapshot (NHDPlusV21_NationalData_WBDSnapshot_FileGDB_05). The feature class has been edited for use in for EPA ORD's EnviroAtlas. Features in Canada and Mexico have been removed, the boundaries of three 12-digit HUCs have been edited to eliminate gaps and overlaps, the dataset has been dissolved on HUC_12 to create multipart polygons, and information on the percent land area has been added. Hawaii, Puerto Rico, and the U.S. Virgin Islands have been removed, and can be downloaded separately. Other than these modifications, the dataset is the same as the WBD Snapshot included in NHDPlus V2. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - NHDPlus V2 WBD Snapshot, EnviroAtlas version - Conterminous United States",
-            "description": "This EnviroAtlas dataset is a digital hydrologic unit boundary layer to the Subwatershed (12-digit) 6th level for the conterminous United States, based on the January 6, 2015 NHDPlus V2 WBD (Watershed Boundary Dataset) Snapshot (NHDPlusV21_NationalData_WBDSnapshot_FileGDB_05). The feature class has been edited for use in for EPA ORD's EnviroAtlas. Features in Canada and Mexico have been removed, the boundaries of three 12-digit HUCs have been edited to eliminate gaps and overlaps, the dataset has been dissolved on HUC_12 to create multipart polygons, and information on the percent land area has been added. Hawaii, Puerto Rico, and the U.S. Virgin Islands have been removed, and can be downloaded separately. Other than these modifications, the dataset is the same as the WBD Snapshot included in NHDPlus V2. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BA1041E9-02B6-40ED-8DB0-B1EEF68B6CA7}",
+            "issued": "2015-02-02",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -253505,46 +253524,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-02-02",
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
+            "temporal": "2015-02-02/2015-02-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - NHDPlus V2 WBD Snapshot, EnviroAtlas version - Conterminous United States"
         },
-            "identifier": "{BA1041E9-02B6-40ED-8DB0-B1EEF68B6CA7}",
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
-            "temporal": "2015-02-02/2015-02-02",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-02-02",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of the National Dams Inventory data from 2009 survey. The file contains counts of inventoried dams by 12-digit hydrologic units codes (March 2011) and total maximum storage capacity in millions of gallons. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - National Inventory of Dams for the Conterminous United States",
-            "description": "This EnviroAtlas dataset is a summary of the National Dams Inventory data from 2009 survey. The file contains counts of inventoried dams by 12-digit hydrologic units codes (March 2011) and total maximum storage capacity in millions of gallons. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{86B29750-880D-4A58-91F2-2054FEA2E553}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -253606,46 +253625,46 @@
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
+            "temporal": "2012-07-31/2012-07-31",
+            "theme": "environment",
+            "title": "EnviroAtlas - National Inventory of Dams for the Conterminous United States"
         },
-            "identifier": "{86B29750-880D-4A58-91F2-2054FEA2E553}",
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
-            "temporal": "2012-07-31/2012-07-31",
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
+            "description": "This EnviroAtlas dataset describes the non-native freshwater aquatic diversity by 12-digit HUC (subwatershed) for the conterminous United States. It includes animals and plants. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Non-Native Freshwater Aquatic Biodiversity by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset describes the non-native freshwater aquatic diversity by 12-digit HUC (subwatershed) for the conterminous United States. It includes animals and plants. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ee50a529-93f1-417e-bbb8-7e4ff22cc0dd}",
+            "issued": "2018-05-25",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -253709,46 +253728,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-05-25",
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
+            "temporal": "2017-01-01/2017-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Non-Native Freshwater Aquatic Biodiversity by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{ee50a529-93f1-417e-bbb8-7e4ff22cc0dd}",
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
-            "temporal": "2017-01-01/2017-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-05-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas Near Road Tree Buffer Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dcd2efb8-818b-4318-a80d-d8c0616f08d1}",
+            "issued": "2016-12-12",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -253821,46 +253840,46 @@
                 "Paterson, NJ",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-12-12",
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
+            "title": "EnviroAtlas Near Road Tree Buffer Web Service"
         },
-            "identifier": "{dcd2efb8-818b-4318-a80d-d8c0616f08d1}",
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
-            "issued": "2016-12-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 6,378 block groups in New York City, New York. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York City, NY - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 6,378 block groups in New York City, New York. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{179EADB0-3D2F-4EE2-9781-1D4E46868B9E}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -253880,46 +253899,46 @@
                 "Human Well-being",
                 "New York, NY"
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York City, NY - BenMAP Results by Block Group"
         },
-            "identifier": "{179EADB0-3D2F-4EE2-9781-1D4E46868B9E}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
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
+            "description": "This EnviroAtlas dataset is the base layer for the New York, NY EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the New York, NY EnviroAtlas community. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{942A7ADA-A95E-415D-A4F7-D3C9AA7C2413}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -253932,46 +253951,46 @@
                 "Environmental Atlas",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Block Groups"
         },
-            "identifier": "{942A7ADA-A95E-415D-A4F7-D3C9AA7C2413}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8BCC6170-4A08-406C-8D48-CA3590799D95}",
+            "issued": "2015-11-03",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -253988,46 +254007,46 @@
                 "Boundaries",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-11-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - New York, NY - Demographics by Block Group"
         },
-            "identifier": "{8BCC6170-4A08-406C-8D48-CA3590799D95}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-03",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the New York, NY EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the New York, NY EnviroAtlas Community. It represents the outside edge of all the block groups included in the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{6511C082-5F8D-4210-B5DE-FDF45C0A09EC}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254040,46 +254059,46 @@
                 "Boundaries",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - EnviroAtlas Community Boundary"
         },
-            "identifier": "{6511C082-5F8D-4210-B5DE-FDF45C0A09EC}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is defined as Trees & Forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "enviroatlas-new-york-ny-tree-cover-configuration-and-connectivity",
+            "issued": "2017-05-30",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -254094,46 +254113,46 @@
                 "Environmental Atlas",
                 "New York, NY"
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-12-04/2015-12-04",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "enviroatlas-new-york-ny-tree-cover-configuration-and-connectivity",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-12-04/2015-12-04",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The New York City Department of Environmental Protection (NYCDEP) manages the city's water supply. Water use within the EnviroAtlas-defined study area was estimated at 125.8 GPD for 2009. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The New York City Department of Environmental Protection (NYCDEP) manages the city's water supply. Water use within the EnviroAtlas-defined study area was estimated at 125.8 GPD for 2009. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FE581208-427C-4B6C-A6CD-60AD8BCEF62F}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -254153,46 +254172,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{FE581208-427C-4B6C-A6CD-60AD8BCEF62F}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4DF48560-B867-4430-99B4-D6075C553248}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -254208,46 +254227,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{4DF48560-B867-4430-99B4-D6075C553248}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7aab6b8b-c807-488a-8cb5-5f21d4893357}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -254271,46 +254290,46 @@
                 "Communities",
                 "New York, NY"
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{7aab6b8b-c807-488a-8cb5-5f21d4893357}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E1342BE9-4994-4898-9B88-0E6838D3F20E}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254325,46 +254344,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Green Space Proximity Gradient"
         },
-            "identifier": "{E1342BE9-4994-4898-9B88-0E6838D3F20E}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{12980773-8872-4FF8-85BF-68983EC915AF}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254380,46 +254399,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Historic Places by Census Block Group"
         },
-            "identifier": "{12980773-8872-4FF8-85BF-68983EC915AF}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{398782A7-F722-4B5F-AE06-D2C413562B10}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254433,46 +254452,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2016-02-03/2016-02-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Impervious Proximity Gradient"
         },
-            "identifier": "{398782A7-F722-4B5F-AE06-D2C413562B10}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2016-02-03/2016-02-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D70DE411-6B72-4806-9B40-04921B3EA230}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -254487,46 +254506,46 @@
                 "Human Well-being",
                 "New York, NY"
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
+            "spatial": "-62.619838, 19.030151, -62.209104, 19.468980",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{D70DE411-6B72-4806-9B40-04921B3EA230}",
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
-            "spatial": "-62.619838, 19.030151, -62.209104, 19.468980",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 6,378 block groups in New York City, New York. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York City, NY - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 6,378 block groups in New York City, New York. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{66D59A4F-9117-42AB-8723-2B4C207E64AE}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -254545,46 +254564,46 @@
                 "Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2008-01-01/2008-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York City, NY - Ecosystem Services by Block Group"
         },
-            "identifier": "{66D59A4F-9117-42AB-8723-2B4C207E64AE}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2008-01-01/2008-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. In this community, forest is defined as Trees & Forest and green space is defined as Trees & Forest and Grass & Herbaceous. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. In this community, forest is defined as Trees & Forest and green space is defined as Trees & Forest and Grass & Herbaceous. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5BAE6663-0916-448A-BABB-7A99485C8BEB}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -254600,46 +254619,46 @@
                 "Environmental Atlas",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Land Cover by Block Group"
         },
-            "identifier": "{5BAE6663-0916-448A-BABB-7A99485C8BEB}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The New York, NY EnviroAtlas Meter-scale Urban Land Cover (MULC) Data were generated by the University of Vermont Spatial Analysis Laboratory (SAL) under the direction of Jarlath O'Neil-Dunne as part of the United States Forest Service Urban Tree Canopy (UTC) assessment program. Seven classes were mapped using LiDAR and high resolution orthophotography: Tree Canopy, Grass/Shrub, Bare Soil, Water, Buildings, Roads/Railroads, and Other Paved Surfaces. These data were subsequently merged to fit with the EPA classification. The SAL project covered the five boroughs within the NYC city limits. However the EPA study area encompassed that area plus a 1 kilometer buffer. Additional land cover for the buffer area was generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution from July, 2011 and LiDAR from 2010. Six land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, grass-herbaceous non-woody vegetation, and agriculture. An accuracy assessment of 600 completely random and 55 stratified random photo interpreted reference points yielded an overall User's fuzzy accuracy of 87 percent. The area mapped is the US Census Bureau's 2010 Urban Statistical Area for New York City plus a 1 km buffer. This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy assessment program, and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- New York, NY -- Meter-Scale Urban Land Cover (MULC) Data (2008)",
-            "description": "The New York, NY EnviroAtlas Meter-scale Urban Land Cover (MULC) Data were generated by the University of Vermont Spatial Analysis Laboratory (SAL) under the direction of Jarlath O'Neil-Dunne as part of the United States Forest Service Urban Tree Canopy (UTC) assessment program. Seven classes were mapped using LiDAR and high resolution orthophotography: Tree Canopy, Grass/Shrub, Bare Soil, Water, Buildings, Roads/Railroads, and Other Paved Surfaces. These data were subsequently merged to fit with the EPA classification. The SAL project covered the five boroughs within the NYC city limits. However the EPA study area encompassed that area plus a 1 kilometer buffer. Additional land cover for the buffer area was generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution from July, 2011 and LiDAR from 2010. Six land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, grass-herbaceous non-woody vegetation, and agriculture. An accuracy assessment of 600 completely random and 55 stratified random photo interpreted reference points yielded an overall User's fuzzy accuracy of 87 percent. The area mapped is the US Census Bureau's 2010 Urban Statistical Area for New York City plus a 1 km buffer. This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy assessment program, and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FDB995B6-5B64-422B-A59F-0C272A83216B}",
+            "issued": "2016-02-19",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -254662,46 +254681,46 @@
                 "Communities",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-19",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2008-01-01/2008-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- New York, NY -- Meter-Scale Urban Land Cover (MULC) Data (2008)"
         },
-            "identifier": "{FDB995B6-5B64-422B-A59F-0C272A83216B}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2008-01-01/2008-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{01C8CA2C-D7E9-4160-B498-6F30D1F015EE}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -254719,46 +254738,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Near Road Tree Buffer"
         },
-            "identifier": "{01C8CA2C-D7E9-4160-B498-6F30D1F015EE}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F4C398A8-D1DC-40ED-B53A-1FA79EEEFF23}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -254777,46 +254796,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Near Road Block Group Summary"
         },
-            "identifier": "{F4C398A8-D1DC-40ED-B53A-1FA79EEEFF23}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8C097B4B-6883-45D7-BF40-56440C4B92DC}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254831,46 +254850,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Park Access by Block Group"
         },
-            "identifier": "{8C097B4B-6883-45D7-BF40-56440C4B92DC}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/EnviroAtlas/DataFactSheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/EnviroAtlas/DataFactSheets).",
+            ],
+            "identifier": "{4860A2BF-B3EB-4199-A3F2-6DDB7E97F880}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -254884,46 +254903,46 @@
                 "Human Well-being",
                 "New York, NY"
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Proximity to Parks"
         },
-            "identifier": "{4860A2BF-B3EB-4199-A3F2-6DDB7E97F880}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{E36A4F4F-C50F-4F7F-B35A-0D8CB51CF5CB}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -254941,46 +254960,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{E36A4F4F-C50F-4F7F-B35A-0D8CB51CF5CB}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D8406925-C2A8-4E29-991F-0BA8FC2DB685}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -254995,46 +255014,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{D8406925-C2A8-4E29-991F-0BA8FC2DB685}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{10FA39C0-792E-4585-AF1E-B01D9A8F5BBA}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255054,46 +255073,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{10FA39C0-792E-4585-AF1E-B01D9A8F5BBA}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{EFA73792-E26A-4047-9457-B9A7E8CEE166}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255113,46 +255132,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{EFA73792-E26A-4047-9457-B9A7E8CEE166}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{AF1F2F8B-B6FE-40A8-9B11-2684F6AB9D98}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255172,46 +255191,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{AF1F2F8B-B6FE-40A8-9B11-2684F6AB9D98}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{E168D559-E416-46D0-857F-09CE07FE3740}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255231,46 +255250,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{E168D559-E416-46D0-857F-09CE07FE3740}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees & Forest and vegetated cover is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, forest is defined as Trees & Forest and vegetated cover is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{781EA0A4-51C4-492F-A04C-679C634371FC}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255291,46 +255310,46 @@
                 "Drinking Water",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{781EA0A4-51C4-492F-A04C-679C634371FC}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CEA4B57B-C073-4108-8BAC-707BE6B8898F}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -255348,46 +255367,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{CEA4B57B-C073-4108-8BAC-707BE6B8898F}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - New York, NY - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{516FC3B1-3569-49B7-A4CA-3A0B32D15211}",
+            "issued": "2016-02-03",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -255403,46 +255422,46 @@
                 "Human Well-being",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-02-03",
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
+            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
+            "temporal": "2015-11-03/2015-11-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - New York, NY - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{516FC3B1-3569-49B7-A4CA-3A0B32D15211}",
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
-            "spatial": "-74.25602, 40.49599, -73.69687, 40.91307",
-            "temporal": "2015-11-03/2015-11-03",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-02-03",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains annual (2002) simulated estimations of edge-of-field agricultural nitrogen (N) and phosphorus (P) lost in surface runoff, subsurface flow (tile and non-tile) and percolate, N and P attached to eroding soil (sediment loss) and associated surface, subsurface and vertical water flow and surface soil erosion. The dataset was generated using Weather Research Forecast (WRF) modeled weather, Community Multi-Scale Air Quality (CMAQ) model deposition and the Environmental Policy Integrated Climate (EPIC) model as implemented under the Fertilizer Emission Scenario Tool for CMAQ (FEST-C), all run for 12-km rectangular grids across the continental US. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/NewYorkNY",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2002 Edge-of-Field Simulated Nitrogen, Phosphorus and Water Quantity Loss by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains annual (2002) simulated estimations of edge-of-field agricultural nitrogen (N) and phosphorus (P) lost in surface runoff, subsurface flow (tile and non-tile) and percolate, N and P attached to eroding soil (sediment loss) and associated surface, subsurface and vertical water flow and surface soil erosion. The dataset was generated using Weather Research Forecast (WRF) modeled weather, Community Multi-Scale Air Quality (CMAQ) model deposition and the Environmental Policy Integrated Climate (EPIC) model as implemented under the Fertilizer Emission Scenario Tool for CMAQ (FEST-C), all run for 12-km rectangular grids across the continental US. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f8b3f367-e43b-42e5-a4d0-6c8267c782f9}",
+            "issued": "2016-08-19",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -255516,46 +255535,48 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-19",
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
+            "temporal": "2002-01-01/2002-12-31",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2002 Edge-of-Field Simulated Nitrogen, Phosphorus and Water Quantity Loss by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{f8b3f367-e43b-42e5-a4d0-6c8267c782f9}",
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
-            "temporal": "2002-01-01/2002-12-31",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-08-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This dataset includes the number of days in 2017 that the maximum 8-hour average ozone concentration predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 70 ppb. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Ozone Concentration - Days with 8-hour average over 70 ppb in 2017 for the Conterminous United States",
-            "description": "This dataset includes the number of days in 2017 that the maximum 8-hour average ozone concentration predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 70 ppb. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "E1E819B0-86E1-4D99-B27B-F974805658C7",
+            "issued": "2021-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -255618,31 +255639,34 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-12-16",
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
+            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
+            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
+            "title": "EnviroAtlas - Ozone Concentration - Days with 8-hour average over 70 ppb in 2017 for the Conterminous United States"
         },
-            "identifier": "E1E819B0-86E1-4D99-B27B-F974805658C7",
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
-            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
-            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-12-16",
+            "description": "This dataset includes the number of days in 2017 that the maximum 8-hour average ozone concentration predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 80 ppb. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -255652,12 +255676,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Ozone Concentration - Days with 8-hour average over 80 ppb in 2017 for the Conterminous United States",
-            "description": "This dataset includes the number of days in 2017 that the maximum 8-hour average ozone concentration predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 80 ppb. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "0AC1466B-4DCF-4179-93F7-A9DD724ACF10",
+            "issued": "2021-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -255720,46 +255741,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-12-16",
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
+            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
+            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
+            "title": "EnviroAtlas - Ozone Concentration - Days with 8-hour average over 80 ppb in 2017 for the Conterminous United States"
         },
-            "identifier": "0AC1466B-4DCF-4179-93F7-A9DD724ACF10",
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
-            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
-            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-12-16",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. For specific information about methods used to develop data for each community, consult their individual metadata records: Austin, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6D2657C3-52F8-4E41-BC35-00EE9DAADE4E%7D); Birmingham, AL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Be2f2445f-f7df-4b83-9004-eb4e1c45bed9%7D); Baltimore, MD (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B920a6fb4-812e-421d-a4fa-f6a328c1f3d3%7D); Brownsville, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bc31dcddc-6750-4504-9121-668f2c6d53d3%7D); Cleveland, OH (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0ced9d35-9f11-46ca-abf0-1e10ebae1331%7D); Des Moines, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B7BDA7EB9-C5F8-4C15-90A4-A3CB285671D9%7D); Durham, NC (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B38956084-2AB2-422C-B56D-068C8CA6AAFE%7D); Fresno, CA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5D957C70-5A37-48A6-B7D4-1E304710417F%7D); Green Bay, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8675EC55-2CCE-4B83-972A-A23CD6618B09%7D); Memphis, TN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBBF52A70-DCCF-4DB6-ACDE-82A321A03F8C%7D); Minneapolis/St. Paul, MN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6a46d7c8-a344-4d19-a111-0c96a2fda15f%7D); Milwaukee, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE0EC8E26-0688-4EC5-8611-BF300054820E%7D); New Bedford, MA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B15DE4903-7C9D-4F61-9761-53D9904447C1%7D); New Haven, CT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9d0bac80-69fc-4649-9131-95f276da0ca0%7D); New York, NY (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4860A2BF-B3EB-4199-A3F2-6DDB7E97F880%7D); Phoenix, AZ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B42936F73-D645-4C86-820A-72A19FBB213A%7D); Pittsburgh, PA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA62B08BE-36D7-43EF-8C89-4EDC2EB5EF54%7D); Portland, ME (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF3BA2EEB-784B-45C2-B8BD-DC2C2CEE2479%7D); Paterson, NJ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B90E93159-7A1E-4BAB-95FC-8B04A15070E3%7D); Portland, OR (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4671F2A5-B691-47F9-9A1D-C11AA0F952D0%7D); Salt Lake City, UT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4671F2A5-B691-47F9-9A1D-C11AA0F952D0%7D);Tampa, FL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC17799CA-F743-4CE6-BC71-3D4C82E5F2BC%7D); and Woodbine, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B667D6539-13C6-45A2-BD5B-80108BAA5213%7D). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas Proximity to Parks Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. For specific information about methods used to develop data for each community, consult their individual metadata records: Austin, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6D2657C3-52F8-4E41-BC35-00EE9DAADE4E%7D); Birmingham, AL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Be2f2445f-f7df-4b83-9004-eb4e1c45bed9%7D); Baltimore, MD (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B920a6fb4-812e-421d-a4fa-f6a328c1f3d3%7D); Brownsville, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bc31dcddc-6750-4504-9121-668f2c6d53d3%7D); Cleveland, OH (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0ced9d35-9f11-46ca-abf0-1e10ebae1331%7D); Des Moines, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B7BDA7EB9-C5F8-4C15-90A4-A3CB285671D9%7D); Durham, NC (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B38956084-2AB2-422C-B56D-068C8CA6AAFE%7D); Fresno, CA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5D957C70-5A37-48A6-B7D4-1E304710417F%7D); Green Bay, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8675EC55-2CCE-4B83-972A-A23CD6618B09%7D); Memphis, TN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBBF52A70-DCCF-4DB6-ACDE-82A321A03F8C%7D); Minneapolis/St. Paul, MN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6a46d7c8-a344-4d19-a111-0c96a2fda15f%7D); Milwaukee, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE0EC8E26-0688-4EC5-8611-BF300054820E%7D); New Bedford, MA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B15DE4903-7C9D-4F61-9761-53D9904447C1%7D); New Haven, CT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9d0bac80-69fc-4649-9131-95f276da0ca0%7D); New York, NY (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4860A2BF-B3EB-4199-A3F2-6DDB7E97F880%7D); Phoenix, AZ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B42936F73-D645-4C86-820A-72A19FBB213A%7D); Pittsburgh, PA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA62B08BE-36D7-43EF-8C89-4EDC2EB5EF54%7D); Portland, ME (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF3BA2EEB-784B-45C2-B8BD-DC2C2CEE2479%7D); Paterson, NJ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B90E93159-7A1E-4BAB-95FC-8B04A15070E3%7D); Portland, OR (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4671F2A5-B691-47F9-9A1D-C11AA0F952D0%7D); Salt Lake City, UT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4671F2A5-B691-47F9-9A1D-C11AA0F952D0%7D);Tampa, FL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC17799CA-F743-4CE6-BC71-3D4C82E5F2BC%7D); and Woodbine, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B667D6539-13C6-45A2-BD5B-80108BAA5213%7D). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8e728fbb-dc7b-46b1-aa49-7861032f8f03}",
+            "issued": "2016-12-12",
             "keyword": [
                 "Texas",
                 "Green Bay, WI",
@@ -255805,46 +255824,46 @@
                 "Paterson, NJ",
                 "New York, NY"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-12-12",
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
+            "title": "EnviroAtlas Proximity to Parks Web Service"
         },
-            "identifier": "{8e728fbb-dc7b-46b1-aa49-7861032f8f03}",
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
-            "issued": "2016-12-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 2,434 block groups in Phoenix, AZ. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 2,434 block groups in Phoenix, AZ. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AB868E6F-1D81-4FEA-AE8E-32FB7C2C18E3}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -255864,46 +255883,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - BenMAP Results by Block Group"
         },
-            "identifier": "{AB868E6F-1D81-4FEA-AE8E-32FB7C2C18E3}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Phoenix, AZ EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Phoenix, AZ EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C1E5F645-BE7B-4703-9404-2EED95E999D0}",
+            "issued": "2013-11-13",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -255916,46 +255935,46 @@
                 "Environmental Atlas",
                 "Arizona"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-13",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-06/2013-11-06",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Block Groups"
         },
-            "identifier": "{C1E5F645-BE7B-4703-9404-2EED95E999D0}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-06/2013-11-06",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AA13D671-AEEE-4B01-BBC5-5A7B6D64B1A9}",
+            "issued": "2013-11-13",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -255972,46 +255991,46 @@
                 "Arizona",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-13",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Phoenix, AZ - Demographics by Block Group"
         },
-            "identifier": "{AA13D671-AEEE-4B01-BBC5-5A7B6D64B1A9}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-13",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Phoenix, AZ Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Phoenix, AZ Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FBCC48BF-FB8E-4664-988A-6A0AD57F218D}",
+            "issued": "2013-10-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256024,46 +256043,46 @@
                 "Arizona",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-08/2013-11-08",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Atlas Area Boundary"
         },
-            "identifier": "{FBCC48BF-FB8E-4664-988A-6A0AD57F218D}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-08/2013-11-08",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CAD428A6-C9B6-4C86-AAF4-95A79B1FF3F9}",
+            "issued": "2017-05-30",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -256078,46 +256097,46 @@
                 "Environmental Atlas",
                 "Arizona"
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{CAD428A6-C9B6-4C86-AAF4-95A79B1FF3F9}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2015-03-24/2015-03-24",
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
+            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Within the EnviroAtlas Phoenix boundary, there are 53 service providers with 2000-2009 water use estimates ranging from 108 to 366 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Domestic Water Demand per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Within the EnviroAtlas Phoenix boundary, there are 53 service providers with 2000-2009 water use estimates ranging from 108 to 366 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{822B887E-004D-4E45-9085-C437D79E2B4F}",
+            "issued": "2016-08-11",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -256137,46 +256156,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-11",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Domestic Water Demand per Day by U.S. Census Block Group"
         },
-            "identifier": "{822B887E-004D-4E45-9085-C437D79E2B4F}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-08-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{38BD796B-A478-4622-9CE1-E7B54A8B710F}",
+            "issued": "2014-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -256192,46 +256211,46 @@
                 "Arizona",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-06-18",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2014-06-11/2014-06-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{38BD796B-A478-4622-9CE1-E7B54A8B710F}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2014-06-11/2014-06-11",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-06-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ade906bd-0bb7-436e-9d7a-6475c0279545}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -256255,46 +256274,46 @@
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
+            "spatial": "-112.454517, 33.20325, -111.476631, 33.812514",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{ade906bd-0bb7-436e-9d7a-6475c0279545}",
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
-            "spatial": "-112.454517, 33.20325, -111.476631, 33.812514",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, and Agriculture. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, and Agriculture. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FE7A4116-FE4B-4912-BE50-39D2F47C3FD4}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256309,46 +256328,46 @@
                 "Arizona",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2015-03-20/2015-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Greenspace Proximity Gradient"
         },
-            "identifier": "{FE7A4116-FE4B-4912-BE50-39D2F47C3FD4}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4DCE07DB-79C0-4307-A92D-86E86701DBF2}",
+            "issued": "2014-09-16",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256364,46 +256383,46 @@
                 "Arizona",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Historic Places by Census Block Group"
         },
-            "identifier": "{4DCE07DB-79C0-4307-A92D-86E86701DBF2}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{85A299D5-4D55-495E-9DEB-2D3793DC584E}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256417,48 +256436,48 @@
                 "Arizona",
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
-            },
-            "identifier": "{85A299D5-4D55-495E-9DEB-2D3793DC584E}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
             "temporal": "2015-03-26/2015-03-26",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-14",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "EnviroAtlas - Phoenix, AZ - Impervious Proximity Gradient"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
-            "keyword": [
-                "Ecosystem Services",
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
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{AFC1F0E1-EC52-41E4-8682-8885BED5A9B7}",
+            "issued": "2019-06-19",
+            "keyword": [
+                "Ecosystem Services",
                 "Health",
                 "Environment",
                 "Ecosystem",
@@ -256471,46 +256490,46 @@
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
+            "spatial": "-112.68293, 33.19513, -111.58459, 34.0523",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{AFC1F0E1-EC52-41E4-8682-8885BED5A9B7}",
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
-            "spatial": "-112.68293, 33.19513, -111.58459, 34.0523",
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
+            "description": "This dataset presents environmental benefits of the urban forest in 2,434 block groups in Phoenix, Arizona. Carbon attributes, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. Temperature reduction values for Phoenix will be added when they become available. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Ecosystem Services by Block Group",
-            "description": "This dataset presents environmental benefits of the urban forest in 2,434 block groups in Phoenix, Arizona. Carbon attributes, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. Temperature reduction values for Phoenix will be added when they become available. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8A0904B6-E3D6-4B77-8E42-5D2067C0B7F9}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -256529,46 +256548,46 @@
                 "Arizona",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Ecosystem Services by Block Group"
         },
-            "identifier": "{8A0904B6-E3D6-4B77-8E42-5D2067C0B7F9}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, agriculture, and green space. Forest is combination of trees and forest. Green space is a combination of trees and forest, grass and herbaceous, and agriculture. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, agriculture, and green space. Forest is combination of trees and forest. Green space is a combination of trees and forest, grass and herbaceous, and agriculture. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8A1C721F-3043-4E4B-BC66-C5DB496592A5}",
+            "issued": "2014-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -256585,46 +256604,46 @@
                 "Environmental Atlas",
                 "Arizona"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-06-18",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2014-05-13/2014-05-13",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Land Cover by Block Group"
         },
-            "identifier": "{8A1C721F-3043-4E4B-BC66-C5DB496592A5}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2014-05-13/2014-05-13",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-06-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The EnviroAtlas Phoenix, AZ Meter-Scale Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near-infrared) aerial photography taken from June through September, 2010 at 1 m spatial resolution. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, shrubs, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment using a completely random sampling of 598 land cover reference points yielded an overall user's accuracy (MAX) of 69.2% and an overall fuzzy user's accuracy of 75.4%. The area mapped includes the entirety of the Central Arizona-Phoenix Long-Term Ecological Research (CAP-LTER) area, which was classified by the Environmental Remote Sensing and Geoinformatics Lab (ERSG) at Arizona State University. The land cover dataset also includes an area of approximately 625 square kilometers which is located north of Phoenix. This section was classified by the EPA land cover classification team. This dataset was produced by the Environmental Remote Sensing and Geoinformatics Lab (ERSG) at Arizona State University and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Phoenix, AZ -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The EnviroAtlas Phoenix, AZ Meter-Scale Urban Land Cover (MULC) data and map were generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near-infrared) aerial photography taken from June through September, 2010 at 1 m spatial resolution. Seven land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, shrubs, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment using a completely random sampling of 598 land cover reference points yielded an overall user's accuracy (MAX) of 69.2% and an overall fuzzy user's accuracy of 75.4%. The area mapped includes the entirety of the Central Arizona-Phoenix Long-Term Ecological Research (CAP-LTER) area, which was classified by the Environmental Remote Sensing and Geoinformatics Lab (ERSG) at Arizona State University. The land cover dataset also includes an area of approximately 625 square kilometers which is located north of Phoenix. This section was classified by the EPA land cover classification team. This dataset was produced by the Environmental Remote Sensing and Geoinformatics Lab (ERSG) at Arizona State University and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D556044C-FCCC-4E8B-B157-5E7B8587AEE7}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -256647,46 +256666,46 @@
                 "Phoenix, AZ",
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
+            "spatial": "-112.828955, 33.148357, -111.503980, 34.057945",
+            "temporal": "2010-06-01/2010-09-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Phoenix, AZ -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{D556044C-FCCC-4E8B-B157-5E7B8587AEE7}",
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
-            "spatial": "-112.828955, 33.148357, -111.503980, 34.057945",
-            "temporal": "2010-06-01/2010-09-01",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D61133BB-ED25-4AE6-BA2E-176C5E51E37B}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -256704,46 +256723,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Near Road Tree Buffer"
         },
-            "identifier": "{D61133BB-ED25-4AE6-BA2E-176C5E51E37B}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5B1AF46D-4FB7-46EE-A99E-B859BC867B29}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -256763,46 +256782,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Near Road Block Group Summary"
         },
-            "identifier": "{5B1AF46D-4FB7-46EE-A99E-B859BC867B29}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7CC51B15-3A7C-4E14-9E6E-5CBC0508ADA9}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256817,46 +256836,46 @@
                 "Arizona",
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
+            "spatial": "-112.454517, 33.203250, -111.476631, 33.812514",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Park Access by Block Group"
         },
-            "identifier": "{7CC51B15-3A7C-4E14-9E6E-5CBC0508ADA9}",
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
-            "spatial": "-112.454517, 33.203250, -111.476631, 33.812514",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{42936F73-D645-4C86-820A-72A19FBB213A}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -256870,46 +256889,46 @@
                 "Arizona",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Proximity to Parks"
         },
-            "identifier": "{42936F73-D645-4C86-820A-72A19FBB213A}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{1540AAB6-3F17-4EFF-8CA6-0EF46D054C10}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -256927,46 +256946,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{1540AAB6-3F17-4EFF-8CA6-0EF46D054C10}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6A2FE776-5822-4137-BCB9-02D54F772C72}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -256984,46 +257003,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{6A2FE776-5822-4137-BCB9-02D54F772C72}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2A001B49-9A58-437D-952C-9F83E49DA557}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257043,46 +257062,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-15/2013-11-15",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{2A001B49-9A58-437D-952C-9F83E49DA557}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-15/2013-11-15",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D0023539-F076-4A89-8B2B-758758D276E6}",
+            "issued": "2013-11-14",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257102,46 +257121,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-14",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-14/2013-11-14",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{D0023539-F076-4A89-8B2B-758758D276E6}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-14/2013-11-14",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BA04F125-A93D-41CC-A904-C609F2557F24}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257161,46 +257180,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-15/2013-11-15",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{BA04F125-A93D-41CC-A904-C609F2557F24}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-15/2013-11-15",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{DB489B15-0C42-4835-9978-52704DB63170}",
+            "issued": "2013-11-13",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257220,46 +257239,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-11-13",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2013-11-13/2013-11-13",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{DB489B15-0C42-4835-9978-52704DB63170}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2013-11-13/2013-11-13",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-11-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B07B93C9-4628-40C4-8113-84EB01691768}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257280,46 +257299,46 @@
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2014-05-13/2014-05-13",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{B07B93C9-4628-40C4-8113-84EB01691768}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2014-05-13/2014-05-13",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{BE9CAF31-2F21-4707-80A5-B3B94060C6E6}",
+            "issued": "2014-06-17",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -257337,46 +257356,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-06-17",
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
+            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
+            "temporal": "2014-06-12/2014-06-12",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{BE9CAF31-2F21-4707-80A5-B3B94060C6E6}",
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
-            "spatial": "-112.68293, 33.19514, -111.58459, 34.05230",
-            "temporal": "2014-06-12/2014-06-12",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-06-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Phoenix, AZ - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6a042f2c-d992-4517-a6ac-c20835d37ed7}",
+            "issued": "2017-05-31",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -257392,46 +257411,46 @@
                 "Water",
                 "Human Well-being"
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
+            "spatial": "-112.69948, 33.20517, -111.5789, 34.04193",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Phoenix, AZ - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{6a042f2c-d992-4517-a6ac-c20835d37ed7}",
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
-            "spatial": "-112.69948, 33.20517, -111.5789, 34.04193",
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
+            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in the conterminous United States (CONUS) that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) U.S. Forest Service (USFS) Tree Canopy Cover dataset (CONUS). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhoenixAZ",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in the conterminous United States (CONUS) that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) U.S. Forest Service (USFS) Tree Canopy Cover dataset (CONUS). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{36d4a918-f83d-44c1-be38-280f8bf81689}",
+            "issued": "2020-01-23",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -257494,46 +257513,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-23",
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{36d4a918-f83d-44c1-be38-280f8bf81689}",
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
-            "issued": "2020-01-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in Hawaii that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) USFS Tree Canopy Cover (Hawaii) dataset. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for Hawaii",
-            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in Hawaii that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) USFS Tree Canopy Cover (Hawaii) dataset. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b8036927-5cd1-4ffd-b5ae-b44ba40718dd}",
+            "issued": "2020-06-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -257548,46 +257567,46 @@
                 "United States",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-06-01",
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
+            "spatial": "-160.250434, 18.893384, -154.732119, 22.228151",
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for Hawaii"
         },
-            "identifier": "{b8036927-5cd1-4ffd-b5ae-b44ba40718dd}",
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
-            "spatial": "-160.250434, 18.893384, -154.732119, 22.228151",
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-06-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in Puerto Rico and the US Virgin Islands that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) USFS Tree Canopy Cover (Puerto Rico) dataset. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for Puerto Rico and the U.S. Virgin Islands",
-            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in Puerto Rico and the US Virgin Islands that is classified as tree canopy using the National Land Cover Database 2016 (NLCD2016) USFS Tree Canopy Cover (Puerto Rico) dataset. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{26f38d8d-f17a-4758-a78f-084ab83d4c28}",
+            "issued": "2020-06-02",
             "keyword": [
                 "Puerto Rico",
                 "Ecosystem Services",
@@ -257603,46 +257622,46 @@
                 "United States",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-06-02",
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
+            "spatial": "-67.951455, 17.673736, -64.565191, 18.516091",
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2016 Percent Tree Canopy Cover by 12-digit HUC for Puerto Rico and the U.S. Virgin Islands"
         },
-            "identifier": "{26f38d8d-f17a-4758-a78f-084ab83d4c28}",
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
-            "spatial": "-67.951455, 17.673736, -64.565191, 18.516091",
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-06-02",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the percent of each 12-digit Hydrologic Unit (HUC) subwatershed in the contiguous U.S. with potentially restorable wetlands. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Potentially restorable wetlands for this map are lands currently in agriculture that naturally accumulate water and historically had poor drainage and hydric soils. By restoring some of these wetlands, it is hoped that the benefits of wetlands would also be restored. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percent of Each 12-Digit HUC in the Contiguous U.S. with Potentially Restorable Wetlands",
-            "description": "This EnviroAtlas dataset shows the percent of each 12-digit Hydrologic Unit (HUC) subwatershed in the contiguous U.S. with potentially restorable wetlands. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Potentially restorable wetlands for this map are lands currently in agriculture that naturally accumulate water and historically had poor drainage and hydric soils. By restoring some of these wetlands, it is hoped that the benefits of wetlands would also be restored. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{80AFCF1D-0C2B-4E4A-B07A-B2B57E6772D5}",
+            "issued": "2013-03-31",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -257704,46 +257723,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-03-31",
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
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Percent of Each 12-Digit HUC in the Contiguous U.S. with Potentially Restorable Wetlands"
         },
-            "identifier": "{80AFCF1D-0C2B-4E4A-B07A-B2B57E6772D5}",
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
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-03-31",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the percent land cover with potentially restorable wetlands on agricultural land for each 12-digit Hydrologic Unit (HUC) watershed in the contiguous U.S. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potentially restorable wetlands, as developed for this map, are lands currently in agriculture that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percent Land Cover with Potentially Restorable Wetlands on Agricultural Land by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset shows the percent land cover with potentially restorable wetlands on agricultural land for each 12-digit Hydrologic Unit (HUC) watershed in the contiguous U.S. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potentially restorable wetlands, as developed for this map, are lands currently in agriculture that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{11801f1f-42f2-4dca-afc4-cbc08d3fb21f}",
+            "issued": "2018-07-23",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -257805,46 +257824,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-23",
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
+            "title": "EnviroAtlas - Percent Land Cover with Potentially Restorable Wetlands on Agricultural Land by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{11801f1f-42f2-4dca-afc4-cbc08d3fb21f}",
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
-            "issued": "2018-07-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas Estimated Percent Green Space Along Walkable Roads Web Service",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3275e906-3d2b-422c-8747-9d53d288be56}",
+            "issued": "2016-10-06",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -257917,46 +257936,46 @@
                 "Paterson, NJ",
                 "New York, NY"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas Estimated Percent Green Space Along Walkable Roads Web Service"
         },
-            "identifier": "{3275e906-3d2b-422c-8747-9d53d288be56}",
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
-            "issued": "2016-10-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas Estimated Percent Tree Cover Along Walkable Roads Web Service",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{24d7a1db-6b9d-4174-98ae-26866f022bcf}",
+            "issued": "2016-10-06",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -258029,46 +258048,48 @@
                 "Paterson, NJ",
                 "New York, NY"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas Estimated Percent Tree Cover Along Walkable Roads Web Service"
         },
-            "identifier": "{24d7a1db-6b9d-4174-98ae-26866f022bcf}",
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
+                "fn": "Anne Neale",
+                "hasEmail": "mailto:neale.anne@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-10-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Percentage Potential Wetland Area by HUC-12 on Cultivated Cropland (Pct_PWAC) layer shows areas where conditions may be suitable for wetland restoration or creation on cropland at a 10-m resolution. Since the 1600's, an estimated 53% of wetlands in the Conterminous United States have been lost, with many areas being converted for agricultural or urban use. The ecosystems services provided by wetlands are extremely valuable, providing flood attenuation, water filtration, nutrient sequestration, vital habitat, and many others. Wetland restoration or creation can help restore these benefits for the surrounding community. There are several government and community projects that can utilize these data to assist in site selection for wetland restoration projects. \nThis layer was created using the Random Forest (RF) machine learning algorithm in Google Earth Engine (GEE). The RF model utilized 17 data inputs to identify areas where attributes on the landscape are similar to the attributes found in existing wetlands. The input data for this layer fall into three categories: topographic variables, soils, and satellite imagery. \nTopographic - DEM's sourced from USGS 3D Elevation Program (10-m)\n-Elevation\n-Aspect\n-Slope\n-Compound Topographic Index (CTI)\n-Vertical Overland Flow Distance (VOFD)\n-Horizontal Overland Flow Distance (HOFD)\n-Pythagoras Overland Flow Distance (POFD)\n-Soils - Natural Resource Conservation Service's gNATSGO and gSSURGO products\n\u00b7 Potential Wetland Soils (PWS)\n-European Space Agency's Sentinel-1 Synthetic Aperture Radar (10-m) \n\nUsing these variables, the Random Forest model was run for each 2 digit Hydrologic Unit Code (HUC) in Google Earth Engine. The model used wetlands from the National Wetland Inventory (NWI) to create training data, masking out deep water areas such as the centers of lakes and rivers, and excluding estuarine and marine wetlands. For each HUC an equal number of wetland and non-wetland training points proportional to the size of the HUC were generated, with 30% of those points being reserved for accuracy assessment. The model results were then summarized to calculate the areal coverage of PWA within each HUC-12 watershed in the United States. This dataset shows the percentage of each 12-digit HUC that is both potential wetland area and cropland.\n\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://enviroatlas.epa.gov/download/"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percent Potential Wetland on Cultivated Cropland Area by 12-digit HUC for the Conterminous United States",
-            "description": "The Percentage Potential Wetland Area by HUC-12 on Cultivated Cropland (Pct_PWAC) layer shows areas where conditions may be suitable for wetland restoration or creation on cropland at a 10-m resolution. Since the 1600's, an estimated 53% of wetlands in the Conterminous United States have been lost, with many areas being converted for agricultural or urban use. The ecosystems services provided by wetlands are extremely valuable, providing flood attenuation, water filtration, nutrient sequestration, vital habitat, and many others. Wetland restoration or creation can help restore these benefits for the surrounding community. There are several government and community projects that can utilize these data to assist in site selection for wetland restoration projects. \nThis layer was created using the Random Forest (RF) machine learning algorithm in Google Earth Engine (GEE). The RF model utilized 17 data inputs to identify areas where attributes on the landscape are similar to the attributes found in existing wetlands. The input data for this layer fall into three categories: topographic variables, soils, and satellite imagery. \nTopographic - DEM's sourced from USGS 3D Elevation Program (10-m)\n-Elevation\n-Aspect\n-Slope\n-Compound Topographic Index (CTI)\n-Vertical Overland Flow Distance (VOFD)\n-Horizontal Overland Flow Distance (HOFD)\n-Pythagoras Overland Flow Distance (POFD)\n-Soils - Natural Resource Conservation Service's gNATSGO and gSSURGO products\n\u00b7 Potential Wetland Soils (PWS)\n-European Space Agency's Sentinel-1 Synthetic Aperture Radar (10-m) \n\nUsing these variables, the Random Forest model was run for each 2 digit Hydrologic Unit Code (HUC) in Google Earth Engine. The model used wetlands from the National Wetland Inventory (NWI) to create training data, masking out deep water areas such as the centers of lakes and rivers, and excluding estuarine and marine wetlands. For each HUC an equal number of wetland and non-wetland training points proportional to the size of the HUC were generated, with 30% of those points being reserved for accuracy assessment. The model results were then summarized to calculate the areal coverage of PWA within each HUC-12 watershed in the United States. This dataset shows the percentage of each 12-digit HUC that is both potential wetland area and cropland.\n\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "21BC802B-9777-4419-8473-F3CDF2BFE022",
+            "issued": "2024-07-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -258135,31 +258156,34 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-07-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, Nation Atlas for Sustainability"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Anne Neale",
-                "hasEmail": "mailto:neale.anne@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-128.007244, 22.868654, -65.25485, 51.64959",
+            "temporal": "2016-01-01T00:00:00/2021-12-31T00:00:00",
+            "title": "EnviroAtlas - Percent Potential Wetland on Cultivated Cropland Area by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "21BC802B-9777-4419-8473-F3CDF2BFE022",
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
-            "temporal": "2016-01-01T00:00:00/2021-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Anne Neale",
+                "hasEmail": "mailto:neale.anne@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2024-07-30",
+            "description": "The Percentage Potential Wetland Area by HUC-12 (Pct_PWA) layer shows areas where conditions may be suitable for wetland restoration or creation at a 10-m resolution. Since the 1600's, an estimated 53% of wetlands in the Conterminous United States have been lost, with many areas being converted for agricultural or urban use. The ecosystems services provided by wetlands are extremely valuable, providing flood attenuation, water filtration, nutrient sequestration, vital habitat, and many others. Wetland restoration or creation can help restore these benefits for the surrounding community. There are several government and community projects that can utilize these data to assist in site selection for wetland restoration projects. \nThis layer was created using the Random Forest (RF) machine learning algorithm in Google Earth Engine (GEE). The RF model utilized 17 data inputs to identify areas where attributes on the landscape are similar to the attributes found in existing wetlands. The input data for this layer fall into three categories: topographic variables, soils, and satellite imagery. \nTopographic - DEM's sourced from USGS 3D Elevation Program (10-m)\n-Elevation\n-Aspect\n-Slope\n-Compound Topographic Index (CTI)\n-Vertical Overland Flow Distance (VOFD)\n-Horizontal Overland Flow Distance (HOFD)\n-Pythagoras Overland Flow Distance (POFD)\n-Soils - Natural Resource Conservation Service's gNATSGO and gSSURGO products\n\u00b7 Potential Wetland Soils (PWS)\n-European Space Agency's Sentinel-1 Synthetic Aperture Radar (10-m) \n\nUsing these variables, the Random Forest model was run for each 2 digit Hydrologic Unit Code (HUC) in Google Earth Engine. The model used wetlands from the National Wetland Inventory (NWI) to create training data, masking out deep water areas such as the centers of lakes and rivers, and excluding estuarine and marine wetlands. For each HUC an equal number of wetland an non-wetland training points proportional to the size of the HUC were generated, with 30% of those points being reserved for accuracy assessment. The model results were then summarized to calculate the areal coverage of PWA within each HUC-12 watershed in the United States.\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -258169,12 +258193,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percent Potential Wetland Area by 12-digit HUC for the Conterminous United States",
-            "description": "The Percentage Potential Wetland Area by HUC-12 (Pct_PWA) layer shows areas where conditions may be suitable for wetland restoration or creation at a 10-m resolution. Since the 1600's, an estimated 53% of wetlands in the Conterminous United States have been lost, with many areas being converted for agricultural or urban use. The ecosystems services provided by wetlands are extremely valuable, providing flood attenuation, water filtration, nutrient sequestration, vital habitat, and many others. Wetland restoration or creation can help restore these benefits for the surrounding community. There are several government and community projects that can utilize these data to assist in site selection for wetland restoration projects. \nThis layer was created using the Random Forest (RF) machine learning algorithm in Google Earth Engine (GEE). The RF model utilized 17 data inputs to identify areas where attributes on the landscape are similar to the attributes found in existing wetlands. The input data for this layer fall into three categories: topographic variables, soils, and satellite imagery. \nTopographic - DEM's sourced from USGS 3D Elevation Program (10-m)\n-Elevation\n-Aspect\n-Slope\n-Compound Topographic Index (CTI)\n-Vertical Overland Flow Distance (VOFD)\n-Horizontal Overland Flow Distance (HOFD)\n-Pythagoras Overland Flow Distance (POFD)\n-Soils - Natural Resource Conservation Service's gNATSGO and gSSURGO products\n\u00b7 Potential Wetland Soils (PWS)\n-European Space Agency's Sentinel-1 Synthetic Aperture Radar (10-m) \n\nUsing these variables, the Random Forest model was run for each 2 digit Hydrologic Unit Code (HUC) in Google Earth Engine. The model used wetlands from the National Wetland Inventory (NWI) to create training data, masking out deep water areas such as the centers of lakes and rivers, and excluding estuarine and marine wetlands. For each HUC an equal number of wetland an non-wetland training points proportional to the size of the HUC were generated, with 30% of those points being reserved for accuracy assessment. The model results were then summarized to calculate the areal coverage of PWA within each HUC-12 watershed in the United States.\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "396BB64F-7E84-4874-B9E0-426B4619A980",
+            "issued": "2024-07-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -258240,46 +258261,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-07-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, Nation Atlas for Sustainability"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Anne Neale",
-                "hasEmail": "mailto:neale.anne@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-128.007244, 22.868654, -65.25485, 51.64959",
+            "temporal": "2016-01-01T00:00:00/2021-12-31T00:00:00",
+            "title": "EnviroAtlas - Percent Potential Wetland Area by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "396BB64F-7E84-4874-B9E0-426B4619A980",
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
-            "temporal": "2016-01-01T00:00:00/2021-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2024-07-30",
+            "description": "This EnviroAtlas dataset estimates the percent urban land for each 12-digit hydrologic unit code (HUC) in the conterminous United States. For the purposes of this map, urban land cover includes a variety of development, such as open spaces, parks, golf courses, single family homes, multifamily housing units, retail, commercial, industrial sites, and associated infrastructure. Urban land cover is not confined to city limits. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://enviroatlas.epa.gov/download/"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percent Urban Land Cover by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset estimates the percent urban land for each 12-digit hydrologic unit code (HUC) in the conterminous United States. For the purposes of this map, urban land cover includes a variety of development, such as open spaces, parks, golf courses, single family homes, multifamily housing units, retail, commercial, industrial sites, and associated infrastructure. Urban land cover is not confined to city limits. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0068AF7C-DE6C-4510-806A-BC35F333FE24}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -258342,46 +258361,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Percent Urban Land Cover by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{0068AF7C-DE6C-4510-806A-BC35F333FE24}",
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
-            "temporal": "9999-01-01/9999-01-01",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 3974 block groups in Philadelphia, PA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Philadelphia City and County, PA, New Castle County, DE, Cecil County, MD, Camden County, NJ, Atlantic County, NJ, Gloucester County, NJ, Burlington County, NJ, Delaware County, PA, Bucks County, PA, Chester County, PA, and Montgomery County, PA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 3974 block groups in Philadelphia, PA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Philadelphia City and County, PA, New Castle County, DE, Cecil County, MD, Camden County, NJ, Atlantic County, NJ, Gloucester County, NJ, Burlington County, NJ, Delaware County, PA, Bucks County, PA, Chester County, PA, and Montgomery County, PA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{63082fc2-f386-41c4-b431-1c629b08b868}",
+            "issued": "2018-11-30",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -258401,46 +258420,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-30",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - BenMAP Results by Block Group"
         },
-            "identifier": "{63082fc2-f386-41c4-b431-1c629b08b868}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Philadelphia, PA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Philadelphia, PA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a3f58942-f73e-4854-86be-7c5b75da34d1}",
+            "issued": "2018-07-20",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -258453,46 +258472,46 @@
                 "Environmental Atlas",
                 "Philadelphia, PA"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-20",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Census Block Groups"
         },
-            "identifier": "{a3f58942-f73e-4854-86be-7c5b75da34d1}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cfbbd51b-0de3-42a4-8e89-234aee549d29}",
+            "issued": "2018-07-20",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -258509,46 +258528,46 @@
                 "Philadelphia, PA",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-20",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Philadelphia, PA - Demographics by Block Group"
         },
-            "identifier": "{cfbbd51b-0de3-42a4-8e89-234aee549d29}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-20",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Philadelphia, PA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Philadelphia, PA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{43908204-43e6-46c9-b606-d0ff0733e91a}",
+            "issued": "2018-07-20",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -258561,46 +258580,46 @@
                 "Philadelphia, PA",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-20",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - EnviroAtlas Community Boundary"
         },
-            "identifier": "{43908204-43e6-46c9-b606-d0ff0733e91a}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c05ee584-f8a8-43d4-a6ff-bc7158deb657}",
+            "issued": "2019-11-07",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -258616,46 +258635,46 @@
                 "Environmental Atlas",
                 "Pennsylvania"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-07",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{c05ee584-f8a8-43d4-a6ff-bc7158deb657}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Domestic water demand was calculated and applied using the Pennsylvania Department of Environmental Protection (PADEP) PWS Service Areas layer, population served per provider, and average domestic water use per provider. Within the EnviroAtlas study area, there are 108 service providers with 2016 estimates ranging from 26 to 323 GPD. In the absence of finer scale data, USGS Water Use Report county-level estimates were used for the study area extending into Delaware (80 GPD), Maryland (71 GPD), and New Jersey (80 GPD). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Domestic Water Demand per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Domestic water demand was calculated and applied using the Pennsylvania Department of Environmental Protection (PADEP) PWS Service Areas layer, population served per provider, and average domestic water use per provider. Within the EnviroAtlas study area, there are 108 service providers with 2016 estimates ranging from 26 to 323 GPD. In the absence of finer scale data, USGS Water Use Report county-level estimates were used for the study area extending into Delaware (80 GPD), Maryland (71 GPD), and New Jersey (80 GPD). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f5720842-4fe0-41ba-b355-880586a2ccf3}",
+            "issued": "2019-02-12",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -258675,46 +258694,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-02-12",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Domestic Water Demand per Day by U.S. Census Block Group"
         },
-            "identifier": "{f5720842-4fe0-41ba-b355-880586a2ccf3}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-02-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2bd2b55a-b357-44b3-9c5f-a28157744d88}",
+            "issued": "2018-07-20",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -258730,46 +258749,46 @@
                 "Philadelphia, PA",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-20",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{2bd2b55a-b357-44b3-9c5f-a28157744d88}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, https://msc.fema.gov/portal/advanceSearch). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, https://msc.fema.gov/portal/advanceSearch). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ca55e46a-9a25-4316-b09a-49fcc7de0f37}",
+            "issued": "2019-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -258793,46 +258812,46 @@
                 "Pennsylvania",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-19",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2018-08-27/2018-08-27",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{ca55e46a-9a25-4316-b09a-49fcc7de0f37}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2018-08-27/2018-08-27",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{096a8b50-07be-4765-92f2-d3da4a9e2040}",
+            "issued": "2018-07-22",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -258847,46 +258866,46 @@
                 "Philadelphia, PA",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-22",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Greenspace Proximity Gradient"
         },
-            "identifier": "{096a8b50-07be-4765-92f2-d3da4a9e2040}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{46076b5a-da12-4522-ad5b-2347714779f6}",
+            "issued": "2019-02-01",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -258902,46 +258921,46 @@
                 "Pennsylvania",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-02-01",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Historic Places by Census Block Group"
         },
-            "identifier": "{46076b5a-da12-4522-ad5b-2347714779f6}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-02-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8fcc1784-a564-46df-8adb-4c2a9fc83d43}",
+            "issued": "2018-07-22",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -258955,46 +258974,46 @@
                 "Philadelphia, PA",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-22",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Impervious Proximity Gradient"
         },
-            "identifier": "{8fcc1784-a564-46df-8adb-4c2a9fc83d43}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-22",
-            "language": "en-us",
-            "theme": "environment",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ab73b737-0251-4f7c-b936-6bad0cda0109}",
+            "issued": "2018-07-23",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259009,46 +259028,46 @@
                 "Transportation",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-23",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{ab73b737-0251-4f7c-b936-6bad0cda0109}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 3974 block groups in Philadelphia, PA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 3974 block groups in Philadelphia, PA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c96e1215-567c-4b46-bd0a-2c05eff355c1}",
+            "issued": "2018-11-30",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -259067,46 +259086,46 @@
                 "Pennsylvania",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-30",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2008-01-01/2008-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Ecosystem Services by Block Group"
         },
-            "identifier": "{c96e1215-567c-4b46-bd0a-2c05eff355c1}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2008-01-01/2008-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, Orchards, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture and Orchards. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, Orchards, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture and Orchards. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a1f71e9b-e112-42b7-8890-1bfd8c75885d}",
+            "issued": "2019-02-06",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259122,46 +259141,46 @@
                 "Environmental Atlas",
                 "Pennsylvania"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-02-06",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Land Cover by Block Group"
         },
-            "identifier": "{a1f71e9b-e112-42b7-8890-1bfd8c75885d}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-02-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Philadelphia, PA Meter-Scale Urban Land Cover (MULC) dataset comprises 7184 km2 around the city of Philadelphia and surrounding land in parts of fourteen counties within four states (PA, DE, NJ, MD): New Castle County in Delaware and Cecil County Maryland; Bucks, Chester, Lancaster, Montgomery, Philadelphia, and Delaware Counties in Pennsylvania; and Burlington, Mercer, Camden, Gloucester, Salmen and Atlantic Counties in New Jersey. These MULC data and maps were derived from several sources from multiple years: leaf-off LiDAR; 1-m pixel, four-band (red, green, blue, and near-infrared) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP); 1-ft pixel orthoimagery; additional leaf-on and leaf-off imagery as well as ancillary vector data (e.g., roads, building footprints.). Ten land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forested, Shrub, Grass/Herbaceous NonWoody Vegetation, Agriculture, Orchard, and Wetlands (Woody and Emergent). Wetlands were delineated using the best available existing wetlands data, which was a National Wetlands Inventory (NWI) layer. An analysis of 600 completely random and 251 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 78% and an overall fuzzy user's accuracy (RIGHT) of 86% (see confusion matrices below). This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy (UTC) assessment program, and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Philadelphia, PA -- Meter-Scale Urban Land Cover Data (MULC) Data (2013)",
-            "description": "The Philadelphia, PA Meter-Scale Urban Land Cover (MULC) dataset comprises 7184 km2 around the city of Philadelphia and surrounding land in parts of fourteen counties within four states (PA, DE, NJ, MD): New Castle County in Delaware and Cecil County Maryland; Bucks, Chester, Lancaster, Montgomery, Philadelphia, and Delaware Counties in Pennsylvania; and Burlington, Mercer, Camden, Gloucester, Salmen and Atlantic Counties in New Jersey. These MULC data and maps were derived from several sources from multiple years: leaf-off LiDAR; 1-m pixel, four-band (red, green, blue, and near-infrared) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP); 1-ft pixel orthoimagery; additional leaf-on and leaf-off imagery as well as ancillary vector data (e.g., roads, building footprints.). Ten land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forested, Shrub, Grass/Herbaceous NonWoody Vegetation, Agriculture, Orchard, and Wetlands (Woody and Emergent). Wetlands were delineated using the best available existing wetlands data, which was a National Wetlands Inventory (NWI) layer. An analysis of 600 completely random and 251 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 78% and an overall fuzzy user's accuracy (RIGHT) of 86% (see confusion matrices below). This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy (UTC) assessment program, and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c28bb96a-9a58-445b-a284-9ed2b9147704}",
+            "issued": "2018-07-13",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -259187,46 +259206,46 @@
                 "Communities",
                 "Pennsylvania"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-13",
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
+            "spatial": "-76.089481, 39.182267, -74.547769, 40.754351",
+            "temporal": "2012-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Philadelphia, PA -- Meter-Scale Urban Land Cover Data (MULC) Data (2013)"
         },
-            "identifier": "{c28bb96a-9a58-445b-a284-9ed2b9147704}",
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
-            "spatial": "-76.089481, 39.182267, -74.547769, 40.754351",
-            "temporal": "2012-01-01/2012-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{625a28a9-3fa5-4009-9904-0a5969f3436f}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259244,46 +259263,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{625a28a9-3fa5-4009-9904-0a5969f3436f}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{49b48e48-d40b-4474-b47b-501ef35e89d0}",
+            "issued": "2018-07-20",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259302,46 +259321,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-20",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{49b48e48-d40b-4474-b47b-501ef35e89d0}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-20",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4947cfa4-0614-49e2-b321-0fb3b8641e9f}",
+            "issued": "2018-09-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -259356,46 +259375,46 @@
                 "Philadelphia, PA",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-24",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Park Access by Block Group"
         },
-            "identifier": "{4947cfa4-0614-49e2-b321-0fb3b8641e9f}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7a75b14a-0a19-4eec-b557-82a38c908c9b}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -259409,46 +259428,46 @@
                 "Philadelphia, PA",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Proximity to Parks"
         },
-            "identifier": "{7a75b14a-0a19-4eec-b557-82a38c908c9b}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
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
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PhiladelphiaPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Philadelphia, PA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d84e06cd-3b93-4c91-bc62-3c55d562315c}",
+            "issued": "2018-07-24",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259466,46 +259485,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-24",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{d84e06cd-3b93-4c91-bc62-3c55d562315c}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b65ca0bd-3ea6-417f-96b6-67a010e96e96}",
+            "issued": "2018-07-23",
             "keyword": [
                 "Ecosystem Services",
                 "Philadelphia, PA",
@@ -259523,46 +259542,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-23",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{b65ca0bd-3ea6-417f-96b6-67a010e96e96}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-23",
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
-            "title": "EnviroAtlas - Philadelphia, PA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6cb4b1dd-a3bf-41f8-89d7-75505337fda2}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259582,46 +259601,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{6cb4b1dd-a3bf-41f8-89d7-75505337fda2}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{32b1263f-921a-4aa3-9fa0-d72d87544686}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259641,46 +259660,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{32b1263f-921a-4aa3-9fa0-d72d87544686}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
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
-            "title": "EnviroAtlas - Philadelphia, PA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{deacd43e-e4cc-4c02-81ef-27a44dd0cddd}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259700,46 +259719,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{deacd43e-e4cc-4c02-81ef-27a44dd0cddd}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e6710a3f-ca84-4ab5-822d-3b3a66ec3a3d}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259759,46 +259778,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{e6710a3f-ca84-4ab5-822d-3b3a66ec3a3d}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest and Woody Wetlands, and vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest and Woody Wetlands, and vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{79db3b23-5435-46ab-99fa-83fd3d44776d}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259819,46 +259838,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{79db3b23-5435-46ab-99fa-83fd3d44776d}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6f526c69-af3f-4d77-8170-8e6a2d91b1b8}",
+            "issued": "2018-07-22",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -259876,46 +259895,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-22",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{6f526c69-af3f-4d77-8170-8e6a2d91b1b8}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-22",
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
-            "title": "EnviroAtlas - Philadelphia, PA - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{be3d9eff-36ca-4ad2-be91-cb8d24365bb1}",
+            "issued": "2018-07-21",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -259931,46 +259950,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-07-21",
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
+            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Philadelphia, PA - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{be3d9eff-36ca-4ad2-be91-cb8d24365bb1}",
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
-            "spatial": "-75.96899, 39.49219, -74.68399, 40.44512",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-07-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains information about physical characteristics, such as temperature, elevation, and precipitation, in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of abiotic conditions for stream confluence catchments for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about physical characteristics, such as temperature, elevation, and precipitation, in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{59c6b038-2877-40de-adcf-e4126415c003}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -260030,46 +260049,46 @@
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
+            "temporal": "2015-11-19/2015-11-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of abiotic conditions for stream confluence catchments for the Conterminous United States"
         },
-            "identifier": "{59c6b038-2877-40de-adcf-e4126415c003}",
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
-            "temporal": "2015-11-19/2015-11-19",
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
+            "description": "This EnviroAtlas dataset contains information about physical characteristics, such as temperature, elevation, and precipitation, in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of abiotic conditions for stream confluence watersheds for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about physical characteristics, such as temperature, elevation, and precipitation, in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6d9ccbb0-23e3-47d5-980a-9c24bee83472}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -260129,46 +260148,46 @@
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
+            "temporal": "2015-11-19/2015-11-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of abiotic conditions for stream confluence watersheds for the Conterminous United States"
         },
-            "identifier": "{6d9ccbb0-23e3-47d5-980a-9c24bee83472}",
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
-            "temporal": "2015-11-19/2015-11-19",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,089 block groups in Pittsburgh, PA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,089 block groups in Pittsburgh, PA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5596A087-44F0-428F-8ECD-4B64A04A08F4}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -260188,46 +260207,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - BenMAP Results by Block Group"
         },
-            "identifier": "{5596A087-44F0-428F-8ECD-4B64A04A08F4}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Pittsburgh, PA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Pittsburgh, PA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9159FFCB-F1DC-43F2-A50E-DF350DE165F5}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -260240,46 +260259,46 @@
                 "Environmental Atlas",
                 "Pennsylvania"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-05/2013-11-05",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Block Groups"
         },
-            "identifier": "{9159FFCB-F1DC-43F2-A50E-DF350DE165F5}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-05/2013-11-05",
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
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9FF2E3B6-949C-4B1A-86C8-466A17A6CA7B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -260296,46 +260315,46 @@
                 "Pennsylvania",
                 "Boundaries"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Pittsburgh, PA - Demographics by Block Group"
         },
-            "identifier": "{9FF2E3B6-949C-4B1A-86C8-466A17A6CA7B}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Pittsburgh, PA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Pittsburgh, PA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FF438EA9-EA03-4A2A-B6DA-6365D4F829E5}",
+            "issued": "2013-10-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -260348,46 +260367,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-10-24/2013-10-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Atlas Area Boundary"
         },
-            "identifier": "{FF438EA9-EA03-4A2A-B6DA-6365D4F829E5}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-10-24/2013-10-24",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A6BB21AA-E4AA-4C14-B6F0-E37370E0DDBE}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -260402,46 +260421,46 @@
                 "Environmental Atlas",
                 "Pennsylvania"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{A6BB21AA-E4AA-4C14-B6F0-E37370E0DDBE}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Domestic water demand was calculated and applied using the Pennsylvania Department of Environmental Protection (PADEP) PWS Service Areas layer, population served per provider, and average water use per provider. Within the EnviroAtlas study area, there are 43 service providers with 2010-2013 estimates ranging from 34 to 102 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Domestic water demand was calculated and applied using the Pennsylvania Department of Environmental Protection (PADEP) PWS Service Areas layer, population served per provider, and average water use per provider. Within the EnviroAtlas study area, there are 43 service providers with 2010-2013 estimates ranging from 34 to 102 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9FB6737D-A5BA-43D5-84A9-EB2B9E766974}",
+            "issued": "2014-11-10",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -260461,46 +260480,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-11-10",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{9FB6737D-A5BA-43D5-84A9-EB2B9E766974}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-11-10",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{EBBF64AC-E34B-4F2F-9A1F-C10609ECF4C1}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -260516,46 +260535,46 @@
                 "Pennsylvania",
                 "Human Well-being"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-04/2013-11-04",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{EBBF64AC-E34B-4F2F-9A1F-C10609ECF4C1}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-04/2013-11-04",
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
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e19e1ec2-7730-4e4e-a4d9-dd286cabd7d6}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -260579,46 +260598,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{e19e1ec2-7730-4e4e-a4d9-dd286cabd7d6}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{38F000B9-0ECB-41B6-94D2-4A29992A4088}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -260633,46 +260652,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2015-03-20/2015-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Greenspace Proximity Gradient"
         },
-            "identifier": "{38F000B9-0ECB-41B6-94D2-4A29992A4088}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{23727E56-F4FD-4D81-BA01-68E61264B049}",
+            "issued": "2014-08-26",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -260688,46 +260707,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Historic Places by Census Block Group"
         },
-            "identifier": "{23727E56-F4FD-4D81-BA01-68E61264B049}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{DB557F85-3D0C-4A0C-ACE1-07B1E307C73D}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -260741,46 +260760,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2015-03-25/2015-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Impervious Proximity Gradient"
         },
-            "identifier": "{DB557F85-3D0C-4A0C-ACE1-07B1E307C73D}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{DA4B629D-3224-45AD-8C32-F27253634ED4}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -260795,46 +260814,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{DA4B629D-3224-45AD-8C32-F27253634ED4}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,089 block groups in Pittsburgh, Pennsylvania. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,089 block groups in Pittsburgh, Pennsylvania. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E937396D-EF92-4382-8818-D6316D5A1D0B}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -260853,46 +260872,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Ecosystem Services by Block Group"
         },
-            "identifier": "{E937396D-EF92-4382-8818-D6316D5A1D0B}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A7A825CD-02E4-4527-BE07-40FA80495F98}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -260909,46 +260928,46 @@
                 "Environmental Atlas",
                 "Pennsylvania"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-01/2013-11-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Land Cover by Block Group"
         },
-            "identifier": "{A7A825CD-02E4-4527-BE07-40FA80495F98}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-01/2013-11-01",
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
+            "description": "The EnviroAtlas Pittsburgh, PA Meter-Scale Urban Land Cover (MULC) data was generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution. Imagery was collected on multiple dates in June 2010. Five land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, and grass and herbaceous non-woody vegetation. An accuracy assessment of 500 completely random and 81 stratified random points yielded an overall user's accuracy (MAX) of 86.57% and an overall fuzzy user's accuracy (RIGHT) of 89.33%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Pittsburgh, PA. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Pittsburgh, PA -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The EnviroAtlas Pittsburgh, PA Meter-Scale Urban Land Cover (MULC) data was generated from United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1 m spatial resolution. Imagery was collected on multiple dates in June 2010. Five land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, and grass and herbaceous non-woody vegetation. An accuracy assessment of 500 completely random and 81 stratified random points yielded an overall user's accuracy (MAX) of 86.57% and an overall fuzzy user's accuracy (RIGHT) of 89.33%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Pittsburgh, PA. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2474DC34-035D-495B-99A7-70346BA9CAD5}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -260971,46 +260990,46 @@
                 "Communities",
                 "Pennsylvania"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-06-01/2010-06-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Pittsburgh, PA -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{2474DC34-035D-495B-99A7-70346BA9CAD5}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2010-06-01/2010-06-01",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{452510F7-4AAC-4E56-A982-6F5B757D5DA2}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -261028,46 +261047,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Near Road Tree Buffer"
         },
-            "identifier": "{452510F7-4AAC-4E56-A982-6F5B757D5DA2}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CCFA8480-ED62-4E2B-A357-18D3986151EC}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -261087,46 +261106,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Near Road Block Group Summary"
         },
-            "identifier": "{CCFA8480-ED62-4E2B-A357-18D3986151EC}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{796332AC-95F3-4497-B299-99E7F9C5B17D}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -261141,46 +261160,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2015-10-02/2015-10-02",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Park Access by Block Group"
         },
-            "identifier": "{796332AC-95F3-4497-B299-99E7F9C5B17D}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2015-10-02/2015-10-02",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A62B08BE-36D7-43EF-8C89-4EDC2EB5EF54}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -261194,46 +261213,46 @@
                 "Pennsylvania",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Proximity to Parks"
         },
-            "identifier": "{A62B08BE-36D7-43EF-8C89-4EDC2EB5EF54}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{0C9150F5-A4E4-491E-87A0-319861DCE079}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -261251,46 +261270,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{0C9150F5-A4E4-491E-87A0-319861DCE079}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9DFA46F0-5610-4BB0-AD19-0812DA87A736}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -261308,46 +261327,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{9DFA46F0-5610-4BB0-AD19-0812DA87A736}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9CF44800-A341-4256-98B0-A39AE5964047}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261367,46 +261386,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-08/2013-11-08",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{9CF44800-A341-4256-98B0-A39AE5964047}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-08/2013-11-08",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{16C421EF-C4AF-403B-A8CF-A92AE2C8D649}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261426,46 +261445,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-08/2013-11-08",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{16C421EF-C4AF-403B-A8CF-A92AE2C8D649}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-08/2013-11-08",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{216FCA4C-060A-4941-826E-4C1C1D4820C0}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261485,46 +261504,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-08/2013-11-08",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{216FCA4C-060A-4941-826E-4C1C1D4820C0}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-08/2013-11-08",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A73674D8-E2AD-4DD4-850D-73F7D4299BB0}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261544,46 +261563,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-08/2013-11-08",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{A73674D8-E2AD-4DD4-850D-73F7D4299BB0}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-08/2013-11-08",
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
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{04FD87BB-E2A7-4D05-B817-C2121648C633}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261604,46 +261623,46 @@
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2013-11-07/2013-11-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{04FD87BB-E2A7-4D05-B817-C2121648C633}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2013-11-07/2013-11-07",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{03FA9849-3EA5-48A0-9C0A-B963FFAF027D}",
+            "issued": "2014-06-17",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -261661,46 +261680,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-06-17",
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2014-06-11/2014-06-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{03FA9849-3EA5-48A0-9C0A-B963FFAF027D}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2014-06-11/2014-06-11",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-06-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Pittsburgh, PA - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6F575B19-1785-483B-A36A-4E9BFD02A048}",
+            "issued": "2013-10-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -261716,46 +261735,48 @@
                 "Water",
                 "Human Well-being"
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
+            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
+            "temporal": "2014-06-10/2014-06-10",
+            "theme": "environment",
+            "title": "EnviroAtlas - Pittsburgh, PA - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{6F575B19-1785-483B-A36A-4E9BFD02A048}",
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
-            "spatial": "-80.29781, 40.24197, -79.68825, 40.67122",
-            "temporal": "2014-06-10/2014-06-10",
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
+            "description": "This raster GIS dataset includes the number of days in 2017 that the concentration of particulate matter with a diameter of 2.5 micrometers or smaller (PM2.5) predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 35 micrograms per cubic meter.  This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PittsburghPA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Particulate Matter Concentration (PM2.5) - Days over 35 micrograms per cubic meter in 2017 for the Conterminous United States",
-            "description": "This raster GIS dataset includes the number of days in 2017 that the concentration of particulate matter with a diameter of 2.5 micrometers or smaller (PM2.5) predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 35 micrograms per cubic meter.  This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "DF8359EB-C8E6-4FC1-BD1E-767745C886DE",
+            "issued": "2021-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -261818,31 +261839,34 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-12-16",
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
+            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
+            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
+            "title": "EnviroAtlas - Particulate Matter Concentration (PM2.5) - Days over 35 micrograms per cubic meter in 2017 for the Conterminous United States"
         },
-            "identifier": "DF8359EB-C8E6-4FC1-BD1E-767745C886DE",
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
-            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
-            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-12-16",
+            "description": "This raster GIS dataset includes the number of days in 2017 that the concentration of particulate matter with a diameter of 2.5 micrometers or smaller (PM2.5) predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 65 micrograms per cubic meter.  This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -261852,12 +261876,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Particulate Matter Concentration (PM2.5) - Days over 65 micrograms per cubic meter in 2017 for the Conterminous United States",
-            "description": "This raster GIS dataset includes the number of days in 2017 that the concentration of particulate matter with a diameter of 2.5 micrometers or smaller (PM2.5) predicted by the Community Multiscale Air Quality modeling system (CMAQ) exceeds a threshold value of 65 micrograms per cubic meter.  This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "C42BDB78-4974-41A6-A153-EC145B5E4264",
+            "issued": "2021-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -261920,46 +261941,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-12-16",
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
+            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
+            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
+            "title": "EnviroAtlas - Particulate Matter Concentration (PM2.5) - Days over 65 micrograms per cubic meter in 2017 for the Conterminous United States"
         },
-            "identifier": "C42BDB78-4974-41A6-A153-EC145B5E4264",
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
-            "spatial": "-128.4049, 22.607417, -64.237763, 51.93219",
-            "temporal": "2017-01-01T00:00:00/2017-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-12-16",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 146 block groups in Portland, Maine. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 146 block groups in Portland, Maine. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{414CC99E-E301-404B-A693-19ABF424D135}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -261979,46 +261998,46 @@
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - BenMAP Results by Block Group"
         },
-            "identifier": "{414CC99E-E301-404B-A693-19ABF424D135}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Portland, ME EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Portland, ME EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{48DC351F-CBBC-4E7A-9B1F-F68047007A81}",
+            "issued": "2013-03-27",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -262031,46 +262050,46 @@
                 "Environmental Atlas",
                 "Portland, ME"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-03-27",
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Block Groups"
         },
-            "identifier": "{48DC351F-CBBC-4E7A-9B1F-F68047007A81}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
-            "temporal": "2012-03-01/2012-03-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-03-27",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{30D95C69-8473-4374-85A5-AD4292B7F011}",
+            "issued": "2014-08-07",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -262087,46 +262106,46 @@
                 "Portland, ME",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-07",
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Portland, ME - Demographics by Block Group"
         },
-            "identifier": "{30D95C69-8473-4374-85A5-AD4292B7F011}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-07",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Portland, ME Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Portland, ME Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3F07E5C3-EBC4-44C9-A672-B6A3F886BDF1}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -262139,46 +262158,46 @@
                 "Portland, ME",
                 "Boundaries"
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Atlas Area Boundary"
         },
-            "identifier": "{3F07E5C3-EBC4-44C9-A672-B6A3F886BDF1}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
-            "temporal": "2012-03-01/2012-03-01",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8FF72C94-A9F3-4DD5-AE38-47DD43B085FF}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -262193,46 +262212,46 @@
                 "Environmental Atlas",
                 "Portland, ME"
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{8FF72C94-A9F3-4DD5-AE38-47DD43B085FF}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
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
+            "description": "As included in this EnviroAtlas dataset, the community domestic water use was calculated using local domestic water use per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these provider-supplied estimates are also considered representative of local self-supplied water use. Specific to Portland, ME, the Portland Water District (PWD) is the main provider for the study area. Within the study area, PWD supports Portland, South Portland, Westbrook, Scarborough, and Cape Elizabeth. PWD estimates current residential water use to be ~52 GPD. The southern portion of the study area is supported by the Biddeford and Saco Water Company (BSWC). Within the study area, their service area includes Biddeford, Saco, Old Orchard Beach, and Pine Point. BSWC estimates current residential water usage to be ~50 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community domestic water use was calculated using local domestic water use per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these provider-supplied estimates are also considered representative of local self-supplied water use. Specific to Portland, ME, the Portland Water District (PWD) is the main provider for the study area. Within the study area, PWD supports Portland, South Portland, Westbrook, Scarborough, and Cape Elizabeth. PWD estimates current residential water use to be ~52 GPD. The southern portion of the study area is supported by the Biddeford and Saco Water Company (BSWC). Within the study area, their service area includes Biddeford, Saco, Old Orchard Beach, and Pine Point. BSWC estimates current residential water usage to be ~50 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{B57C01B0-F9E5-4607-BAFC-C5140920951F}",
+            "issued": "2016-08-11",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -262252,46 +262271,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-08-11",
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{B57C01B0-F9E5-4607-BAFC-C5140920951F}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-08-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary, as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary, as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{977E8DF8-A8F1-4EF2-BEA1-963A0078DB27}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -262307,46 +262326,46 @@
                 "Portland, ME",
                 "Human Well-being"
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{977E8DF8-A8F1-4EF2-BEA1-963A0078DB27}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
-            "temporal": "9999-01-01/9999-01-01",
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
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ed880428-f69d-4a89-b507-a1a761236c6e}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -262370,46 +262389,46 @@
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{ed880428-f69d-4a89-b507-a1a761236c6e}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4C8E0B20-D07D-4FFA-A832-0E27A84AD24A}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -262424,46 +262443,46 @@
                 "Portland, ME",
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
+            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
+            "temporal": "2015-03-19/2015-03-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - Portland, ME - Greenspace Proximity Gradient"
         },
-            "identifier": "{4C8E0B20-D07D-4FFA-A832-0E27A84AD24A}",
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
-            "spatial": "-70.493457, 43.446672, -70.078404, 43.880517",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/PortlandME",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Portland, ME - Historic Places by Census Block Group",
```

