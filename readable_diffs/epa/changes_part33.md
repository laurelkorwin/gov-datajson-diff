# Change History for epa.json (Part 33)

### Changes from 31606f9 to dd2190f (Part 23/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-11-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4B2537E4-942C-4F94-B024-CC83CBE24F14}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -230274,46 +230293,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Impervious Proximity Gradient"
         },
-            "identifier": "{4B2537E4-942C-4F94-B024-CC83CBE24F14}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A5C3A6F2-CA61-4E78-B57D-289E45B34EF5}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -230328,46 +230347,46 @@
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
+            "spatial": "-93.889368, 41.442507, -93.348494, 41.778535",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{A5C3A6F2-CA61-4E78-B57D-289E45B34EF5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.889368, 41.442507, -93.348494, 41.778535",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 312 block groups in Des Moines, IA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 312 block groups in Des Moines, IA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B834A03C-90AF-4333-910E-D1165033D0E8}",
+            "issued": "2015-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -230386,46 +230405,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-09-09",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Ecosystem Services by Block Group"
         },
-            "identifier": "{B834A03C-90AF-4333-910E-D1165033D0E8}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-01-01/2015-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and agriculture. Forest is defined as Trees & Forest. Green space is defined as Trees & Forest, Grass & Herbaceous, and Agriculture. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, and agriculture. Forest is defined as Trees & Forest. Green space is defined as Trees & Forest, Grass & Herbaceous, and Agriculture. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FF40DDC0-76FC-449C-AF78-8E61FAF54AB4}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -230442,46 +230461,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Land Cover by Block Group"
         },
-            "identifier": "{FF40DDC0-76FC-449C-AF78-8E61FAF54AB4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "The Des Moines, IA EnviroAtlas Meter-Scale Urban Land Cover (MULC) Data were generated from the High Resolution Land Cover (HRLC) product created by the Iowa Department of Natural Resources (IDNR), consisting of data for Dallas, Polk, and Warren counties. The 14 class IDNR land cover product was modified to fit the land cover classification structure of the EPA EnviroAtlas resulting in six land cover classes mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment of 600 completely random and 90 stratified random points yielded an overall user's accuracy of 78% and an overall user's fuzzy accuracy of 85%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Des Moines, IA plus a 1 km buffer. This dataset was produced by the Iowa Department of Natural Resources and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Des Moines, IA -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The Des Moines, IA EnviroAtlas Meter-Scale Urban Land Cover (MULC) Data were generated from the High Resolution Land Cover (HRLC) product created by the Iowa Department of Natural Resources (IDNR), consisting of data for Dallas, Polk, and Warren counties. The 14 class IDNR land cover product was modified to fit the land cover classification structure of the EPA EnviroAtlas resulting in six land cover classes mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, and agriculture. An accuracy assessment of 600 completely random and 90 stratified random points yielded an overall user's accuracy of 78% and an overall user's fuzzy accuracy of 85%. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Des Moines, IA plus a 1 km buffer. This dataset was produced by the Iowa Department of Natural Resources and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A4152198-978D-4C0B-959F-42EABA9C4E1B}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -230504,46 +230523,46 @@
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
+            "spatial": "-93.911162, 41.433485, -93.332772, 41.787472",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Des Moines, IA -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{A4152198-978D-4C0B-959F-42EABA9C4E1B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.911162, 41.433485, -93.332772, 41.787472",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3C688DB4-B351-42F2-ADED-8A2C98A3AE3B}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -230562,46 +230581,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Near Road Tree Buffer"
         },
-            "identifier": "{3C688DB4-B351-42F2-ADED-8A2C98A3AE3B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{71273470-AFC8-4AAE-B334-072E921AD1CF}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -230620,46 +230639,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Near Road Block Group Summary"
         },
-            "identifier": "{71273470-AFC8-4AAE-B334-072E921AD1CF}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
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
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{56100C52-19B8-4BFE-88E4-F42CCB19E44F}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -230674,46 +230693,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Park Access by Block Group"
         },
-            "identifier": "{56100C52-19B8-4BFE-88E4-F42CCB19E44F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7BDA7EB9-C5F8-4C15-90A4-A3CB285671D9}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -230727,46 +230746,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Proximity to Parks"
         },
-            "identifier": "{7BDA7EB9-C5F8-4C15-90A4-A3CB285671D9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{2ED3979D-CBA0-45EF-A325-A148EC9EC64D}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -230784,46 +230803,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{2ED3979D-CBA0-45EF-A325-A148EC9EC64D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{09FE7D60-B636-405C-BB07-68147DFE8CAF}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -230841,46 +230860,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{09FE7D60-B636-405C-BB07-68147DFE8CAF}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. Forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. Forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{6867E66E-3395-44B5-91B0-7C09845BF069}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -230900,46 +230919,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{6867E66E-3395-44B5-91B0-7C09845BF069}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{B0A92F1E-0881-4A9F-99BB-3CB4AF0E1461}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -230959,46 +230978,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{B0A92F1E-0881-4A9F-99BB-3CB4AF0E1461}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. Forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. Forest is defined as Trees & Forest. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{870A2D00-9E04-41DF-9867-2C34214AF6D5}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -231018,46 +231037,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{870A2D00-9E04-41DF-9867-2C34214AF6D5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets)",
+            ],
+            "identifier": "{30E04D02-E660-42A0-B3C3-3C37D3936897}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -231077,46 +231096,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{30E04D02-E660-42A0-B3C3-3C37D3936897}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. Forest is defined as Trees & Forest. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. Forest is defined as Trees & Forest. Vegetated cover is defined as Trees & Forest and Grass & Herbaceous. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{842B3FD1-CF7C-4CFE-876A-554317CF32E4}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -231137,46 +231156,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{842B3FD1-CF7C-4CFE-876A-554317CF32E4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. Forest is defined as Trees & Forest. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{97B64205-0459-4B9B-9663-9401A86768B1}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -231194,46 +231213,46 @@
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{97B64205-0459-4B9B-9663-9401A86768B1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Des Moines, IA - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F2C570C2-BE3E-43B4-9FC3-1053CFFBDF7A}",
+            "issued": "2015-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -231249,46 +231268,46 @@
                 "Water",
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
+            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
+            "temporal": "2015-10-07/2015-10-07",
+            "theme": "environment",
+            "title": "EnviroAtlas - Des Moines, IA - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{F2C570C2-BE3E-43B4-9FC3-1053CFFBDF7A}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-93.8939549, 41.442507, -93.348494, 41.778535",
-            "temporal": "2015-10-07/2015-10-07",
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
+            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DesMoinesIA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2011 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3d578618-571f-476c-9f67-f8939df9fcfb}",
+            "issued": "2018-05-24",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -231352,46 +231371,46 @@
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
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2011 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{3d578618-571f-476c-9f67-f8939df9fcfb}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2018-05-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 2015 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9e5639f1-3089-4f27-a904-840fd5a35797}",
+            "issued": "2018-05-24",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -231455,46 +231474,46 @@
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
+            "temporal": "2015-01-01/2015-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2015 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{9e5639f1-3089-4f27-a904-840fd5a35797}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2015-01-01/2015-01-01",
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
+            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 2017 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes a number of Discharge Monitoring Report (DMR) metrics summarized by watershed for a given year (https://echo.epa.gov/help/loading-tool/watershed-statistics-help). These metrics include the number of facilities and wastewater discharges located within watersheds according to the Integrated Compliance Information System National Pollutant Discharge Elimination System (ICIS-NPDES), to track the permit compliance and enforcement status of facilities regulated by the NPDES under the Clean Water Act (https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{60e00df2-f4ee-47e2-abfe-722363d22e87}",
+            "issued": "2018-05-24",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -231558,46 +231577,46 @@
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
+            "temporal": "2017-01-01/2017-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 2017 EPA Discharge Monitoring Report Watershed Statistics by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{60e00df2-f4ee-47e2-abfe-722363d22e87}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2018-05-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 193 block groups in Durham, North Carolina. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 193 block groups in Durham, North Carolina. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8674FC78-EF42-49BC-8704-BDE65721D8D9}",
+            "issued": "2016-10-26",
             "keyword": [
                 "North Carolina",
                 "Exposure",
@@ -231617,46 +231636,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - BenMAP Results by Block Group"
         },
-            "identifier": "{8674FC78-EF42-49BC-8704-BDE65721D8D9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Durham, NC EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Durham, NC EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{FFCADD2D-FF08-4045-A2CB-30DB6762D51A}",
+            "issued": "2013-03-26",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -231669,46 +231688,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-03-26",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Block Groups"
         },
-            "identifier": "{FFCADD2D-FF08-4045-A2CB-30DB6762D51A}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2012-03-01/2012-03-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-03-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{B53F3963-9997-48AF-BDC5-0E769B0113CF}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Human",
@@ -231725,46 +231744,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Durham, NC - Demographics by Block Group"
         },
-            "identifier": "{B53F3963-9997-48AF-BDC5-0E769B0113CF}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset shows the boundary of the Durham, NC Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Durham, NC Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{777F7F2D-032E-4D90-93CD-0A598E7A5170}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -231777,46 +231796,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Atlas Area Boundary"
         },
-            "identifier": "{777F7F2D-032E-4D90-93CD-0A598E7A5170}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{C337BA5F-8275-4BA8-9647-F63C443F317D}",
+            "issued": "2015-05-20",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -231831,46 +231850,46 @@
                 "Durham, NC",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2015-03-03/2015-03-03",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{C337BA5F-8275-4BA8-9647-F63C443F317D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2015-03-03/2015-03-03",
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
+            "description": "As included in this EnviroAtlas dataset, the community domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also considered representative of local self-supplied water use. Specific to Durham, NC, the Division of Water Resources (DWR), part of the North Carolina Department of Natural Resources (NCDENR), has made local water supply plans centrally available online. All local governments are required to provide public water service. Community water systems with 1,000+ service connections or 3,000+ residents are required to prepare a local water supply plan. These plans include residential, also known as domestic, water usage. To account for variations due to weather, a ten-year average was calculated for Durham, Hillsborough, and the Orange Water and Sewer Authority (OWASA), which supplies southeast Orange County, including Chapel Hill and Carrboro. The ten-year average included available data between 2000 and 2010. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also considered representative of local self-supplied water use. Specific to Durham, NC, the Division of Water Resources (DWR), part of the North Carolina Department of Natural Resources (NCDENR), has made local water supply plans centrally available online. All local governments are required to provide public water service. Community water systems with 1,000+ service connections or 3,000+ residents are required to prepare a local water supply plan. These plans include residential, also known as domestic, water usage. To account for variations due to weather, a ten-year average was calculated for Durham, Hillsborough, and the Orange Water and Sewer Authority (OWASA), which supplies southeast Orange County, including Chapel Hill and Carrboro. The ten-year average included available data between 2000 and 2010. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9F3F4B02-1836-4472-913B-4357D3FA3535}",
+            "issued": "2016-08-11",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -231890,46 +231909,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{9F3F4B02-1836-4472-913B-4357D3FA3535}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{1B934FE7-DA12-4DBE-943E-A5448DF2836B}",
+            "issued": "2014-08-06",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -231945,46 +231964,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-06",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2012-04-20/2012-04-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{1B934FE7-DA12-4DBE-943E-A5448DF2836B}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2012-04-20/2012-04-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c8ba361b-85f8-4288-947f-f5df80181c3f}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -232008,46 +232027,46 @@
                 "Durham, NC",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{c8ba361b-85f8-4288-947f-f5df80181c3f}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest and Grass & Herbaceous. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{D3F797DB-7865-4E2C-A409-50F168EF355D}",
+            "issued": "2015-05-14",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232064,46 +232083,46 @@
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2015-03-18/2015-03-18",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Greenspace Proximity Gradient"
         },
-            "identifier": "{D3F797DB-7865-4E2C-A409-50F168EF355D}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2015-03-18/2015-03-18",
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
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{AA7BE287-4207-443C-889A-5B39B028D44C}",
+            "issued": "2014-08-26",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232119,46 +232138,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Historic Places by Census Block Group"
         },
-            "identifier": "{AA7BE287-4207-443C-889A-5B39B028D44C}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{315039B8-7682-40BB-9A71-BB04B75214A2}",
+            "issued": "2015-05-14",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232172,46 +232191,46 @@
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2015-03-25/2015-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Impervious Proximity Gradient"
         },
-            "identifier": "{315039B8-7682-40BB-9A71-BB04B75214A2}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AF794837-71B0-4B3F-AA95-996A9C19D8A6}",
+            "issued": "2019-06-19",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232226,46 +232245,46 @@
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
-            },
-            "identifier": "{AF794837-71B0-4B3F-AA95-996A9C19D8A6}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-79.16606, 35.86197, -78.77793, 36.12529",
             "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-19",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "EnviroAtlas - Durham, NC - Estimated Intersection Density of Walkable Roads"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 193 block groups in Durham, North Carolina. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 193 block groups in Durham, North Carolina. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{AA3CA642-7493-4391-BD8E-D361EC9F5D2D}",
