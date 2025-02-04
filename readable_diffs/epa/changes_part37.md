# Change History for epa.json (Part 37)

### Changes from 31606f9 to dd2190f (Part 27/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dfe2b041-54a3-49dc-9a22-cff39dd70559}",
+            "issued": "2019-11-14",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -272917,46 +272936,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-14",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{dfe2b041-54a3-49dc-9a22-cff39dd70559}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "2016-01-01/2016-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-14",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Two reports were used with city- or water supply authority- level domestic water demand data, in addition to county level data. The 2013 Jefferson County Data Book provides detailed publicly, privately, and self supplied water use and population served for 2013 and covers the Jefferson County, MO portion of the EnviroAtlas study area. The 2019 Census of Missouri Public Water Systems provides detailed publicly supplied water use and population served for 2019 and covers all of Missouri. The 2010 USGS Estimated Use of Water in the United States in 2010 report covers the missing areas, including counties in Illinois within the study area. Data from these reports were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 25 and 427 GPD for each of the subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Two reports were used with city- or water supply authority- level domestic water demand data, in addition to county level data. The 2013 Jefferson County Data Book provides detailed publicly, privately, and self supplied water use and population served for 2013 and covers the Jefferson County, MO portion of the EnviroAtlas study area. The 2019 Census of Missouri Public Water Systems provides detailed publicly supplied water use and population served for 2019 and covers all of Missouri. The 2010 USGS Estimated Use of Water in the United States in 2010 report covers the missing areas, including counties in Illinois within the study area. Data from these reports were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 25 and 427 GPD for each of the subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{18650143-5a5a-4163-962e-25d93d3c2548}",
+            "issued": "2019-08-29",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -272976,46 +272995,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{18650143-5a5a-4163-962e-25d93d3c2548}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e78c6e89-9368-449b-8c45-21fd54ad7ac6}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -273031,46 +273050,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{e78c6e89-9368-449b-8c45-21fd54ad7ac6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9f0694e5-14b6-4cb6-8770-9b1877881f6e}",
+            "issued": "2019-06-26",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -273094,46 +273113,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-26",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{9f0694e5-14b6-4cb6-8770-9b1877881f6e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e0a0172f-23f4-457d-b4d2-fd1a96f0fb59}",
+            "issued": "2019-06-24",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -273148,46 +273167,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-24",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Greenspace Proximity Gradient"
         },
-            "identifier": "{e0a0172f-23f4-457d-b4d2-fd1a96f0fb59}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e8be9461-2c50-4a02-a943-5414f839deab}",
+            "issued": "2019-08-28",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -273203,46 +273222,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-28",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Historic Places by Census Block Group"
         },
-            "identifier": "{e8be9461-2c50-4a02-a943-5414f839deab}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-28",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5f89063b-986b-4d2b-96bb-5e16da9e67e0}",
+            "issued": "2019-06-24",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -273256,46 +273275,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-24",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Impervious Proximity Gradient"
         },
-            "identifier": "{5f89063b-986b-4d2b-96bb-5e16da9e67e0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dd227381-8941-4073-8381-c8975b3141de}",
+            "issued": "2019-06-26",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -273310,50 +273329,50 @@
                 "Transportation",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-26",
+            "programCode": [
+                "020:072"
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
-            "identifier": "{dd227381-8941-4073-8381-c8975b3141de}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
             "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-26",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "EnviroAtlas - St. Louis, MO - Estimated Intersection Density of Walkable Roads"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1552 block groups in the Greater St. Louis, MO region. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
-            "keyword": [
-                "Ecosystem Services",
-                "Modeling",
-                "Air",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1552 block groups in the Greater St. Louis, MO region. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{5096ea51-01e2-42fe-a808-85ab0e57498c}",
+            "issued": "2019-08-05",
+            "keyword": [
+                "Ecosystem Services",
+                "Modeling",
+                "Air",
                 "Trees",
                 "St. Louis, MO",
                 "Environment",
@@ -273368,46 +273387,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-08-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Ecosystem Services by Block Group"
         },
-            "identifier": "{5096ea51-01e2-42fe-a808-85ab0e57498c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-08-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this commmunity, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this commmunity, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3be0bc4f-3548-4142-9173-84db58dd4c00}",
+            "issued": "2019-06-21",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -273423,46 +273442,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Land Cover by Block Group"
         },
-            "identifier": "{3be0bc4f-3548-4142-9173-84db58dd4c00}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The EnviroAtlas St. Louis, Missouri Meter-Scale Urban Land Cover (MULC) dataset comprises 4188 km2 around the city of St. Louis and surrounding land in parts of eleven counties within Illinois and Missouri. These MULC data and maps were derived from several sources from multiple years: LiDAR (2008-2012); 1-m pixel, four-band (red, green, blue, and near-infrared) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP, 2012, 2014-2016); leaf-off 6-inch pixel four-band imagery (2015) as well as ancillary vector data (e.g., roads, building footprints.). Eight land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forested, Grass/Herbaceous Non Woody Vegetation, Agriculture, and Wetlands (Woody and Emergent). Wetlands were delineated using the best available existing wetlands data, which was a National Wetlands Inventory (NWI) layer. An analysis of 745 completely random and 226 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 81% and an overall fuzzy user's accuracy (RIGHT) of 90% (see confusion matrices below). This dataset was produced in three phases by the University of Missouri and the East-West Gateway Council of Governments for the Missouri Resource Assessment Partnership (MoRAP) and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- St. Louis, MO -- Meter-Scale Urban Land Cover Data (MULC) Data (2016)",
-            "description": "The EnviroAtlas St. Louis, Missouri Meter-Scale Urban Land Cover (MULC) dataset comprises 4188 km2 around the city of St. Louis and surrounding land in parts of eleven counties within Illinois and Missouri. These MULC data and maps were derived from several sources from multiple years: LiDAR (2008-2012); 1-m pixel, four-band (red, green, blue, and near-infrared) leaf-on aerial photography acquired from the United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP, 2012, 2014-2016); leaf-off 6-inch pixel four-band imagery (2015) as well as ancillary vector data (e.g., roads, building footprints.). Eight land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forested, Grass/Herbaceous Non Woody Vegetation, Agriculture, and Wetlands (Woody and Emergent). Wetlands were delineated using the best available existing wetlands data, which was a National Wetlands Inventory (NWI) layer. An analysis of 745 completely random and 226 stratified random photo-interpreted land cover reference points yielded a simple overall user's accuracy (MAX) of 81% and an overall fuzzy user's accuracy (RIGHT) of 90% (see confusion matrices below). This dataset was produced in three phases by the University of Missouri and the East-West Gateway Council of Governments for the Missouri Resource Assessment Partnership (MoRAP) and the US EPA to support research and online mapping activities related to the EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{f0e4c532-b1d8-4b96-8d1c-855103e5099c}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -273486,46 +273505,46 @@
                 "Agriculture",
                 "Communities"
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
+            "spatial": "-90.990687, 38.148596, -89.744822, 38.948874",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- St. Louis, MO -- Meter-Scale Urban Land Cover Data (MULC) Data (2016)"
         },
-            "identifier": "{f0e4c532-b1d8-4b96-8d1c-855103e5099c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.990687, 38.148596, -89.744822, 38.948874",
-            "temporal": "9999-01-01/9999-01-01",
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
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dde2da85-1fe8-469f-a3f3-b6c460a962be}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -273543,46 +273562,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{dde2da85-1fe8-469f-a3f3-b6c460a962be}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{06c695ee-ac11-4808-a0ca-f080ce6d5d0d}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -273601,46 +273620,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{06c695ee-ac11-4808-a0ca-f080ce6d5d0d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d8b7eb25-b431-46dc-83ae-5559b32d9965}",
+            "issued": "2019-07-29",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -273655,46 +273674,46 @@
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
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Park Access by Block Group"
         },
-            "identifier": "{d8b7eb25-b431-46dc-83ae-5559b32d9965}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6d857d72-acbd-45e5-8a4a-a1bb47bcca80}",
+            "issued": "2019-07-29",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -273708,46 +273727,46 @@
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
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Proximity to Parks"
         },
-            "identifier": "{6d857d72-acbd-45e5-8a4a-a1bb47bcca80}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
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
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{af462b4b-3925-45b0-aa41-b0a89aa419ff}",
+            "issued": "2019-06-26",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -273765,46 +273784,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-26",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{af462b4b-3925-45b0-aa41-b0a89aa419ff}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f229b54f-4356-44ec-9c8a-fee8e03edb70}",
+            "issued": "2019-06-26",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -273822,46 +273841,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-26",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{f229b54f-4356-44ec-9c8a-fee8e03edb70}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0e4d16d8-7a7f-4044-a066-ac7174e42094}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -273881,46 +273900,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{0e4d16d8-7a7f-4044-a066-ac7174e42094}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3aef592f-b49e-4b2b-8a39-6a5f19407fcc}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -273940,46 +273959,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{3aef592f-b49e-4b2b-8a39-6a5f19407fcc}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{198c18ea-6cb3-4605-bc53-273ab5f671a2}",
+            "issued": "2019-06-23",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -273999,46 +274018,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{198c18ea-6cb3-4605-bc53-273ab5f671a2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{28a80766-d229-48be-856a-ec2faf476358}",
+            "issued": "2019-06-23",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -274058,46 +274077,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{28a80766-d229-48be-856a-ec2faf476358}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4dc58d75-67db-4b7a-9622-385bc5f8e1ac}",
+            "issued": "2019-06-22",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -274118,46 +274137,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{4dc58d75-67db-4b7a-9622-385bc5f8e1ac}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-22",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{caee74f4-72b4-400b-9656-af1cd9d9a7e8}",
+            "issued": "2019-06-24",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -274175,46 +274194,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-24",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{caee74f4-72b4-400b-9656-af1cd9d9a7e8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-24",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - St. Louis, MO - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1fc2c7ec-f506-46e6-84bb-0cef90ff0ac2}",
+            "issued": "2019-06-23",
             "keyword": [
                 "Ecosystem Services",
                 "St. Louis, MO",
@@ -274230,46 +274249,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-06-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - St. Louis, MO - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{1fc2c7ec-f506-46e6-84bb-0cef90ff0ac2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-90.97891, 38.18429, -89.75686, 38.91245",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-06-23",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The annual average direct normal solar resources by 12-Digit Hydrologic Unit (HUC) was estimated from maps produced by the National Renewable Energy Laboratory for the U.S. Department of Energy (February 2009). The original data was from 10km, satellite modeled dataset (SUNY/NREL, 2007) representing data from 1998-2005. The 10km data was converted to 30m grid cells, and then zonal statistics were estimated for a final value of average kWh/m2/day for each 12-digit HUC. For more information about the original dataset please refer to the National Renewable Energy Laboratory (NREL) website at www.nrel.gov/gis/data_solar.html. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/StLouisMO",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Average Direct Normal Solar resources kWh/m2/Day by 12-Digit HUC for the Conterminous United States",
-            "description": "The annual average direct normal solar resources by 12-Digit Hydrologic Unit (HUC) was estimated from maps produced by the National Renewable Energy Laboratory for the U.S. Department of Energy (February 2009). The original data was from 10km, satellite modeled dataset (SUNY/NREL, 2007) representing data from 1998-2005. The 10km data was converted to 30m grid cells, and then zonal statistics were estimated for a final value of average kWh/m2/day for each 12-digit HUC. For more information about the original dataset please refer to the National Renewable Energy Laboratory (NREL) website at www.nrel.gov/gis/data_solar.html. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6858E347-5D85-4C2B-91A2-254BCF0E2CA6}",
+            "issued": "2015-05-07",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -274330,46 +274349,46 @@
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
+            "temporal": "2012-01-18/2012-01-18",
+            "theme": "environment",
+            "title": "EnviroAtlas - Average Direct Normal Solar resources kWh/m2/Day by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{6858E347-5D85-4C2B-91A2-254BCF0E2CA6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2012-01-18/2012-01-18",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 386 block groups in Sonoma County, CA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Sonoma County, CA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 386 block groups in Sonoma County, CA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Sonoma County, CA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{40672a47-d07a-498f-a6be-31f4f1cfd8b0}",
+            "issued": "2018-12-13",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -274389,46 +274408,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-12-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - BenMAP Results by Block Group"
         },
-            "identifier": "{40672a47-d07a-498f-a6be-31f4f1cfd8b0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-12-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Sonoma County, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Sonoma County, CA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{367ff46b-ecce-444f-be3e-1d91c53815f1}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -274441,46 +274460,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Census Block Groups"
         },
