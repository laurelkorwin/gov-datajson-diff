# Change History for epa.json (Part 41)

### Changes from 31606f9 to dd2190f (Part 31/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "4157F3E9-7C82-4BD8-BD4B-E9888DF70CEA",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317481,39 +317446,39 @@
                 "Sea Level Rise",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-02-28",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jordan West",
-                "hasEmail": "mailto:west.jordan@epa.gov"
+            "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
+            "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "Low Marsh at St. Jones, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "56B9C288-CB5C-4E34-A947-D8236C6AD7E2",
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
-            "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
-            "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2019-02-01",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jordan West",
+                "hasEmail": "mailto:west.jordan@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/StJLow_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Symbology of SLAMM output raster",
-            "description": "Symbology used by the marsh gain and loss raster in the SLAMM report",
+            ],
+            "identifier": "56B9C288-CB5C-4E34-A947-D8236C6AD7E2",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317522,6 +317487,7 @@
                 "Natural Resources",
                 "Delaware",
                 "Environment",
+                "Downloadable Data",
                 "020:094",
                 "Ecosystem",
                 "Relative Vulnerability",
@@ -317530,39 +317496,92 @@
                 "Sea Level Rise",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2018-02-28",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
             },
+            "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
+            "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "Total Marsh at St. Jones, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jordan West",
                 "hasEmail": "mailto:west.jordan@epa.gov"
             },
+            "description": "Symbology used by the marsh gain and loss raster in the SLAMM report",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Symbology.zip"
+                }
+            ],
             "identifier": "FADE9634-0956-4214-9616-5FC3132B00BB",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "issued": "2019-02-01",
+            "keyword": [
+                "New Jersey",
+                "Exposure",
+                "Modeling",
+                "Estuary",
+                "Natural Resources",
+                "Delaware",
+                "Environment",
+                "020:094",
+                "Ecosystem",
+                "Relative Vulnerability",
+                "geospatial",
+                "Coastal Wetland",
+                "Sea Level Rise",
+                "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2018-02-28",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
+            },
             "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
             "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2019-02-01",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Symbology.zip"
-                }
-            ]
+            "title": "Symbology of SLAMM output raster"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Human Well-Being Index (HWBI) for U.S. Counties, 2000-2010",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Linda Harwell",
+                "hasEmail": "mailto:Harwell.linda@Epa.gov"
+            },
+            "describedBy": "https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NHEERL&dirEntryId=289300",
             "description": "The Human Well-being Index (HWBI) for U.S. counties is a set of nationally consistent demonstration results that may be used to characterize community well-being. This composite index was developed by U.S. EPA Office of Research and Development in support of its Sustainable and Healthy Communities (SHC) Research. It serves as an endpoint measure for use in the creation of community decision-support tools. The HWBI characterizes community conditions in the context of the flow of economic, social and ecological services. The index calculation approach used a nested-indicator design. A decade (2000-2010) of cultural, economic, and social data were drawn from publicly available sources (e.g., US Census, Bureau of Economic Analysis, American Community Survey, General Social Survey, Centers for Disease Control) to provide the foundation for well-being related indicators. Indicators are integrated into one of eight domains or sub-indices of well-being. These domains were synthesized to represent different aspects of well-being characteristics common across communities of all sizes. Service indicators reflect the availability of select socio-ecological services that influence well-being. Community decisions often result in changes in the flow of community services. Collectively, well-being and service measures provide a means to evaluate relationships between the availability of certain community services and overall well-being. Data used to generate service indicators were also collected from existing data sources. Detailed information about the attributes of the HWBI, its components and related service indicators are described in Indicators and Methods for Constructing a U.S. Human Well-being Index (HWBI) for Ecosystem Services Research (EPA/600/R-12/023. pp. 121) and Indicators and Methods for Evaluating Economic, Ecosystem and Social Services Provisioning (EPA/600/R-14/184. pp. 174), respectively.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{8ef76910-ebf9-4eee-b7a0-ff620064aad6}",
+            "issued": "2017-12-15",
             "keyword": [
                 "Connecticut",
                 "Texas",
@@ -317623,95 +317642,45 @@
                 "Pennsylvania",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2017-12-15",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Health and Environmental Effects Research Laboratory-Gulf Ecology Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Linda Harwell",
-                "hasEmail": "mailto:Harwell.linda@Epa.gov"
-            },
-            "identifier": "{8ef76910-ebf9-4eee-b7a0-ff620064aad6}",
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
             "temporal": "2000-01-01/2010-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NHEERL&dirEntryId=289300",
-            "issued": "2017-12-15",
-            "language": "en-us",
             "theme": "economy",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Human Well-Being Index (HWBI) for U.S. Counties, 2000-2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Alaska",
-            "description": "Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. The ecoregions of Alaska are a framework for organizing and interpreting environmental data for State, national, and international level inventory, monitoring, and research efforts. The map and descriptions for 20 ecological regions were derived by synthesizing information on the geographic distribution of environmental factors such as climate, physiography, geology, permafrost, soils, and vegetation. A qualitative assessment was used to interpret the distributional patterns and relative importance of these factors from place to place (Gallant and others, 1995). Numeric identifiers assigned to the ecoregions are coordinated with those used on the map of \"Ecoregions of the Conterminous United States\" (Omernik 1987, U.S. EPA 2010) as a continuation of efforts to map ecoregions for the United States. Additionally, the ecoregions for Alaska and the conterminous United States, along with ecological regions for Canada (Wiken 1986) and Mexico, have been combined for maps at three hierarchical levels for North America (Omernik 1995, Commission for Environmental Cooperation, 1997, 2006). A Roman numeral hierarchical scheme has been adopted for different levels of ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions. At Level III, there are currently 182 ecological regions for North America. Level IV ecoregions have been developed for the conterminous United States, but Level III is the highest level available for Alaska. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America - toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Commission for Environmental Cooperation, 2006, Ecological regions of North America, Level III, Map scale 1:10,000,000, https://www.epa.gov/eco-research/ecoregions-north-america. Gallant, A.L., Binnian, E.F. Omernik, J.M. and Shasby, M.B., 1995, Ecoregions of Alaska: U.S. Geological Survey Professional Paper 1567. Omernik, J.M., 1987, Ecoregions of the Conterminous United States: Annals of the Association of American Geographers, v. 77, no.1, p. 118-125. Omernik, J.M., 1995, Ecoregions: a Framework for Managing Ecosystems: The George Wright Forum, v. 12, no. 1, p. 35-51. U.S. Environmental Protection Agency, 2010, Level III ecoregions of the continental United States (revision of Omernik, 1987): Corvallis, Oregon, USEPA - National Health and Environmental Effects Research Laboratory, Map M-1, various scales. Wiken, E.B., 1986, Terrestrial Ecozones of Canada: Lands Directorate, Environmental Canada Ecological Land Classification Series 19, 26 p. Comments and questions regarding ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
-            "keyword": [
-                "Natural Resources",
-                "Environment",
-                "Surface Water",
-                "Management",
-                "Ecosystem",
-                "geospatial",
-                "Alaska",
-                "United States"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2012-01-01",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Randy Comeleo",
                 "hasEmail": "mailto:comeleo.randy@epa.gov"
             },