+            "issued": "2015-06-18",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232284,46 +232303,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Ecosystem Services by Block Group"
         },
-            "identifier": "{AA3CA642-7493-4391-BD8E-D361EC9F5D2D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, wetland, and agriculture. Impervious is a combination of dark and light impervious. Green space is a combination of trees and forest and grass and herbaceous. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Land Cover Summaries by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, wetland, and agriculture. Impervious is a combination of dark and light impervious. Green space is a combination of trees and forest and grass and herbaceous. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{47B04639-1BEC-4CEA-9BF0-8392D946F53B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232340,46 +232359,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2012-04-04/2012-04-04",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Land Cover Summaries by Block Group"
         },
-            "identifier": "{47B04639-1BEC-4CEA-9BF0-8392D946F53B}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2012-04-04/2012-04-04",
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
+            "description": "The EnviroAtlas Durham, NC Meter-Scale Urban Land Cover (MULC) data was generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from July 2010 at 1 m spatial resolution. Five land cover classes were mapped: impervious surface, soil and barren, grass and herbaceous, trees and forest, and water. An accuracy assessment using a stratified random sampling of 500 samples yielded an overall accuracy of 83 percent using a minimum mapping unit of 9 pixels (3x3 pixel window). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Durham, and includes the cities of Durham, Chapel Hill, Carrboro and Hillsborough, NC. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Durham, NC -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The EnviroAtlas Durham, NC Meter-Scale Urban Land Cover (MULC) data was generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from July 2010 at 1 m spatial resolution. Five land cover classes were mapped: impervious surface, soil and barren, grass and herbaceous, trees and forest, and water. An accuracy assessment using a stratified random sampling of 500 samples yielded an overall accuracy of 83 percent using a minimum mapping unit of 9 pixels (3x3 pixel window). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Durham, and includes the cities of Durham, Chapel Hill, Carrboro and Hillsborough, NC. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2FF66877-A037-4693-9718-D1870AA3F084}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -232402,46 +232421,46 @@
                 "Communities",
                 "Durham, NC"
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-07-01/2010-07-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Durham, NC -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{2FF66877-A037-4693-9718-D1870AA3F084}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2010-07-01/2010-07-01",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{3F2450A1-F022-4769-B5BD-07E160DC981D}",
+            "issued": "2015-05-19",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232459,46 +232478,46 @@
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Near Road Tree Buffer"
         },
-            "identifier": "{3F2450A1-F022-4769-B5BD-07E160DC981D}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{F2AF286C-349C-46FF-B31D-5E0C51438B2B}",
+            "issued": "2015-05-19",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232518,46 +232537,46 @@
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Near Road Block Group Summary"
         },
-            "identifier": "{F2AF286C-349C-46FF-B31D-5E0C51438B2B}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{0ECF494E-DF62-44CC-B7DE-598899314D2D}",
+            "issued": "2015-11-10",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232572,46 +232591,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Park Access by Block Group"
         },
-            "identifier": "{0ECF494E-DF62-44CC-B7DE-598899314D2D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{38956084-2AB2-422C-B56D-068C8CA6AAFE}",
+            "issued": "2020-01-08",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232625,46 +232644,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Proximity to Parks"
         },
-            "identifier": "{38956084-2AB2-422C-B56D-068C8CA6AAFE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{5A797B3F-9BD8-4910-8789-4DDCDCF57233}",
+            "issued": "2015-12-02",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232682,46 +232701,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{5A797B3F-9BD8-4910-8789-4DDCDCF57233}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F341A26B-4972-4C6B-B675-9B5E02F4F25F}",
+            "issued": "2015-08-07",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232739,46 +232758,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{F341A26B-4972-4C6B-B675-9B5E02F4F25F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{6201C7D5-C28D-4065-A74C-E9047C4A20FC}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232798,46 +232817,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2013-03-21/2013-03-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{6201C7D5-C28D-4065-A74C-E9047C4A20FC}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2013-03-21/2013-03-21",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{9FB2E550-65E5-4A4B-9103-AF38ECFF9208}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232857,46 +232876,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2013-03-21/2013-03-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{9FB2E550-65E5-4A4B-9103-AF38ECFF9208}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2013-03-21/2013-03-21",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{7EE86539-98B8-42F5-AFA6-1279B3400CAD}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232916,46 +232935,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2013-03-25/2013-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{7EE86539-98B8-42F5-AFA6-1279B3400CAD}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2013-03-25/2013-03-25",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{16916F24-DE3C-41E1-A5B8-10459BB82C6E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -232975,46 +232994,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2013-03-21/2013-03-21",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{16916F24-DE3C-41E1-A5B8-10459BB82C6E}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2013-03-21/2013-03-21",
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
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{206329EB-D807-42FA-9668-E42C62F973F8}",
+            "issued": "2014-08-13",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -233035,46 +233054,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-13",
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2013-03-20/2013-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{206329EB-D807-42FA-9668-E42C62F973F8}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2013-03-20/2013-03-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{48AB84F3-1315-489C-9C56-1A026BBE125C}",
+            "issued": "2014-06-17",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -233092,46 +233111,46 @@
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
+            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
+            "temporal": "2014-06-10/2014-06-10",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{48AB84F3-1315-489C-9C56-1A026BBE125C}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-79.134618, 35.844552, -78.788325, 36.133857",
-            "temporal": "2014-06-10/2014-06-10",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Durham, NC - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1ac9e95f-5911-4462-90d0-23dd823ff2c0}",
+            "issued": "2017-05-31",
             "keyword": [
                 "North Carolina",
                 "Ecosystem Services",
@@ -233147,46 +233166,48 @@
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
+            "spatial": "-78.788325, 35.844552, -79.134618, 36.133857",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Durham, NC - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{1ac9e95f-5911-4462-90d0-23dd823ff2c0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-78.788325, 35.844552, -79.134618, 36.133857",
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
+            "description": "This map displays predicted probability of a 12-digit Hydrologic Unit (HUC12) being at risk of violating the drinking water nitrate standard. Risk is defined as there being greater than a 50% chance of having a drinking water violation. Observed violations of the nitrate standard in public drinking water was used to make predictions across the conterminous United States. The data on nitrate violations comes from the EPA's Safe Drinking Water Information System (SDWIS) and the data used as predictor variables in the prediction models comes from EPA's StreamCat database. The original predictions were made at the National Hydrography Dataset (NHD) Catchment scale and summarized at the HUC12 scale and/or 300 m pixel scale. The maps show that 19% of the conterminous United States is at risk of groundwater sourced drinking violations, while 16% of the U.S. is at risk of nitrate violations from surface water sources. Regions with the highest risk of nitrate drinking violations from groundwater sources are found in the southwest, south central plains, parts of north west, mid-Atlantic. Surface water sourced nitrate violations have the greatest risk primarily in the southwest and south-central areas of the U.S. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/DurhamNC",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Predicted drinking water nitrate violations by 12-Digit HUC for the Conterminous United States",
-            "description": "This map displays predicted probability of a 12-digit Hydrologic Unit (HUC12) being at risk of violating the drinking water nitrate standard. Risk is defined as there being greater than a 50% chance of having a drinking water violation. Observed violations of the nitrate standard in public drinking water was used to make predictions across the conterminous United States. The data on nitrate violations comes from the EPA's Safe Drinking Water Information System (SDWIS) and the data used as predictor variables in the prediction models comes from EPA's StreamCat database. The original predictions were made at the National Hydrography Dataset (NHD) Catchment scale and summarized at the HUC12 scale and/or 300 m pixel scale. The maps show that 19% of the conterminous United States is at risk of groundwater sourced drinking violations, while 16% of the U.S. is at risk of nitrate violations from surface water sources. Regions with the highest risk of nitrate drinking violations from groundwater sources are found in the southwest, south central plains, parts of north west, mid-Atlantic. Surface water sourced nitrate violations have the greatest risk primarily in the southwest and south-central areas of the U.S. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "7c44dad0-98aa-45ee-8011-4e3d2332c5c7",
+            "issued": "2020-12-29",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233252,46 +233273,44 @@
                 "Contaminant",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-31",
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
+            "spatial": "-128.028392, 22.734889, -65.203364, 51.67736",
+            "temporal": "2011-01-01T00:00:00/2011-12-31T00:00:00",
+            "title": "EnviroAtlas - Predicted drinking water nitrate violations by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "7c44dad0-98aa-45ee-8011-4e3d2332c5c7",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.028392, 22.734889, -65.203364, 51.67736",
-            "temporal": "2011-01-01T00:00:00/2011-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-12-29",
+            "description": "This EnviroAtlas dataset includes domestic water demand attributes which provide insight into the amount of water currently used for indoor and outdoor residential purposes in the contiguous United States. The values are based on 2010 water demand and 2010 population distribution, and have been summarized by subwatershed, or 12-digit hydrologic unit code (HUC12). For the purposes of this metric, domestic water use includes residential uses, such as for drinking, bathing, cleaning, landscaping, and pools. Depending on the location, domestic water can be self-supplied, such as by private wells, or publicly-supplied, such as by municipalities. Sources include surface water and groundwater. Estimates are for primary residences only (i.e., excluding second homes and tourism rentals). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Domestic Water Demand by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes domestic water demand attributes which provide insight into the amount of water currently used for indoor and outdoor residential purposes in the contiguous United States. The values are based on 2010 water demand and 2010 population distribution, and have been summarized by subwatershed, or 12-digit hydrologic unit code (HUC12). For the purposes of this metric, domestic water use includes residential uses, such as for drinking, bathing, cleaning, landscaping, and pools. Depending on the location, domestic water can be self-supplied, such as by private wells, or publicly-supplied, such as by municipalities. Sources include surface water and groundwater. Estimates are for primary residences only (i.e., excluding second homes and tourism rentals). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C6DBEBAB-03EF-43C8-8DCA-8D2845E06A96}",
+            "issued": "2015-12-15",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233355,46 +233374,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-15",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Domestic Water Demand by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{C6DBEBAB-03EF-43C8-8DCA-8D2845E06A96}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2015-12-15",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains indices of ecological integrity in the upstream catchments and watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Indices of Ecological Integrity of stream confluences for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains indices of ecological integrity in the upstream catchments and watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7e8ed032-dacf-42bd-8acc-5a79ba895382}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233454,46 +233473,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Indices of Ecological Integrity of stream confluences for the Conterminous United States"
         },
-            "identifier": "{7e8ed032-dacf-42bd-8acc-5a79ba895382}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset contains points depicting the location of market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets. Additional biodiversity data were obtained from the Regulatory In-lieu Fee and Bank Information Tracking System (RIBITS) database in 2015. Points represent the centroids (i.e., center points) of market coverage areas, project footprints, or project primary impact areas in which ecosystem service markets or projects operate. National-level markets are an exception to this norm with points representing administrative headquarters locations. Attribute data include information regarding the methodology, design, and development of biodiversity, carbon, and water markets and projects. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Ecosystem Service Market and Project Locations, U.S., 2015, Forest Trends' Ecosystem Marketplace",
-            "description": "This EnviroAtlas dataset contains points depicting the location of market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets. Additional biodiversity data were obtained from the Regulatory In-lieu Fee and Bank Information Tracking System (RIBITS) database in 2015. Points represent the centroids (i.e., center points) of market coverage areas, project footprints, or project primary impact areas in which ecosystem service markets or projects operate. National-level markets are an exception to this norm with points representing administrative headquarters locations. Attribute data include information regarding the methodology, design, and development of biodiversity, carbon, and water markets and projects. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{10C12176-4D56-44FF-94FC-F748B3AF2EE1}",
+            "issued": "2015-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233567,46 +233586,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-16",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2016-11-01/2016-11-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Ecosystem Service Market and Project Locations, U.S., 2015, Forest Trends' Ecosystem Marketplace"
         },
-            "identifier": "{10C12176-4D56-44FF-94FC-F748B3AF2EE1}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2016-11-01/2016-11-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains polygons depicting the geographic areas of market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. Depending upon the type of market or project and data availability, polygons reflect market coverage areas, project footprints, or project primary impact areas in which ecosystem service markets and projects operate. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets. Additional biodiversity data were obtained from the Regulatory In-lieu Fee and Bank Information Tracking System (RIBITS) database in 2015. Attribute data include information regarding the methodology, design, and development of biodiversity, carbon, and water markets and projects. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Ecosystem Service Market and Project Areas, U.S., 2015, Forest Trends' Ecosystem Marketplace",
-            "description": "This EnviroAtlas dataset contains polygons depicting the geographic areas of market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. Depending upon the type of market or project and data availability, polygons reflect market coverage areas, project footprints, or project primary impact areas in which ecosystem service markets and projects operate. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets. Additional biodiversity data were obtained from the Regulatory In-lieu Fee and Bank Information Tracking System (RIBITS) database in 2015. Attribute data include information regarding the methodology, design, and development of biodiversity, carbon, and water markets and projects. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E1E8576C-BAB7-4EC2-8541-E47271FCA5AD}",
+            "issued": "2015-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233680,46 +233699,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-16",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2016-11-01/2016-11-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Ecosystem Service Market and Project Areas, U.S., 2015, Forest Trends' Ecosystem Marketplace"
         },