-            "identifier": "{367ff46b-ecce-444f-be3e-1d91c53815f1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6a84a73e-cbf2-4f52-80b7-3fd84e03c942}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -274497,46 +274516,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Sonoma County, CA - Demographics by Block Group"
         },
-            "identifier": "{6a84a73e-cbf2-4f52-80b7-3fd84e03c942}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Sonoma County, CA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Sonoma County, CA - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Sonoma County, CA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a3ec8c72-cda4-4dce-8aa1-eb8e5dfd8d0e}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -274549,46 +274568,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - EnviroAtlas Community Boundary"
         },
-            "identifier": "{a3ec8c72-cda4-4dce-8aa1-eb8e5dfd8d0e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{00d21e45-9d53-4b66-8d1e-60ce6c18b9ea}",
+            "issued": "2019-11-08",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -274604,46 +274623,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{00d21e45-9d53-4b66-8d1e-60ce6c18b9ea}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Sonoma County, CA, Urban Water Management Plans (available via data.ca.gov and individual providers) and an average of available Residential Gallons Per Capita per Day (R-GPCD) data (available through the California State Water Resources Control Board (CSWRCB)) were used. Within the EnviroAtlas community boundary, provider estimates range from 57 to 101 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Domestic Water Demand per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, community level domestic water demand is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by Census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Sonoma County, CA, Urban Water Management Plans (available via data.ca.gov and individual providers) and an average of available Residential Gallons Per Capita per Day (R-GPCD) data (available through the California State Water Resources Control Board (CSWRCB)) were used. Within the EnviroAtlas community boundary, provider estimates range from 57 to 101 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{61b300b9-6fa1-4929-b512-732435a53d1c}",
+            "issued": "2019-02-25",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -274663,46 +274682,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-02-25",
+            "programCode": [
+                "020:072"
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
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Domestic Water Demand per Day by U.S. Census Block Group"
         },
-            "identifier": "{61b300b9-6fa1-4929-b512-732435a53d1c}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-02-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f23e11e5-03a2-4502-aae7-bd5da1b5bf80}",
+            "issued": "2018-11-05",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -274718,46 +274737,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{f23e11e5-03a2-4502-aae7-bd5da1b5bf80}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Sonoma County, CA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e310bcdb-0937-4810-93c8-33210272039e}",
+            "issued": "2018-09-25",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -274781,46 +274800,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-25",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{e310bcdb-0937-4810-93c8-33210272039e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-25",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2eca67fd-55bf-41f8-bece-2cedbb541748}",
+            "issued": "2018-11-05",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -274835,46 +274854,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Greenspace Proximity Gradient"
         },
-            "identifier": "{2eca67fd-55bf-41f8-bece-2cedbb541748}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-05",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d27ce7c6-2ed2-45cd-89f2-4ab7cf73503c}",
+            "issued": "2018-12-07",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -274890,46 +274909,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-12-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Historic Places by Census Block Group"
         },
-            "identifier": "{d27ce7c6-2ed2-45cd-89f2-4ab7cf73503c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-12-07",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{66429674-bbfd-4fcd-a33f-7ad0e8638279}",
+            "issued": "2018-11-06",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -274943,46 +274962,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Impervious Proximity Gradient"
         },
-            "identifier": "{66429674-bbfd-4fcd-a33f-7ad0e8638279}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cb1d04bd-b992-44f2-ae27-655e9819bff9}",
+            "issued": "2018-09-24",
             "keyword": [
                 "Ecosystem Services",
                 "Health",
@@ -274997,46 +275016,46 @@
                 "Transportation",
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
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{cb1d04bd-b992-44f2-ae27-655e9819bff9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2011-01-01/2011-01-01",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 386 block groups in Sonoma County, CA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 386 block groups in Sonoma County, CA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a6056198-43dc-4d8c-86a8-2bb49781c50b}",
+            "issued": "2018-12-13",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -275055,46 +275074,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-12-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Ecosystem Services by Block Group"
         },
-            "identifier": "{a6056198-43dc-4d8c-86a8-2bb49781c50b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-12-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, Orchards, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture and Orchards. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, Orchards, and Woody Wetlands. Green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture and Orchards. Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{09df2061-bd30-4d4c-aaad-0c392d8f802d}",
+            "issued": "2019-02-06",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275110,46 +275129,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
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
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Land Cover by Block Group"
         },
-            "identifier": "{09df2061-bd30-4d4c-aaad-0c392d8f802d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
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
+            "description": "The EnviroAtlas Sonoma County, CA Meter-scale Urban Land Cover (MULC) data were generated from four-band (red, green, blue, and near infrared) aerial photography and LiDAR data at 6-inch spatial resolution, collected in late 2013, as well as ancillary vector data (e.g., roads, agriculture, wetlands) provided by the Sonoma County Vegetation Mapping and LiDAR Program (http://Sonomavegmap.org). Ten land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, shrub, grass-herbaceous non-woody vegetation, agriculture, orchards, as well as woody wetlands and emergent herbaceous wetlands. An accuracy assessment of 629 completely random and 176 stratified random photo-interpreted reference points yielded an overall MAX accuracy of 79 percent and an overall RIGHT accuracy of 80 percent (See overview section for more details on accuracy assessment). The area mapped is Sonoma County, CA. This dataset was produced by the Sonoma County Vegetation Mapping and LiDAR Program and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Meter-Scale Urban Land Cover (MULC) Data (2013)",
-            "description": "The EnviroAtlas Sonoma County, CA Meter-scale Urban Land Cover (MULC) data were generated from four-band (red, green, blue, and near infrared) aerial photography and LiDAR data at 6-inch spatial resolution, collected in late 2013, as well as ancillary vector data (e.g., roads, agriculture, wetlands) provided by the Sonoma County Vegetation Mapping and LiDAR Program (http://Sonomavegmap.org). Ten land cover classes were mapped: water, impervious surfaces, soil and barren land, trees, shrub, grass-herbaceous non-woody vegetation, agriculture, orchards, as well as woody wetlands and emergent herbaceous wetlands. An accuracy assessment of 629 completely random and 176 stratified random photo-interpreted reference points yielded an overall MAX accuracy of 79 percent and an overall RIGHT accuracy of 80 percent (See overview section for more details on accuracy assessment). The area mapped is Sonoma County, CA. This dataset was produced by the Sonoma County Vegetation Mapping and LiDAR Program and the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b5bdc84c-02f4-4768-93a9-49755acb5808}",
+            "issued": "2018-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "California",
@@ -275172,46 +275191,46 @@
                 "Agriculture",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.565396, 37.865670, -122.276940, 39.248379",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Meter-Scale Urban Land Cover (MULC) Data (2013)"
         },
-            "identifier": "{b5bdc84c-02f4-4768-93a9-49755acb5808}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.565396, 37.865670, -122.276940, 39.248379",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-05",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9e414fa7-d021-41bc-9a39-b4ea3800f01f}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -275229,46 +275248,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{9e414fa7-d021-41bc-9a39-b4ea3800f01f}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{39300a70-6097-4226-8d18-a2883c65863a}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -275287,46 +275306,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{39300a70-6097-4226-8d18-a2883c65863a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{713c26cb-deae-4e0c-949f-93e40b33c3c0}",
+            "issued": "2018-09-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -275341,46 +275360,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Park Access by Block Group"
         },
-            "identifier": "{713c26cb-deae-4e0c-949f-93e40b33c3c0}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
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
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5f7d20ba-cd99-4671-bece-0aace9d94d57}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -275394,46 +275413,46 @@
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
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Proximity to Parks"
         },
-            "identifier": "{5f7d20ba-cd99-4671-bece-0aace9d94d57}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
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
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SonomaCountyCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sonoma County, CA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Agriculture, Orchards, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c8c8a916-5414-4ae8-9902-5cd20075976c}",
+            "issued": "2018-10-27",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -275451,46 +275470,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-10-27",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{c8c8a916-5414-4ae8-9902-5cd20075976c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-10-27",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{92f1d7f7-6a6e-4e61-8c81-52e4e49d6bce}",
+            "issued": "2018-10-27",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -275508,46 +275527,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-10-27",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{92f1d7f7-6a6e-4e61-8c81-52e4e49d6bce}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-10-27",
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
-            "title": "EnviroAtlas - Sonoma County, CA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8c68de76-baad-4c92-a64d-001d94002d39}",
+            "issued": "2018-09-07",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275567,46 +275586,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{8c68de76-baad-4c92-a64d-001d94002d39}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-07",
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
-            "title": "EnviroAtlas - Sonoma County, CA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8d5ac29d-ed96-434e-b6b4-a7218a79d507}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275626,46 +275645,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{8d5ac29d-ed96-434e-b6b4-a7218a79d507}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{58afbccf-7941-416e-81c1-146152cf5e58}",
+            "issued": "2018-09-07",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275685,46 +275704,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{58afbccf-7941-416e-81c1-146152cf5e58}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-07",
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
-            "title": "EnviroAtlas - Sonoma County, CA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{bb93bdab-0d01-44cf-b2d9-8ab04a208db4}",
+            "issued": "2018-09-07",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275744,46 +275763,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{bb93bdab-0d01-44cf-b2d9-8ab04a208db4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Shrubs, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{faabf24b-7fce-406f-b141-61680b85ff6c}",
+            "issued": "2018-09-06",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275804,46 +275823,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{faabf24b-7fce-406f-b141-61680b85ff6c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-09-06",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, Orchards, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{adb8983a-f33a-4a74-9fff-afe6515079d9}",
+            "issued": "2018-11-05",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -275861,46 +275880,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-11-05",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{adb8983a-f33a-4a74-9fff-afe6515079d9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-11-05",
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
-            "title": "EnviroAtlas - Sonoma County, CA - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d8389a26-4f3e-4257-8eb1-a7c6aea067a9}",
+            "issued": "2018-10-30",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -275916,46 +275935,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-10-30",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
+            "temporal": "2013-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Sonoma County, CA - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{d8389a26-4f3e-4257-8eb1-a7c6aea067a9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-123.53196, 38.07387, -122.34041, 38.85106",
-            "temporal": "2013-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2018-10-30",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a point feature class showing the locations of stream confluences, with attributes showing indices of ecological integrity in the upstream catchments and watersheds of stream confluences and the results of a cluster analysis of these indices. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Map Data",
-            "description": "This EnviroAtlas dataset is a point feature class showing the locations of stream confluences, with attributes showing indices of ecological integrity in the upstream catchments and watersheds of stream confluences and the results of a cluster analysis of these indices. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8c2c2741-2a96-4933-8e77-cf9613e7f33a}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -276015,46 +276034,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Map Data"
         },
-            "identifier": "{8c2c2741-2a96-4933-8e77-cf9613e7f33a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset contains information about stressors in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Stressors for stream confluence catchments for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about stressors in the upstream catchments of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9e0fd4f8-ddb1-4d70-b78e-613bec653d4e}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -276114,46 +276133,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Stressors for stream confluence catchments for the Conterminous United States"
         },