-            "identifier": "{d60d4f92-706f-4f6a-9e38-6fb063bd2962}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-180.000000, 49.177353, 180.000000, 71.405930",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. The ecoregions of Alaska are a framework for organizing and interpreting environmental data for State, national, and international level inventory, monitoring, and research efforts. The map and descriptions for 20 ecological regions were derived by synthesizing information on the geographic distribution of environmental factors such as climate, physiography, geology, permafrost, soils, and vegetation. A qualitative assessment was used to interpret the distributional patterns and relative importance of these factors from place to place (Gallant and others, 1995). Numeric identifiers assigned to the ecoregions are coordinated with those used on the map of \"Ecoregions of the Conterminous United States\" (Omernik 1987, U.S. EPA 2010) as a continuation of efforts to map ecoregions for the United States. Additionally, the ecoregions for Alaska and the conterminous United States, along with ecological regions for Canada (Wiken 1986) and Mexico, have been combined for maps at three hierarchical levels for North America (Omernik 1995, Commission for Environmental Cooperation, 1997, 2006). A Roman numeral hierarchical scheme has been adopted for different levels of ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions. At Level III, there are currently 182 ecological regions for North America. Level IV ecoregions have been developed for the conterminous United States, but Level III is the highest level available for Alaska. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America - toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Commission for Environmental Cooperation, 2006, Ecological regions of North America, Level III, Map scale 1:10,000,000, https://www.epa.gov/eco-research/ecoregions-north-america. Gallant, A.L., Binnian, E.F. Omernik, J.M. and Shasby, M.B., 1995, Ecoregions of Alaska: U.S. Geological Survey Professional Paper 1567. Omernik, J.M., 1987, Ecoregions of the Conterminous United States: Annals of the Association of American Geographers, v. 77, no.1, p. 118-125. Omernik, J.M., 1995, Ecoregions: a Framework for Managing Ecosystems: The George Wright Forum, v. 12, no. 1, p. 35-51. U.S. Environmental Protection Agency, 2010, Level III ecoregions of the continental United States (revision of Omernik, 1987): Corvallis, Oregon, USEPA - National Health and Environmental Effects Research Laboratory, Map M-1, various scales. Wiken, E.B., 1986, Terrestrial Ecozones of Canada: Lands Directorate, Environmental Canada Ecological Land Classification Series 19, 26 p. Comments and questions regarding ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ak/ak_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Alabama",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{d60d4f92-706f-4f6a-9e38-6fb063bd2962}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317719,47 +317688,48 @@
                 "Management",
                 "Ecosystem",
                 "geospatial",
+                "Alaska",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-180.000000, 49.177353, 180.000000, 71.405930",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Alaska"
         },
-            "identifier": "{89DF761A-F2A6-48FB-983E-5736C6417212}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.656721, 29.959092, -84.446142, 35.185028",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/al/al_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Alabama",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{89DF761A-F2A6-48FB-983E-5736C6417212}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317769,45 +317739,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.656721, 29.959092, -84.446142, 35.185028",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Alabama"
         },
-            "identifier": "{9B5C253A-2F94-4F81-8B8C-59EC486D1417}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.656721, 29.959092, -84.446142, 35.185028",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/al/al_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Arkansas",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{9B5C253A-2F94-4F81-8B8C-59EC486D1417}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317817,45 +317787,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.656721, 29.959092, -84.446142, 35.185028",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Alabama"
         },
-            "identifier": "{45577980-FBDD-4989-B20A-503B9CBEA10C}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-94.678738, 32.872256, -89.597087, 36.632464",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ar/ar_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Arkansas",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{45577980-FBDD-4989-B20A-503B9CBEA10C}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317865,45 +317835,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-94.678738, 32.872256, -89.597087, 36.632464",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Arkansas"
         },
-            "identifier": "{FC709A14-353E-43A5-BFFF-B929BB23B215}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-94.678738, 32.872256, -89.597087, 36.632464",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ar/ar_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Arizona",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{FC709A14-353E-43A5-BFFF-B929BB23B215}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317913,45 +317883,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-94.678738, 32.872256, -89.597087, 36.632464",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Arkansas"
         },
-            "identifier": "{E9ABDDF4-4A91-4765-9775-5F8091FDB862}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-115.882880, 30.572625, -108.138986, 37.635581",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/az/az_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Arizona",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E9ABDDF4-4A91-4765-9775-5F8091FDB862}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -317961,45 +317931,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-115.882880, 30.572625, -108.138986, 37.635581",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Arizona"
         },
-            "identifier": "{0B364A4C-5F06-491B-82BA-2396DC49352B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-115.882880, 30.572625, -108.138986, 37.635581",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/az/az_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of California",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{0B364A4C-5F06-491B-82BA-2396DC49352B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318009,45 +317979,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-115.882880, 30.572625, -108.138986, 37.635581",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Arizona"
         },
-            "identifier": "{5B16439E-D46F-446B-9D48-3496797C1B72}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.012651, 31.431829, -113.803595, 43.455059",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ca/ca_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of California",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{5B16439E-D46F-446B-9D48-3496797C1B72}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318057,45 +318027,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.012651, 31.431829, -113.803595, 43.455059",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of California"
         },
-            "identifier": "{628CB0CC-872A-4DB2-A067-892D63C83F94}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.012651, 31.431829, -113.803595, 43.455059",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ca/ca_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Colorado",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{628CB0CC-872A-4DB2-A067-892D63C83F94}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318105,45 +318075,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.012651, 31.431829, -113.803595, 43.455059",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of California"
         },
-            "identifier": "{3799BBED-0C08-4E74-9E37-4B371460E42E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-109.77311, 36.445923, -101.727971, 41.522845",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/co/co_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Colorado",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{3799BBED-0C08-4E74-9E37-4B371460E42E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318153,45 +318123,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-109.77311, 36.445923, -101.727971, 41.522845",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Colorado"
         },
-            "identifier": "{63FCFC49-3520-486A-B9F0-C397072FBF76}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-109.77311, 36.445923, -101.727971, 41.522845",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/co/co_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Connecticut",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{63FCFC49-3520-486A-B9F0-C397072FBF76}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318201,45 +318171,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-109.77311, 36.445923, -101.727971, 41.522845",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Colorado"
         },
-            "identifier": "{B159EA3D-BD79-420E-9291-B36A9839D698}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-73.821951, 40.688589, -71.596666, 42.318274",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ct/ct_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Connecticut",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{B159EA3D-BD79-420E-9291-B36A9839D698}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318249,45 +318219,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-73.821951, 40.688589, -71.596666, 42.318274",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Connecticut"
         },
-            "identifier": "{F0848CDA-90D3-4D55-9A53-FEA404C313AB}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-73.821951, 40.688589, -71.596666, 42.318274",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ct/ct_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Delaware",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F0848CDA-90D3-4D55-9A53-FEA404C313AB}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318297,45 +318267,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-73.821951, 40.688589, -71.596666, 42.318274",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Connecticut"
         },
-            "identifier": "{65D3DA25-1BC1-435B-9E46-B9634DF0330B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-76.121973, 38.355292, -74.681544, 39.874001",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/de/de_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Delaware",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{65D3DA25-1BC1-435B-9E46-B9634DF0330B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318345,45 +318315,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-76.121973, 38.355292, -74.681544, 39.874001",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Delaware"
         },
-            "identifier": "{922D8923-B50C-4803-902F-6441D883C404}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-76.121973, 38.355292, -74.681544, 39.874001",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/de/de_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Florida",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{922D8923-B50C-4803-902F-6441D883C404}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318393,45 +318363,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-76.121973, 38.355292, -74.681544, 39.874001",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Delaware"
         },