-            "identifier": "{E1E8576C-BAB7-4EC2-8541-E47271FCA5AD}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2016-11-01/2016-11-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains polygons depicting conditions enabling market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. Polygons represent the area in which a particular condition, policy, or regulation is implemented with the result of direct or indirect facilitation of a market-based approach to investing in and protecting biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and/or water ecosystem services. The data were collected via desk research conducted by Forest Trends' Ecosystem Marketplace during 2015-2016. Attribute data include the ecosystem service(s) of interest, year established, design mechanisms(s) employed, and the regulatory authority associated with a particular condition. This dataset was produced by Forest Trends' Ecosystem Marketplace for Enviroatlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Ecosystem Service Market and Project Enabling Conditions, U.S., 2016, Forest Trends' Ecosystem Marketplace",
-            "description": "This EnviroAtlas dataset contains polygons depicting conditions enabling market-based programs, referred to herein as markets, and projects addressing ecosystem services protection in the United States. Polygons represent the area in which a particular condition, policy, or regulation is implemented with the result of direct or indirect facilitation of a market-based approach to investing in and protecting biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and/or water ecosystem services. The data were collected via desk research conducted by Forest Trends' Ecosystem Marketplace during 2015-2016. Attribute data include the ecosystem service(s) of interest, year established, design mechanisms(s) employed, and the regulatory authority associated with a particular condition. This dataset was produced by Forest Trends' Ecosystem Marketplace for Enviroatlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2D652B59-89E4-484F-A960-0C6A7690E143}",
+            "issued": "2015-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233791,46 +233810,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-16",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2015-09-01/2015-09-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Ecosystem Service Market and Project Enabling Conditions, U.S., 2016, Forest Trends' Ecosystem Marketplace"
         },
-            "identifier": "{2D652B59-89E4-484F-A960-0C6A7690E143}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2015-09-01/2015-09-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains polygons depicting the number of watershed-level market-based programs, referred to herein as markets, in operation per 8-digit HUC watershed throughout the United States. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace during 2014 regarding markets operating to protect watershed ecosystem services. Utilizing these data, the number of water market coverage areas overlaying each HUC8 watershed were calculated to produce this dataset. Only water markets identified as operating at the watershed level (i.e., single or multiple watersheds define the market boundaries) were included in the count of water markets per HUC8 watershed. Excluded were water markets operating at the national, state, county, or federal lands level and all water projects. Attribute data include the watershed's 8-digit hydrologic unit code and name, in addition to the watershed-level water market count associated with the watershed. This dataset was produced by Forest Trends' Ecosystem Marketplace to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Number of Water Markets per HUC8 Watershed, U.S., 2015, Forest Trends' Ecosystem Marketplace",
-            "description": "This EnviroAtlas dataset contains polygons depicting the number of watershed-level market-based programs, referred to herein as markets, in operation per 8-digit HUC watershed throughout the United States. The data were collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace during 2014 regarding markets operating to protect watershed ecosystem services. Utilizing these data, the number of water market coverage areas overlaying each HUC8 watershed were calculated to produce this dataset. Only water markets identified as operating at the watershed level (i.e., single or multiple watersheds define the market boundaries) were included in the count of water markets per HUC8 watershed. Excluded were water markets operating at the national, state, county, or federal lands level and all water projects. Attribute data include the watershed's 8-digit hydrologic unit code and name, in addition to the watershed-level water market count associated with the watershed. This dataset was produced by Forest Trends' Ecosystem Marketplace to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B6A72AB0-2DF1-42F4-BD45-0C046FF69F62}",
+            "issued": "2015-12-16",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -233899,46 +233918,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-12-16",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2015-06-01/2015-06-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Number of Water Markets per HUC8 Watershed, U.S., 2015, Forest Trends' Ecosystem Marketplace"
         },
-            "identifier": "{B6A72AB0-2DF1-42F4-BD45-0C046FF69F62}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2015-06-01/2015-06-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-12-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service contains layers depicting market-based programs and projects addressing ecosystem services protection in the United States. Layers include data collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets and enabling conditions that facilitate, directly or indirectly, market-based approaches to protecting and investing in those ecosystem services. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Ecosystem Services Market-Based Programs Web Service, U.S., 2016, Forest Trends' Ecosystem Marketplace",
-            "description": "This EnviroAtlas web service contains layers depicting market-based programs and projects addressing ecosystem services protection in the United States. Layers include data collected via surveys and desk research conducted by Forest Trends' Ecosystem Marketplace from 2008 to 2016 on biodiversity (i.e., imperiled species/habitats; wetlands and streams), carbon, and water markets and enabling conditions that facilitate, directly or indirectly, market-based approaches to protecting and investing in those ecosystem services. This dataset was produced by Forest Trends' Ecosystem Marketplace for EnviroAtlas in order to support public access to and use of information related to environmental markets. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e1c4e0d2-6612-4fb1-a0c7-74672a2c6895}",
+            "issued": "2017-02-17",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234014,46 +234033,46 @@
                 "Alaska",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-02-17",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
+            "temporal": "2015-06-01/2015-06-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Ecosystem Services Market-Based Programs Web Service, U.S., 2016, Forest Trends' Ecosystem Marketplace"
         },
-            "identifier": "{e1c4e0d2-6612-4fb1-a0c7-74672a2c6895}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
-            "temporal": "2015-06-01/2015-06-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-02-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset identifies rare ecosystems using base landcover data from the USGS GAP Analysis Program (Version 2, 2011) combined with landscape ecology principles. The metrics included in this data set identify total rare acres and the protected rare acres within each 12-digit Hydrologic Unit (HUC). The percentage of the terrestrial area of each HUC covered by rare ecosystems as well as the percent of rare acres that are protected are also included. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Ecosystem Rarity Metrics by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset identifies rare ecosystems using base landcover data from the USGS GAP Analysis Program (Version 2, 2011) combined with landscape ecology principles. The metrics included in this data set identify total rare acres and the protected rare acres within each 12-digit Hydrologic Unit (HUC). The percentage of the terrestrial area of each HUC covered by rare ecosystems as well as the percent of rare acres that are protected are also included. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5E591817-C13D-498A-BA0D-F3D28D986324}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234124,46 +234143,42 @@
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
-            },
-            "identifier": "{5E591817-C13D-498A-BA0D-F3D28D986324}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-128.02839229, 22.7348894, -65.20336449, 51.6773602",
             "temporal": "2013-02-05/2013-02-05",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-07",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "EnviroAtlas - Ecosystem Rarity Metrics by 12-digit HUC for the Conterminous United States"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EJ and Impervious Cover",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
             "description": "Geographic analysis of impervious cover and demographic attributes by 2010 Census block group. Demographic attributes and Census block groups were downloaded from the EJScreen web page (www.epa.gov/ejscreen). EJScreen technical documentation is available at website; click on the technical information link on the landing page; the link of the documentation is in the center of the web page.  NLCD2019 data for impervious cover were downloaded from www.mrlc.gov.  The impervious cover for 2001 and 2019 in the NLCD2019 database were used in the analysis.  The Census block groups downloaded from EJScreen were projected into Albers Conic Equal Area to match the NLCD2019 projection (Albers Conic Equal Area: central meridian=96.0 W; origin latitude=23.0 N; false easting=0.0; false northing=0.0; standard parallel 1=29.5 N; standard parallel 2=49.5 N; Geographic coordinate system=WGS84; WKID=4326) .\n\t\t",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/EJ_IC.zip"
+                }
+            ],
+            "identifier": "9e1265d8-13c1-4563-a867-20a300aa6987",
+            "issued": "2023-01-09",
             "keyword": [
                 "020:072",
                 "010",
@@ -234182,39 +234197,43 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-01-09",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, Center for Public Health and Environmental Assessment"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "James Wickham",
-                "hasEmail": "mailto:wickham.james@epa.gov"
+            "spatial": "-127.700452, 23.360434, -66.103258, 51.42191",
+            "temporal": "2020-11-25T00:00:00/None",
+            "title": "EJ and Impervious Cover"
         },
-            "identifier": "9e1265d8-13c1-4563-a867-20a300aa6987",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.700452, 23.360434, -66.103258, 51.42191",
-            "temporal": "2020-11-25T00:00:00/None",
-            "issued": "2023-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
+            "description": "This EnviroAtlas dataset shows the employment rate, or the percent of the population aged 16-64 who have worked in the past 12 months. The employment rate is a measure of the percent of the working-age population who are employed. It is an indicator of the prevalence of unemployment, which is often used to assess labor market conditions by economists. It is a widely used metric to evaluate the sustainable development of communities (NRC, 2011, UNECE, 2009). This dataset is based on the American Community Survey 5-year data for 2008-2012. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/public/ORD/EnviroAtlas/EJ_IC.zip"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Percentage of Working Age Population Who Are Employed by Block Group for the Conterminous United States",
-            "description": "This EnviroAtlas dataset shows the employment rate, or the percent of the population aged 16-64 who have worked in the past 12 months. The employment rate is a measure of the percent of the working-age population who are employed. It is an indicator of the prevalence of unemployment, which is often used to assess labor market conditions by economists. It is a widely used metric to evaluate the sustainable development of communities (NRC, 2011, UNECE, 2009). This dataset is based on the American Community Survey 5-year data for 2008-2012. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9A23AC68-7B13-4F79-B01C-D4679B75308D}",
+            "issued": "2015-06-09",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234278,46 +234297,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2008-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Percentage of Working Age Population Who Are Employed by Block Group for the Conterminous United States"
         },
-            "identifier": "{9A23AC68-7B13-4F79-B01C-D4679B75308D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2008-01-01/2012-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset intelligently reallocates 2010 population from census blocks to 30 meter pixels based on land cover and slope. Used for metrics that require population to be spatially allocated at a pixel level, primarily in the urban section of the atlas. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Dasymetric Population in the Conterminous United States Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset intelligently reallocates 2010 population from census blocks to 30 meter pixels based on land cover and slope. Used for metrics that require population to be spatially allocated at a pixel level, primarily in the urban section of the atlas. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{988BD6D1-CD27-4D67-BF44-F9AEDD83D9B8}",
+            "issued": "2013-05-30",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234387,46 +234406,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-30",
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
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Dasymetric Population in the Conterminous United States Web Service"
         },
-            "identifier": "{988BD6D1-CD27-4D67-BF44-F9AEDD83D9B8}",
+        {
+            "@type": "dcat:Dataset",
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
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-05-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service includes maps that illustrate factors affecting transit accessibility, and indicators of accessibility. Accessibility measures how easily people can reach destinations such as their workplaces and can be measured in terms of both time and distance. It is affected by factors such as the proximity of housing to jobs, transit stops, stores, and services; the availability of various transit modes; and land use patterns. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Accessibility Characteristics in the Conterminous U.S. Web Service",
-            "description": "This EnviroAtlas web service includes maps that illustrate factors affecting transit accessibility, and indicators of accessibility. Accessibility measures how easily people can reach destinations such as their workplaces and can be measured in terms of both time and distance. It is affected by factors such as the proximity of housing to jobs, transit stops, stores, and services; the availability of various transit modes; and land use patterns. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{670e195f-b629-48c9-aa94-1ec06cda2bca}",
+            "issued": "2015-06-09",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234490,46 +234509,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Accessibility Characteristics in the Conterminous U.S. Web Service"
         },
-            "identifier": "{670e195f-b629-48c9-aa94-1ec06cda2bca}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service includes maps that illustrate population and residential activity in each census block group as well as residential-location-based socioeconomic variables. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Population and Residential Activity in the Conterminous U.S. Web Service",
-            "description": "This EnviroAtlas web service includes maps that illustrate population and residential activity in each census block group as well as residential-location-based socioeconomic variables. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{62075a6a-2339-47a6-be3a-6845159001ae}",
+            "issued": "2015-06-09",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234593,46 +234612,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Population and Residential Activity in the Conterminous U.S. Web Service"
         },
-            "identifier": "{62075a6a-2339-47a6-be3a-6845159001ae}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service includes maps that illustrate job activity in each census block group. Employment diversity, employment density, and proximity of employment to housing can affect commuting patterns. Having plentiful and diverse jobs located near housing can reduce commute time and allow for a greater variety of commute modes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Employment Activity in the Conterminous U.S. Web Service",
-            "description": "This EnviroAtlas web service includes maps that illustrate job activity in each census block group. Employment diversity, employment density, and proximity of employment to housing can affect commuting patterns. Having plentiful and diverse jobs located near housing can reduce commute time and allow for a greater variety of commute modes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c75b6623-5d47-498f-a50a-dae83e0e4363}",
+            "issued": "2015-06-09",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234696,46 +234715,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Employment Activity in the Conterminous U.S. Web Service"
         },