-            "identifier": "{9e0fd4f8-ddb1-4d70-b78e-613bec653d4e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset contains information about stressors in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Stream Confluence Dataset - Stressors for stream confluence watersheds for the Conterminous United States",
-            "description": "This EnviroAtlas dataset contains information about stressors in the upstream watersheds of stream confluences. Stream confluences are important components of fluvial networks. Hydraulic forces meeting at stream confluences often produce changes in streambed morphology and sediment distribution, and these changes often increase habitat heterogeneity relative to upstream and downstream locations. Increases in habitat heterogeneity at stream confluences have led some to identify them as biological hotspots. Despite their potential ecological importance, there are relatively few empirical studies documenting ecological patterns across the upstream-confluence-downstream gradient. To facilitate more studies of the ecological value and role of stream confluences in fluvial networks, we have produced a database of stream confluences and their associated watershed attributes for the conterminous United States. The database includes 1,085,629 stream confluences and 383 attributes for each confluence that are organized into 15 database tables for both tributary and mainstem upstream catchments (\"local\" watersheds) and watersheds. Themes represented by the database tables include hydrology (e.g., stream order), land cover and land cover change, geology (e.g., calcium content of underlying lithosphere), physical condition (e.g., precipitation), measures of ecological integrity, and stressors (e.g., impaired streams). We use measures of ecological integrity (Thornbrugh et al. 2018) from the StreamCat database (Hill et al. 2016) to classify stream confluences using disjoint clustering and validate the cluster results using decision tree analysis. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6318c4f6-26f6-4e9c-bf84-55a8dc3bf181}",
+            "issued": "2020-09-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -276213,46 +276232,46 @@
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
+            "title": "EnviroAtlas - Stream Confluence Dataset - Stressors for stream confluence watersheds for the Conterminous United States"
         },
-            "identifier": "{6318c4f6-26f6-4e9c-bf84-55a8dc3bf181}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 526 block groups in Tacoma, Washington. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Tacoma, WA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the US Forest Service to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Other",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 526 block groups in Tacoma, Washington. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Tacoma, WA. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the US Forest Service to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6f1faef8-0469-4323-9734-4d584944e824}",
+            "issued": "2021-02-08",
             "keyword": [
                 "Exposure",
                 "Tacoma, WA",
@@ -276272,47 +276291,47 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-02-08",
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
-            },
-            "identifier": "{6f1faef8-0469-4323-9734-4d584944e824}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-122.779859, 46.848943, -121.889940, 47.413195",
             "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-02-08",
-            "language": "en-us",
             "theme": "environment",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "EnviroAtlas - Tacoma, WA - BenMAP Results by Block Group"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Tacoma, WA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
-            "keyword": [
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
+            "description": "This EnviroAtlas dataset is the base layer for the Tacoma, WA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SanDiegoCA",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{964a2872-70b1-4d65-8236-b2e15567527a}",
+            "issued": "2022-07-06",
+            "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
                 "Washington",
@@ -276324,46 +276343,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Census Block Groups"
         },
-            "identifier": "{964a2872-70b1-4d65-8236-b2e15567527a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/SanDiegoCA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7080b12f-43fd-405a-9c8c-65c17f54f668}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Human",
@@ -276380,46 +276399,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Tacoma, WA - Demographics by Block Group"
         },
-            "identifier": "{7080b12f-43fd-405a-9c8c-65c17f54f668}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Tacoma, WA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Tacoma, WA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{817131b6-17b8-40d7-a6a6-5fd71a2fd94f}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276432,46 +276451,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - EnviroAtlas Community Boundary"
         },
-            "identifier": "{817131b6-17b8-40d7-a6a6-5fd71a2fd94f}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Water use estimates in this EnviroAtlas-defined study area range from 84 to 110 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Water use estimates in this EnviroAtlas-defined study area range from 84 to 110 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{235e7026-c86e-44fb-8f87-eb74f0511564}",
+            "issued": "2015-05-26",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276491,46 +276510,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-05-26",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{235e7026-c86e-44fb-8f87-eb74f0511564}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-05-26",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0bcd404d-0a0f-4b61-930f-7c893c8c8d72}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276546,46 +276565,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{0bcd404d-0a0f-4b61-930f-7c893c8c8d72}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b401cc48-2ab3-46ef-bf3c-59fa9e274226}",
+            "issued": "2022-11-16",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -276609,46 +276628,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-16",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{b401cc48-2ab3-46ef-bf3c-59fa9e274226}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-11-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{408f3030-63b6-4682-857d-58f7bfc7befc}",
+            "issued": "2022-07-13",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276663,46 +276682,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-13",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2013-11-05/2013-11-05",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Greenspace Proximity Gradient"
         },
-            "identifier": "{408f3030-63b6-4682-857d-58f7bfc7befc}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2013-11-05/2013-11-05",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA- Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{955f42bb-f540-43c1-bf7f-919af9ee213e}",
+            "issued": "2022-07-13",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276718,46 +276737,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-13",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA- Historic Places by Census Block Group"
         },
-            "identifier": "{955f42bb-f540-43c1-bf7f-919af9ee213e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6b944886-37da-401f-bd91-a6677dcf64c1}",
+            "issued": "2022-07-13",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276771,46 +276790,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-13",
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
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2013-11-05/2013-11-05",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Impervious Proximity Gradient"
         },
-            "identifier": "{6b944886-37da-401f-bd91-a6677dcf64c1}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2013-11-05/2013-11-05",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 526 block groups in Tacoma, Washington. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the US Forest Service to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 526 block groups in Tacoma, Washington. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the US Forest Service to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{861d61bf-5b7e-4e48-97b6-510c96115f9e}",
+            "issued": "2021-03-17",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276829,46 +276848,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2021-03-17",
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
+            "spatial": "-122.779859, 46.848943, -121.889940, 47.413195",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Ecosystem Services by Block Group"
         },
-            "identifier": "{861d61bf-5b7e-4e48-97b6-510c96115f9e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.779859, 46.848943, -121.889940, 47.413195",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2021-03-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{af294d26-bc74-48a5-8506-30a2219be65b}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -276884,46 +276903,48 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Land Cover by Block Group"
         },
-            "identifier": "{af294d26-bc74-48a5-8506-30a2219be65b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Tacoma, WA Meter Urban Land Cover (MULC) dataset was generated from 1-meter image pixel resolution data sourced from 2011 USDA National Agricultural Imagery Program (NAIP) four band (red, green, blue and near infrared) aerial ortho-imagery. LiDAR point density data (9/m^2 point spacing), available for years 2010 and 2011, was used to map most areas of Pierce County, and supplemental LiDAR data, available for earlier years, was used to map area segments where 2010-2011 LiDAR data was not available.  A 7-band stack consisting of 1-meter, four-band (red, green, blue, and near-infrared) aerial photography, Normalized Difference Vegetation Index (NDVI), and lidar-derived intensity and height above ground was created and primarily used to classify land cover using Genie Pro automated feature extraction software. Several ancillary datasets, such as hydrographic and transportation feature data, were edited in ArcGIS and integrated into the classification workflow.\n\nThe Tacoma, WA land cover dataset includes data for the Tacoma metropolitan area of Pierce County, WA, and encompasses a total approximate area of 1,995 square kilometers. The thematic landcover data is confined to areas included within the US Census Bureau's 2010 Urban Statistical area boundaries for Pierce County, WA, with an additional 1km buffer extension that include bits of Kitsap, King and Thurston Counties.\n\nThe following seven land cover classes were mapped: Water, Impervious, Soil or Barren, Trees or Forest, Grass or Herbaceous, Woody Wetlands and Emergent Wetlands.\n\nMapped water bodies were generated using combined high-resolution LiDAR and ancillary hydrological data.\n\nIntegrated wetland features were derived using ancillary National Wetlands Inventory (NWI) polygon data (version 2), downloaded from the Unites States Fish and Wildlife Service (USFWS) Wetland Mapper web mapping service (https://www.fws.gov/wetlands/data/mapper.html). Metadata for the NWI wetlands data layer can be found at http://www.fws.gov/wetlands/Data/Metadata.html.\n\nAn accuracy assessment of the classified product, using 482 completely random and 46 (Soil/Barren) stratified random photo-interpreted land cover reference sample points yielded an overall user's accuracy (MAX) of 85.1 percent and a fuzzy user's accuracy (RIGHT) of 86.9 percent.\n\nFor data workflow processing details see Overview Description section.\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (http://enviroatlas.epa.gov/EnviroAtlas/DataFactSheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Tacoma, WA -- Meter-Scale Urban Land Cover (MULC) Data (2011)",
-            "description": "The Tacoma, WA Meter Urban Land Cover (MULC) dataset was generated from 1-meter image pixel resolution data sourced from 2011 USDA National Agricultural Imagery Program (NAIP) four band (red, green, blue and near infrared) aerial ortho-imagery. LiDAR point density data (9/m^2 point spacing), available for years 2010 and 2011, was used to map most areas of Pierce County, and supplemental LiDAR data, available for earlier years, was used to map area segments where 2010-2011 LiDAR data was not available.  A 7-band stack consisting of 1-meter, four-band (red, green, blue, and near-infrared) aerial photography, Normalized Difference Vegetation Index (NDVI), and lidar-derived intensity and height above ground was created and primarily used to classify land cover using Genie Pro automated feature extraction software. Several ancillary datasets, such as hydrographic and transportation feature data, were edited in ArcGIS and integrated into the classification workflow.\n\nThe Tacoma, WA land cover dataset includes data for the Tacoma metropolitan area of Pierce County, WA, and encompasses a total approximate area of 1,995 square kilometers. The thematic landcover data is confined to areas included within the US Census Bureau's 2010 Urban Statistical area boundaries for Pierce County, WA, with an additional 1km buffer extension that include bits of Kitsap, King and Thurston Counties.\n\nThe following seven land cover classes were mapped: Water, Impervious, Soil or Barren, Trees or Forest, Grass or Herbaceous, Woody Wetlands and Emergent Wetlands.\n\nMapped water bodies were generated using combined high-resolution LiDAR and ancillary hydrological data.\n\nIntegrated wetland features were derived using ancillary National Wetlands Inventory (NWI) polygon data (version 2), downloaded from the Unites States Fish and Wildlife Service (USFWS) Wetland Mapper web mapping service (https://www.fws.gov/wetlands/data/mapper.html). Metadata for the NWI wetlands data layer can be found at http://www.fws.gov/wetlands/Data/Metadata.html.\n\nAn accuracy assessment of the classified product, using 482 completely random and 46 (Soil/Barren) stratified random photo-interpreted land cover reference sample points yielded an overall user's accuracy (MAX) of 85.1 percent and a fuzzy user's accuracy (RIGHT) of 86.9 percent.\n\nFor data workflow processing details see Overview Description section.\n\nThis dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (http://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (http://enviroatlas.epa.gov/EnviroAtlas/DataFactSheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services/Supplemental/Landcover_AllCommunities/ImageServer"
+                }
+            ],
+            "identifier": "A0DFB8D1-96E9-4DFE-BF08-65485735A3B4",
+            "issued": "2022-04-14",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -276950,46 +276971,44 @@
                 "Communities",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-07-28",
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
+            "spatial": "-122.779872, 46.848943, -121.88994, 47.413204",
+            "temporal": "2011-01-01T00:00:00/2011-12-31T00:00:00",
+            "title": "EnviroAtlas -- Tacoma, WA -- Meter-Scale Urban Land Cover (MULC) Data (2011)"
         },
-            "identifier": "A0DFB8D1-96E9-4DFE-BF08-65485735A3B4",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-122.779872, 46.848943, -121.88994, 47.413204",
-            "temporal": "2011-01-01T00:00:00/2011-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-04-14",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services/Supplemental/Landcover_AllCommunities/ImageServer"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Estimated Tree Cover Along Busy Roads",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{2e28394c-0c2e-456c-a567-554eebf5954c}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277007,46 +277026,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{2e28394c-0c2e-456c-a567-554eebf5954c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Tree Cover Along Walkable Roads by Block Group",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{342f4d0e-289d-4c96-a6f3-2035f03fe394}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277065,46 +277084,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Tree Cover Along Walkable Roads by Block Group"
         },