-            "identifier": "{F5F6A87D-8190-4887-B3AE-E64D4BE9880E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.176637, 24.287999, -79.214598, 31.407589",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/fl/fl_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Florida",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F5F6A87D-8190-4887-B3AE-E64D4BE9880E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318441,45 +318411,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.176637, 24.287999, -79.214598, 31.407589",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Florida"
         },
-            "identifier": "{6DDCA5E6-2F1B-4BDB-87DF-A2FA28061736}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.176637, 24.287999, -79.214598, 31.407589",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/fl/fl_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Georgia",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{6DDCA5E6-2F1B-4BDB-87DF-A2FA28061736}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318489,45 +318459,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.176637, 24.287999, -79.214598, 31.407589",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Florida"
         },
-            "identifier": "{769847E2-51A1-47B5-9D80-B31D51A5075B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-86.143725, 30.226883, -80.315819, 35.245903",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ga/ga_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Georgia",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{769847E2-51A1-47B5-9D80-B31D51A5075B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318537,45 +318507,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
-            },
-            "identifier": "{10F48305-03B1-41FA-89AB-4CFBD6BB0C69}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None",
             "spatial": "-86.143725, 30.226883, -80.315819, 35.245903",
             "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
             "theme": "boundaries",
+            "title": "Level III Ecoregions of Georgia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ga/ga_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Iowa",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{10F48305-03B1-41FA-89AB-4CFBD6BB0C69}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318585,45 +318555,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-86.143725, 30.226883, -80.315819, 35.245903",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Georgia"
         },
-            "identifier": "{47DDEB30-C0A1-4138-A39E-C1EE8232E0B7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-86.143725, 30.226883, -80.315819, 35.245903",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ia/ia_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Iowa",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{47DDEB30-C0A1-4138-A39E-C1EE8232E0B7}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318633,45 +318603,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-86.143725, 30.226883, -80.315819, 35.245903",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Iowa"
         },
-            "identifier": "{D6185305-23F2-446A-B9B4-0BA13444AE45}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-96.647648, 40.327417, -90.015967, 43.587317",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ia/ia_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Idaho",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{D6185305-23F2-446A-B9B4-0BA13444AE45}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318681,45 +318651,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-96.647648, 40.327417, -90.015967, 43.587317",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Iowa"
         },
-            "identifier": "{62CC5654-AF61-4A4F-AA09-B5B9D6A894C3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-119.260208, 41.192391, -110.525874, 49.633134",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/id/id_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Idaho",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{62CC5654-AF61-4A4F-AA09-B5B9D6A894C3}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318729,45 +318699,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-119.260208, 41.192391, -110.525874, 49.633134",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Idaho"
         },
-            "identifier": "{FFD03B52-D773-44F1-9595-5BABB371E45C}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-119.260208, 41.192391, -110.525874, 49.633134",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/id/id_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Illinois",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{FFD03B52-D773-44F1-9595-5BABB371E45C}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318777,45 +318747,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-119.260208, 41.192391, -110.525874, 49.633134",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Idaho"
         },
-            "identifier": "{B67E9982-ADF1-4BF5-A0D8-3C77D9F13C6F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.699034, 36.878477, -87.040671, 42.668303",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/il/il_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Illinois",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{B67E9982-ADF1-4BF5-A0D8-3C77D9F13C6F}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318825,45 +318795,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.699034, 36.878477, -87.040671, 42.668303",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Illinois"
         },
-            "identifier": "{C3842C17-E83B-4377-8148-7BFF58EA0C24}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.699034, 36.878477, -87.040671, 42.668303",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/il/il_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Indiana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{C3842C17-E83B-4377-8148-7BFF58EA0C24}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318873,45 +318843,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.699034, 36.878477, -87.040671, 42.668303",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Illinois"
         },
-            "identifier": "{42733496-A8EC-499B-8F85-4DFF41E837D5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.110819, 37.539095, -84.327416, 41.975493",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/in/in_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Indiana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{42733496-A8EC-499B-8F85-4DFF41E837D5}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318921,45 +318891,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.110819, 37.539095, -84.327416, 41.975493",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Indiana"
         },
-            "identifier": "{9CC5F1EF-B84D-4408-AF41-B4FF3199BBD7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-88.110819, 37.539095, -84.327416, 41.975493",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/in/in_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Kansas",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{9CC5F1EF-B84D-4408-AF41-B4FF3199BBD7}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -318969,45 +318939,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-88.110819, 37.539095, -84.327416, 41.975493",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Indiana"
         },
-            "identifier": "{868D4F3B-C49B-4CAF-9AF8-D44B1A3D8574}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-102.295019, 36.848056, -94.55727, 40.148559",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ks/ks_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Kansas",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{868D4F3B-C49B-4CAF-9AF8-D44B1A3D8574}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319017,45 +318987,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-102.295019, 36.848056, -94.55727, 40.148559",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Kansas"
         },
-            "identifier": "{2235970A-CBFE-4D50-BF70-AAD10EE57A4F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-102.295019, 36.848056, -94.557276, 40.148559",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ks/ks_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Kentucky",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{2235970A-CBFE-4D50-BF70-AAD10EE57A4F}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319065,45 +319035,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-102.295019, 36.848056, -94.557276, 40.148559",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Kansas"
         },
-            "identifier": "{F4F83FB5-1624-4969-8A74-46852B0DC9BA}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-89.575989, 35.881631, -81.714453, 39.477458",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ky/ky_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Kentucky",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F4F83FB5-1624-4969-8A74-46852B0DC9BA}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319113,45 +319083,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-89.575989, 35.881631, -81.714453, 39.477458",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Kentucky"
         },
-            "identifier": "{03638C3D-7906-4671-A9AD-DBAC42657069}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-89.575989, 35.881631, -81.714453, 39.477458",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ky/ky_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Louisiana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{03638C3D-7906-4671-A9AD-DBAC42657069}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319161,45 +319131,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-89.575989, 35.881631, -81.714453, 39.477458",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Kentucky"
         },
-            "identifier": "{A69EDBB2-FD28-4AA0-8FAD-EB7F31131442}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-94.134829, 28.894307, -88.548746, 33.089601",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/la/la_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Louisiana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{A69EDBB2-FD28-4AA0-8FAD-EB7F31131442}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319209,45 +319179,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-94.134829, 28.894307, -88.548746, 33.089601",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Louisiana"
         },