-            "identifier": "{c75b6623-5d47-498f-a50a-dae83e0e4363}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service includes maps that illustrate the number and density of housing units. Housing density and the proximity of housing to employment can affect commuting patterns. Housing located near jobs can reduce commute time and allow for a greater variety of commute modes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Housing in the Conterminous U.S. Web Service",
-            "description": "This EnviroAtlas web service includes maps that illustrate the number and density of housing units. Housing density and the proximity of housing to employment can affect commuting patterns. Housing located near jobs can reduce commute time and allow for a greater variety of commute modes. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9ea5e3e1-0964-4a94-914c-01ecce4e3b94}",
+            "issued": "2015-06-09",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234799,46 +234818,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-06-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Housing in the Conterminous U.S. Web Service"
         },
-            "identifier": "{9ea5e3e1-0964-4a94-914c-01ecce4e3b94}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-06-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). The EnviroAtlas Potentially Restorable Wetlands on Agricultural Land (PRW-Ag) dataset shows potentially restorable wetlands at 30-meter resolution. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potentially restorable wetlands, as developed for this map, are lands currently in agriculture that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Potentially Restorable Wetlands on Agricultural Land - Contiguous United States Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). The EnviroAtlas Potentially Restorable Wetlands on Agricultural Land (PRW-Ag) dataset shows potentially restorable wetlands at 30-meter resolution. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potentially restorable wetlands, as developed for this map, are lands currently in agriculture that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{994C0DD5-3EFB-403F-84B4-3FDE1EC16ED5}",
+            "issued": "2016-03-08",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234899,46 +234918,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-03-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Potentially Restorable Wetlands on Agricultural Land - Contiguous United States Web Service"
         },
-            "identifier": "{994C0DD5-3EFB-403F-84B4-3FDE1EC16ED5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2016-03-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). The EnviroAtlas Potential Wetland Areas (PWA) dataset shows potential wetland areas at 30-meter resolution. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potential wetland areas, as developed for this map, are lands that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Potential Wetland Areas - Contiguous United States Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). The EnviroAtlas Potential Wetland Areas (PWA) dataset shows potential wetland areas at 30-meter resolution. Beginning two centuries ago, many wetlands were turned into farm fields or urban areas, yet wetlands play an important role in removing water pollution, regulating water storage and flows, and providing habitat for wildlife. Wetland restoration could help restore these benefits. Potential wetland areas, as developed for this map, are lands that naturally accumulate water due to topography and have historically had poorly or very poorly draining soils. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D8C16461-4057-412C-994E-98C12033CB96}",
+            "issued": "2016-03-08",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -234999,46 +235018,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-03-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Potential Wetland Areas - Contiguous United States Web Service"
         },
-            "identifier": "{D8C16461-4057-412C-994E-98C12033CB96}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2016-03-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset identifies rare ecosystems using base landcover data from the USGS GAP Analysis Program (Version 2, 2011) combined with landscape ecology principles. This raster dataset represents an index of rarity ranging from 0 (common) to 100 (rare). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Rare Ecosystems in the Conterminous United States Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). This EnviroAtlas dataset identifies rare ecosystems using base landcover data from the USGS GAP Analysis Program (Version 2, 2011) combined with landscape ecology principles. This raster dataset represents an index of rarity ranging from 0 (common) to 100 (rare). EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FD683594-C5DB-428F-880B-B454A3CAE2B0}",
+            "issued": "2013-05-21",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -235117,46 +235136,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-05-21",
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
+            "temporal": "2013-02-06/2013-02-06",
+            "theme": "environment",
+            "title": "EnviroAtlas - Rare Ecosystems in the Conterminous United States Web Service"
         },
-            "identifier": "{FD683594-C5DB-428F-880B-B454A3CAE2B0}",
+        {
+            "@type": "dcat:Dataset",
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
-            "temporal": "2013-02-06/2013-02-06",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2013-05-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "Understanding the relationship between flood inundation and floodplains is critical for ecosystem and community health and well-being, as well as targeting floodplain and riparian restoration. Many communities in the United States, particularly those in rural areas, lack inundation maps due to the high cost of flood modeling. Only 60% of the conterminous United States has Flood Insurance Rate Maps (FIRMs) through the U.S. Federal Emergency Management Agency (FEMA). This EnviroAtlas dataset provides an estimate of the 100-year floodplain for the conterminous United States at 30-meter resolution to fill the gaps in the FIRM. The model hit rate for the CONUS was 0.79 compared to the FIRM, indicating that the model captured 79% of the 100-year floodplain identified by FEMA. This product provides complete coverage for the CONUS by identifying floodplains in areas without FIRMs, while also identifying floodplains in tributaries sometimes excluded by FEMA. More information can be found in the journal article (https://doi.org/10.1016/j.scitotenv.2018.07.353). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Estimated floodplain map for the Conterminous United States",
-            "description": "Understanding the relationship between flood inundation and floodplains is critical for ecosystem and community health and well-being, as well as targeting floodplain and riparian restoration. Many communities in the United States, particularly those in rural areas, lack inundation maps due to the high cost of flood modeling. Only 60% of the conterminous United States has Flood Insurance Rate Maps (FIRMs) through the U.S. Federal Emergency Management Agency (FEMA). This EnviroAtlas dataset provides an estimate of the 100-year floodplain for the conterminous United States at 30-meter resolution to fill the gaps in the FIRM. The model hit rate for the CONUS was 0.79 compared to the FIRM, indicating that the model captured 79% of the 100-year floodplain identified by FEMA. This product provides complete coverage for the CONUS by identifying floodplains in areas without FIRMs, while also identifying floodplains in tributaries sometimes excluded by FEMA. More information can be found in the journal article (https://doi.org/10.1016/j.scitotenv.2018.07.353). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4c37f02a-0c91-49b2-b7df-82ea4a6b9750}",
+            "issued": "2018-08-27",
             "keyword": [
                 "Connecticut",
                 "Exposure",
@@ -235220,46 +235239,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-08-27",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2018-06-04/2018-06-04",
+            "theme": "climatologyMeteorologyAtmosphere",
+            "title": "EnviroAtlas - Estimated floodplain map for the Conterminous United States"
         },
-            "identifier": "{4c37f02a-0c91-49b2-b7df-82ea4a6b9750}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2018-06-04/2018-06-04",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-08-27",
-            "language": "en-us",
-            "theme": "climatologyMeteorologyAtmosphere",
+            "description": "This EnviroAtlas dataset contains a count of the number of local farmers markets within each census block group (CBG) based on their location given within the USDA National Farmers Market Directory (https://www.ams.usda.gov/local-food-directories/farmersmarkets). This data has been processed from the original directory to remove duplicate locations, as well as a small subsample (25 markets) were corrected by hand in order avoid duplication across block group boundaries. This dataset is contemporary as of 5/20/2016, and downloaded from the USDA Agricultural Marketing Service (AMS) website. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Availability of Local Food by Census Block Group for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains a count of the number of local farmers markets within each census block group (CBG) based on their location given within the USDA National Farmers Market Directory (https://www.ams.usda.gov/local-food-directories/farmersmarkets). This data has been processed from the original directory to remove duplicate locations, as well as a small subsample (25 markets) were corrected by hand in order avoid duplication across block group boundaries. This dataset is contemporary as of 5/20/2016, and downloaded from the USDA Agricultural Marketing Service (AMS) website. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{00cafb6e-770d-4afa-9ed5-de95a831e0d8}",
+            "issued": "2018-10-23",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -235324,46 +235343,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-10-23",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2016-05-20/2018-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Availability of Local Food by Census Block Group for the Conterminous United States"
         },
-            "identifier": "{00cafb6e-770d-4afa-9ed5-de95a831e0d8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2016-05-20/2018-07-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-10-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains a count of the number of local farmers markets within each subwatershed (12-digit HUC) based on their location given within the USDA National Farmers Market Directory (https://www.ams.usda.gov/local-food-directories/farmersmarkets). This data has been processed from the original directory to remove duplicate locations, as well as a small subsample (25 markets) were corrected by hand in order avoid duplication across block group boundaries. This dataset is contemporary as of 5/20/2016, and downloaded from the USDA Agricultural Marketing Service (AMS) website. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Availability of Local Food by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains a count of the number of local farmers markets within each subwatershed (12-digit HUC) based on their location given within the USDA National Farmers Market Directory (https://www.ams.usda.gov/local-food-directories/farmersmarkets). This data has been processed from the original directory to remove duplicate locations, as well as a small subsample (25 markets) were corrected by hand in order avoid duplication across block group boundaries. This dataset is contemporary as of 5/20/2016, and downloaded from the USDA Agricultural Marketing Service (AMS) website. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{30136338-174b-46f6-aa6d-a014e0391c8b}",
+            "issued": "2018-10-23",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -235428,46 +235447,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-10-23",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2016-05-20/2018-07-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Availability of Local Food by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{30136338-174b-46f6-aa6d-a014e0391c8b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2016-05-20/2018-07-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-10-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 405 block groups in Fresno, California. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 405 block groups in Fresno, California. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{736EE126-C066-482D-9CE8-A412693A70E9}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -235487,46 +235506,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - BenMAP Results by Block Group"
         },
-            "identifier": "{736EE126-C066-482D-9CE8-A412693A70E9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Fresno, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Fresno, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{46061103-98CF-49DB-87F6-9F05D9DE2762}",
+            "issued": "2014-07-09",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235539,46 +235558,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-09/2014-04-09",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Block Groups"
         },
-            "identifier": "{46061103-98CF-49DB-87F6-9F05D9DE2762}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-09/2014-04-09",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{958E8716-A21E-4700-A559-6F1120392869}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -235595,46 +235614,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Fresno, CA - Demographics by Block Group"
         },
-            "identifier": "{958E8716-A21E-4700-A559-6F1120392869}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the boundary of the Fresno, CA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Fresno, CA Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6185ECB8-CC77-4860-8A76-1B23A5AAF48D}",
+            "issued": "2014-05-01",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235647,46 +235666,46 @@
                 "Environmental Atlas",
                 "Boundaries"
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2013-04-09/2013-04-09",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Atlas Area Boundary"
         },
-            "identifier": "{6185ECB8-CC77-4860-8A76-1B23A5AAF48D}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2013-04-09/2013-04-09",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is only trees & forest. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{84B98749-9C1C-4679-AE24-9B9C0998EBA5}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235701,46 +235720,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{84B98749-9C1C-4679-AE24-9B9C0998EBA5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Fresno, CA, urban water management plan data is available through the California Department of Water Resources (CADWR). Suppliers that provide over 3,000 acre-feet or serve more than 3,000 connections are required to evaluate future water supplies and implement plans to reduce 2010 baseline consumption by 20% by 2020. Within the EnviroAtlas Fresno study area, there are two service providers, City of Fresno and City of Clovis, with baseline 2010 water use estimates of 313 and 249 GPD respectively. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Domestic Water Demand per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Fresno, CA, urban water management plan data is available through the California Department of Water Resources (CADWR). Suppliers that provide over 3,000 acre-feet or serve more than 3,000 connections are required to evaluate future water supplies and implement plans to reduce 2010 baseline consumption by 20% by 2020. Within the EnviroAtlas Fresno study area, there are two service providers, City of Fresno and City of Clovis, with baseline 2010 water use estimates of 313 and 249 GPD respectively. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6B64B355-3589-48AC-AF12-20F38D747D5B}",
+            "issued": "2016-08-11",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235760,46 +235779,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Domestic Water Demand per Day by U.S. Census Block Group"
         },
-            "identifier": "{6B64B355-3589-48AC-AF12-20F38D747D5B}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4A1239EC-FA85-41FF-94B3-12DD5F7D6CE6}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235815,46 +235834,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{4A1239EC-FA85-41FF-94B3-12DD5F7D6CE6}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
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
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{88f9659b-6c60-4665-b46d-ccda25924c7e}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -235878,46 +235897,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.5072999, 36.968864",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{88f9659b-6c60-4665-b46d-ccda25924c7e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.5072999, 36.968864",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, and Orchards. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, and Orchards. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D85DE191-9A4E-4559-9542-EBFAC5F9B191}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235932,46 +235951,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2015-03-20/2015-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Greenspace Proximity Gradient"
         },
-            "identifier": "{D85DE191-9A4E-4559-9542-EBFAC5F9B191}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2015-03-20/2015-03-20",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{57C0EA7C-52A2-4F5D-A638-C0E36990BA98}",
+            "issued": "2014-09-16",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -235987,46 +236006,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Historic Places by Census Block Group"
         },
-            "identifier": "{57C0EA7C-52A2-4F5D-A638-C0E36990BA98}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8864D0B8-A3FB-45C4-AAD9-C7359D3BB578}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236040,46 +236059,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2015-03-25/2015-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Impervious Proximity Gradient"
         },