-            "identifier": "{342f4d0e-289d-4c96-a6f3-2035f03fe394}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. green space is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{d903e923-cd6f-4a12-a203-393e822396da}",
+            "issued": "2022-06-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277122,46 +277141,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-06-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{d903e923-cd6f-4a12-a203-393e822396da}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-06-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{eb63c43d-4057-4dcd-aae5-95ff9429c068}",
+            "issued": "2022-06-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277179,46 +277198,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-06-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{eb63c43d-4057-4dcd-aae5-95ff9429c068}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-06-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b96a9dba-c5d9-41c8-aba0-da80c0a2fd55}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277238,46 +277257,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{b96a9dba-c5d9-41c8-aba0-da80c0a2fd55}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{da76f00e-3959-4057-b4c5-c7de90ed940c}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277297,46 +277316,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{da76f00e-3959-4057-b4c5-c7de90ed940c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ba1d230f-36fd-43f8-9d5f-cc4045fe4d7e}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277356,46 +277375,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{ba1d230f-36fd-43f8-9d5f-cc4045fe4d7e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c06c0a42-4d4f-4b2a-868d-1f305eef6b64}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277415,46 +277434,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{c06c0a42-4d4f-4b2a-868d-1f305eef6b64}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3696b31c-44c2-4286-9c0d-15e3d81882f6}",
+            "issued": "2022-07-07",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277475,46 +277494,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-07",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{3696b31c-44c2-4286-9c0d-15e3d81882f6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-07",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{87cc7d18-6410-4e86-9415-a8ca73f927f9}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277532,46 +277551,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development - Center for Public Health and Environmental Assessment CPHEA, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{87cc7d18-6410-4e86-9415-a8ca73f927f9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tacoma, WA - Residents with Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{e8600596-b594-49dc-b6b1-7d1d094657c6}",
+            "issued": "2022-07-06",
             "keyword": [
                 "Tacoma, WA",
                 "Ecosystem Services",
@@ -277587,46 +277606,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-07-06",
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
+            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tacoma, WA - Residents with Potential Window Views of Water by Block Group"
         },
-            "identifier": "{e8600596-b594-49dc-b6b1-7d1d094657c6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-122.76678, 46.86297, -121.90338, 47.39917",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-07-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,833 block groups in Tampa Bay, Florida. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TacomaWA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa Bay, FL - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1,833 block groups in Tampa Bay, Florida. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Cuyahoga, Geauga, Lake, Lorain, Medina, Portage, and Summit Counties, OH. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{75E1F73B-B20C-4F21-8DB6-BB5A6FCD7757}",
+            "issued": "2016-10-26",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -277646,46 +277665,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa Bay, FL - BenMAP Results by Block Group"
         },
-            "identifier": "{75E1F73B-B20C-4F21-8DB6-BB5A6FCD7757}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Tampa, FL EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Tampa, FL EnviroAtlas Area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A03EEABD-D4E1-4C79-A2A6-68F7B3437B51}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -277698,46 +277717,46 @@
                 "Environmental Atlas",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Block Groups"
         },
-            "identifier": "{A03EEABD-D4E1-4C79-A2A6-68F7B3437B51}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4417BC7A-793E-4C2C-8E4C-B27CF190E271}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -277754,46 +277773,46 @@
                 "Boundaries",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Tampa, FL - Demographics by Block Group"
         },
-            "identifier": "{4417BC7A-793E-4C2C-8E4C-B27CF190E271}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset shows the boundary of the Tampa, FL Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Atlas Area Boundary",
-            "description": "This EnviroAtlas dataset shows the boundary of the Tampa, FL Atlas Area. It represents the outside edge of all the block groups included in the EnviroAtlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{655B9FA6-40CE-40BF-A21F-EA2C94F5C6BC}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -277806,46 +277825,46 @@
                 "Boundaries",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2012-03-01/2012-03-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Atlas Area Boundary"
         },
-            "identifier": "{655B9FA6-40CE-40BF-A21F-EA2C94F5C6BC}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/research/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Tree Cover Configuration and Connectivity, Water Background",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, forest is trees & forest and woody wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/research/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{864118E7-7E57-4F1D-810D-A71D37C82DB2}",
+            "issued": "2015-05-20",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -277860,46 +277879,46 @@
                 "Environmental Atlas",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2015-03-24/2015-03-24",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Tree Cover Configuration and Connectivity, Water Background"
         },
-            "identifier": "{864118E7-7E57-4F1D-810D-A71D37C82DB2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Florida, oversight of water resources is handled by five water management districts, each comprised of a board of Governor-appointed volunteers. These Districts focus on water supply, flood protection, water quality, and natural system preservation. Tampa is in the Southwest Florida Water Management District (SWFWMD). Within the EnviroAtlas Tampa boundary, there are 67 service providers with 2003-2007 estimates ranging from 59 to 230 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use was calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). For the purposes of this metric, these publicly-supplied estimates are also applied and considered representative of local self-supplied water use. Specific to Florida, oversight of water resources is handled by five water management districts, each comprised of a board of Governor-appointed volunteers. These Districts focus on water supply, flood protection, water quality, and natural system preservation. Tampa is in the Southwest Florida Water Management District (SWFWMD). Within the EnviroAtlas Tampa boundary, there are 67 service providers with 2003-2007 estimates ranging from 59 to 230 GPD. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{AF009233-761D-4CFE-B22A-F94BCA66182B}",
+            "issued": "2014-10-31",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -277919,46 +277938,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{AF009233-761D-4CFE-B22A-F94BCA66182B}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F1E335DA-3895-4B33-A882-BEADF85CE918}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -277974,46 +277993,46 @@
                 "Environmental Atlas",
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-12/2013-04-12",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{F1E335DA-3895-4B33-A882-BEADF85CE918}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-12/2013-04-12",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{95626fc8-a7bf-419f-a93c-fb2728e12f2b}",
+            "issued": "2017-07-19",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -278037,46 +278056,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{95626fc8-a7bf-419f-a93c-fb2728e12f2b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{89AEB768-0338-4CF5-A46B-EC1B7A5B3924}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278091,46 +278110,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2015-03-19/2015-03-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Greenspace Proximity Gradient"
         },
-            "identifier": "{89AEB768-0338-4CF5-A46B-EC1B7A5B3924}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{E8A7E200-C10B-485D-AB2A-CC25CB5DB4FC}",
+            "issued": "2014-08-26",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278146,46 +278165,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Historic Places by Census Block Group"
         },
-            "identifier": "{E8A7E200-C10B-485D-AB2A-CC25CB5DB4FC}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{82565C20-0896-419B-A2E9-43421E19976C}",
+            "issued": "2015-05-14",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278199,46 +278218,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2015-03-26/2015-03-26",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Impervious Proximity Gradient"
         },
-            "identifier": "{82565C20-0896-419B-A2E9-43421E19976C}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2015-03-26/2015-03-26",
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
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{356EC846-7733-4AA3-8E0D-83DFA5AA2C52}",
+            "issued": "2019-06-19",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278253,46 +278272,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{356EC846-7733-4AA3-8E0D-83DFA5AA2C52}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,833 block groups in Tampa Bay, Florida. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1,833 block groups in Tampa Bay, Florida. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{DD093AC0-9827-446C-A2A7-0D22BC39DD4D}",
+            "issued": "2015-06-18",
             "keyword": [
                 "Ecosystem Services",
                 "Modeling",
@@ -278311,46 +278330,46 @@
                 "Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Ecosystem Services by Block Group"
         },
-            "identifier": "{DD093AC0-9827-446C-A2A7-0D22BC39DD4D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, wetland, and agriculture. Impervious is a combination of dark and light impervious. Forest is a combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands.This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of each block group that is classified as impervious, forest, green space, wetland, and agriculture. Impervious is a combination of dark and light impervious. Forest is a combination of trees and forest and woody wetlands. Green space is a combination of trees and forest, grass and herbaceous, agriculture, woody wetlands, and emergent wetlands. Wetlands includes both Woody and Emergent Wetlands.This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{CD8DBCBC-72C8-4ACD-817F-A497BA4B5E22}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -278367,46 +278386,46 @@
                 "Environmental Atlas",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-12/2013-04-12",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Land Cover by Block Group"
         },
-            "identifier": "{CD8DBCBC-72C8-4ACD-817F-A497BA4B5E22}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-12/2013-04-12",
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
+            "description": "The EnviroAtlas Tampa, FL Meter-Scale Urban Land Cover (MULC) data was generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from April-May 2010 at 1 m spatial resolution. Eight land cover classes were mapped: impervious surface, soil and barren, grass and herbaceous, trees and forest, water, agriculture, woody wetland, and emergent wetland. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Tampa, and includes the cities of Clearwater and St. Petersburg, as well as additional out-lying areas. An accuracy assessment using a stratified random sampling of 600 samples (100 per class) yielded an overall accuracy of 70.67 percent and an area weighted accuracy of 81.87 percent using a minimum mapping unit of 9 pixels (3x3 pixel window). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Tampa, FL -- Meter-Scale Urban Land Cover (MULC) Data (2010)",
-            "description": "The EnviroAtlas Tampa, FL Meter-Scale Urban Land Cover (MULC) data was generated from USDA NAIP (National Agricultural Imagery Program) four band (red, green, blue and near infrared) aerial photography from April-May 2010 at 1 m spatial resolution. Eight land cover classes were mapped: impervious surface, soil and barren, grass and herbaceous, trees and forest, water, agriculture, woody wetland, and emergent wetland. The area mapped is defined by the US Census Bureau's 2010 Urban Statistical Area for Tampa, and includes the cities of Clearwater and St. Petersburg, as well as additional out-lying areas. An accuracy assessment using a stratified random sampling of 600 samples (100 per class) yielded an overall accuracy of 70.67 percent and an area weighted accuracy of 81.87 percent using a minimum mapping unit of 9 pixels (3x3 pixel window). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{9AD339AD-9243-4EFB-A70B-E2471D96A23E}",
+            "issued": "2017-09-05",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -278429,46 +278448,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-04-01/2010-05-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Tampa, FL -- Meter-Scale Urban Land Cover (MULC) Data (2010)"
         },
-            "identifier": "{9AD339AD-9243-4EFB-A70B-E2471D96A23E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2010-04-01/2010-05-01",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Near Road Tree Buffer",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{F7B7E9EC-B189-4327-BBEA-C3734DFBD404}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Ecosystem Services",
                 "Air",
@@ -278486,46 +278505,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Near Road Tree Buffer"
         },
-            "identifier": "{F7B7E9EC-B189-4327-BBEA-C3734DFBD404}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. Forest is defined as Trees & Forest and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6F0C61B7-7BB9-4670-A69D-A789D7EBA97C}",
+            "issued": "2015-05-19",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278545,46 +278564,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Near Road Block Group Summary"
         },
-            "identifier": "{6F0C61B7-7BB9-4670-A69D-A789D7EBA97C}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5FC3F0F9-11FA-4D30-9964-E1D69F6EDF3B}",
+            "issued": "2015-11-10",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278599,46 +278618,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2015-10-05/2015-10-05",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Park Access by Block Group"
         },
-            "identifier": "{5FC3F0F9-11FA-4D30-9964-E1D69F6EDF3B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2015-10-05/2015-10-05",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{C17799CA-F743-4CE6-BC71-3D4C82E5F2BC}",
+            "issued": "2020-01-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -278652,46 +278671,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2014-08-20/2014-08-20",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Proximity to Parks"
         },