-            "identifier": "{868BEA48-C245-49E9-8A1E-34F1C0E9359F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-94.134829, 28.894307, -88.548746, 33.089601",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/la/la_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of the Mississippi Alluvial Plain",
-            "description": "Ecoregions for the Mississippi Alluvial Plain were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. By recognizing the spatial differences in the capacities and potentials of ecosystems, ecoregions stratify the environment by its probable response to disturbance (Bryce and others, 1999). These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and non-government organizations that are responsible for different types of resources within the same geographical areas (Omernik and others, 2000). The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of the spatial patterns and the composition of biotic and abiotic phenomena that affect or reflect differences in ecosystem quality and integrity (Wiken, 1986; Omernik, 1987, 1995). These phenomena include geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another regardless of the hierarchical level. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). This product is part of a collaborative effort primarily between USEPA Region VII, USEPA National Health and Environmental Effects Research Laboratory (Corvallis, Oregon), Mississippi Department of Environmental Quality, Arkansas Department of Environmental Quality, Arkansas Multi-Agency Wetland Planning Team (MAWPT), U.S. Army Corps of Engineers (USACE), U.S. Department of Agriculture (USDA) - Natural Resources Conservation Service (NRCS), U.S. Department of Interior - Fish and Wildlife Service (USFWS), and U.S. Department of Interior - U.S. Geological Survey (USGS) - Earth Resources Observation Systems (EROS) Data Center. The project is associated with an interagency effort to develop a common framework of ecological regions. Reaching that objective requires recognition of the differences in the conceptual approaches and mapping methodologies that have been used to develop the most common ecoregion-type frameworks, including those developed by the U.S. Department of Agriculture - Forest Service (USFS) (Bailey and others, 1994), the USEPA (Omernik, 1987, 1995), and the NRCS (United States Department of Agriculture - Soil Conservation Service, 1981). As each of these frameworks is further refined, their differences are becoming less discernible. Regional collaborative projects such as this one in the Mississippi Alluvial Plain, where agreement can be reached among multiple resource management agencies, are a step toward attaining consensus and consistency in ecoregion frameworks for the entire nation. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{868BEA48-C245-49E9-8A1E-34F1C0E9359F}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319257,45 +319227,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-94.134829, 28.894307, -88.548746, 33.089601",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Louisiana"
         },
-            "identifier": "{4321938f-c784-47cc-9261-71a8f755858c}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-92.525413, 28.897483, -88.098311, 37.457045",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions for the Mississippi Alluvial Plain were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. By recognizing the spatial differences in the capacities and potentials of ecosystems, ecoregions stratify the environment by its probable response to disturbance (Bryce and others, 1999). These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and non-government organizations that are responsible for different types of resources within the same geographical areas (Omernik and others, 2000). The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of the spatial patterns and the composition of biotic and abiotic phenomena that affect or reflect differences in ecosystem quality and integrity (Wiken, 1986; Omernik, 1987, 1995). These phenomena include geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another regardless of the hierarchical level. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). This product is part of a collaborative effort primarily between USEPA Region VII, USEPA National Health and Environmental Effects Research Laboratory (Corvallis, Oregon), Mississippi Department of Environmental Quality, Arkansas Department of Environmental Quality, Arkansas Multi-Agency Wetland Planning Team (MAWPT), U.S. Army Corps of Engineers (USACE), U.S. Department of Agriculture (USDA) - Natural Resources Conservation Service (NRCS), U.S. Department of Interior - Fish and Wildlife Service (USFWS), and U.S. Department of Interior - U.S. Geological Survey (USGS) - Earth Resources Observation Systems (EROS) Data Center. The project is associated with an interagency effort to develop a common framework of ecological regions. Reaching that objective requires recognition of the differences in the conceptual approaches and mapping methodologies that have been used to develop the most common ecoregion-type frameworks, including those developed by the U.S. Department of Agriculture - Forest Service (USFS) (Bailey and others, 1994), the USEPA (Omernik, 1987, 1995), and the NRCS (United States Department of Agriculture - Soil Conservation Service, 1981). As each of these frameworks is further refined, their differences are becoming less discernible. Regional collaborative projects such as this one in the Mississippi Alluvial Plain, where agreement can be reached among multiple resource management agencies, are a step toward attaining consensus and consistency in ecoregion frameworks for the entire nation. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/map/map_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of the Mississippi Alluvial Plain",
-            "description": "Ecoregions for the Mississippi Alluvial Plain were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. By recognizing the spatial differences in the capacities and potentials of ecosystems, ecoregions stratify the environment by its probable response to disturbance (Bryce and others, 1999). These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and non-government organizations that are responsible for different types of resources within the same geographical areas (Omernik and others, 2000). The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of the spatial patterns and the composition of biotic and abiotic phenomena that affect or reflect differences in ecosystem quality and integrity (Wiken, 1986; Omernik, 1987, 1995). These phenomena include geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another regardless of the hierarchical level. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). This product is part of a collaborative effort primarily between USEPA Region VII, USEPA National Health and Environmental Effects Research Laboratory (Corvallis, Oregon), Mississippi Department of Environmental Quality, Arkansas Department of Environmental Quality, Arkansas Multi-Agency Wetland Planning Team (MAWPT), U.S. Army Corps of Engineers (USACE), U.S. Department of Agriculture (USDA) - Natural Resources Conservation Service (NRCS), U.S. Department of Interior - Fish and Wildlife Service (USFWS), and U.S. Department of Interior - U.S. Geological Survey (USGS) - Earth Resources Observation Systems (EROS) Data Center. The project is associated with an interagency effort to develop a common framework of ecological regions. Reaching that objective requires recognition of the differences in the conceptual approaches and mapping methodologies that have been used to develop the most common ecoregion-type frameworks, including those developed by the U.S. Department of Agriculture - Forest Service (USFS) (Bailey and others, 1994), the USEPA (Omernik, 1987, 1995), and the NRCS (United States Department of Agriculture - Soil Conservation Service, 1981). As each of these frameworks is further refined, their differences are becoming less discernible. Regional collaborative projects such as this one in the Mississippi Alluvial Plain, where agreement can be reached among multiple resource management agencies, are a step toward attaining consensus and consistency in ecoregion frameworks for the entire nation. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{4321938f-c784-47cc-9261-71a8f755858c}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319305,45 +319275,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-92.525413, 28.897483, -88.098311, 37.457045",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of the Mississippi Alluvial Plain"
         },
-            "identifier": "{9177ffb8-4dbf-45db-9382-9c2eded1db51}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-92.525413, 28.897483, -88.098311, 37.457045",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions for the Mississippi Alluvial Plain were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. By recognizing the spatial differences in the capacities and potentials of ecosystems, ecoregions stratify the environment by its probable response to disturbance (Bryce and others, 1999). These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and non-government organizations that are responsible for different types of resources within the same geographical areas (Omernik and others, 2000). The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of the spatial patterns and the composition of biotic and abiotic phenomena that affect or reflect differences in ecosystem quality and integrity (Wiken, 1986; Omernik, 1987, 1995). These phenomena include geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another regardless of the hierarchical level. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). This product is part of a collaborative effort primarily between USEPA Region VII, USEPA National Health and Environmental Effects Research Laboratory (Corvallis, Oregon), Mississippi Department of Environmental Quality, Arkansas Department of Environmental Quality, Arkansas Multi-Agency Wetland Planning Team (MAWPT), U.S. Army Corps of Engineers (USACE), U.S. Department of Agriculture (USDA) - Natural Resources Conservation Service (NRCS), U.S. Department of Interior - Fish and Wildlife Service (USFWS), and U.S. Department of Interior - U.S. Geological Survey (USGS) - Earth Resources Observation Systems (EROS) Data Center. The project is associated with an interagency effort to develop a common framework of ecological regions. Reaching that objective requires recognition of the differences in the conceptual approaches and mapping methodologies that have been used to develop the most common ecoregion-type frameworks, including those developed by the U.S. Department of Agriculture - Forest Service (USFS) (Bailey and others, 1994), the USEPA (Omernik, 1987, 1995), and the NRCS (United States Department of Agriculture - Soil Conservation Service, 1981). As each of these frameworks is further refined, their differences are becoming less discernible. Regional collaborative projects such as this one in the Mississippi Alluvial Plain, where agreement can be reached among multiple resource management agencies, are a step toward attaining consensus and consistency in ecoregion frameworks for the entire nation. Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/map/map_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Massachusetts",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{9177ffb8-4dbf-45db-9382-9c2eded1db51}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319353,45 +319323,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-92.525413, 28.897483, -88.098311, 37.457045",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of the Mississippi Alluvial Plain"
         },