-            "identifier": "{8864D0B8-A3FB-45C4-AAD9-C7359D3BB578}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0D3E33D1-81C5-456E-A581-58049701ACED}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236094,46 +236113,46 @@
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
+            "spatial": "-119.98725, 36.616154, -119.50730, 36.968864",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{0D3E33D1-81C5-456E-A581-58049701ACED}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.98725, 36.616154, -119.50730, 36.968864",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 405 block groups in Fresno, California. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 405 block groups in Fresno, California. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A101F058-B7A7-4E0C-85D7-B0ACCC5B0D90}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -236152,46 +236171,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Ecosystem Services by Block Group"
         },
-            "identifier": "{A101F058-B7A7-4E0C-85D7-B0ACCC5B0D90}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest and Orchards. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, and Orchards. Agriculture is defined as Agriculture and Orchards. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest and Orchards. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, and Orchards. Agriculture is defined as Agriculture and Orchards. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{95EA4EB8-8403-4DD5-B8D0-32C831938098}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236207,46 +236226,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Land Cover by Block Group"
         },
-            "identifier": "{95EA4EB8-8403-4DD5-B8D0-32C831938098}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Fresno, CA EnviroAtlas Meter-Scale Urban Land Cover (MULC) Data were generated via supervised classification of combined aerial photography and LiDAR data. The air photos were United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1-m spatial resolution. Aerial photography ('imagery') was collected on multiple dates in summer 2010. Seven land cover classes were mapped: Water, impervious surfaces (Impervious), soil and barren (Soil), trees and forest (Tree), and grass and herbaceous non-woody vegetation (Grass), agriculture (Ag), and Orchards. An accuracy assessment of 500 completely random and 103 stratified random points yielded an overall user's accuracy (MAX) of 81.1 percent and a fuzzy user's accuracy (RIGHT) of 86.9 (see below). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Fresno, CA plus a 1-km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Fresno, California -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The Fresno, CA EnviroAtlas Meter-Scale Urban Land Cover (MULC) Data were generated via supervised classification of combined aerial photography and LiDAR data. The air photos were United States Department of Agriculture (USDA) National Agricultural Imagery Program (NAIP) four band (red, green, blue, and near infrared) aerial photography at 1-m spatial resolution. Aerial photography ('imagery') was collected on multiple dates in summer 2010. Seven land cover classes were mapped: Water, impervious surfaces (Impervious), soil and barren (Soil), trees and forest (Tree), and grass and herbaceous non-woody vegetation (Grass), agriculture (Ag), and Orchards. An accuracy assessment of 500 completely random and 103 stratified random points yielded an overall user's accuracy (MAX) of 81.1 percent and a fuzzy user's accuracy (RIGHT) of 86.9 (see below). The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Fresno, CA plus a 1-km buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{87041CF3-05BC-43C3-82DA-F066267C9871}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "California",
@@ -236269,46 +236288,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Fresno, California -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{87041CF3-05BC-43C3-82DA-F066267C9871}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Orchards. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Orchards. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D8060C78-A6DE-43E7-B119-E6822489BFF6}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236326,46 +236345,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Near Road Tree Buffer"
         },
-            "identifier": "{D8060C78-A6DE-43E7-B119-E6822489BFF6}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Orchards. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Orchards. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{08BF6A10-ACE5-4485-BFE1-F941C3614D22}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236385,46 +236404,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Near Road Block Group Summary"
         },
-            "identifier": "{08BF6A10-ACE5-4485-BFE1-F941C3614D22}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{690458F0-D39F-44F7-B129-C972EE09FDFC}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236439,46 +236458,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.5072999, 36.968864",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Park Access by Block Group"
         },
-            "identifier": "{690458F0-D39F-44F7-B129-C972EE09FDFC}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.5072999, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5D957C70-5A37-48A6-B7D4-1E304710417F}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236492,46 +236511,46 @@
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
+            "title": "EnviroAtlas - Fresno, CA - Proximity to Parks"
         },
-            "identifier": "{5D957C70-5A37-48A6-B7D4-1E304710417F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{BB50BF0D-935F-440F-B636-6DD3D1018EDE}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236549,46 +236568,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{BB50BF0D-935F-440F-B636-6DD3D1018EDE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B71334B9-C53A-4674-A739-1031969E5163}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236606,46 +236625,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{B71334B9-C53A-4674-A739-1031969E5163}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5CE0686B-A793-49F1-8E32-1409F96BDD42}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236665,46 +236684,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{5CE0686B-A793-49F1-8E32-1409F96BDD42}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3BF28BB1-D669-4A91-9D4B-7A5D92F36B90}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236724,46 +236743,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{3BF28BB1-D669-4A91-9D4B-7A5D92F36B90}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{51D9FA33-4FB2-401C-BB8F-EBC865C04B92}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236783,46 +236802,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{51D9FA33-4FB2-401C-BB8F-EBC865C04B92}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2D474841-C677-4466-95F1-F8E9FF4EC7CD}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236842,46 +236861,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{2D474841-C677-4466-95F1-F8E9FF4EC7CD}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6DD8093C-178C-4606-9004-0731974643F4}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236902,46 +236921,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-04-30/2014-04-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{6DD8093C-178C-4606-9004-0731974643F4}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-04-30/2014-04-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas ) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{1DDD75AC-3545-47DC-8FC7-EA2C810028D5}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -236959,46 +236978,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-06-25/2014-06-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{1DDD75AC-3545-47DC-8FC7-EA2C810028D5}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-06-25/2014-06-25",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Fresno, CA - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1EEAE107-0B7E-4436-917E-E0F1BC82601F}",
+            "issued": "2014-07-25",
             "keyword": [
                 "Ecosystem Services",
                 "Fresno, CA",
@@ -237014,46 +237033,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-07-25",
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2014-06-25/2014-06-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Fresno, CA - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{1EEAE107-0B7E-4436-917E-E0F1BC82601F}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
-            "temporal": "2014-06-25/2014-06-25",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-07-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains data on the mean synthetic nitrogen (N) fertilizer application to cultivated crop and hay/pasture lands per 12-digit Hydrologic Unit (HUC) in 2006. Synthetic N fertilizer inputs in 2006 were estimated using county-level estimates of farm N fertilizer inputs. We acquired county-level data describing total farm-level inputs (kg N/yr) of synthetic N fertilizer to individual counties in 2006 from the United States Geological Survey (USGS) (http://pubs.usgs.gov/sir/2012/5207/). These data were converted to per area rates (kg N/ha/yr) of synthetic N fertilizer application by dividing the total N input by the land area (ha) of combined cultivated crop and hay/pasture lands within a county as determined from county-level (http://cta.ornl.gov/transnet/Boundaries.html) summarization of the 2006 National Land Cover Database (NLCD; http://www.mrlc.gov/nlcd06_data.php). We distributed county-specific, annual per area N inputs rates (kg N/ha/yr) to cultivated crop and hay/pasture lands (30 x 30 m pixels) within the corresponding county using the raster calculator tool in ArcMap 10.0 (ESRI, Inc., Redlands, CA). Fertilizer data described here represent an average input to a typical agricultural land type within a county, i.e., they are not specific to individual crop types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/FresnoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Synthetic N fertilizer application to agricultural lands by 12-digit HUC in the Conterminous United States, 2006",
-            "description": "This EnviroAtlas dataset contains data on the mean synthetic nitrogen (N) fertilizer application to cultivated crop and hay/pasture lands per 12-digit Hydrologic Unit (HUC) in 2006. Synthetic N fertilizer inputs in 2006 were estimated using county-level estimates of farm N fertilizer inputs. We acquired county-level data describing total farm-level inputs (kg N/yr) of synthetic N fertilizer to individual counties in 2006 from the United States Geological Survey (USGS) (http://pubs.usgs.gov/sir/2012/5207/). These data were converted to per area rates (kg N/ha/yr) of synthetic N fertilizer application by dividing the total N input by the land area (ha) of combined cultivated crop and hay/pasture lands within a county as determined from county-level (http://cta.ornl.gov/transnet/Boundaries.html) summarization of the 2006 National Land Cover Database (NLCD; http://www.mrlc.gov/nlcd06_data.php). We distributed county-specific, annual per area N inputs rates (kg N/ha/yr) to cultivated crop and hay/pasture lands (30 x 30 m pixels) within the corresponding county using the raster calculator tool in ArcMap 10.0 (ESRI, Inc., Redlands, CA). Fertilizer data described here represent an average input to a typical agricultural land type within a county, i.e., they are not specific to individual crop types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{09DF9B39-6CC8-4DFF-A14D-1BA14C06321F}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -237115,46 +237134,46 @@
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
+            "title": "EnviroAtlas - Synthetic N fertilizer application to agricultural lands by 12-digit HUC in the Conterminous United States, 2006"
         },
-            "identifier": "{09DF9B39-6CC8-4DFF-A14D-1BA14C06321F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas national map displays the application rate of inorganic phosphorus (P) fertilizer on agricultural land in the conterminous United States (excluding Hawaii and Alaska) for the year 2012 by 12-digit HUC. These data are based on International Plant Nutrition Institute (IPNI) compilations of county and state fertilizer sales for 2012 and cropland area from the USGS's U.S. conterminous wall-to-wall anthropogenic land use trends (NWALT) 2012 land cover data. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Inorganic phosphorus fertilizer application for 2012 by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas national map displays the application rate of inorganic phosphorus (P) fertilizer on agricultural land in the conterminous United States (excluding Hawaii and Alaska) for the year 2012 by 12-digit HUC. These data are based on International Plant Nutrition Institute (IPNI) compilations of county and state fertilizer sales for 2012 and cropland area from the USGS's U.S. conterminous wall-to-wall anthropogenic land use trends (NWALT) 2012 land cover data. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{35ba485f-b30f-4d03-a5bc-11a4f0025904}",
+            "issued": "2016-10-28",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -237217,46 +237236,46 @@
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
+            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
+            "temporal": "2012-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Inorganic phosphorus fertilizer application for 2012 by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{35ba485f-b30f-4d03-a5bc-11a4f0025904}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-119.987249, 36.616154, -119.507299, 36.968864",
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
+            "description": "This EnviroAtlas dataset includes the total number of recreational days per year demanded by people ages 18 and over for freshwater fishing by location in the contiguous United States. These values are based on 2010 population distribution, 2011 U.S. Fish and Wildlife Service (FWS) Fish, Hunting, and Wildlife-Associated Recreation (FHWAR) survey data, and 2011 U.S. Department of Agriculture (USDA) Forest Service National Visitor Use Monitoring program data, and have been summarized by 12-digit hydrologic unit code (HUC). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Freshwater Fishing Recreation Demand by 12-Digit HUC in the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes the total number of recreational days per year demanded by people ages 18 and over for freshwater fishing by location in the contiguous United States. These values are based on 2010 population distribution, 2011 U.S. Fish and Wildlife Service (FWS) Fish, Hunting, and Wildlife-Associated Recreation (FHWAR) survey data, and 2011 U.S. Department of Agriculture (USDA) Forest Service National Visitor Use Monitoring program data, and have been summarized by 12-digit hydrologic unit code (HUC). This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{28db3b57-618c-4257-bb4a-4946e9c1e8c4}",
+            "issued": "2016-06-13",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -237320,46 +237339,46 @@
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
+            "title": "EnviroAtlas - Freshwater Fishing Recreation Demand by 12-Digit HUC in the Conterminous United States"
         },
-            "identifier": "{28db3b57-618c-4257-bb4a-4946e9c1e8c4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas data set depicts estimates for mean cash rent paid for land by farmers, sorted by county for irrigated cropland, non-irrigated cropland, and pasture by for most of the conterminous US. This data comes from national surveys which includes approximately 240,000 farms and applies to all crops. According to the USDA (U.S. Department of Agriculture) National Agricultural Statistics Service (NASS), these surveys do not include land rented for a share of the crop, on a fee per head, per pound of gain, by animal unit month (AUM), rented free of charge, or land that includes buildings such as barns. \u00a0For each land use category with positive acres, respondents are given the option of reporting rent per acre or total dollars paid. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Farm Service Land Rental Rates by County for the United States",
-            "description": "This EnviroAtlas data set depicts estimates for mean cash rent paid for land by farmers, sorted by county for irrigated cropland, non-irrigated cropland, and pasture by for most of the conterminous US. This data comes from national surveys which includes approximately 240,000 farms and applies to all crops. According to the USDA (U.S. Department of Agriculture) National Agricultural Statistics Service (NASS), these surveys do not include land rented for a share of the crop, on a fee per head, per pound of gain, by animal unit month (AUM), rented free of charge, or land that includes buildings such as barns. \u00a0For each land use category with positive acres, respondents are given the option of reporting rent per acre or total dollars paid. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5437f70d-c37a-4b3a-a4d0-a501cd8fb19b}",
+            "issued": "2017-02-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -237422,46 +237441,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-02-07",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2017-01-04/2017-01-06",
+            "theme": "environment",
+            "title": "EnviroAtlas - Farm Service Land Rental Rates by County for the United States"
         },