-            "identifier": "{C17799CA-F743-4CE6-BC71-3D4C82E5F2BC}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets ).",
+            ],
+            "identifier": "{791C9D8F-4F23-44F0-9F4B-E8256D66EE0B}",
+            "issued": "2015-12-02",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278709,46 +278728,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{791C9D8F-4F23-44F0-9F4B-E8256D66EE0B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{790D6F59-241C-40FD-B603-337A4CEA9299}",
+            "issued": "2015-08-07",
             "keyword": [
                 "Tampa, FL",
                 "Ecosystem Services",
@@ -278766,46 +278785,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{790D6F59-241C-40FD-B603-337A4CEA9299}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{432B30DD-DA4D-44BD-81C6-13BBD9FC3661}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -278825,46 +278844,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-26/2013-04-26",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{432B30DD-DA4D-44BD-81C6-13BBD9FC3661}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-26/2013-04-26",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{453A7D4C-80FC-4A22-8715-17BB566E9CDF}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -278884,46 +278903,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-26/2013-04-26",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{453A7D4C-80FC-4A22-8715-17BB566E9CDF}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-26/2013-04-26",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{82E64BD7-359B-41E6-8C2A-8F25C59A7B16}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -278943,46 +278962,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-26/2013-04-26",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{82E64BD7-359B-41E6-8C2A-8F25C59A7B16}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-26/2013-04-26",
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
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8CBCD2C4-15A5-41A2-88FD-DE098C2C1709}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -279002,46 +279021,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-26/2013-04-26",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{8CBCD2C4-15A5-41A2-88FD-DE098C2C1709}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-26/2013-04-26",
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
+            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of different land cover types within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the Atlas Area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{493C82A9-D0C3-41F1-BC25-C41F56C0FCA8}",
+            "issued": "2014-08-13",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -279062,46 +279081,46 @@
                 "Drinking Water",
                 "Florida"
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2013-04-19/2013-04-19",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{493C82A9-D0C3-41F1-BC25-C41F56C0FCA8}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
-            "temporal": "2013-04-19/2013-04-19",
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
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Residents with Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees & forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{66FE1B8E-FE35-4BF5-8960-F4BF406FAA9A}",
+            "issued": "2014-06-17",
             "keyword": [
                 "Ecosystem Services",
                 "Natural Resources",
@@ -279119,46 +279138,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-06-17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Environmental Protection Agency, Research Triangle Park"
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
-            },
-            "identifier": "{66FE1B8E-FE35-4BF5-8960-F4BF406FAA9A}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Environmental Protection Agency, Research Triangle Park"
+            },
             "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
             "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
             "temporal": "2014-06-10/2014-06-10",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Residents with Potential Window Views of Trees by Block Group"
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
-            "issued": "2014-06-17",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of waterbodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Tampa, FL - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of waterbodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The residential locations are defined using the EnviroAtlas Dasymetric (2011 version) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas ) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{72A68A05-3DAF-4B0C-A93B-7CBCFAE352DE}",
+            "issued": "2013-10-24",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -279174,46 +279193,46 @@
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
+            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
+            "temporal": "2014-06-10/2014-06-10",
+            "theme": "environment",
+            "title": "EnviroAtlas - Tampa, FL - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{72A68A05-3DAF-4B0C-A93B-7CBCFAE352DE}",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-82.851123, 27.651249, -82.056207, 28.418373",
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
+            "description": "This EnviroAtlas dataset is a summary of the thermoelectric water consumption based on the December 2016 US Energy Information Administration (EIA) monthly electric generator inventory, a 2014 review of water consumption for electricity generation (Macknick et al.), and reported water consumption estimates from a 2009 Department of Energy (DOE) report. The file contains total water withdrawal and consumption in gallons per year by 12-digit hydrologic unit codes (HUC_12s) from the boundary file named NHDPlusV2_WBDSnapshot_EnviroAtlas_CONUS. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/TampaFL",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Thermoelectric Water Use by 12-Digit HUC for the Conterminous United States",
-            "description": "This EnviroAtlas dataset is a summary of the thermoelectric water consumption based on the December 2016 US Energy Information Administration (EIA) monthly electric generator inventory, a 2014 review of water consumption for electricity generation (Macknick et al.), and reported water consumption estimates from a 2009 Department of Energy (DOE) report. The file contains total water withdrawal and consumption in gallons per year by 12-digit hydrologic unit codes (HUC_12s) from the boundary file named NHDPlusV2_WBDSnapshot_EnviroAtlas_CONUS. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{A15BD49A-0C75-4E64-902B-581D89F7B8AC}",
+            "issued": "2017-03-20",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279278,46 +279297,46 @@
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
+            "temporal": "2016-01-01/2016-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Thermoelectric Water Use by 12-Digit HUC for the Conterminous United States"
         },
-            "identifier": "{A15BD49A-0C75-4E64-902B-581D89F7B8AC}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2017-03-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset includes the summed below ground live tree root dry biomass estimate by 12-digit Hydrologic Unit (HUC) in metric tons (megagrams) from the 2000 National Biomass and Carbon Dataset (Version 2.0) developed by the Woods Hole Research Center, released in October, 2012. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Below Ground Live Tree Biomass Carbon Storage by 12-Digit HUC for the Conterminous United States - Forested",
-            "description": "This EnviroAtlas dataset includes the summed below ground live tree root dry biomass estimate by 12-digit Hydrologic Unit (HUC) in metric tons (megagrams) from the 2000 National Biomass and Carbon Dataset (Version 2.0) developed by the Woods Hole Research Center, released in October, 2012. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0587242D-9CFC-460C-91B1-FC89B65AC66F}",
+            "issued": "2017-10-20",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279382,46 +279401,46 @@
                 "Pennsylvania",
                 "12-digit HUCs"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-10-20",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Below Ground Live Tree Biomass Carbon Storage by 12-Digit HUC for the Conterminous United States - Forested"
         },
-            "identifier": "{0587242D-9CFC-460C-91B1-FC89B65AC66F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-10-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset was produced by a joint effort of New Mexico State University, US Environmental Protection Agency (US EPA,) and the U.S. Geological Survey (USGS) to support research and online mapping activities related to EnviroAtlas. Ecosystem services, i.e., services provided to humans from ecological systems have become a key issue of this century in resource management, conservation planning, and environmental decision analysis. Mapping and quantifying ecosystem services have become strategic national interests for integrating ecology with economics to help understand the effects of human policies and actions and their subsequent impacts on both ecosystem function and human well-being. Some aspects of biodiversity are valued by humans in varied ways, and thus are important to include in any assessment that seeks to identify and quantify the benefits of ecosystems to humans. Some biodiversity metrics clearly reflect ecosystem services (e.g., abundance and diversity of harvestable species), whereas others may reflect indirect and difficult to quantify relationships to services (e.g., relevance of species diversity to ecosystem resilience, cultural and aesthetic values). Wildlife habitat has been modeled at broad spatial scales and can be used to map a number of biodiversity metrics. We map 15 biodiversity metrics reflecting ecosystem services or other aspects of biodiversity for all vertebrate species except fish. Metrics include species richness for all vertebrates, specific taxon groups, harvestable species (i.e., upland game, waterfowl, furbearers, small game, and big game), threatened and endangered species, and state-designated species of greatest conservation need, and also a metric for ecosystem (i.e., land cover) diversity. This dataset contains information on Reptile Species Richness, the number of reptile species per 12-digit Hydrologic Unit (HUC). The EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Total reptile species by 12-digit HUC for the conterminous United States",
-            "description": "This EnviroAtlas dataset was produced by a joint effort of New Mexico State University, US Environmental Protection Agency (US EPA,) and the U.S. Geological Survey (USGS) to support research and online mapping activities related to EnviroAtlas. Ecosystem services, i.e., services provided to humans from ecological systems have become a key issue of this century in resource management, conservation planning, and environmental decision analysis. Mapping and quantifying ecosystem services have become strategic national interests for integrating ecology with economics to help understand the effects of human policies and actions and their subsequent impacts on both ecosystem function and human well-being. Some aspects of biodiversity are valued by humans in varied ways, and thus are important to include in any assessment that seeks to identify and quantify the benefits of ecosystems to humans. Some biodiversity metrics clearly reflect ecosystem services (e.g., abundance and diversity of harvestable species), whereas others may reflect indirect and difficult to quantify relationships to services (e.g., relevance of species diversity to ecosystem resilience, cultural and aesthetic values). Wildlife habitat has been modeled at broad spatial scales and can be used to map a number of biodiversity metrics. We map 15 biodiversity metrics reflecting ecosystem services or other aspects of biodiversity for all vertebrate species except fish. Metrics include species richness for all vertebrates, specific taxon groups, harvestable species (i.e., upland game, waterfowl, furbearers, small game, and big game), threatened and endangered species, and state-designated species of greatest conservation need, and also a metric for ecosystem (i.e., land cover) diversity. This dataset contains information on Reptile Species Richness, the number of reptile species per 12-digit Hydrologic Unit (HUC). The EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{54A8FEC4-97C2-40D1-90FE-DA932E6B5EFE}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279488,46 +279507,48 @@
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
+            "temporal": "2013-03-25/2013-03-25",
+            "theme": "environment",
+            "title": "EnviroAtlas - Total reptile species by 12-digit HUC for the conterminous United States"
         },
-            "identifier": "{54A8FEC4-97C2-40D1-90FE-DA932E6B5EFE}",
+        {
+            "@type": "dcat:Dataset",
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
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with beef cows and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Only data regarding beef cows are displayed in this layer. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage beef cows, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Beef Cow Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with beef cows and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Only data regarding beef cows are displayed in this layer. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage beef cows, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                }
+            ],
+            "identifier": "7A57C3F6-4683-4EFC-9A13-8EA81AA8EEBB",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279602,31 +279623,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Beef Cow Operations by County"
         },
-            "identifier": "7A57C3F6-4683-4EFC-9A13-8EA81AA8EEBB",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations that sell broiler chickens and the number of heads they sell. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they sell. For each county and Census year, the dataset reports the number of farm operations that sell broiler chickens, the number of heads they sold throughout the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -279636,12 +279660,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Broiler Chicken Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations that sell broiler chickens and the number of heads they sell. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they sell. For each county and Census year, the dataset reports the number of farm operations that sell broiler chickens, the number of heads they sold throughout the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "E8B220EA-2935-4147-BE65-1ACAC6FF0DFA",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279716,31 +279737,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-01-01T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Broiler Chicken Operations by County"
         },
-            "identifier": "E8B220EA-2935-4147-BE65-1ACAC6FF0DFA",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-01-01T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations that sell calves and the number of heads they sell. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they sell. For each county and Census year, the dataset reports the number of farm operations that sell calves, the number of heads they sold throughout the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -279750,12 +279774,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Calf Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations that sell calves and the number of heads they sell. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they sell. For each county and Census year, the dataset reports the number of farm operations that sell calves, the number of heads they sold throughout the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "4DAFFE99-6892-4013-8FF8-DAF26DE31B2F",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279830,31 +279851,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-01-01T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Calf Operations by County"
         },
-            "identifier": "4DAFFE99-6892-4013-8FF8-DAF26DE31B2F",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-01-01T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with cattle and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Data regarding all three categories are displayed in this layer. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage cattle, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -279864,12 +279888,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Cattle Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with cattle and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Data regarding all three categories are displayed in this layer. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage cattle, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "C9412C2D-3645-4C19-9B12-EC05A256881C",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -279944,31 +279965,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Cattle Operations by County"
         },
-            "identifier": "C9412C2D-3645-4C19-9B12-EC05A256881C",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with dairy cows and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Only data regarding dairy cows are displayed in this layer.  Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage dairy cows, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -279978,12 +280002,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Dairy Cow Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with dairy cows and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. The Census classifies cattle managed on operations as beef cows, dairy cows, or other cattle (which encompasses heifers, steers, bulls, and calves). Only data regarding dairy cows are displayed in this layer.  Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage dairy cows, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "667406AE-A97D-4614-B8DF-12E54D7A3D04",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280058,31 +280079,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Dairy Cow Operations by County"
         },