-            "identifier": "{2ADC5C7C-7887-4180-9AC6-22E9E26E9549}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-73.608821, 41.088039, -69.448037, 43.300614",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ma/ma_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Massachusetts",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{2ADC5C7C-7887-4180-9AC6-22E9E26E9549}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319401,45 +319371,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-73.608821, 41.088039, -69.448037, 43.300614",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Massachusetts"
         },
-            "identifier": "{FE3B8466-35B5-4F00-8356-E97A55BB4A02}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-73.608821, 41.088039, -69.448037, 43.300614",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ma/ma_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Maryland",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{FE3B8466-35B5-4F00-8356-E97A55BB4A02}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319449,45 +319419,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-73.608821, 41.088039, -69.448037, 43.300614",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Massachusetts"
         },
-            "identifier": "{4FCCF746-A5AD-45B9-9A44-7BAD0817C525}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-79.759437, 37.788086, -74.721471, 40.250703",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/md/md_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Maryland",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{4FCCF746-A5AD-45B9-9A44-7BAD0817C525}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319497,45 +319467,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-79.759437, 37.788086, -74.721471, 40.250703",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Maryland"
         },
-            "identifier": "{F147B70A-6D27-4059-8D27-DDDD4CCC9936}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-79.759437, 37.788086, -74.721471, 40.250703",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/md/md_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Maine",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F147B70A-6D27-4059-8D27-DDDD4CCC9936}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319545,45 +319515,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-79.759437, 37.788086, -74.721471, 40.250703",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Maryland"
         },
-            "identifier": "{E3BDDE35-477F-44AD-B8FC-509FC1677FB8}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-71.831665, 42.489864, -66.0065, 47.731693",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/me/me_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Maine",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E3BDDE35-477F-44AD-B8FC-509FC1677FB8}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319593,45 +319563,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-71.831665, 42.489864, -66.0065, 47.731693",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Maine"
         },
-            "identifier": "{FED0500B-32D9-4AC1-BE06-8EC5B994369D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-71.831665, 42.489864, -66.0065, 47.731693",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/me/me_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Michigan",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{FED0500B-32D9-4AC1-BE06-8EC5B994369D}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319641,45 +319611,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-71.831665, 42.489864, -66.0065, 47.731693",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Maine"
         },
-            "identifier": "{99F2BCB4-D719-488D-A464-D2EEC7BF71F5}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-90.783117, 41.400263, -81.433673, 48.27753",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mi/mi_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Michigan",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{99F2BCB4-D719-488D-A464-D2EEC7BF71F5}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319689,45 +319659,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-90.783117, 41.400263, -81.433673, 48.27753",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Michigan"
         },
-            "identifier": "{070AA5A2-C32C-4D7A-AF46-8D6520337A78}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-90.783117, 41.400263, -81.433673, 48.27753",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mi/mi_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Minnesota",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{070AA5A2-C32C-4D7A-AF46-8D6520337A78}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319737,45 +319707,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-90.783117, 41.400263, -81.433673, 48.27753",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Michigan"
         },
-            "identifier": "{0C38126A-B4AC-4B27-820F-DF4773BC2A45}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-97.247273, 43.360038, -89.366368, 49.386888",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mn/mn_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Minnesota",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{0C38126A-B4AC-4B27-820F-DF4773BC2A45}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319785,45 +319755,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-97.247273, 43.360038, -89.366368, 49.386888",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Minnesota"
         },
-            "identifier": "{2F99A34C-F710-410D-8574-DCE85A89DEB2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-97.247273, 43.360038, -89.366368, 49.386888",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mn/mn_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Missouri",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{2F99A34C-F710-410D-8574-DCE85A89DEB2}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319833,45 +319803,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-97.247273, 43.360038, -89.366368, 49.386888",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Minnesota"
         },
-            "identifier": "{A3F01242-401A-407B-811E-6D31CC148F11}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-95.787941, 00.004, -88.757346, 40.685321",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mo/mo_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Missouri",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{A3F01242-401A-407B-811E-6D31CC148F11}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319881,45 +319851,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-95.787941, 00.004, -88.757346, 40.685321",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Missouri"
         },
-            "identifier": "{038133F4-A9D4-4874-87DC-FADDBC1E659E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-95.787941, 35.933699, -88.757346, 40.685321",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mo/mo_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Mississippi",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{038133F4-A9D4-4874-87DC-FADDBC1E659E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319929,45 +319899,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-95.787941, 35.933699, -88.757346, 40.685321",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Missouri"
         },
-            "identifier": "{80C6F375-0E43-4161-94FA-4354CEF5F4E4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.706215, 30.106391, -87.936654, 35.165908",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ms/ms_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Mississippi",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{80C6F375-0E43-4161-94FA-4354CEF5F4E4}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -319977,45 +319947,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.706215, 30.106391, -87.936654, 35.165908",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Mississippi"
         },
-            "identifier": "{9CDD16D7-01B9-4FA1-A124-65A83FAFEBCE}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.706215, 30.106391, -87.936654, 35.165908",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ms/ms_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Montana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{9CDD16D7-01B9-4FA1-A124-65A83FAFEBCE}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320025,45 +319995,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.706215, 30.106391, -87.936654, 35.165908",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Mississippi"
         },
-            "identifier": "{19D42E2B-584B-4C48-BA2A-C405FBFE442E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-116.360174, 43.901156, -103.574576, 50.191186",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mt/mt_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Montana",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{19D42E2B-584B-4C48-BA2A-C405FBFE442E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320073,45 +320043,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-116.360174, 43.901156, -103.574576, 50.191186",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Montana"
         },
-            "identifier": "{1FFA355E-5967-4828-94DC-89B1A2921E0E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-116.360174, 43.901156, -103.574576, 50.191186",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/mt/mt_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of North Carolina",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{1FFA355E-5967-4828-94DC-89B1A2921E0E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320121,45 +320091,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-116.360174, 43.901156, -103.574576, 50.191186",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Montana"
         },
-            "identifier": "{A1AEA979-6834-42E2-98E2-2B14C9DC0DBD}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-84.387208, 33.43288, -75.193935, 37.6331",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nc/nc_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of North Carolina",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{A1AEA979-6834-42E2-98E2-2B14C9DC0DBD}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320169,45 +320139,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-84.387208, 33.43288, -75.193935, 37.6331",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of North Carolina"
         },
-            "identifier": "{A396D59D-6E44-4D0D-BB7C-59654ABDA31B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-84.387208, 33.43288, -75.193935, 37.6331",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nc/nc_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of North Dakota",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{A396D59D-6E44-4D0D-BB7C-59654ABDA31B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320217,45 +320187,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-84.387208, 33.43288, -75.193935, 37.6331",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of North Carolina"
         },
-            "identifier": "{D1959436-0A65-4FFA-878C-D2A6F9690274}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.048918, 45.935018, -96.554509, 49.000691",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nd/nd_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of North Dakota",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{D1959436-0A65-4FFA-878C-D2A6F9690274}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320265,45 +320235,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.048918, 45.935018, -96.554509, 49.000691",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of North Dakota"
         },
-            "identifier": "{AC3775BD-59CB-4F39-BB39-4459B2B08DD6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.048918, 45.935018, -96.554509, 49.000691",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nd/nd_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Nebraska",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{AC3775BD-59CB-4F39-BB39-4459B2B08DD6}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320313,45 +320283,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.048918, 45.935018, -96.554509, 49.000691",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of North Dakota"
         },