-            "identifier": "{5437f70d-c37a-4b3a-a4d0-a501cd8fb19b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2017-01-04/2017-01-06",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-02-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 155 block groups in Green Bay, Wisconsin. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 155 block groups in Green Bay, Wisconsin. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{49310074-5E28-4378-9549-45E32F40F1E4}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Green Bay",
@@ -237481,46 +237500,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - BenMAP Results by Block Group"
         },
-            "identifier": "{49310074-5E28-4378-9549-45E32F40F1E4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Green Bay, WI EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Green Bay, WI EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{0E92B56C-F58E-4FAC-8B75-BE483AFF22D7}",
+            "issued": "2014-07-09",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237533,46 +237552,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-05-01/2014-05-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Block Groups"
         },
-            "identifier": "{0E92B56C-F58E-4FAC-8B75-BE483AFF22D7}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-05-01/2014-05-01",
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
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{15E44C6E-3B16-414B-AFB5-5AAD66D7F4AB}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Green Bay, WI",
                 "Human",
@@ -237589,46 +237608,46 @@
                 "Environmental Atlas",
                 "Boundaries"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Green Bay, WI - Demographics by Block Group"
         },
-            "identifier": "{15E44C6E-3B16-414B-AFB5-5AAD66D7F4AB}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
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
+            "description": "This EnviroAtlas dataset shows the boundary of the Green Bay, WI Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Green Bay, WI Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{592586B0-4078-4CF7-B610-29C9DDE1D9F5}",
+            "issued": "2014-05-01",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237641,46 +237660,46 @@
                 "Environmental Atlas",
                 "Boundaries"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2013-05-01/2013-05-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Atlas Area Boundary"
         },
-            "identifier": "{592586B0-4078-4CF7-B610-29C9DDE1D9F5}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2013-05-01/2013-05-01",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{69E48A44-3D30-4E84-A764-38FBDCCAC3D0}",
+            "issued": "2017-05-30",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237695,46 +237714,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{69E48A44-3D30-4E84-A764-38FBDCCAC3D0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Water utility service reporting in the EnviroAtlas-defined study area is available through the Public Service Commission of Wisconsin (http://psc.wi.gov/). Within the Green Bay boundary, there are seven service providers with 2008-2013 estimates ranging from 36 to 48 GPD. This dataset was produced by the U.S. EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Water utility service reporting in the EnviroAtlas-defined study area is available through the Public Service Commission of Wisconsin (http://psc.wi.gov/). Within the Green Bay boundary, there are seven service providers with 2008-2013 estimates ranging from 36 to 48 GPD. This dataset was produced by the U.S. EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{EE1BCD10-006A-46A4-BA65-E354ABDBE1EF}",
+            "issued": "2014-09-11",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237754,46 +237773,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-09-11",
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{EE1BCD10-006A-46A4-BA65-E354ABDBE1EF}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-09-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{7F21696D-7159-44A3-AB1E-67EE0B722AB4}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237809,46 +237828,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{7F21696D-7159-44A3-AB1E-67EE0B722AB4}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{199d2a45-0375-45b4-bcc6-d1fed26091b0}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237872,46 +237891,46 @@
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
+            "spatial": "-88.34016, 44.3551, -87.87987, 44.6401",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{199d2a45-0375-45b4-bcc6-d1fed26091b0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.3551, -87.87987, 44.6401",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{8E481B1F-B729-4C8C-BFFD-7E17B6E4EF18}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237926,46 +237945,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2015-03-20/2015-03-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Greenspace Proximity Gradient"
         },
-            "identifier": "{8E481B1F-B729-4C8C-BFFD-7E17B6E4EF18}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{0E4377FF-C5EE-43B2-BD6A-1BA38713E994}",
+            "issued": "2014-09-16",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -237981,46 +238000,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Historic Places by Census Block Group"
         },
-            "identifier": "{0E4377FF-C5EE-43B2-BD6A-1BA38713E994}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{2114EC25-BC5A-481A-9F51-12116CD8993A}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238034,46 +238053,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2015-03-27/2015-03-27",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Impervious Proximity Gradient"
         },
-            "identifier": "{2114EC25-BC5A-481A-9F51-12116CD8993A}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
-            "temporal": "2015-03-27/2015-03-27",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{FF478160-DCFF-453D-A7B7-F2C03DF1BC85}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238088,46 +238107,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{FF478160-DCFF-453D-A7B7-F2C03DF1BC85}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 155 block groups in Green Bay, Wisconsin. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 155 block groups in Green Bay, Wisconsin. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{88838E57-BACF-459B-AB5D-0465A637CA09}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238146,46 +238165,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Ecosystem Services by Block Group"
         },
-            "identifier": "{88838E57-BACF-459B-AB5D-0465A637CA09}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, and green space. Forest is combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands. This dataset also includes the area per capita for each block group for impervious, forest, and green space land cover. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{384D86C0-1B54-48CC-AFB4-2419D479A1B3}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238202,46 +238221,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Land Cover by Block Group"
         },
-            "identifier": "{384D86C0-1B54-48CC-AFB4-2419D479A1B3}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "The Green Bay, WI Meter-Scale Urban Land Cover (MULC) dataset comprises 936 km2 around the city of Green Bay, surrounding towns, tribal lands and rural areas in Brown and Outagamie Counties. These leaf-on LC data and maps were derived from 1-m pixel, four-band (red, green, blue, and near-infrared) aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) on three dates in 2010: July 3, July 25, and August 5. LiDAR data collected on November 18, 2010 was integrated for the Brown County portion. Eight land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, agriculture, and wetlands (woody and emergent). Wetlands were copied from the best available existing wetlands data. Analysis of a random sampling of 566 photo-interpreted land cover reference points yielded an overall user's accuracy (MAX) of 90.4% and a fuzzy user's accuracy (RIGHT) of 94.1%. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Green Bay, Wisconsin -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The Green Bay, WI Meter-Scale Urban Land Cover (MULC) dataset comprises 936 km2 around the city of Green Bay, surrounding towns, tribal lands and rural areas in Brown and Outagamie Counties. These leaf-on LC data and maps were derived from 1-m pixel, four-band (red, green, blue, and near-infrared) aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) on three dates in 2010: July 3, July 25, and August 5. LiDAR data collected on November 18, 2010 was integrated for the Brown County portion. Eight land cover classes were mapped: water, impervious surfaces, soil and barren land, trees and forest, grass and herbaceous non-woody vegetation, agriculture, and wetlands (woody and emergent). Wetlands were copied from the best available existing wetlands data. Analysis of a random sampling of 566 photo-interpreted land cover reference points yielded an overall user's accuracy (MAX) of 90.4% and a fuzzy user's accuracy (RIGHT) of 94.1%. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{D602E7C9-7F53-4C24-8237-746FD3A82CE8}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238264,46 +238283,46 @@
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
+            "spatial": "-88.361895, 44.342264, -87.853055, 44.653172",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Green Bay, Wisconsin -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{D602E7C9-7F53-4C24-8237-746FD3A82CE8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.361895, 44.342264, -87.853055, 44.653172",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{CCBA48F8-FAC6-47A9-9214-2CC572EDC00C}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238321,46 +238340,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Near Road Tree Buffer"
         },
-            "identifier": "{CCBA48F8-FAC6-47A9-9214-2CC572EDC00C}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{70B5DB55-197E-4250-8324-00C5AA1F7F15}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238380,46 +238399,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Near Road Block Group Summary"
         },
-            "identifier": "{70B5DB55-197E-4250-8324-00C5AA1F7F15}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{A8EA353A-6EFF-4D2C-8222-37A677E69ABB}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238434,46 +238453,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2015-10-01/2015-10-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Park Access by Block Group"
         },
-            "identifier": "{A8EA353A-6EFF-4D2C-8222-37A677E69ABB}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8675EC55-2CCE-4B83-972A-A23CD6618B09}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238487,46 +238506,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-06-13/2014-06-13",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Proximity to Parks"
         },
-            "identifier": "{8675EC55-2CCE-4B83-972A-A23CD6618B09}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-06-13/2014-06-13",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{32478BA0-2D81-492D-89EC-27F2C327F005}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238544,46 +238563,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{32478BA0-2D81-492D-89EC-27F2C327F005}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{B9AFEBED-9C29-4DB0-8B54-0CAF58BE5A2D}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238601,46 +238620,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{B9AFEBED-9C29-4DB0-8B54-0CAF58BE5A2D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-88.34016, 44.35510, -87.87987, 44.64010",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{5CC680BB-A78C-4381-8463-63E1FC3F98F5}",
+            "issued": "2013-11-08",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238660,46 +238679,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{5CC680BB-A78C-4381-8463-63E1FC3F98F5}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{1682BACA-928B-4D10-B569-B038DFE260E8}",
+            "issued": "2014-03-11",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238719,46 +238738,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-03-11",
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{1682BACA-928B-4D10-B569-B038DFE260E8}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-03-11",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{ABEA2C9A-9BA6-4B06-BDA8-5271C625DBFA}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238778,46 +238797,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{ABEA2C9A-9BA6-4B06-BDA8-5271C625DBFA}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{F3B58426-2B09-455C-80EC-2DBFCCBC06D4}",
+            "issued": "2014-08-04",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238837,46 +238856,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{F3B58426-2B09-455C-80EC-2DBFCCBC06D4}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{54F3AE50-5F01-427C-87C8-5A061BFA6D6D}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238897,46 +238916,46 @@
                 "Water",
                 "Drinking Water"
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-03-11/2014-03-11",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{54F3AE50-5F01-427C-87C8-5A061BFA6D6D}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-03-11/2014-03-11",
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
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{37EB23AE-51E4-4F96-980E-26C1CD0CCBEA}",
+            "issued": "2014-07-31",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -238954,46 +238973,46 @@
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-06-12/2014-06-12",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Residents with Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{37EB23AE-51E4-4F96-980E-26C1CD0CCBEA}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-06-12/2014-06-12",
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
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Green Bay, WI - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{BA2AA91A-E450-48E0-BE36-B5123CBE6024}",
+            "issued": "2014-08-01",
             "keyword": [
                 "Green Bay, WI",
                 "Ecosystem Services",
@@ -239009,46 +239028,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-08-01",
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
+            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
+            "temporal": "2014-06-12/2014-06-12",
+            "theme": "environment",
+            "title": "EnviroAtlas - Green Bay, WI - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{BA2AA91A-E450-48E0-BE36-B5123CBE6024}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88.34016, 44.35510, -87.87984, 44.64010",
-            "temporal": "2014-06-12/2014-06-12",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2014-08-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset contains indices of geologic (lithosphere) conditions in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/GreenBayWI",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of geologic (lithosphere) conditions for stream confluence catchments for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains indices of geologic (lithosphere) conditions in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{70100219-c75f-473f-81e8-fc4abab28a00}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239108,46 +239127,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of geologic (lithosphere) conditions for stream confluence catchments for the Conterminous United States"
         },
-            "identifier": "{70100219-c75f-473f-81e8-fc4abab28a00}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset contains indices of geologic (lithosphere) conditions in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of geologic (lithosphere) conditions for stream confluence watersheds for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains indices of geologic (lithosphere) conditions in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1724c61b-f548-4fae-aa7f-b323f59be739}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239207,46 +239226,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Indicators of geologic (lithosphere) conditions for stream confluence watersheds for the Conterminous United States"
         },
-            "identifier": "{1724c61b-f548-4fae-aa7f-b323f59be739}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset shows the number of major grains grown, yield in tons, and area in hectares for several major grains and for cotton by 12-digit Hydrologic Unit (HUC). It is based on the United States Department of Agriculture's 2010 Cropland Data Layer (CDL) and data on yields and sales from the National Agricultural Statistics Service (NASS). The grains included in this dataset are corn, barley, cotton, durum wheat, oats, rye, rice, sorghum, spring wheat, soybeans, and winter wheat; it does not include data on every grain. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Major Grains and Cotton by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset shows the number of major grains grown, yield in tons, and area in hectares for several major grains and for cotton by 12-digit Hydrologic Unit (HUC). It is based on the United States Department of Agriculture's 2010 Cropland Data Layer (CDL) and data on yields and sales from the National Agricultural Statistics Service (NASS). The grains included in this dataset are corn, barley, cotton, durum wheat, oats, rye, rice, sorghum, spring wheat, soybeans, and winter wheat; it does not include data on every grain. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0AB7D24B-BFC6-40CF-9C1B-641F36C18EFE}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239310,46 +239329,46 @@
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
+            "temporal": "2007-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Major Grains and Cotton by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{0AB7D24B-BFC6-40CF-9C1B-641F36C18EFE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2007-01-01/2010-01-01",
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
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas Green Space Proximity Gradient Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3a8f566a-2b4f-4a44-8cb4-6fa31c84fa3b}",
+            "issued": "2016-12-12",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239419,46 +239438,48 @@
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
+            "title": "EnviroAtlas Green Space Proximity Gradient Web Service"
         },