-            "identifier": "667406AE-A97D-4614-B8DF-12E54D7A3D04",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with ducks and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage ducks and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280092,12 +280116,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Duck Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with ducks and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage ducks and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "65316ECA-324E-418C-A608-8D94CE5245D3",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280172,31 +280193,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Duck Operations by County"
         },
-            "identifier": "65316ECA-324E-418C-A608-8D94CE5245D3",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with horses and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage horses and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280206,12 +280230,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Horse Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with horses and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage horses and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "C43C8699-7879-4B9F-8D6F-6F619A4B2F0B",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280285,31 +280306,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Horse Operations by County"
         },
-            "identifier": "C43C8699-7879-4B9F-8D6F-6F619A4B2F0B",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with laying hens and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage laying hens, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280319,12 +280343,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Laying Hen Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with laying hens and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage laying hens, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "7B34A45A-EBF2-4C27-BEE6-B597C67AA7A9",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280399,31 +280420,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Laying Hen Operations by County"
         },
-            "identifier": "7B34A45A-EBF2-4C27-BEE6-B597C67AA7A9",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with sheep and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage sheep, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280433,12 +280457,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Sheep Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with sheep and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage sheep, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "512A5873-0983-40EE-9765-2043C82444CD",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280512,31 +280533,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Sheep Operations by County"
         },
-            "identifier": "512A5873-0983-40EE-9765-2043C82444CD",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with swine and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage swine, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280546,12 +280570,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Swine Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with swine and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. Operations are categorized into small, medium, or large, based on how many heads they manage. For each county and Census year, the dataset reports the number of farm operations that manage swine, the number of heads on their property at the end of the Census year, and a breakdown of the operations into small, medium, and large. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "D4360D3B-3E0E-4B8A-B995-9D8964424198",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280626,31 +280647,34 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Swine Operations by County"
         },
-            "identifier": "D4360D3B-3E0E-4B8A-B995-9D8964424198",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with turkeys and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage turkeys and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -280660,12 +280684,9 @@
                     "@type": "dcat:Distribution",
                     "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Turkey Operations by County",
-            "description": "This EnviroAtlas dataset summarizes by county the number of farm operations with turkeys and the number of heads they manage. The data come from the Census of Agriculture, which is administered every five years by the US Department of Agriculture (USDA), and include the years 2002, 2007, 2012, and 2017. For each county and Census year, the dataset reports the number of farm operations that manage turkeys and the number of heads on their property at the end of the Census year. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "14333F2D-4870-4407-96EE-DD5D90A8C8F3",
+            "issued": "2022-03-14",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -280740,46 +280761,44 @@
                 "Alaska",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-01-26",
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
+            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
+            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
+            "title": "EnviroAtlas - Turkey Operations by County"
         },
-            "identifier": "14333F2D-4870-4407-96EE-DD5D90A8C8F3",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-179.14734, 18.917466, -66.949895, 71.352561",
-            "temporal": "2002-12-31T00:00:00/2002-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2022-03-14",
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1057 block groups in Virginia Beach/Williamsburg, VA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for the cities of Chesapeake, Hampton, Newport News, Norfolk, Poquoson, Portsmouth, Suffolk, Virgina Beach, and Williamsburg; and Charles City, Gloucester, Isle of Wight, James City, Surry, and York Counties, Virginia. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/EnviroAtlas/National/"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://enviroatlas.epa.gov/arcgis/rest/services"
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 1057 block groups in Virginia Beach/Williamsburg, VA. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for the cities of Chesapeake, Hampton, Newport News, Norfolk, Poquoson, Portsmouth, Suffolk, Virgina Beach, and Williamsburg; and Charles City, Gloucester, Isle of Wight, James City, Surry, and York Counties, Virginia. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4743fe7e-942e-4bb5-b161-c98395b217ac}",
+            "issued": "2017-11-29",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Exposure",
@@ -280799,46 +280818,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2000-01-01/2000-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - BenMAP Results by Block Group"
         },
-            "identifier": "{4743fe7e-942e-4bb5-b161-c98395b217ac}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2000-01-01/2000-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is the base layer for the Virginia Beach/Williamsburg, VA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Virginia Beach/Williamsburg, VA EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{bb9325b7-c94b-4db5-a4ae-4f0e200f6168}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -280851,46 +280870,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Block Groups"
         },
-            "identifier": "{bb9325b7-c94b-4db5-a4ae-4f0e200f6168}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0c2e9d5f-337f-4289-92ec-92ac2631cfff}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Human",
@@ -280907,46 +280926,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Demographics by Block Group"
         },
-            "identifier": "{0c2e9d5f-337f-4289-92ec-92ac2631cfff}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Virginia Beach/Williamsburg, VA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Virginia Beach/Williamsburg, VA EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{714edeba-8202-40e6-b738-72fd64ccd8e6}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -280959,46 +280978,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2017-06-29/2017-06-29",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - EnviroAtlas Community Boundary"
         },
-            "identifier": "{714edeba-8202-40e6-b738-72fd64ccd8e6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2017-06-29/2017-06-29",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{93cb0173-447e-486d-a286-346f3defd685}",
+            "issued": "2019-11-20",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281014,46 +281033,46 @@
                 "EnviroAtlas",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-11-20",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.86916, 36.53924, -75.87687, 37.41207",
+            "temporal": "2013-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{93cb0173-447e-486d-a286-346f3defd685}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.86916, 36.53924, -75.87687, 37.41207",
-            "temporal": "2013-01-01/2014-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-11-20",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The 2011 Hampton Roads Water Supply Plan estimates for 2007 domestic water use were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 47 and 124 GPD for each of the 13 subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach, VA - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). The 2011 Hampton Roads Water Supply Plan estimates for 2007 domestic water use were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 47 and 124 GPD for each of the 13 subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3890bacf-de41-47fc-8e33-9bea128d5332}",
+            "issued": "2015-09-18",
             "keyword": [
                 "Ecosystem Services",
                 "Virginia",
@@ -281073,46 +281092,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2015-09-18",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.886426, 36.550453, -75.867044, 37.401501",
+            "temporal": "9999-01-01/9999-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach, VA - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{3890bacf-de41-47fc-8e33-9bea128d5332}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.886426, 36.550453, -75.867044, 37.401501",
-            "temporal": "9999-01-01/9999-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2015-09-18",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1719e72a-0067-4d87-9a8c-078255193831}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281128,46 +281147,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{1719e72a-0067-4d87-9a8c-078255193831}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c0520b68-30c1-4d72-b208-726ec081bc60}",
+            "issued": "2017-12-21",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -281191,46 +281210,46 @@
                 "Communities",
                 "Flood"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-12-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{c0520b68-30c1-4d72-b208-726ec081bc60}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2017-01-30/2017-01-30",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-12-21",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Green Space Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4b7c2ba4-4c40-4766-a84f-c5486c6204f3}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281245,46 +281264,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Green Space Proximity Gradient"
         },
-            "identifier": "{4b7c2ba4-4c40-4766-a84f-c5486c6204f3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{7da9c116-87db-458a-95e3-fb9c6c763833}",
+            "issued": "2017-08-01",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281300,46 +281319,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-08-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.886426, 36.550453, -75.867044, 37.401501",
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Historic Places by Census Block Group"
         },
-            "identifier": "{7da9c116-87db-458a-95e3-fb9c6c763833}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.886426, 36.550453, -75.867044, 37.401501",
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-08-01",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{5f1f469a-0e2e-44a9-bd84-e0208fab84d5}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281353,46 +281372,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Impervious Proximity Gradient"
         },
-            "identifier": "{5f1f469a-0e2e-44a9-bd84-e0208fab84d5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Intersection Density of Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates the intersection density of walkable roads within a 750 meter radius of any given 10 meter pixel in the community. Intersections are defined as any point where 3 or more roads meet and density is calculated using kernel density, where closer intersections are weighted higher than further intersections. Intersection density is highly correlated with walking for transportation. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3ff033c2-1d11-4dbf-aea7-f8bb8244bcc3}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281407,46 +281426,46 @@
                 "Transportation",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Intersection Density of Walkable Roads"
         },
-            "identifier": "{3ff033c2-1d11-4dbf-aea7-f8bb8244bcc3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1057 block groups in Virginia Beach/Williamsburg, VA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Ecosystem Services by Block Group",
-            "description": "This EnviroAtlas dataset presents environmental benefits of the urban forest in 1057 block groups in Virginia Beach/Williamsburg, VA. Carbon attributes, temperature reduction, pollution removal and value, and runoff effects are calculated for each block group using i-Tree models (www.itreetools.org), local weather data, pollution data, EPA provided city boundary and land cover data, and U.S. Census derived block group boundary data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{eab1bf2c-216a-48db-aadf-bf86b4c74e9a}",
+            "issued": "2017-11-29",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281465,46 +281484,46 @@
                 "Climate",
                 "Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-11-29",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Ecosystem Services by Block Group"
         },
-            "identifier": "{eab1bf2c-216a-48db-aadf-bf86b4c74e9a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-11-29",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "\"This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Land Cover by Block Group",
-            "description": "\"This EnviroAtlas dataset describes the breakdown of the land cover classes with each Census Block Group. In this community, forest is defined as Trees & Forest, and Woody Wetlands. Green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Agriculture is defined as Agriculture alone.Wetlands are defined as Woody Wetlands and Emergent Wetlands. This dataset also includes the area per capita for each block group for some land cover types. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cff40031-bd71-4e16-a022-0229244b9f73}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281519,46 +281538,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Land Cover by Block Group"
         },
-            "identifier": "{cff40031-bd71-4e16-a022-0229244b9f73}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "The Virginia Beach, VA EnviroAtlas Meter-scale Urban Land Cover (MULC) dataset comprises 3,724 km2 of southeast Virginia and includes Hampton, Newport News, Suffolk, Virginia Beach and Williamsburg. The area was selected based on the US Census Bureau's 2010 Urban Area for Virginia Beach, VA with a 1 km buffer added. These MULC data and maps are an adaptation of data developed in succession by three organizations. First, WorldView Solutions Inc., a contractor of the Virginia Geographic Information Network (VGIN), created an original dataset for the state of Virginia that used 6 inch to 1 foot-resolution, four-band (red, green, blue, and near-infrared), leaf-off imagery collected in 2013 for the Virginia Base Mapping Program, as well as 2015 VGIN LiDAR, and ancillary data inputs. These data did not fully capture tree canopy. Second, the Chesapeake Conservancy amended the original dataset using 2014, leaf-on United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) and 2010 and 2013 LiDAR data. The amendments added some of the tree canopy missing from the original data. Third, EPA amended the data further by collapsing multiple land cover classes into the seven EnviroAtlas Meter-scale Urban Land Cover (MULC) classes, and making corrections to the Wetlands classes, also using 2010 and 2013 LiDAR. Seven land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forest, Grass/Herbaceous Non-Woody Vegetation, Agriculture (Cultivated Crops) and Wetlands (Woody and Emergent). An analysis of 712 photo-interpreted land cover reference points yielded an overall user's accuracy of 83.5% (MAX) and an overall fuzzy user's accuracy of 84.1% (RIGHT) (see confusion matrices below). This dataset was produced by Virginia Geographic Information Network and their contractor WorldView Solutions Inc. (WSI), in collaboration with the Chesapeake Bay High-Resolution Land Cover Project - a cooperative agreement between the Chesapeake Conservancy and the National Park Service. It was adapted by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://enviroatlas.epa.gov/EnviroAtlas/DataFactSheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas -- Virginia Beach/Williamsburg, VA -- Meter-Scale Urban Land Cover (MULC)",
-            "description": "The Virginia Beach, VA EnviroAtlas Meter-scale Urban Land Cover (MULC) dataset comprises 3,724 km2 of southeast Virginia and includes Hampton, Newport News, Suffolk, Virginia Beach and Williamsburg. The area was selected based on the US Census Bureau's 2010 Urban Area for Virginia Beach, VA with a 1 km buffer added. These MULC data and maps are an adaptation of data developed in succession by three organizations. First, WorldView Solutions Inc., a contractor of the Virginia Geographic Information Network (VGIN), created an original dataset for the state of Virginia that used 6 inch to 1 foot-resolution, four-band (red, green, blue, and near-infrared), leaf-off imagery collected in 2013 for the Virginia Base Mapping Program, as well as 2015 VGIN LiDAR, and ancillary data inputs. These data did not fully capture tree canopy. Second, the Chesapeake Conservancy amended the original dataset using 2014, leaf-on United States Department of Agriculture (USDA) National Agriculture Imagery Program (NAIP) and 2010 and 2013 LiDAR data. The amendments added some of the tree canopy missing from the original data. Third, EPA amended the data further by collapsing multiple land cover classes into the seven EnviroAtlas Meter-scale Urban Land Cover (MULC) classes, and making corrections to the Wetlands classes, also using 2010 and 2013 LiDAR. Seven land cover classes were mapped: Water, Impervious Surfaces, Soil/Barren, Tree/Forest, Grass/Herbaceous Non-Woody Vegetation, Agriculture (Cultivated Crops) and Wetlands (Woody and Emergent). An analysis of 712 photo-interpreted land cover reference points yielded an overall user's accuracy of 83.5% (MAX) and an overall fuzzy user's accuracy of 84.1% (RIGHT) (see confusion matrices below). This dataset was produced by Virginia Geographic Information Network and their contractor WorldView Solutions Inc. (WSI), in collaboration with the Chesapeake Bay High-Resolution Land Cover Project - a cooperative agreement between the Chesapeake Conservancy and the National Park Service. It was adapted by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://enviroatlas.epa.gov/EnviroAtlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://enviroatlas.epa.gov/EnviroAtlas/DataFactSheets).",
+            ],
+            "identifier": "{97ef08f1-4c48-499d-a5be-72b35824bc65}",
+            "issued": "2017-10-16",
             "keyword": [
                 "Ecosystem Services",
                 "Land Cover",
@@ -281581,46 +281600,46 @@
                 "Agriculture",
                 "Communities"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-10-16",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.901980, 36.530153, -75.855670, 37.421087",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas -- Virginia Beach/Williamsburg, VA -- Meter-Scale Urban Land Cover (MULC)"
         },