-            "identifier": "{A64B5800-986E-4C78-A752-D2B8AAE80392}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.285778, 39.751006, -95.275571, 43.248163",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ne/ne_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Nebraska",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{A64B5800-986E-4C78-A752-D2B8AAE80392}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320361,45 +320331,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.285778, 39.751006, -95.275571, 43.248163",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Nebraska"
         },
-            "identifier": "{F02D728E-48E6-452E-A14A-4DA85503611F}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.285778, 39.751006, -95.275571, 43.248163",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ne/ne_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of New Hampshire",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F02D728E-48E6-452E-A14A-4DA85503611F}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320409,45 +320379,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.285778, 39.751006, -95.275571, 43.248163",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Nebraska"
         },
-            "identifier": "{D3993BE4-5109-4FE3-95C6-5080D9176D91}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-72.661589, 42.436554, -69.923321, 45.422227",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nh/nh_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of New Hampshire",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{D3993BE4-5109-4FE3-95C6-5080D9176D91}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320457,45 +320427,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-72.661589, 42.436554, -69.923321, 45.422227",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of New Hampshire"
         },
-            "identifier": "{78BEBAE5-2B94-434B-BF4F-18E337FEA969}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-72.661589, 42.436554, -69.923321, 45.422227",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nh/nh_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of New Jersey",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{78BEBAE5-2B94-434B-BF4F-18E337FEA969}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320505,45 +320475,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-72.661589, 42.436554, -69.923321, 45.422227",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of New Hampshire"
         },
-            "identifier": "{3ACF7D6D-1D95-4035-B499-AA7EE19127D2}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-75.722592, 38.829092, -73.647186, 41.41414",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nj/nj_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of New Jersey",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{3ACF7D6D-1D95-4035-B499-AA7EE19127D2}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320553,45 +320523,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-75.722592, 38.829092, -73.647186, 41.41414",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of New Jersey"
         },
-            "identifier": "{F9AA0978-C622-41BD-A14F-95EFF789F614}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-75.722592, 38.829092, -73.647186, 41.41414",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nj/nj_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of New Mexico",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F9AA0978-C622-41BD-A14F-95EFF789F614}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320601,45 +320571,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-75.722592, 38.829092, -73.647186, 41.41414",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of New Jersey"
         },
-            "identifier": "{569D3C9F-2524-435A-8E71-CF0640670848}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-110.022491, 31.239256, -102.547958, 37.498166",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nm/nm_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of New Mexico",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{569D3C9F-2524-435A-8E71-CF0640670848}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320649,45 +320619,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-110.022491, 31.239256, -102.547958, 37.498166",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of New Mexico"
         },
-            "identifier": "{981766F3-763F-45CC-8B05-6797DF06ECE6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-110.022491, 31.239256, -102.547958, 37.498166",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nm/nm_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Nevada",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{981766F3-763F-45CC-8B05-6797DF06ECE6}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320697,45 +320667,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-110.022491, 31.239256, -102.547958, 37.498166",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of New Mexico"
         },
-            "identifier": "{F46A0A75-6F07-4279-9AB8-095CCB49805E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-120.984704, 42.938699, -112.452802, 42.938699",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nv/nv_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Nevada",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F46A0A75-6F07-4279-9AB8-095CCB49805E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320745,45 +320715,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-120.984704, 42.938699, -112.452802, 42.938699",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Nevada"
         },
-            "identifier": "{E984E6BE-9B9A-465F-BCA0-16BDD90EE9ED}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-120.984704, 34.307110, -112.452802, 42.938699",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/nv/nv_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of New York",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E984E6BE-9B9A-465F-BCA0-16BDD90EE9ED}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320793,45 +320763,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-120.984704, 34.307110, -112.452802, 42.938699",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Nevada"
         },
-            "identifier": "{24C97D8B-80DA-41E5-BCD6-E46A48351E2B}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-79.97406, 40.116925, -70.59714, 45.838613",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ny/ny_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of New York",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{24C97D8B-80DA-41E5-BCD6-E46A48351E2B}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320841,45 +320811,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-79.97406, 40.116925, -70.59714, 45.838613",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of New York"
         },
-            "identifier": "{147E8848-7673-46E1-8267-D1771DF2C2FD}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-79.97406, 40.116925, -70.59714, 45.838613",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ny/ny_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Ohio",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{147E8848-7673-46E1-8267-D1771DF2C2FD}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320889,45 +320859,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-79.97406, 40.116925, -70.59714, 45.838613",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of New York"
         },
-            "identifier": "{37EB4CC2-62C3-4B65-A9DC-5F199050AD88}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-85.271115, 38.226015, -80.227784, 42.411432",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/oh/oh_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Ohio",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{37EB4CC2-62C3-4B65-A9DC-5F199050AD88}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320937,45 +320907,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-85.271115, 38.226015, -80.227784, 42.411432",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Ohio"
         },
-            "identifier": "{BF2F6ECD-F4ED-4F88-AFE3-3CF18F26761E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-85.271115, 38.226015, -80.227784, 42.411432",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/oh/oh_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Oklahoma",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{BF2F6ECD-F4ED-4F88-AFE3-3CF18F26761E}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -320985,45 +320955,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-85.271115, 38.226015, -80.227784, 42.411432",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Ohio"
         },
-            "identifier": "{5517EA5B-F04B-45A0-A8B5-DAFE37BD11D9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-103.049074, 33.428354, -94.393233, 37.203079",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ok/ok_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Oklahoma",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{5517EA5B-F04B-45A0-A8B5-DAFE37BD11D9}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -321033,45 +321003,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-103.049074, 33.428354, -94.393233, 37.203079",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Oklahoma"
         },
-            "identifier": "{349F6459-5FBC-4E0F-BEDE-BFE0A9CD81F6}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-103.049074, 33.428354, -94.393233, 37.203079",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ok/ok_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Oregon",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{349F6459-5FBC-4E0F-BEDE-BFE0A9CD81F6}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -321081,45 +321051,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-103.049074, 33.428354, -94.393233, 37.203079",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Oklahoma"
         },
-            "identifier": "{221C3915-9B2E-4B84-8685-D296D61D8954}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.988884, 40.685851, -115.46, 47.507285",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/or/or_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Oregon",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{221C3915-9B2E-4B84-8685-D296D61D8954}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -321129,45 +321099,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.988884, 40.685851, -115.46, 47.507285",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Oregon"
         },
-            "identifier": "{E172999C-CB31-4F5B-AB0E-989739AFFEFB}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.988884, 40.685851, -115.46, 47.507285",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/or/or_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Pennsylvania",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E172999C-CB31-4F5B-AB0E-989739AFFEFB}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -321177,45 +321147,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.988884, 40.685851, -115.46, 47.507285",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Oregon"
         },
-            "identifier": "{244587F6-BB23-4BEC-B979-D78DDBA88856}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-80.995619, 38.918718, -74.21005, 42.706316",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/pa/pa_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Pennsylvania",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{244587F6-BB23-4BEC-B979-D78DDBA88856}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -321225,45 +321195,93 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
+            "rights": "Use Constraints: None",
+            "spatial": "-80.995619, 38.918718, -74.21005, 42.706316",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Pennsylvania"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Randy Comeleo",
                 "hasEmail": "mailto:comeleo.randy@epa.gov"
             },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/pa/pa_eco_l4.zip",