-            "identifier": "{3a8f566a-2b4f-4a44-8cb4-6fa31c84fa3b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset summarizes several U.S. Geological Survey (USGS) water budget and surficial groundwater datasets by 12-digit HUC. It includes average rates of evapotranspiration, quick-flow runoff, effective recharge (which reflects the quantity of water available to replenish the groundwater table), and total recharge (which also includes an estimate for the recharge quantity that was subsequently intercepted by riparian vegetation and converted to evapotranspiration) based on the USGS' 800m water budget estimates for the Conterminous United States (CONUS) at long-term timescales for 2000-2013. These datasets were produced by Reitz et al. (https://doi.org/10.5066/F7PN93P0).\n\nIt also includes modeled averages of depth to the water table, mean water transit time across the vadose zone (or unsaturated zone), shallow aquifer transmissivity, long term average soil water content of the unsaturated zone, and mean water residence time in the root zone, based on the USGS's MODFLOW-6 groundwater flow models. These models were driven by spatially-distributed recharge estimated by Reitz et al. using average water-budget information for 1985-2015 and calibrated against long-term average water levels in observation wells, as well as water-level estimates derived from perennial first-order streams and wetlands. The development of the model input and output files included in the USGS data release, as well as post-processing used to derive additional water-budget components also included in this data release, are documented in the Water Resources Research article (https://doi.org/10.1029/2019WR026724).\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Water Balance and Surficial Groundwater by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset summarizes several U.S. Geological Survey (USGS) water budget and surficial groundwater datasets by 12-digit HUC. It includes average rates of evapotranspiration, quick-flow runoff, effective recharge (which reflects the quantity of water available to replenish the groundwater table), and total recharge (which also includes an estimate for the recharge quantity that was subsequently intercepted by riparian vegetation and converted to evapotranspiration) based on the USGS' 800m water budget estimates for the Conterminous United States (CONUS) at long-term timescales for 2000-2013. These datasets were produced by Reitz et al. (https://doi.org/10.5066/F7PN93P0).\n\nIt also includes modeled averages of depth to the water table, mean water transit time across the vadose zone (or unsaturated zone), shallow aquifer transmissivity, long term average soil water content of the unsaturated zone, and mean water residence time in the root zone, based on the USGS's MODFLOW-6 groundwater flow models. These models were driven by spatially-distributed recharge estimated by Reitz et al. using average water-budget information for 1985-2015 and calibrated against long-term average water levels in observation wells, as well as water-level estimates derived from perennial first-order streams and wetlands. The development of the model input and output files included in the USGS data release, as well as post-processing used to derive additional water-budget components also included in this data release, are documented in the Water Resources Research article (https://doi.org/10.1029/2019WR026724).\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "FC7E73FC-65ED-4498-B8BD-417978D72D41",
+            "issued": "2022-01-04",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239524,46 +239545,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-04",
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
+            "temporal": "1985-01-01T00:00:00/2015-01-01T00:00:00",
+            "title": "EnviroAtlas - Water Balance and Surficial Groundwater by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "FC7E73FC-65ED-4498-B8BD-417978D72D41",
+        {
+            "@type": "dcat:Dataset",
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
-            "temporal": "1985-01-01T00:00:00/2015-01-01T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-01-04",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each 12-digit Hydrologic Unit (HUC). The historic places data were compiled from the National Park Service's National Register of Historic Places (NRHP), which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Historic Places by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each 12-digit Hydrologic Unit (HUC). The historic places data were compiled from the National Park Service's National Register of Historic Places (NRHP), which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b6653c73-f15b-4de2-bb81-93d54ac701f7}",
+            "issued": "2016-06-13",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239628,46 +239647,46 @@
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
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Historic Places by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{b6653c73-f15b-4de2-bb81-93d54ac701f7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "1966-01-01/2013-01-01",
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
+            "description": "This EnviroAtlas dataset contains information about hydrologic attributes of the upstream catchments and watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Hydrologic attributes of stream confluences for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about hydrologic attributes of the upstream catchments and watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a9e794f5-7b01-4477-97b3-47461cb929de}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239727,47 +239746,47 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Hydrologic attributes of stream confluences for the Conterminous United States"
         },
-            "identifier": "{a9e794f5-7b01-4477-97b3-47461cb929de}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset shows the percentages of stream and water body shoreline lengths within 30 meters of impervious cover by 12-digit Hydrologic Unit (HUC) subwatershed in the contiguous U.S. Impervious cover alters the hydrologic behavior of streams and water bodies, promoting increased storm water runoff and lower stream flow during periods in between rainfall events. Impervious cover also promotes increased pollutant loads in receiving waters and degraded streamside habitat. This dataset shows were impervious cover occurs close to streams and water bodies, where it is likely to have a greater adverse impact on receiving waters. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Percentage of stream and water body shoreline lengths within 30 meters of >= 5% or >= 15% impervious cover by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset shows the percentages of stream and water body shoreline lengths within 30 meters of impervious cover by 12-digit Hydrologic Unit (HUC) subwatershed in the contiguous U.S. Impervious cover alters the hydrologic behavior of streams and water bodies, promoting increased storm water runoff and lower stream flow during periods in between rainfall events. Impervious cover also promotes increased pollutant loads in receiving waters and degraded streamside habitat. This dataset shows were impervious cover occurs close to streams and water bodies, where it is likely to have a greater adverse impact on receiving waters. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
-            "keyword": [
+            ],
+            "identifier": "{cf3132f1-4d70-4316-9cf2-07ffec3e4112}",
+            "issued": "2016-06-13",
+            "keyword": [
                 "Connecticut",
                 "Texas",
                 "Ecosystem Services",
@@ -239832,46 +239851,46 @@
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
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Percentage of stream and water body shoreline lengths within 30 meters of >= 5% or >= 15% impervious cover by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{cf3132f1-4d70-4316-9cf2-07ffec3e4112}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2016-06-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset depicts the total length of stream or river flowlines that have impairments submitted to the EPA by states under section 303(d) of the Clean Water Act. It also contains the total lengths of streams, rivers, and canals, total waterbody area, and stream density (stream length per area) from the US Geological Survey's high-resolution National Hydrography Dataset (NHD). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - 303(d) Impairments by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset depicts the total length of stream or river flowlines that have impairments submitted to the EPA by states under section 303(d) of the Clean Water Act. It also contains the total lengths of streams, rivers, and canals, total waterbody area, and stream density (stream length per area) from the US Geological Survey's high-resolution National Hydrography Dataset (NHD). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F6AE1B0B-9C59-463C-9D80-BAE4AA460CEE}",
+            "issued": "2016-04-27",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -239938,46 +239957,48 @@
                 "Contaminant",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2016-04-27",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2015-05-01/2015-05-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - 303(d) Impairments by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{F6AE1B0B-9C59-463C-9D80-BAE4AA460CEE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2015-05-01/2015-05-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2016-04-27",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in the conterminous United State that is impervious to water infiltration using the National Land Cover Database 2019 (NLCD2019) Percent Developed Impervious dataset.\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - 2019 Percent Impervious Cover by 12-digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset represents the percentage of land area within each 12-digit hydrologic unit code (HUC) in the conterminous United State that is impervious to water infiltration using the National Land Cover Database 2019 (NLCD2019) Percent Developed Impervious dataset.\n\nThis dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "{831D980C-FA14-4093-9BE9-CDE589C35339}",
+            "issued": "2022-03-25",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -240044,46 +240065,44 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-11-18",
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
+            "title": "EnviroAtlas - 2019 Percent Impervious Cover by 12-digit HUC for the Conterminous United States"
         },
-            "identifier": "{831D980C-FA14-4093-9BE9-CDE589C35339}",
+        {
+            "@type": "dcat:Dataset",
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
-            "issued": "2022-03-25",
+            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
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
-            "title": "EnviroAtlas Impervious Proximity Gradient Web Service",
-            "description": "This EnviroAtlas web service supports research and online mapping activities related to EnviroAtlas (https://www.epa.gov/enviroatlas). In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1c335481-1280-4767-8ee7-205d6c05d6f2}",
+            "issued": "2016-12-12",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -240152,46 +240171,46 @@
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
+            "title": "EnviroAtlas Impervious Proximity Gradient Web Service"
         },
-            "identifier": "{1c335481-1280-4767-8ee7-205d6c05d6f2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset portrays the percentage of population within different household income ranges for each Census Block Group (CBG), a threshold estimated to be an optimal household income for quality of life, and the percentage of households with income below this threshold. Data were compiled from the Census ACS (American Community Survey) 5-year Summary Data (2008-2012). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Household income metrics related to quality of life by Census Block Group for the Conterminous United States",
-            "description": "This EnviroAtlas dataset portrays the percentage of population within different household income ranges for each Census Block Group (CBG), a threshold estimated to be an optimal household income for quality of life, and the percentage of households with income below this threshold. Data were compiled from the Census ACS (American Community Survey) 5-year Summary Data (2008-2012). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b188b882-f130-43c6-9000-cd1e6f871a6d}",
+            "issued": "2017-03-27",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -240255,46 +240274,46 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-27",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2008-01-01/2012-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Household income metrics related to quality of life by Census Block Group for the Conterminous United States"
         },
-            "identifier": "{b188b882-f130-43c6-9000-cd1e6f871a6d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2008-01-01/2012-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-27",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset includes industrial water demand attributes which provide insight into the amount of water currently used for manufacturing and production of commodities in the contiguous United States. The values are based on 2010 water demand and Dun and Bradstreet's 2009/2010 source data, and have been summarized by watershed or 12-digit hydrologic unit code (HUC). For the purposes of this metric, industrial water use includes chemical, food, paper, wood, and metal production. The industrial water is for self-supplied only such as by private wells or reservoirs. Sources include either surface water or groundwater. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Industrial Water Demand (2010) by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset includes industrial water demand attributes which provide insight into the amount of water currently used for manufacturing and production of commodities in the contiguous United States. The values are based on 2010 water demand and Dun and Bradstreet's 2009/2010 source data, and have been summarized by watershed or 12-digit hydrologic unit code (HUC). For the purposes of this metric, industrial water use includes chemical, food, paper, wood, and metal production. The industrial water is for self-supplied only such as by private wells or reservoirs. Sources include either surface water or groundwater. This dataset was produced by the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4E58C04B-8A17-4B07-9EE4-1D9365D5B0D9}",
+            "issued": "2017-03-20",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -240360,46 +240379,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-03-20",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2009-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Industrial Water Demand (2010) by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{4E58C04B-8A17-4B07-9EE4-1D9365D5B0D9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2009-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-03-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in each EnviroAtlas community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. For specific information about each community's intersection density layer, consult their individual metadata records: Austin, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B72177756-4DD2-4133-8E85-C4C46BFAEEE2%7D); Birmingham, AL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bc892e710-81cf-4ba3-a551-8024ffa7049f%7D); Baltimore, MD (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Ba950ce43-bbe0-44ba-805a-b413147e0092%7D); Brownsville, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B990c2af4-2ac6-40f8-a7dc-cfea1479616b%7D); Chicago, IL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bb521f10b-4505-4867-ba2d-70719f667bbb%7D); Cleveland, OH (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Beb14c0ca-f26c-47eb-8198-02fba73784d6%7D); Des Moines, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA5C3A6F2-CA61-4E78-B57D-289E45B34EF5%7D); Durham, NC (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAF794837-71B0-4B3F-AA95-996A9C19D8A6%7D); Fresno, CA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0D3E33D1-81C5-456E-A581-58049701ACED%7D); Green Bay, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFF478160-DCFF-453D-A7B7-F2C03DF1BC85%7D); Memphis, TN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9C5E1317-F07D-4CEF-935A-A494E0BE7A7F%7D); Minneapolis/St. Paul, MN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bea532fdb-df76-4c5b-afcf-2af27d5b5e10%7D); Milwaukee, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B991BCB95-1624-4102-95D5-6B1E382F5C12%7D); New Bedford, MA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B89E0CE0B-DAEE-430E-A8E4-C486B3FD803F%7D); New Haven, CT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bf39d7d21-064d-4498-9926-743d543bc8f0%7D); New York, NY (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BD70DE411-6B72-4806-9B40-04921B3EA230%7D); Phoenix, AZ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAFC1F0E1-EC52-41E4-8682-8885BED5A9B7%7D); Pittsburgh, PA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDA4B629D-3224-45AD-8C32-F27253634ED4%7D); Portland, ME (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1CAE7A89-3562-4706-AA12-1E6220006179%7D); Paterson, NJ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE1E6BB36-9E9E-41B8-BF44-33D56CCAE145%7D); Portland, OR (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B17F6E916-7805-40AD-85E1-61B63BBDE193%7D); Salt Lake City, UT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bdbab21bf-487d-4116-bbfc-8a26109daf27%7D); Tampa, FL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B356EC846-7733-4AA3-8E0D-83DFA5AA2C52%7D); Virginia Beach/Williamsburg, VA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B3ff033c2-1d11-4dbf-aea7-f8bb8244bcc3%7D); and Woodbine, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4E7173AD-5D8E-426A-9431-67FE34833523%7D). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas Estimated Intersection Density of Walkable Roads Web Service",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in each EnviroAtlas community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. For specific information about each community's intersection density layer, consult their individual metadata records: Austin, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B72177756-4DD2-4133-8E85-C4C46BFAEEE2%7D); Birmingham, AL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bc892e710-81cf-4ba3-a551-8024ffa7049f%7D); Baltimore, MD (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Ba950ce43-bbe0-44ba-805a-b413147e0092%7D); Brownsville, TX (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B990c2af4-2ac6-40f8-a7dc-cfea1479616b%7D); Chicago, IL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bb521f10b-4505-4867-ba2d-70719f667bbb%7D); Cleveland, OH (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Beb14c0ca-f26c-47eb-8198-02fba73784d6%7D); Des Moines, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA5C3A6F2-CA61-4E78-B57D-289E45B34EF5%7D); Durham, NC (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAF794837-71B0-4B3F-AA95-996A9C19D8A6%7D); Fresno, CA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0D3E33D1-81C5-456E-A581-58049701ACED%7D); Green Bay, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFF478160-DCFF-453D-A7B7-F2C03DF1BC85%7D); Memphis, TN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9C5E1317-F07D-4CEF-935A-A494E0BE7A7F%7D); Minneapolis/St. Paul, MN (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bea532fdb-df76-4c5b-afcf-2af27d5b5e10%7D); Milwaukee, WI (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B991BCB95-1624-4102-95D5-6B1E382F5C12%7D); New Bedford, MA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B89E0CE0B-DAEE-430E-A8E4-C486B3FD803F%7D); New Haven, CT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bf39d7d21-064d-4498-9926-743d543bc8f0%7D); New York, NY (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BD70DE411-6B72-4806-9B40-04921B3EA230%7D); Phoenix, AZ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAFC1F0E1-EC52-41E4-8682-8885BED5A9B7%7D); Pittsburgh, PA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDA4B629D-3224-45AD-8C32-F27253634ED4%7D); Portland, ME (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1CAE7A89-3562-4706-AA12-1E6220006179%7D); Paterson, NJ (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE1E6BB36-9E9E-41B8-BF44-33D56CCAE145%7D); Portland, OR (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B17F6E916-7805-40AD-85E1-61B63BBDE193%7D); Salt Lake City, UT (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bdbab21bf-487d-4116-bbfc-8a26109daf27%7D); Tampa, FL (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B356EC846-7733-4AA3-8E0D-83DFA5AA2C52%7D); Virginia Beach/Williamsburg, VA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B3ff033c2-1d11-4dbf-aea7-f8bb8244bcc3%7D); and Woodbine, IA (https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4E7173AD-5D8E-426A-9431-67FE34833523%7D). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4a7dad9e-a242-42d7-b851-36654d12c220}",
+            "issued": "2016-10-06",
             "keyword": [
                 "Texas",
                 "Green Bay, WI",
@@ -240446,46 +240465,46 @@
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
+            "title": "EnviroAtlas Estimated Intersection Density of Walkable Roads Web Service"
         },