-            "identifier": "{97ef08f1-4c48-499d-a5be-72b35824bc65}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.901980, 36.530153, -75.855670, 37.421087",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-10-16",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "'This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Tree Cover Along Busy Roads",
-            "description": "'This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{dac224eb-d78d-43d1-8051-d1baa98e495c}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281638,46 +281657,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Tree Cover Along Busy Roads"
         },
-            "identifier": "{dac224eb-d78d-43d1-8051-d1baa98e495c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Near Road Block Group Summary",
-            "description": "This EnviroAtlas dataset addresses the tree buffer along heavily traveled roads. The roads are interstates, arterials, and collectors within the EnviroAtlas community boundary. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Sufficient tree bufferage is defined as 25% coverage within the circular moving window with a radius of 14.5m at any given point along the roadway. There are potential negative health affects for those living in a location without a sufficient tree buffer. Those populations are estimated here using dasymetric data calculated for the EnviroAtlas. There are potential negative health effects for those living in a location without a sufficient tree buffer. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{242a4ca4-babc-480d-98f6-cd3c5c962ae8}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281696,46 +281715,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Near Road Block Group Summary"
         },
-            "identifier": "{242a4ca4-babc-480d-98f6-cd3c5c962ae8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Park Access by Block Group",
-            "description": "This EnviroAtlas dataset shows the block group population that is within and beyond an easy walking distance (500m) of a park entrance. Park entrances were included in this analysis if they were within 5km of the EnviroAtlas community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c4bf2c16-d35a-4d17-8a67-41c7a49e4ef6}",
+            "issued": "2020-01-13",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281750,46 +281769,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Park Access by Block Group"
         },
-            "identifier": "{c4bf2c16-d35a-4d17-8a67-41c7a49e4ef6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-01-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Proximity to Parks",
-            "description": "This EnviroAtlas dataset shows the approximate walking distance from a park entrance at any given location within the EnviroAtlas community boundary. The zones are estimated in 1/4 km intervals up to 1km then in 1km intervals up to 5km. Park entrances were included in this analysis if they were within 5km of the community boundary. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{8d84153a-ddc1-4092-bf41-5ce032bdcaf7}",
+            "issued": "2020-01-13",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281803,46 +281822,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2011-01-01/2011-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Proximity to Parks"
         },
-            "identifier": "{8d84153a-ddc1-4092-bf41-5ce032bdcaf7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2011-01-01/2011-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2020-01-13",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/public/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Percent Green Space Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates green space along walkable roads. Green space within 25 meters of the road centerline is included and the percentage is based on the total area between street intersections. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. In this metric, water is also included in green space. Green space provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{71eaf038-3e84-4dd5-bdd2-edb645d1227a}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281860,46 +281879,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Percent Green Space Along Walkable Roads"
         },
-            "identifier": "{71eaf038-3e84-4dd5-bdd2-edb645d1227a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Percent Tree Cover Along Walkable Roads",
-            "description": "This EnviroAtlas dataset estimates tree cover along walkable roads. The road width is estimated for each road and percent tree cover is calculated in a 8.5 meter strip beginning at the estimated road edge. Percent tree cover is calculated for each block between road intersections. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Tree cover provides valuable benefits to neighborhood residents and walkers by providing shade, improved aesthetics, and outdoor gathering spaces. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{4e3a91a2-5c0b-434c-90c1-c0325de54c8a}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281917,46 +281936,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Estimated Percent Tree Cover Along Walkable Roads"
         },
-            "identifier": "{4e3a91a2-5c0b-434c-90c1-c0325de54c8a}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 15m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{65e9995a-36b5-4a88-b42c-e614bd9b4060}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -281976,46 +281995,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 15m Riparian Buffer Forest Cover"
         },
-            "identifier": "{65e9995a-36b5-4a88-b42c-e614bd9b4060}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 15m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 15-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{6cb85ed6-6ae1-4b53-807f-d2dea9cfac6b}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282035,46 +282054,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 15m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{6cb85ed6-6ae1-4b53-807f-d2dea9cfac6b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 51m Riparian Buffer Forest Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is forested. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less forested. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{87b0b4a2-5c2c-4f96-b71e-00ad1682c935}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282094,46 +282113,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 51m Riparian Buffer Forest Cover"
         },
-            "identifier": "{87b0b4a2-5c2c-4f96-b71e-00ad1682c935}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 51m Riparian Buffer Vegetated Cover",
-            "description": "This EnviroAtlas dataset describes the percentage of a 51-m riparian buffer that is vegetated. In this community, vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. There is a potential for decreased water quality in areas where the riparian buffer is less vegetated. The displayed line represents the center of the analyzed riparian buffer. The water bodies analyzed include hydrologically connected streams, rivers, connectors, reservoirs, lakes/ponds, ice masses, washes, locks, and rapids within the EnviroAtlas community area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{c4d0dc53-cd9c-4c55-abb5-4ce091627e2e}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282153,46 +282172,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - 51m Riparian Buffer Vegetated Cover"
         },
-            "identifier": "{c4d0dc53-cd9c-4c55-abb5-4ce091627e2e}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Riparian Buffer Land Cover by Block Group",
-            "description": "This EnviroAtlas dataset describes the percentage of forested, vegetated, and impervious land within 15- and 50-meters of hydrologically connected streams, rivers, and other water bodies within the EnviroAtlas community area. In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. and vegetated land is defined as Trees & Forest, Grass & Herbaceous, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{15276036-4742-4fd2-bf96-b9a406499dc7}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282213,46 +282232,46 @@
                 "Water",
                 "Drinking Water"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Riparian Buffer Land Cover by Block Group"
         },
-            "identifier": "{15276036-4742-4fd2-bf96-b9a406499dc7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Residents with Minimal Potential Window Views of Trees by Block Group",
-            "description": "This EnviroAtlas dataset shows the total block group population and the percentage of the block group population that has little access to potential window views of trees at home. Having little potential access to window views of trees is defined as having no trees and forest land cover within 50 meters. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. In this community, tree cover is defined as Trees & Forest and Woody Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{0af5b568-bb6a-4749-832f-89e1d22fa65f}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282270,46 +282289,46 @@
                 "Trees",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Residents with Minimal Potential Window Views of Trees by Block Group"
         },
-            "identifier": "{0af5b568-bb6a-4749-832f-89e1d22fa65f}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Potential Window Views of Water by Block Group",
-            "description": "This EnviroAtlas dataset describes the block group population and the percentage of the block group population that has potential views of water bodies. A potential view of water is defined as having a body of water that is greater than 300m2 within 50m of a residential location. The window views are considered \"potential\" because the procedure does not account for presence or directionality of windows in one's home. The residential locations are defined using the EnviroAtlas Dasymetric (2011/October 2015) map. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b54e221a-f72e-4f4f-ae14-780afb897457}",
+            "issued": "2017-09-06",
             "keyword": [
                 "Virginia Beach/Williamsburg, VA",
                 "Ecosystem Services",
@@ -282325,46 +282344,46 @@
                 "Water",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-09-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-Sustainable and Healthy Communities Research Program, EnviroAtlas"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EnviroAtlas Coordinator",
-                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
+            "temporal": "2010-01-01/2010-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Virginia Beach/Williamsburg, VA - Potential Window Views of Water by Block Group"
         },
-            "identifier": "{b54e221a-f72e-4f4f-ae14-780afb897457}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currency and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
-            "spatial": "-76.89034, 36.55075, -75.86704, 37.4002",
-            "temporal": "2010-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2017-09-06",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This data set is a complete digital hydrologic unit boundary layer to the Subwatershed (12-digit) 6th level for the entire United States. This data set consists of geo-referenced digital data and associated attributes created in accordance with the \"Federal Guidelines, Requirements, and Procedures for the National Watershed Boundary Dataset; Chapter 3 of Section A, Federal Standards, Book 11, Collection and Delineation of Spatial Data; Techniques and Methods 11-A3\" (04/01/2009). http://www.ncgc.nrcs.usda.gov/products/datasets/watershed/index.html . Polygons are attributed with hydrologic unit codes for 4th level sub-basins, 5th level watersheds, 6th level subwatersheds, name, size, downstream hydrologic unit, type of watershed, non-contributing areas and flow modification.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/VirginiaBeachWilliamsburgVA",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - HU12_polygon",
-            "description": "This data set is a complete digital hydrologic unit boundary layer to the Subwatershed (12-digit) 6th level for the entire United States. This data set consists of geo-referenced digital data and associated attributes created in accordance with the \"Federal Guidelines, Requirements, and Procedures for the National Watershed Boundary Dataset; Chapter 3 of Section A, Federal Standards, Book 11, Collection and Delineation of Spatial Data; Techniques and Methods 11-A3\" (04/01/2009). http://www.ncgc.nrcs.usda.gov/products/datasets/watershed/index.html . Polygons are attributed with hydrologic unit codes for 4th level sub-basins, 5th level watersheds, 6th level subwatersheds, name, size, downstream hydrologic unit, type of watershed, non-contributing areas and flow modification.",
+            ],
+            "identifier": "{C78DF01D-0446-4BA0-B504-F9527F3ED4DB}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Connecticut",
                 "Modeling",
@@ -282448,45 +282467,45 @@
                 "Pennsylvania",
                 "United States"
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
+            "rights": "Use Constraints: The distributor shall not be held liable for improper or incorrect use of this data, based on the description of appropriate/inappropriate uses described in this metadata document. It is strongly recommended that this data is directly ac",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - HU12_polygon"
         },