+                    "title": "Download"
+                }
+            ],
             "identifier": "{2852DB06-91AB-4193-9DE3-50B45F728141}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "issued": "2012-01-01",
+            "keyword": [
+                "Natural Resources",
+                "Environment",
+                "Surface Water",
+                "Management",
+                "Ecosystem",
+                "geospatial",
+                "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2012-01-01",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
+            },
             "rights": "Use Constraints: None",
             "spatial": "-80.995619, 38.918718, -74.21005, 42.706316",
             "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
             "theme": "boundaries",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/pa/pa_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Level IV Ecoregions of Pennsylvania"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 10",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
             "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg10/reg10_eco_l3.zip",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{A21DC751-F3AF-464F-8817-401A81F57D25}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -321279,45 +321297,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-127.115090, 39.893575, -110.525874, 50.649347",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 10"
         },
-            "identifier": "{A21DC751-F3AF-464F-8817-401A81F57D25}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-127.115090, 39.893575, -110.525874, 50.649347",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg10/reg10_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg10/reg10_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 10",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{9F09EC2B-6F3C-4103-A13D-951579357181}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -321333,45 +321351,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-127.115090, 39.893575, -110.525874, 50.649347",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 10"
         },
-            "identifier": "{9F09EC2B-6F3C-4103-A13D-951579357181}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-127.115090, 39.893575, -110.525874, 50.649347",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg10/reg10_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg1/reg1_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 1",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{48E81B01-B7D4-406F-A76E-E5D713E1BC86}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Connecticut",
                 "Vermont",
@@ -321390,45 +321408,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-74.602285, 40.044110, -66.006500, 48.115773",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 1"
         },
-            "identifier": "{48E81B01-B7D4-406F-A76E-E5D713E1BC86}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-74.602285, 40.044110, -66.006500, 48.115773",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg1/reg1_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg1/reg1_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 1",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E7433B98-F24D-406D-A814-454CC2ADFF1D}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Connecticut",
                 "Vermont",
@@ -321447,45 +321465,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-74.602285, 40.044110, -66.006500, 48.115773",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 1"
         },
-            "identifier": "{E7433B98-F24D-406D-A814-454CC2ADFF1D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-74.602285, 40.044110, -66.006500, 48.115773",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg1/reg1_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg2/reg2_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 2",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E07C7D0E-D324-4A5D-97A4-94AF28475F53}",
+            "issued": "2010-05-01",
             "keyword": [
                 "New Jersey",
                 "Natural Resources",
@@ -321500,45 +321518,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-80.338646, 38.520875, -70.597140, 45.838613",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 2"
         },
-            "identifier": "{E07C7D0E-D324-4A5D-97A4-94AF28475F53}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-80.338646, 38.520875, -70.597140, 45.838613",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg2/reg2_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg2/reg2_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 2",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{8724F274-1686-4F8D-B576-B6EC50D2CF24}",
+            "issued": "2010-05-01",
             "keyword": [
                 "New Jersey",
                 "Natural Resources",
@@ -321553,45 +321571,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-80.338646, 38.520875, -70.597140, 45.838613",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 2"
         },
-            "identifier": "{8724F274-1686-4F8D-B576-B6EC50D2CF24}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-80.338646, 38.520875, -70.597140, 45.838613",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg2/reg2_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg3/reg3_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 3",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{E087A25A-6792-4D36-89EA-2FF5C48F6FF4}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Virginia",
@@ -321610,45 +321628,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-83.675409, 35.525667, -74.030504, 42.950804",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 3"
         },
-            "identifier": "{E087A25A-6792-4D36-89EA-2FF5C48F6FF4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-83.675409, 35.525667, -74.030504, 42.950804",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg3/reg3_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg3/reg3_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 3",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{EC589478-0086-4F6C-BCE0-12AEA2305144}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Virginia",
@@ -321667,45 +321685,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-83.675409, 35.525667, -74.030504, 42.950804",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 3"
         },
-            "identifier": "{EC589478-0086-4F6C-BCE0-12AEA2305144}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-83.675409, 35.525667, -74.030504, 42.950804",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg3/reg3_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg4/reg4_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 4",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{4142B546-FFEB-4ED3-A801-F9E759B74921}",
+            "issued": "2010-05-01",
             "keyword": [
                 "North Carolina",
                 "Natural Resources",
@@ -321725,45 +321743,45 @@
                 "Florida",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.945238, 23.914498, -74.796314, 39.562647",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 4"
         },
-            "identifier": "{4142B546-FFEB-4ED3-A801-F9E759B74921}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.945238, 23.914498, -74.796314, 39.562647",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg4/reg4_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg4/reg4_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 4",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{F9B998DD-E7CF-47AF-A38B-17F086FF54E3}",
+            "issued": "2010-05-01",
             "keyword": [
                 "North Carolina",
                 "Natural Resources",
@@ -321784,45 +321802,45 @@
                 "Florida",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-91.945238, 23.914498, -74.796314, 39.562647",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 4"
         },
-            "identifier": "{F9B998DD-E7CF-47AF-A38B-17F086FF54E3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-91.945238, 23.914498, -74.796314, 39.562647",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg4/reg4_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg5/reg5_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 5",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{0BEDEE0B-BF58-4FBC-9A50-481C2404A51D}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Ohio",
                 "Natural Resources",
@@ -321841,45 +321859,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-97.247273, 36.276617, -78.642014, 49.386888",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 5"
         },
-            "identifier": "{0BEDEE0B-BF58-4FBC-9A50-481C2404A51D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-97.247273, 36.276617, -78.642014, 49.386888",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg5/reg5_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg5/reg5_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 5",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{66B86675-3885-4822-ADC3-FF91B9DBC997}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Ohio",
                 "Natural Resources",
@@ -321898,45 +321916,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-97.247273, 36.276617, -78.642014, 49.386888",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 5"
         },
-            "identifier": "{66B86675-3885-4822-ADC3-FF91B9DBC997}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-97.247273, 36.276617, -78.642014, 49.386888",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg5/reg5_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg6/reg6_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 6",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{0401A825-ACF5-4830-82B3-214E09A4FEE3}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Louisiana",
                 "New Mexico",
@@ -321954,45 +321972,45 @@
                 "Oklahoma",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-110.022491, 25.128028, -88.089078, 37.702364",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 6"
         },
-            "identifier": "{0401A825-ACF5-4830-82B3-214E09A4FEE3}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-110.022491, 25.128028, -88.089078, 37.702364",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg6/reg6_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg6/reg6_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 6",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{80DB9709-8CE8-4FC6-A81D-D67763284762}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Louisiana",
                 "New Mexico",
@@ -322010,45 +322028,45 @@
                 "Oklahoma",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-110.022491, 25.128028, -88.089078, 37.702364",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 6"
         },
-            "identifier": "{80DB9709-8CE8-4FC6-A81D-D67763284762}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-110.022491, 25.128028, -88.089078, 37.702364",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg6/reg6_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg7/reg7_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 7",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{188B8C60-3D83-4901-A039-FA92929BD3B7}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Kansas",
@@ -322065,45 +322083,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.326627, 35.891383, -88.451008, 43.587317",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 7"
         },