-            "identifier": "{4a7dad9e-a242-42d7-b851-36654d12c220}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 6421 block groups in Los Angeles County, California. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Los Angeles County, CA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/LosAngelesCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Los Angeles, CA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 6421 block groups in Los Angeles County, California. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Los Angeles County, CA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b4be6186-bd98-4182-882d-e590e2633609}",
+            "issued": "2019-08-07",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -240505,46 +240524,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-07",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - BenMAP Results by Block Group"
         },
-            "identifier": "{b4be6186-bd98-4182-882d-e590e2633609}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Los Angeles, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Los Angeles, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{342f9a6f-b12d-4602-9d25-373efe7684b4}",
+            "issued": "2019-08-12",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -240557,46 +240576,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-12",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Census Block Groups"
         },
-            "identifier": "{342f9a6f-b12d-4602-9d25-373efe7684b4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{fb5fbcb1-234b-46ae-b40f-83bc3a1a0580}",
+            "issued": "2019-08-12",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -240613,46 +240632,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-12",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Los Angeles, CA - Demographics by Block Group"
         },
-            "identifier": "{fb5fbcb1-234b-46ae-b40f-83bc3a1a0580}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-12",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Los Angeles, CA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Los Angeles, CA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{91455ba0-43c0-47e5-a6b2-8eca6076fbb9}",
+            "issued": "2019-08-12",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -240665,46 +240684,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-12",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - EnviroAtlas Community Boundary"
         },
-            "identifier": "{91455ba0-43c0-47e5-a6b2-8eca6076fbb9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-12",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{852303d3-6306-49a2-93e7-a9fb7b784b1b}",
+            "issued": "2019-11-23",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -240720,46 +240739,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-23",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{852303d3-6306-49a2-93e7-a9fb7b784b1b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Los Angeles, CA, Urban Water Management Plans (available via data.ca.gov and individual providers) and an average of available Residential Gallons Per Capita per Day (R-GPCD) data (available through the California State Water Resources Control Board (CSWRCB)) were used. Within the EnviroAtlas community boundary, provider estimates range from 42 to 255 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Domestic Water Demand per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Los Angeles, CA, Urban Water Management Plans (available via data.ca.gov and individual providers) and an average of available Residential Gallons Per Capita per Day (R-GPCD) data (available through the California State Water Resources Control Board (CSWRCB)) were used. Within the EnviroAtlas community boundary, provider estimates range from 42 to 255 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e0001426-94db-4e3c-892d-a21962caa793}",
+            "issued": "2019-09-17",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -240779,46 +240798,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-09-17",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Domestic Water Demand per Day by U.S. Census Block Group"
         },
-            "identifier": "{e0001426-94db-4e3c-892d-a21962caa793}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-118.9272, 33.24023, -117.65058, 34.83098",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-09-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dde72f05-11da-4b0a-b064-9c1631bf04f4}",
+            "issued": "2019-07-13",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -240834,46 +240853,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-13",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{dde72f05-11da-4b0a-b064-9c1631bf04f4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-07-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1fb6f601-845d-4f04-b09c-083ddcbaf547}",
+            "issued": "2019-09-17",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -240897,46 +240916,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-09-17",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{1fb6f601-845d-4f04-b09c-083ddcbaf547}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-09-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{234c3216-619d-4361-8767-a8727d8762e0}",
+            "issued": "2019-08-22",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -240951,46 +240970,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-22",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Greenspace Proximity Gradient"
         },
-            "identifier": "{234c3216-619d-4361-8767-a8727d8762e0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{acf6d295-dc09-4ffc-8ced-bfd7a1d35666}",
+            "issued": "2019-09-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -241006,46 +241025,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-09-09",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Historic Places by Census Block Group"
         },
-            "identifier": "{acf6d295-dc09-4ffc-8ced-bfd7a1d35666}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-09-09",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{993db311-6882-4096-8cb0-9bec80a71280}",
+            "issued": "2019-08-23",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -241059,46 +241078,46 @@
                 "Environmental Atlas",
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
+            "temporal": "2014-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Los Angeles, CA - Impervious Proximity Gradient"
         },
-            "identifier": "{993db311-6882-4096-8cb0-9bec80a71280}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{736e9bb1-d953-4d2e-9cca-de63b0d33f18}",
+            "issued": "2019-08-19",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -241113,46 +241132,46 @@
                 "Transportation",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-19",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{736e9bb1-d953-4d2e-9cca-de63b0d33f18}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-19",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 6421 block groups in Los Angeles County, California. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 6421 block groups in Los Angeles County, California. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{fa12ed2c-24dd-45e2-83aa-5f5d01d95e9c}",
+            "issued": "2021-03-16",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -241171,46 +241190,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-03-16",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Ecosystem Services by Block Group"
         },
-            "identifier": "{fa12ed2c-24dd-45e2-83aa-5f5d01d95e9c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2021-03-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{18f8519b-c5dd-407e-9138-0b0cc2cb3edd}",
+            "issued": "2019-08-13",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -241226,46 +241245,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "title": "EnviroAtlas - Los Angeles, CA - Land Cover by Block Group"
         },
-            "identifier": "{18f8519b-c5dd-407e-9138-0b0cc2cb3edd}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "The Los Angeles County, CA Meter Urban Land Cover (MULC) dataset was generated from sub-meter image pixel resolution data created by the University of Vermont Spatial Analysis Laboratory (SAL) through the combined use of 2016 USDA National Agricultural Imagery Program (NAIP) four band (red, green, blue and near infrared) aerial imagery, 2016 LiDAR data and 2014 ortho-imagery. The sub-meter, thematic landcover data feature attributes were recoded and spatially resampled to a 1-meter spatial scale by EPA for MULC data product integration. The mapped area is confined to the boundaries of US Census Bureau's 2010 Urban Statistical Area for Los Angeles County, with an added 1km coastal water buffer area extension. The following eight land cover classes were mapped: Water, Impervious, Soil or Barren, Trees or Forest, Grass or Herbaceous, Woody Wetlands and Emergent Wetlands. Integrated wetland features were derived using ancillary National Wetlands Inventory (NWI) polygon data (version 2), downloaded from the Unites States Fish and Wildlife Service (USFWS) Wetland Mapper web mapping service (https://www.fws.gov/wetlands/data/mapper.html). Metadata for the NWI wetlands data layer can be found at http://www.fws.gov/wetlands/Data/Metadata.html. An accuracy assessment of the classified product, using 887 completely random and 40 stratified random photo-interpreted land cover reference sample points yielded an overall user's accuracy (MAX) of 61.1 percent and a fuzzy user's accuracy (RIGHT) of 89.2 percent. For data workflow processing details see Overview Description section. This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy (UTC) assessment program, and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas -- Los Angeles County, CA -- Meter-Scale Urban Land Cover (MULC) Data (2016)",
-            "description": "The Los Angeles County, CA Meter Urban Land Cover (MULC) dataset was generated from sub-meter image pixel resolution data created by the University of Vermont Spatial Analysis Laboratory (SAL) through the combined use of 2016 USDA National Agricultural Imagery Program (NAIP) four band (red, green, blue and near infrared) aerial imagery, 2016 LiDAR data and 2014 ortho-imagery. The sub-meter, thematic landcover data feature attributes were recoded and spatially resampled to a 1-meter spatial scale by EPA for MULC data product integration. The mapped area is confined to the boundaries of US Census Bureau's 2010 Urban Statistical Area for Los Angeles County, with an added 1km coastal water buffer area extension. The following eight land cover classes were mapped: Water, Impervious, Soil or Barren, Trees or Forest, Grass or Herbaceous, Woody Wetlands and Emergent Wetlands. Integrated wetland features were derived using ancillary National Wetlands Inventory (NWI) polygon data (version 2), downloaded from the Unites States Fish and Wildlife Service (USFWS) Wetland Mapper web mapping service (https://www.fws.gov/wetlands/data/mapper.html). Metadata for the NWI wetlands data layer can be found at http://www.fws.gov/wetlands/Data/Metadata.html. An accuracy assessment of the classified product, using 887 completely random and 40 stratified random photo-interpreted land cover reference sample points yielded an overall user's accuracy (MAX) of 61.1 percent and a fuzzy user's accuracy (RIGHT) of 89.2 percent. For data workflow processing details see Overview Description section. This dataset was produced by the University of Vermont Spatial Analysis Laboratory, the United States Forest Service Urban Tree Canopy (UTC) assessment program, and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ccc7c413-9908-4e20-83e1-acf01b05de38}",
+            "issued": "2019-09-06",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -241284,46 +241303,46 @@
                 "Environmental Atlas",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-118.983754, 33.225470, -117.630470, 34.836351",
+            "temporal": "2014-01-01/2016-08-31",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Los Angeles County, CA -- Meter-Scale Urban Land Cover (MULC) Data (2016)"
         },
-            "identifier": "{ccc7c413-9908-4e20-83e1-acf01b05de38}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-118.983754, 33.225470, -117.630470, 34.836351",
-            "temporal": "2014-01-01/2016-08-31",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9f421a0b-1a82-42cb-9f51-f68169a53a94}",
+            "issued": "2019-08-20",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -241341,46 +241360,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-20",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{9f421a0b-1a82-42cb-9f51-f68169a53a94}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Los Angeles, CA - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c2959c77-1c79-4e2f-ba99-e70fc1f73e19}",
+            "issued": "2019-08-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -241399,46 +241418,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-19",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Los Angeles, CA - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{c2959c77-1c79-4e2f-ba99-e70fc1f73e19}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-08-19",
-            "language": "en-us",
-            "theme": "environment",
```