-            "identifier": "{C78DF01D-0446-4BA0-B504-F9527F3ED4DB}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: The distributor shall not be held liable for improper or incorrect use of this data, based on the description of appropriate/inappropriate uses described in this metadata document. It is strongly recommended that this data is directly ac",
-            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
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
+            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 2975 block groups in Washington, DC Metro region. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Washington, DC Metro region. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/EnviroAtlas/National",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - BenMAP Results by Block Group",
-            "description": "This EnviroAtlas dataset demonstrates the effect of changes in pollution concentration on local populations in 2975 block groups in Washington, DC Metro region. The US EPA's Environmental Benefits Mapping and Analysis Program (BenMAP) was used to estimate the incidence of adverse health effects (i.e., mortality and morbidity) and associated monetary value that result from changes in pollution concentrations for Washington, DC Metro region. Incidence and value estimates for the block groups are calculated using i-Tree models (www.itreetools.org), local weather data, pollution data, and U.S. Census derived population data. This dataset was produced by the USDA Forest Service with support from The Davey Tree Expert Company to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{3f40987c-0c1c-44e7-8c9b-56495149249f}",
+            "issued": "2019-05-17",
             "keyword": [
                 "Exposure",
                 "Ecosystem Services",
@@ -282506,46 +282525,46 @@
                 "Trees",
                 "Human Well-being"
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
+            "title": "EnviroAtlas - Washington, DC - BenMAP Results by Block Group"
         },
-            "identifier": "{3f40987c-0c1c-44e7-8c9b-56495149249f}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas dataset is the base layer for the Washington, DC EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - Census Block Groups",
-            "description": "This EnviroAtlas dataset is the base layer for the Washington, DC EnviroAtlas area. The block groups are from the US Census Bureau and are included/excluded based on EnviroAtlas criteria described in the procedure log. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{75914521-e2ec-4d7b-959b-ee895f3b577c}",
+            "issued": "2019-04-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -282558,46 +282577,46 @@
                 "Census Block Groups",
                 "Environmental Atlas"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Washington, DC - Census Block Groups"
         },
-            "identifier": "{75914521-e2ec-4d7b-959b-ee895f3b577c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-04-08",
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
-            "title": "EnviroAtlas - Washington, DC - Demographics by Block Group",
-            "description": "This EnviroAtlas dataset is a summary of key demographic groups for the EnviroAtlas community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{ff153f71-b471-4fb8-b3ff-250b279d4a17}",
+            "issued": "2019-04-08",
             "keyword": [
                 "Human",
                 "Ecosystem Services",
@@ -282614,46 +282633,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "2006-01-01/2010-01-01",
+            "theme": "boundaries",
+            "title": "EnviroAtlas - Washington, DC - Demographics by Block Group"
         },
-            "identifier": "{ff153f71-b471-4fb8-b3ff-250b279d4a17}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2006-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-04-08",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "This EnviroAtlas dataset shows the Washington, DC EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - EnviroAtlas Community Boundary",
-            "description": "This EnviroAtlas dataset shows the Washington, DC EnviroAtlas community boundary. It represents the outside edge of all the block groups included in the EnviroAtlas Community. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{31488da1-c938-43e0-ba8a-628c01c40e72}",
+            "issued": "2019-04-08",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -282666,46 +282685,46 @@
                 "Environmental Atlas",
                 "Boundaries"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Washington, DC - EnviroAtlas Community Boundary"
         },
-            "identifier": "{31488da1-c938-43e0-ba8a-628c01c40e72}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-04-08",
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
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/ENVIROATLAS/Communities/WashingtonDC",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EnviroAtlas - Washington, DC - Tree Cover Configuration and Connectivity",
-            "description": "This EnviroAtlas dataset categorizes forest land cover into structural elements (e.g. core, edge, connector, etc.). In this community, tree cover is defined as Trees & Forest, and Woody Wetlands. Water was considered background (value 129) during the analysis to create this dataset, however it has been converted into value 10 to distinguish it from land area background. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{b7ff4073-13bb-445f-9570-85906cccf24d}",
+            "issued": "2019-11-19",
             "keyword": [
                 "Ecosystem Services",
                 "Green Infrastructure",
@@ -282721,46 +282740,46 @@
                 "Washington, DC",
                 "Environmental Atlas"
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
+            "spatial": "-77.86109, 38.3645, -76.68178, 39.42125",
+            "temporal": "2013-01-01/2014-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Tree Cover Configuration and Connectivity"
         },
-            "identifier": "{b7ff4073-13bb-445f-9570-85906cccf24d}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2013-01-01/2014-01-01",
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
+            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Three reports were used with city- or water supply authority- level domestic water demand data, in addition to county level data. The 2011 Northern Virginia Regional Water Supply Plan provides detailed publicly, privately, and self supplied water use and population served for 2007 and covers most of the Virginia side of the EnviroAtlas study area. The 2011 Fauquier County Regional Water Supply Plan provides detailed publicly, privately, and self supplied water use and population served for 2007 and covers Fauquier County, Virginia. The 2010 Washington Metropolitan Area Water Supply Reliability Study, Part 1 from the Interstate Commission on the Potomac River Basin provides detailed publicly, privately, and self supplied water use and population served for 2008 by water supplier for suppliers drawing from the Potomac River. Data from these reports were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 25 and 204 GPD for each of the subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - Domestic Water Use per Day by U.S. Census Block Group",
-            "description": "As included in this EnviroAtlas dataset, the community level domestic water use is calculated using locally available water use data per capita in gallons of water per day (GPD), distributed dasymetrically, and summarized by census block group. Domestic water use, as defined in this case, is intended to represent residential indoor and outdoor water use (e.g., cooking, hygiene, landscaping, pools, etc.) for primary residences (i.e., excluding second homes and tourism rentals). Three reports were used with city- or water supply authority- level domestic water demand data, in addition to county level data. The 2011 Northern Virginia Regional Water Supply Plan provides detailed publicly, privately, and self supplied water use and population served for 2007 and covers most of the Virginia side of the EnviroAtlas study area. The 2011 Fauquier County Regional Water Supply Plan provides detailed publicly, privately, and self supplied water use and population served for 2007 and covers Fauquier County, Virginia. The 2010 Washington Metropolitan Area Water Supply Reliability Study, Part 1 from the Interstate Commission on the Potomac River Basin provides detailed publicly, privately, and self supplied water use and population served for 2008 by water supplier for suppliers drawing from the Potomac River. Data from these reports were weighted across publicly, privately, and self-supplied sources by population served, resulting in a single water use estimate between 25 and 204 GPD for each of the subregions in the study area. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{f8e97775-55bd-4817-904e-ed2c5353c009}",
+            "issued": "2019-04-16",
             "keyword": [
                 "Ecosystem Services",
                 "Demand for Ecosystem Services",
@@ -282780,46 +282799,46 @@
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
+            "title": "EnviroAtlas - Washington, DC - Domestic Water Use per Day by U.S. Census Block Group"
         },
-            "identifier": "{f8e97775-55bd-4817-904e-ed2c5353c009}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
+            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - Greenspace Around Schools by Block Group",
-            "description": "This EnviroAtlas data set shows the number of schools in each block group in the EnviroAtlas community boundary as well as the number of schools where less than 25% of the area within 100 meters of the school is classified as greenspace. green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{19cd5649-c9c8-4f3f-aa47-0590fcda3f08}",
+            "issued": "2019-04-08",
             "keyword": [
                 "Ecosystem Services",
                 "Demographics",
@@ -282835,46 +282854,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-04-08",
+            "programCode": [
+                "020:072"
+            ],
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
+            "title": "EnviroAtlas - Washington, DC - Greenspace Around Schools by Block Group"
         },
-            "identifier": "{19cd5649-c9c8-4f3f-aa47-0590fcda3f08}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "issued": "2019-04-08",
-            "language": "en-us",
-            "theme": "environment",
+            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - People and Land Cover in Floodplains by Block Group",
-            "description": "This EnviroAtlas dataset describes the total counts and percentage of population, land area, and impervious surface in the 1% Annual Chance Flood Hazard area or 0.2% Annual Chance Flood Hazard area of each block group. The flood hazard area is defined by the National Flood Hazard Layer (NFHL) produced by the Federal Emergency Management Agency (FEMA, www.fema.gov). This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{a8ddc470-d1b7-479b-8058-7e681f89958b}",
+            "issued": "2019-06-10",
             "keyword": [
                 "Ecosystem Services",
                 "Hazards",
@@ -282898,46 +282917,46 @@
                 "Communities",
                 "Flood"
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
+            "temporal": "2017-01-30/2017-01-30",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - People and Land Cover in Floodplains by Block Group"
         },
-            "identifier": "{a8ddc470-d1b7-479b-8058-7e681f89958b}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "2017-01-30/2017-01-30",
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
+            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
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
-            "title": "EnviroAtlas - Washington, DC - Greenspace Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of square meters of greenspace within 1/4 square kilometer centered over the given point. In this community, green space is defined as Trees & Forest, Grass & Herbaceous, Agriculture, Woody Wetlands, and Emergent Wetlands. Water is shown as \"-99999\" in this dataset to distinguish it from land areas with very low green space. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{1beee8c1-61bb-471b-90aa-015bfd45cc88}",
+            "issued": "2019-04-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -282952,46 +282971,46 @@
                 "Environmental Atlas",
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
+            "title": "EnviroAtlas - Washington, DC - Greenspace Proximity Gradient"
         },
-            "identifier": "{1beee8c1-61bb-471b-90aa-015bfd45cc88}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "title": "EnviroAtlas - Washington, DC - Historic Places by Census Block Group",
-            "description": "This EnviroAtlas dataset portrays the total number of historic places located within each Census Block Group (CBG). The historic places data were compiled from the National Register of Historic Places, which provides official federal lists of districts, sites, buildings, structures and objects significant to American history, architecture, archeology, engineering, and culture. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{cc9a9d4f-2c86-4909-8753-ec975f793c39}",
+            "issued": "2019-07-23",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -283007,46 +283026,46 @@
                 "Environmental Atlas",
                 "Human Well-being"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2019-07-23",
+            "programCode": [
+                "020:072"
+            ],
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
+            "temporal": "1966-01-01/2013-01-01",
+            "theme": "environment",
+            "title": "EnviroAtlas - Washington, DC - Historic Places by Census Block Group"
         },
-            "identifier": "{cc9a9d4f-2c86-4909-8753-ec975f793c39}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
-            "temporal": "1966-01-01/2013-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EnviroAtlas Coordinator",
+                "hasEmail": "mailto:EnviroAtlas@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/enviroatlas/enviroatlas-data",
-            "issued": "2019-07-23",
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
-            "title": "EnviroAtlas - Washington, DC - Impervious Proximity Gradient",
-            "description": "In any given 1-square meter point in this EnviroAtlas dataset, the value shown gives the percentage of impervious surface within 1 square kilometer centered over the given point. Water is shown as '-99999' in this dataset to distinguish it from land areas with low impervious. This dataset was produced by the US EPA to support research and online mapping activities related to EnviroAtlas. EnviroAtlas (https://www.epa.gov/enviroatlas) allows the user to interact with a web-based, easy-to-use, mapping application to view and analyze multiple ecosystem services for the contiguous United States. The dataset is available as downloadable data (https://edg.epa.gov/data/Public/ORD/EnviroAtlas) or as an EnviroAtlas map service. Additional descriptive information about each attribute in this dataset can be found in its associated EnviroAtlas Fact Sheet (https://www.epa.gov/enviroatlas/enviroatlas-fact-sheets).",
+            ],
+            "identifier": "{19cd5649-c9c8-4f3f-aa47-0590fcda3f08}",
+            "issued": "2019-04-09",
             "keyword": [
                 "Ecosystem Services",
                 "Environment",
@@ -283060,46 +283079,46 @@
                 "Environmental Atlas",
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
+            "title": "EnviroAtlas - Washington, DC - Impervious Proximity Gradient"
         },
-            "identifier": "{19cd5649-c9c8-4f3f-aa47-0590fcda3f08}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
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
```