-            "identifier": "{188B8C60-3D83-4901-A039-FA92929BD3B7}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.326627, 35.891383, -88.451008, 43.587317",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg7/reg7_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg7/reg7_eco_l4.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 7",
-            "description": "Ecoregions by EPA region were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 52 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 104 regions whereas the conterminous United States has 84 (U.S. Environmental Protection Agency, 2005). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{43353295-116D-48B7-A55F-2D3D76DBC83E}",
+            "issued": "2010-05-01",
             "keyword": [
                 "Natural Resources",
                 "Kansas",
@@ -322120,45 +322138,45 @@
                 "United States",
                 "Biology"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-05-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-104.326627, 35.891383, -88.451008, 43.587317",
+            "temporal": "2010-05-01/2010-05-01",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 7"
         },
-            "identifier": "{43353295-116D-48B7-A55F-2D3D76DBC83E}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-104.326627, 35.891383, -88.451008, 43.587317",
-            "temporal": "2010-05-01/2010-05-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-05-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg7/reg7_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg8/reg8_eco_l3.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 8",
-            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{b23d0dd3-502c-421f-8c3f-11fed82fbd90}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322168,93 +322186,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
-            },
-            "identifier": "{b23d0dd3-502c-421f-8c3f-11fed82fbd90}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "Use Constraints: None",
             "spatial": "-117.462417, 35.820315, -96.401643, 50.425890",
             "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
             "theme": "boundaries",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg8/reg8_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "Level III Ecoregions of EPA Region 8"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 8",
-            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
-            "keyword": [
-                "Natural Resources",
-                "Environment",
-                "Surface Water",
-                "Management",
-                "Ecosystem",
-                "geospatial",
-                "United States"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2012-01-01",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Randy Comeleo",
                 "hasEmail": "mailto:comeleo.randy@epa.gov"
             },
-            "identifier": "{453bb823-cca5-4b29-a3e5-ad8f1f7e637f}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-117.462417, 35.820315, -96.401643, 50.425890",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg8/reg8_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of EPA Region 9",
-            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{453bb823-cca5-4b29-a3e5-ad8f1f7e637f}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322264,45 +322234,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-117.462417, 35.820315, -96.401643, 50.425890",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 8"
         },
-            "identifier": "{6518bfb2-d060-4775-bd7d-0b3d0c46abb4}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.012651, 29.34366, -108.138986, 44.278032",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg9/reg9_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of EPA Region 9",
-            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{6518bfb2-d060-4775-bd7d-0b3d0c46abb4}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322312,45 +322282,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.012651, 29.34366, -108.138986, 44.278032",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of EPA Region 9"
         },
-            "identifier": "{b8bc437b-d959-4cba-ba48-b09cf36b38fd}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-125.012651, 29.34366, -108.138986, 44.278032",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions for EPA Administrative Regions were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/reg9/reg9_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of Rhode Island",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{b8bc437b-d959-4cba-ba48-b09cf36b38fd}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322360,45 +322330,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-125.012651, 29.34366, -108.138986, 44.278032",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of EPA Region 9"
         },
-            "identifier": "{99A032B9-8FA9-4AF4-91EC-D64881B4228D}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-72.069017, 41.082067, -70.960729, 42.093647",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ri/ri_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of Rhode Island",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{99A032B9-8FA9-4AF4-91EC-D64881B4228D}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322408,45 +322378,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-72.069017, 41.082067, -70.960729, 42.093647",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level III Ecoregions of Rhode Island"
         },
-            "identifier": "{B3B8AACF-9AE9-4999-B5F2-834B95A706D1}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-72.069017, 41.082067, -70.960729, 42.093647",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ri/ri_eco_l4.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level III Ecoregions of South Carolina",
-            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
+            ],
+            "identifier": "{B3B8AACF-9AE9-4999-B5F2-834B95A706D1}",
+            "issued": "2012-01-01",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -322456,45 +322426,45 @@
                 "geospatial",
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
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            "rights": "Use Constraints: None",
+            "spatial": "-72.069017, 41.082067, -70.960729, 42.093647",
+            "temporal": "2012-05-08/2012-05-08",
+            "theme": "boundaries",
+            "title": "Level IV Ecoregions of Rhode Island"
         },
-            "identifier": "{5E58DDA9-8306-4182-9528-05E2D54C56D9}",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "Use Constraints: None",
-            "spatial": "-83.726653, 31.772683, -78.337883, 35.410471",
-            "temporal": "2012-05-08/2012-05-08",
-            "accrualPeriodicity": "irregular",
-            "issued": "2012-01-01",
-            "language": "en-us",
-            "theme": "boundaries",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:comeleo.randy@epa.gov"
+            },
+            "description": "Ecoregions by state were extracted from the seamless national shapefile. Ecoregions denote areas of general similarity in ecosystems and in the type, quality, and quantity of environmental resources. They are designed to serve as a spatial framework for the research, assessment, management, and monitoring of ecosystems and ecosystem components. These general purpose regions are critical for structuring and implementing ecosystem management strategies across federal agencies, state agencies, and nongovernment organizations that are responsible for different types of resources within the same geographical areas. The approach used to compile this map is based on the premise that ecological regions can be identified through the analysis of patterns of biotic and abiotic phenomena, including geology, physiography, vegetation, climate, soils, land use, wildlife, and hydrology. The relative importance of each characteristic varies from one ecological region to another. A Roman numeral hierarchical scheme has been adopted for different levels for ecological regions. Level I is the coarsest level, dividing North America into 15 ecological regions. Level II divides the continent into 50 regions (Commission for Environmental Cooperation Working Group, 1997). At Level III, the continental United States contains 105 regions whereas the conterminous United States has 85 (U.S. Environmental Protection Agency, 2011). Level IV ecoregions are further subdivisions of Level III ecoregions. Methods used to define the ecoregions are explained in Omernik (1995, 2004), Omernik and others (2000), and Gallant and others (1989). Literature cited: Commission for Environmental Cooperation Working Group, 1997, Ecological regions of North America- toward a common perspective: Montreal, Commission for Environmental Cooperation, 71 p. Gallant, A. L., Whittier, T.R., Larsen, D.P., Omernik, J.M., and Hughes, R.M., 1989, Regionalization as a tool for managing environmental resources: Corvallis, Oregon, U.S. Environmental Protection Agency, EPA/600/3-89/060, 152p. Omernik, J.M., 1995, Ecoregions - a framework for environmental management, in Davis, W.S. and Simon, T.P., eds., Biological assessment and criteria-tools for water resource planning and decision making: Boca Raton, Florida, Lewis Publishers, p.49-62. Omernik, J.M., Chapman, S.S., Lillie, R.A., and Dumke, R.T., 2000, Ecoregions of Wisconsin: Transactions of the Wisconsin Academy of Science, Arts, and Letters, v. 88, p. 77-103. Omernik, J.M., 2004, Perspectives on the nature and definitions of ecological regions: Environmental Management, v. 34, Supplement 1, p. s27-s38. U.S. Environmental Protection Agency. 2011. Level III and IV ecoregions of the continental United States. U.S. EPA, National Health and Environmental Effects Research Laboratory, Corvallis, Oregon, Map scale 1:3,000,000. Available online at: https://www.epa.gov/eco-research/level-iii-and-iv-ecoregions-continental-united-states. Comments and questions regarding Ecoregions should be addressed to Glenn Griffith, USGS, c/o US EPA., 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4465, email:griffith.glenn@epa.gov Alternate: James Omernik, USGS, c/o US EPA, 200 SW 35th Street, Corvallis, OR 97333, (541)-754-4458, email:omernik.james@epa.gov",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/sc/sc_eco_l3.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Level IV Ecoregions of South Carolina",
```

