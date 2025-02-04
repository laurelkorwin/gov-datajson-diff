# Change History for epa.json (Part 40)

### Changes from 31606f9 to dd2190f (Part 30/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "HERO contains the key studies EPA uses to develop environmental risk assessments for the public. EPA uses risk assessments to characterize the nature and magnitude of health risks to humans and the ecosystem from pollutants and chemicals in the environment.",
+            "distribution": [],
             "identifier": "{8E982CE9-B802-4A3B-A4FB-7BD7785A9813}",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "issued": "2014",
+            "keyword": [
+                "Environment",
+                "geospatial",
+                "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2014",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Research & Development (ORD)"
+            },
             "rights": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180, 18, -66, 72",
             "temporal": "\n                                    /\n                                    ",
-            "accrualPeriodicity": "irregular",
-            "issued": "2014",
             "theme": "environment",
-            "distribution": []
+            "title": "Health and Environmental Research Online (HERO) database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "JonesEtAl 2021 Study Locations",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            },
             "description": "This shapefile includes the areas of interest used in our analysis for the analyses published in Jones et al. 2021. Each area of interest is divided into numerous polygonal assessment units as described in the accompanying research article. Each polygon has attributes that include FID, Name, Number (used in our published map figure and tables), and shape area (in meters squared). See Credits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/HydrologicLandscapes/JonesEtAl_2021_Study_Locations.zip"
+                }
+            ],
+            "identifier": "124655B0-C24B-4002-A76F-527F55556843",
+            "issued": "2020-01-13",
             "keyword": [
                 "Natural Resources",
                 "Environment",
@@ -309247,39 +309262,44 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA (US EPA, CPHEA/PESD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.656301, 30.155139, -108.801796, 50.388893",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "JonesEtAl 2021 Study Locations"
         },
-            "identifier": "124655B0-C24B-4002-A76F-527F55556843",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.656301, 30.155139, -108.801796, 50.388893",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-13",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change on raw water concentrations/loads of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050)).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/HydrologicLandscapes/JonesEtAl_2021_Study_Locations.zip"
-                }
-            ]
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "LULC Change From-To Classes for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions",
-            "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change on raw water concentrations/loads of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050)).",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.mrlc.gov/data"
+                }
+            ],
+            "identifier": "E4621A95-1109-4134-844E-8D9593B1DE3E",
+            "issued": "2023-03-03",
             "keyword": [
                 "020:072",
                 "010",
@@ -309298,30 +309318,33 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-03-03",
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
+            "rights": "licenseUnrestricted",
+            "spatial": "-88, -87, 46, 47",
+            "temporal": "2022-02-23T08:00:00/None",
+            "title": "LULC Change From-To Classes for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions"
         },
-            "identifier": "E4621A95-1109-4134-844E-8D9593B1DE3E",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-88, -87, 46, 47",
-            "temporal": "2022-02-23T08:00:00/None",
-            "accrualPeriodicity": "irregular",
-            "issued": "2023-03-03",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change raw water concentrations of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050) for a total of eight scenarios.\n\t\t\n\t\tThe LULC net change file reports total change in hectares between 2011 and 2015 for forest, developed, cropland, pastures, and wetland for the four IPCC SRES scenarios with and without forest recovery.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -309331,12 +309354,9 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.mrlc.gov/data"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "LULC Net Change for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions",
-            "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change raw water concentrations of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050) for a total of eight scenarios.\n\t\t\n\t\tThe LULC net change file reports total change in hectares between 2011 and 2015 for forest, developed, cropland, pastures, and wetland for the four IPCC SRES scenarios with and without forest recovery.",
+            ],
+            "identifier": "E3728DC5-F122-46CA-9978-56A8ECA67C61",
+            "issued": "2023-03-03",
             "keyword": [
                 "020:072",
                 "010",
@@ -309355,45 +309375,36 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-03-03",
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
-            },
-            "identifier": "E3728DC5-F122-46CA-9978-56A8ECA67C61",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-88, -87, 46, 47",
             "temporal": "2022-02-23T08:00:00/None",
-            "accrualPeriodicity": "irregular",
-            "issued": "2023-03-03",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.mrlc.gov/data"
-                }
-            ]
+            "title": "LULC Net Change for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Physiological Parameters Database for Older Adults",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chad Thompson",
+                "hasEmail": "mailto:thompson.chad@epa.gov"
+            },
             "description": "The Physiological Parameters Database for Older Adults is available for download and contains physiological parameters values for healthy older human adults (age 60 and older), as well as data for some individuals with adverse health conditions that may relate to environmental exposure.  The information in this database was collected from review of peer-review published papers.",
+            "distribution": [],
+            "identifier": "{864CD515-C7A4-48FF-9DBC-7C4164DC2FBD}",
+            "issued": "2014",
             "keyword": [
                 "DataFinder",
                 "Human Health",
@@ -309403,37 +309414,37 @@
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
                 "name": "U.S. EPA Office of Research & Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Chad Thompson",
-                "hasEmail": "mailto:thompson.chad@epa.gov"
-            },
-            "identifier": "{864CD515-C7A4-48FF-9DBC-7C4164DC2FBD}",
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
+            "title": "Physiological Parameters Database for Older Adults"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Polychlorinated Biphenyls (PCB) Residue Effects Database",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ECOTOX Support",
+                "hasEmail": "mailto:ecotox.support@epa.gov"
+            },
             "description": "The PCB Residue Effects (PCBRes) Database was developed to assist scientists and risk assessors in correlating PCB and dioxin-like compound residues with toxic effects. The purpose is to develop PCB critical residue values for fish, mammals and birds, especially as these relate to aquatic and aquatic-dependent species.",
+            "distribution": [],
+            "identifier": "{C01775F2-A45E-4367-BE93-9629C82F6872}",
+            "issued": "2014",
             "keyword": [
                 "DataFinder",
                 "Air",
@@ -309446,37 +309457,37 @@
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
                 "name": "U.S. EPA Office of Research & Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ECOTOX Support",
-                "hasEmail": "mailto:ecotox.support@epa.gov"
-            },
-            "identifier": "{C01775F2-A45E-4367-BE93-9629C82F6872}",
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
+            "title": "Polychlorinated Biphenyls (PCB) Residue Effects Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Polychlorinated Biphenyls (PCB) Transformer Registration Database",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "TSCA Hotline",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
             "description": "The Polychlorinated Biphenyls (PCB) Transformer Registration Database tracks geographic and dated information of registered PCB transformers.",
+            "distribution": [],
+            "identifier": "{CDE0CD61-4C9A-4288-92C4-7D9BAAAD480D}",
+            "issued": "2014",
             "keyword": [
                 "DataFinder",
                 "Air",
@@ -309487,37 +309498,45 @@
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
                 "name": "U.S. EPA Office of Solid Waste and Emergency Response (OSWER)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "TSCA Hotline",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
-            },
-            "identifier": "{CDE0CD61-4C9A-4288-92C4-7D9BAAAD480D}",
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
+            "title": "Polychlorinated Biphenyls (PCB) Transformer Registration Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "SWAT Reach Output Seasonal Change Scenarios for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
             "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change on raw water concentrations of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050).  \n\t\t\n\t\tUnits for the MeanDifference variable are different for TN/TP and sediment due to SWAT reporting conventions; TN and TP are in kilograms (kg) and sediment is in megagrams (Mg).  1 Mg = 1,000 kg.  Differences are scenario minus baseline; negative values indicate constituent loads were less for the scenario relative to the baseline.  NLCD2001 was included as a scenario to assess the effect of land cover change.  Negative values for the NLCD2001 scenario indicate that a constituent load was less in 2001 relative to 2011.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.mrlc.gov/data"
+                }
+            ],
+            "identifier": "929385C8-6763-4988-B388-680BCD9E008A",
+            "issued": "2023-03-03",
             "keyword": [
                 "020:072",
                 "010",
@@ -309536,44 +309555,36 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-03-03",
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
-            },
-            "identifier": "929385C8-6763-4988-B388-680BCD9E008A",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-88, -87, 47, 47",
             "temporal": "2022-02-23T08:00:00/None",
-            "issued": "2023-03-03",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.mrlc.gov/data"
-                }
-            ]
+            "title": "SWAT Reach Output Seasonal Change Scenarios for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ToxCast/ToxRefDB",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Katie Paul-Friedman",
+                "hasEmail": "mailto:CCTE@epa.gov"
+            },
             "description": "ToxCast is used as a cost-effective approach for efficiently prioritizing the toxicity testing of thousands of chemicals. It uses data from state-of-the-art high throughput screening (HTS) bioassay and builds computational models to forecast potential chemical toxicity in humans. ToxRefDB stores data related to ToxCast.",
+            "distribution": [],
+            "identifier": "{94ADB175-265C-494D-A25A-1BAF8501A274}",
+            "issued": "2014",
             "keyword": [
                 "Exposure",
                 "Health Risks",
@@ -309586,37 +309597,46 @@
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
-                "fn": "Katie Paul-Friedman",
-                "hasEmail": "mailto:CCTE@epa.gov"
-            },
-            "identifier": "{94ADB175-265C-494D-A25A-1BAF8501A274}",
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
+            "title": "ToxCast/ToxRefDB"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Trends in Source Water Quality for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
             "description": "We developed four 2011-2050 land cover change scenarios and modeled the impact of projected land cover change on influent water quality to support long-term planning for the city of Minneapolis, MN.  Baseline land cover was from the NLCD2011 database.  IPCC SRES scenarios (https://www.ipcc.ch/site/assets/uploads/2018/03/sres-en.pdf) interpreted by Sohl et al. (2014) (https://doi.org/10.1890/13-1245.1) for the conterminous United States were downscaled from 250 meters to 30 meters.  The baseline and scenario land cover data were used as input into the Soil Water and Assessment Tool (SWAT) model to assess the effect of outyear projected land cover change on the source of raw water for the city of Minneapolis, MN. SWAT was used to assess the effect of land cover change on raw water concentrations of sediment, total nitrogen, and total phosphorus. The IPCC SRES evaluated were A1B, A2, B1, and B2.  The four scenarios were implemented with (A1Bf) and without (A1B) forest recovery (e.g., conversion of cropland (2011) to forest (2050).\n\t\t\n\t\tData on treatment of raw (source) water quality, provided by the city of Minneapolis, MN, were used in autoregressive models to determine if there was a temporal trend in mass of treatment chemicals applied.  Models were run separately for each treatment chemical. Data are monthly application rates from 2008 through 2017.  The day of the month for the date variable was nominally set to one (1).  Data for alum were incomplete from 2008 through 2011, which were set to zero (0) and treated as missing in the autoregressive model. Water volume treated is in megagallons (Mg); 1 Mg = 1000 gallons.  A dummy variable for change in management philosphy was included in the model.  The dummy variable was set to zero (0) for the period 2008 - 2014 and one (1) afterward.  The dummy variable is not included in the file.  It had a significant effect only for the CO2 treatment chemical.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.mrlc.gov/data"
+                }
+            ],
+            "identifier": "2567EDA9-95F9-4A49-BA4D-54A002237582",
+            "issued": "2023-03-03",
             "keyword": [
                 "020:072",
                 "010",
@@ -309635,45 +309655,44 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-03-03",
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
+            "rights": "licenseUnrestricted",
+            "spatial": "-88, -87, 46, 47",
+            "temporal": "2022-02-23T08:00:00/None",
+            "title": "Trends in Source Water Quality for: Modeling Future Land Cover and Water Quality Change in Minneapolis, MN, USA to Support Drinking Water Source Protection Decisions"
         },
-            "identifier": "2567EDA9-95F9-4A49-BA4D-54A002237582",
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
-            "spatial": "-88, -87, 46, 47",
-            "temporal": "2022-02-23T08:00:00/None",
-            "accrualPeriodicity": "irregular",
-            "issued": "2023-03-03",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "description": "The U.S. Geological Survey (USGS), in partnership with several federal agencies, has developed and released five National Land Cover Database (NLCD) products over the past two decades: NLCD 1992, 2001, 2006, 2011 and 2016. U.S. EPA leads the accuracy assessment of NLCD land cover products in coordination with USGS and SUNY-ESF. The posted dataset includes map labels and reference labels for 4629 sample locations (pixels) from the NLCD 2016 database. The sample pixels were selected using a stratified random design based on the dual 2011 \u2013 2016 map labels. The data can be used to re-create the accuracy results reported in a forthcoming paper and in support of other applications. Accuracy results are reported for the 2011 and 2016 land cover products in the NLCD2016 database and for selected 2011-2006 changes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/Minneaoplis_Water_Quality_LCscenarios.zip"
+                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/NLCD2016RefData.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.mrlc.gov/data"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "NLCD 2016 Land Cover Reference Data, Conterminous United States",
-            "description": "The U.S. Geological Survey (USGS), in partnership with several federal agencies, has developed and released five National Land Cover Database (NLCD) products over the past two decades: NLCD 1992, 2001, 2006, 2011 and 2016. U.S. EPA leads the accuracy assessment of NLCD land cover products in coordination with USGS and SUNY-ESF. The posted dataset includes map labels and reference labels for 4629 sample locations (pixels) from the NLCD 2016 database. The sample pixels were selected using a stratified random design based on the dual 2011 \u2013 2016 map labels. The data can be used to re-create the accuracy results reported in a forthcoming paper and in support of other applications. Accuracy results are reported for the 2011 and 2016 land cover products in the NLCD2016 database and for selected 2011-2006 changes.",
+            ],
+            "identifier": "D83991AF-31B5-4B03-8218-268E70F7D3EB",
+            "issued": "2020-11-23",
             "keyword": [
                 "020:072",
                 "010",
@@ -309692,43 +309711,35 @@
                 "U.S. Geological Survey (USGS)",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-11-23",
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
+            "title": "NLCD 2016 Land Cover Reference Data, Conterminous United States"
         },
-            "identifier": "D83991AF-31B5-4B03-8218-268E70F7D3EB",
+        {
+            "@type": "dcat:Dataset",
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
-            "issued": "2020-11-23",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://edg.epa.gov/EPADataCommons/Public/ORD/EnviroAtlas/NLCD2016RefData.zip"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.mrlc.gov/data"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1901-1910 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "449D45FE-D1F1-42C1-AA53-9DFDA455E624",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "020:094",
@@ -309738,35 +309749,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period."
         },
-            "identifier": "449D45FE-D1F1-42C1-AA53-9DFDA455E624",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1930 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1901-1930 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "5DC6274A-569E-43BA-84DF-19D73A7E2312",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309777,35 +309788,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1930 and the 1971-2000 Normal period."
         },
-            "identifier": "5DC6274A-569E-43BA-84DF-19D73A7E2312",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1920 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1911-1920  relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "01D3E1C9-5842-40B5-AAC9-4D193483DAE0",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309816,35 +309827,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1920 and the 1971-2000 Normal period."
         },
-            "identifier": "01D3E1C9-5842-40B5-AAC9-4D193483DAE0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1940 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1911-1940 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "9BE7C996-21B7-4303-B5AE-8F38B842C134",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309855,35 +309866,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1940 and the 1971-2000 Normal period."
         },
-            "identifier": "9BE7C996-21B7-4303-B5AE-8F38B842C134",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1930 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1921-1930 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "CB4037D6-80E0-459E-A601-602BB3CD2526",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309894,35 +309905,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1930 and the 1971-2000 Normal period."
         },
-            "identifier": "CB4037D6-80E0-459E-A601-602BB3CD2526",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1950 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1921-1950 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "87D8E0DE-1747-4AC4-BEF6-7305C410786D",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309933,35 +309944,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1950 and the 1971-2000 Normal period."
         },
-            "identifier": "87D8E0DE-1747-4AC4-BEF6-7305C410786D",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1940 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1931-1940 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "C37271C5-8635-46A6-A994-7E9DD1617B47",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -309972,35 +309983,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1940 and the 1971-2000 Normal period."
         },
-            "identifier": "C37271C5-8635-46A6-A994-7E9DD1617B47",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1960 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1931-1960 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "FBFD27A1-629B-43A6-9C40-71868CFE599F",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310011,35 +310022,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1960 and the 1971-2000 Normal period."
         },
-            "identifier": "FBFD27A1-629B-43A6-9C40-71868CFE599F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1950 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1941-1950 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "85067A2F-B75C-45CA-9777-03F11AD807B8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310050,35 +310061,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1950 and the 1971-2000 Normal period."
         },
-            "identifier": "85067A2F-B75C-45CA-9777-03F11AD807B8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1970 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1941-1970 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "46465550-74B5-4E67-80CA-6C67A5A8833C",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310089,35 +310100,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1970 and the 1971-2000 Normal period."
         },
-            "identifier": "46465550-74B5-4E67-80CA-6C67A5A8833C",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1960 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1951-1960 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "CED5AA54-E574-4B8F-B11A-0442DCCFD6A8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310128,35 +310139,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1960 and the 1971-2000 Normal period."
         },
-            "identifier": "CED5AA54-E574-4B8F-B11A-0442DCCFD6A8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1980 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1951-1980 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "375B3F9F-1BC3-4CB5-BBAB-C60DA7235D27",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310167,35 +310178,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1980 and the 1971-2000 Normal period."
         },
-            "identifier": "375B3F9F-1BC3-4CB5-BBAB-C60DA7235D27",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1970 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1961-1970 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "76758C93-5281-4EA4-A23E-C8825A8478E6",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310206,35 +310217,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1970 and the 1971-2000 Normal period."
         },
-            "identifier": "76758C93-5281-4EA4-A23E-C8825A8478E6",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1901-1910 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "69AA2E8F-8CD6-4251-9F2B-741DF27D68B0",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310245,35 +310256,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US EPA, CPHEA/PESD"
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
-            },
-            "identifier": "69AA2E8F-8CD6-4251-9F2B-741DF27D68B0",
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
+                "name": "US EPA, CPHEA/PESD"
+            },
             "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
             "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period."
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1971-1980 and the 1971-2000 Normal period.",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            },
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1971-1980 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "449D45FE-D1F1-42C1-AA53-9DFDA455E624",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310284,35 +310295,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1971-1980 and the 1971-2000 Normal period."
         },
-            "identifier": "449D45FE-D1F1-42C1-AA53-9DFDA455E624",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-2010 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1981-2010 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "A7D9629E-ED5B-46FE-93ED-0B0B1DAA5FAF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310323,35 +310334,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-2010 and the 1971-2000 Normal period."
         },
-            "identifier": "A7D9629E-ED5B-46FE-93ED-0B0B1DAA5FAF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-1990 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1981-1990 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "E3E0D3CC-FA70-4BCC-93CF-065EDA07329B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310362,35 +310373,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-1990 and the 1971-2000 Normal period."
         },
-            "identifier": "E3E0D3CC-FA70-4BCC-93CF-065EDA07329B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1991-2000 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 1991-2000 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "59E5990A-056E-4FC1-8420-DE2F5823C6B8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310401,35 +310412,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1991-2000 and the 1971-2000 Normal period."
         },
-            "identifier": "59E5990A-056E-4FC1-8420-DE2F5823C6B8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 2001-2010 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2001-2010 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "B8453152-E303-4B74-8799-B14077F33DD8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310440,35 +310451,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 2001-2010 and the 1971-2000 Normal period."
         },
-            "identifier": "B8453152-E303-4B74-8799-B14077F33DD8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CanESM2 r5i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (CanESM2 r5i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "64DA7198-0750-43A0-BE1E-7534C9B79290",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310479,35 +310490,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CanESM2 r5i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "64DA7198-0750-43A0-BE1E-7534C9B79290",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CCSM4 r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (CCSM4 r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "4880255F-7A1B-40B4-93A1-DCC80C22973A",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310518,35 +310529,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CCSM4 r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "4880255F-7A1B-40B4-93A1-DCC80C22973A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CCSM4 r4i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (CCSM4 r4i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "9F846E6D-EC8A-4934-8A23-DA46F7323392",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310557,35 +310568,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CCSM4 r4i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "9F846E6D-EC8A-4934-8A23-DA46F7323392",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CESM1 r3i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (CESM1 r3i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "1E6D5071-2E5A-49FE-A73D-D0475C807E70",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310596,35 +310607,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CESM1 r3i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "1E6D5071-2E5A-49FE-A73D-D0475C807E70",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CSIRO-Mk3-6-0 r5i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (CSIRO-Mk3-6-0 r5i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "289AB578-6023-404D-9350-5FC2890652A3",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310635,35 +310646,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (CSIRO-Mk3-6-0 r5i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "289AB578-6023-404D-9350-5FC2890652A3",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (GFDL-CM3 r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (GFDL-CM3 r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "50DE42AF-E3BA-4560-A862-B23B10EC419B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310674,35 +310685,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (GFDL-CM3 r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "50DE42AF-E3BA-4560-A862-B23B10EC419B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (HadGEM2-AO r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (HadGEM2-AO r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "B914F3DC-B4FE-4455-8FE9-7DB6D7156954",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310713,35 +310724,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (HadGEM2-AO r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "B914F3DC-B4FE-4455-8FE9-7DB6D7156954",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (INM-CM4 r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (INM-CM4 r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "0E8E7E64-8BE4-485D-8756-568BA5C27DA3",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310752,35 +310763,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (INM-CM4 r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "0E8E7E64-8BE4-485D-8756-568BA5C27DA3",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (MIROC-ESM r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (MIROC-ESM r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "02819293-A67B-47B9-BE38-0539CD9E44D7",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310791,35 +310802,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (MIROC-ESM r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "02819293-A67B-47B9-BE38-0539CD9E44D7",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (MRI-CGCM3 r1i1p1) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the average Feddema Moisture Index over 2041-2070 (MRI-CGCM3 r1i1p1) and the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "E8D41A68-EC84-41E3-B54A-A069BC228227",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310830,35 +310841,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between modeled 2041-2070 (MRI-CGCM3 r1i1p1) and the 1971-2000 Normal period."
         },
-            "identifier": "E8D41A68-EC84-41E3-B54A-A069BC228227",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1901-1910 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "391E4482-4C4E-4EF7-9451-835A4AE18346",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310869,35 +310880,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1901-1910 and the 1971-2000 Normal period"
         },
-            "identifier": "391E4482-4C4E-4EF7-9451-835A4AE18346",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1901-1930 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "33F4D007-FD78-4BF9-BA0B-FF1B01E1E6A2",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310908,35 +310919,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1901-1930 and the 1971-2000 Normal period"
         },
-            "identifier": "33F4D007-FD78-4BF9-BA0B-FF1B01E1E6A2",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1911-1920 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "67C2B4D2-6137-4351-BB63-C2E3F23D53DF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310947,35 +310958,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1911-1920 and the 1971-2000 Normal period"
         },
-            "identifier": "67C2B4D2-6137-4351-BB63-C2E3F23D53DF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1911-1940 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "1BD821FD-041B-436C-8608-EF6ABFC6498F",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -310986,35 +310997,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1911-1940 and the 1971-2000 Normal period"
         },
-            "identifier": "1BD821FD-041B-436C-8608-EF6ABFC6498F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1921-1930 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "3E243586-38A4-41C5-BA2D-C8B67FD53B76",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311025,35 +311036,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1921-1930 and the 1971-2000 Normal period"
         },
-            "identifier": "3E243586-38A4-41C5-BA2D-C8B67FD53B76",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1921-1950 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "9A1E92D1-010D-4182-94DD-FC76EBF7CE8B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311064,35 +311075,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1921-1950 and the 1971-2000 Normal period"
         },
-            "identifier": "9A1E92D1-010D-4182-94DD-FC76EBF7CE8B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1931-1940 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "8243D30F-224D-4343-9225-99E8DE47EFBE",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311103,35 +311114,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1931-1940 and the 1971-2000 Normal period"
         },
-            "identifier": "8243D30F-224D-4343-9225-99E8DE47EFBE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1931-1960 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "3E9C5C9F-BC9D-4105-A46B-E25F30B87E8B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311142,35 +311153,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1931-1960 and the 1971-2000 Normal period"
         },
-            "identifier": "3E9C5C9F-BC9D-4105-A46B-E25F30B87E8B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1941-1950 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "BDAEB4B3-D3C5-4AEA-B4DE-54C0781F1831",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311181,35 +311192,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1941-1950 and the 1971-2000 Normal period"
         },
-            "identifier": "BDAEB4B3-D3C5-4AEA-B4DE-54C0781F1831",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1941-1970 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "F10BA49C-B617-4433-B171-243E02AB0E36",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311220,35 +311231,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1941-1970 and the 1971-2000 Normal period"
         },
-            "identifier": "F10BA49C-B617-4433-B171-243E02AB0E36",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1951-1960 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "40840E71-9253-4423-8B5A-82B9974A44E0",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311259,35 +311270,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1951-1960 and the 1971-2000 Normal period"
         },
-            "identifier": "40840E71-9253-4423-8B5A-82B9974A44E0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1951-1980 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "1804F0B4-EC0F-4B72-ABC5-F117F2278D28",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311298,35 +311309,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1951-1980 and the 1971-2000 Normal period"
         },
-            "identifier": "1804F0B4-EC0F-4B72-ABC5-F117F2278D28",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1961-1970 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "B527683A-9685-4003-80EC-5EE62CB3CD00",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311337,35 +311348,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1961-1970 and the 1971-2000 Normal period"
         },
-            "identifier": "B527683A-9685-4003-80EC-5EE62CB3CD00",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1961-1990 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "8DF082B1-E84B-441D-994A-856B60DE67DA",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311376,35 +311387,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1961-1990 and the 1971-2000 Normal period"
         },
-            "identifier": "8DF082B1-E84B-441D-994A-856B60DE67DA",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1971-1980 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "7BD7BB16-2E45-4463-A072-A8FEA163B423",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311415,35 +311426,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1971-1980 and the 1971-2000 Normal period"
         },
-            "identifier": "7BD7BB16-2E45-4463-A072-A8FEA163B423",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1981-2010 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "A7023C6A-68E5-4A25-BA9B-B3CDB170ABFF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311454,35 +311465,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1981-2010 and the 1971-2000 Normal period"
         },
-            "identifier": "A7023C6A-68E5-4A25-BA9B-B3CDB170ABFF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1981-1990 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "D4567880-4ECF-4E13-8981-B6B6E1A7D778",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311493,35 +311504,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1981-1990 and the 1971-2000 Normal period"
         },
-            "identifier": "D4567880-4ECF-4E13-8981-B6B6E1A7D778",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1991-2000 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "737FBFD9-C42B-4F0E-9F39-32F8C764D136",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311532,35 +311543,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1991-2000 and the 1971-2000 Normal period"
         },
-            "identifier": "737FBFD9-C42B-4F0E-9F39-32F8C764D136",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 2001-2010 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "F0CD720C-7195-4A08-B55A-DCE0F56DD476",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311571,35 +311582,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 2001-2010 and the 1971-2000 Normal period"
         },
-            "identifier": "F0CD720C-7195-4A08-B55A-DCE0F56DD476",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CanESM2 r5i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "8BAFB498-8049-4D3F-9DEF-5B3A098433EC",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311610,35 +311621,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CanESM2 r5i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "8BAFB498-8049-4D3F-9DEF-5B3A098433EC",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CCSM4 r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "551E1348-3828-4450-869E-3A43CBE4D4DF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311649,35 +311660,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CCSM4 r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "551E1348-3828-4450-869E-3A43CBE4D4DF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CCSM4 r4i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "90043D95-3D59-41DD-86D9-A42FB65EE5FC",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311688,35 +311699,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CCSM4 r4i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "90043D95-3D59-41DD-86D9-A42FB65EE5FC",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CESM1 r3i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "76B0BFEA-5AD4-4A63-99F4-E188456B8591",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311727,35 +311738,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CESM1 r3i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "76B0BFEA-5AD4-4A63-99F4-E188456B8591",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CSIRO-Mk3-6-0 r5i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "E3D6B2B5-4E2B-4A04-A258-46E3E63D65D4",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311766,35 +311777,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (CSIRO-Mk3-6-0 r5i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "E3D6B2B5-4E2B-4A04-A258-46E3E63D65D4",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (GFDL-CM3 r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "A21D1D40-96FF-494E-8A52-517AC2AF24D6",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311805,35 +311816,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (GFDL-CM3 r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "A21D1D40-96FF-494E-8A52-517AC2AF24D6",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (HadGEM2-AO r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "5936100C-D2D2-4AD7-8FC3-D40B5FF86045",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311844,35 +311855,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (HadGEM2-AO r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "5936100C-D2D2-4AD7-8FC3-D40B5FF86045",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (INM-CM4 r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "040C3378-1071-4E32-B61C-0F20A1D06739",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311883,35 +311894,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (INM-CM4 r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "040C3378-1071-4E32-B61C-0F20A1D06739",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "C1477ABB-89EC-4474-9745-221628BE2814",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311922,35 +311933,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "C1477ABB-89EC-4474-9745-221628BE2814",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period and model (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "D98496D8-BCF9-4566-BFF8-26869CC2AA3F",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -311961,35 +311972,39 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period"
         },
-            "identifier": "D98496D8-BCF9-4566-BFF8-26869CC2AA3F",
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
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Hydrologic Landscape Classification of the U.S.",
             "description": "We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. The data in this data set provides the Feddema Moisture Index, classified climate class, and classified season class for each time decade and 30 yr normal period from 1900-2010 and the 10 analyzed climate model projections described in the manuscript below (see Credits).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/HydrologicLandscapes/US_HLScenarioMerge.zip"
+                }
+            ],
+            "identifier": "27CA218B-A81E-4247-9F6F-F6BA72C57213",
+            "issued": "2020-01-13",
             "keyword": [
                 "Natural Resources",
                 "Map Files",
@@ -312001,39 +312016,34 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA (US EPA, CPHEA/PESD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 23.261936, -65.410112, 51.534173",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Hydrologic Landscape Classification of the U.S."
         },
-            "identifier": "27CA218B-A81E-4247-9F6F-F6BA72C57213",
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
-            "spatial": "-127.850214, 23.261936, -65.410112, 51.534173",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-13",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/HydrologicLandscapes/US_HLScenarioMerge.zip"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Hydrologic Landscape Classification of the U.S.",
             "description": "We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. The data in this data set is specifically for the 1971-2000 normal period and summarizes the HL classification for clusters of assessment units for the continental U.S.  Note that the assessment units were clustered by the 5-class HL code to minimize the file size.",
+            "distribution": [],
+            "identifier": "A88A0A4E-525B-47AB-B247-298081E26A0B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Natural Resources",
                 "Map Files",
@@ -312045,34 +312055,34 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA (US EPA, CPHEA/PESD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.853812, 23.199843, -65.38667, 51.541774",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Hydrologic Landscape Classification of the U.S."
         },
-            "identifier": "A88A0A4E-525B-47AB-B247-298081E26A0B",
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
-            "spatial": "-127.853812, 23.199843, -65.38667, 51.541774",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index over 1901-1910 relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312089,34 +312099,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1910 and the 1971-2000 Normal period."
         },
-            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1930 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period. relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "81E45806-E1D4-4986-8B54-DECEC2D10805",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312133,34 +312143,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1901-1930 and the 1971-2000 Normal period."
         },
-            "identifier": "81E45806-E1D4-4986-8B54-DECEC2D10805",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1920 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "72AD4BB8-C0B1-424B-AA38-731C9BC27E2D",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312177,34 +312187,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1920 and the 1971-2000 Normal period."
         },
-            "identifier": "72AD4BB8-C0B1-424B-AA38-731C9BC27E2D",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1940 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "E7A1FA74-691E-4300-8C57-AA87C3A0CCB9",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312221,34 +312231,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1911-1940 and the 1971-2000 Normal period."
         },
-            "identifier": "E7A1FA74-691E-4300-8C57-AA87C3A0CCB9",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1930 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "09CBCE8F-4B87-4B74-AC9B-A494D6B018E4",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312265,34 +312275,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1930 and the 1971-2000 Normal period."
         },
-            "identifier": "09CBCE8F-4B87-4B74-AC9B-A494D6B018E4",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1950 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "C2B0EB71-A770-4536-871E-590CEE697256",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312309,34 +312319,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1921-1950 and the 1971-2000 Normal period."
         },
-            "identifier": "C2B0EB71-A770-4536-871E-590CEE697256",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1940 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "27CA032B-8FE2-466F-A228-1DD010166FFC",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312353,34 +312363,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1940 and the 1971-2000 Normal period."
         },
-            "identifier": "27CA032B-8FE2-466F-A228-1DD010166FFC",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1960 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "3810065B-FDEC-4C59-AED3-C9BF85636772",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312397,34 +312407,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1931-1960 and the 1971-2000 Normal period."
         },
-            "identifier": "3810065B-FDEC-4C59-AED3-C9BF85636772",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1950 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "9550392F-9920-4EF1-AA71-62BC5C83074A",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312441,34 +312451,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1950 and the 1971-2000 Normal period."
         },
-            "identifier": "9550392F-9920-4EF1-AA71-62BC5C83074A",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1970 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "EC280B24-BFE0-41A0-ADD5-8E8C25F47A3C",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312485,34 +312495,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1941-1970 and the 1971-2000 Normal period."
         },
-            "identifier": "EC280B24-BFE0-41A0-ADD5-8E8C25F47A3C",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1960 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312529,34 +312539,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1960 and the 1971-2000 Normal period."
         },
-            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1980 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "ECD298F8-CD6F-43C7-ACD5-9D5CCC037DE6",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312573,34 +312583,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1951-1980 and the 1971-2000 Normal period."
         },
-            "identifier": "ECD298F8-CD6F-43C7-ACD5-9D5CCC037DE6",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1970 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "783CD6CA-DFFA-41F8-97DD-EC97532EBCF7",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312617,34 +312627,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1970 and the 1971-2000 Normal period."
         },
-            "identifier": "783CD6CA-DFFA-41F8-97DD-EC97532EBCF7",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1990 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "81B2E7FC-5B3F-4CF3-B782-8415226873FC",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312661,34 +312671,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1961-1990 and the 1971-2000 Normal period."
         },
-            "identifier": "81B2E7FC-5B3F-4CF3-B782-8415226873FC",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1971-1980 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "C3D8BA23-107A-4B50-8FCE-AE5939E93F09",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312705,34 +312715,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1971-1980 and the 1971-2000 Normal period."
         },
-            "identifier": "C3D8BA23-107A-4B50-8FCE-AE5939E93F09",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-2010 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "F5B063DA-EE6E-46C2-A45D-10733A99F2C4",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312749,34 +312759,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-2010 and the 1971-2000 Normal period."
         },
-            "identifier": "F5B063DA-EE6E-46C2-A45D-10733A99F2C4",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-1990 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "C9E1CC9B-A954-4D8C-AE80-17934F641970",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312793,34 +312803,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1981-1990 and the 1971-2000 Normal period."
         },
-            "identifier": "C9E1CC9B-A954-4D8C-AE80-17934F641970",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1991-2000 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "B38F93BB-8BD1-45EB-8C1D-5AD3963215D6",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312837,34 +312847,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 1991-2000 and the 1971-2000 Normal period."
         },
-            "identifier": "B38F93BB-8BD1-45EB-8C1D-5AD3963215D6",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 2000-2010 and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the timeperiod specified in the title relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312881,34 +312891,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between 2000-2010 and the 1971-2000 Normal period."
         },
-            "identifier": "3913726F-C3BB-432B-86CD-279A0B64A63F",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CanESM2 r5i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "16BC7F0C-BF71-4F66-BA60-8CCA801FB3F5",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312925,34 +312935,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CanESM2 r5i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "16BC7F0C-BF71-4F66-BA60-8CCA801FB3F5",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CCSM4 r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "4F8E4463-C145-49EE-B59D-740817F0FDCB",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -312969,34 +312979,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.067758, 50.665312",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CCSM4 r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "4F8E4463-C145-49EE-B59D-740817F0FDCB",
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
-            "spatial": "-127.854174, 29.335308, -108.067758, 50.665312",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CCSM4 r4i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "7B2637F5-07E2-47E9-99EF-973E8E20781D",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313013,34 +313023,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CCSM4 r4i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "7B2637F5-07E2-47E9-99EF-973E8E20781D",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CESM1 r3i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "AD15796A-1951-46E1-9301-967E9D9E6AD0",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313057,34 +313067,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CESM1 r3i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "AD15796A-1951-46E1-9301-967E9D9E6AD0",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CSIRO-Mk3-6-0 r5i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "1BF29B57-A82C-426A-AA24-BA9FB08C5D49",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313101,34 +313111,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (CSIRO-Mk3-6-0 r5i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "1BF29B57-A82C-426A-AA24-BA9FB08C5D49",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (GFDL-CM3 r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "A1204136-ACDC-4E62-97A3-F3253B392EBE",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313145,34 +313155,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (GFDL-CM3 r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "A1204136-ACDC-4E62-97A3-F3253B392EBE",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (HadGEM2-AO r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "95E50F6A-7EEC-46CC-B3BC-C25B4872043D",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313189,34 +313199,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (HadGEM2-AO r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "95E50F6A-7EEC-46CC-B3BC-C25B4872043D",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (INM-CM4 r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "2DED8B34-350D-4AA8-A3B5-223418D41DE6",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313233,34 +313243,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (INM-CM4 r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "2DED8B34-350D-4AA8-A3B5-223418D41DE6",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (MIROC-ESM r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "C56F1B88-7C29-4E56-B936-25E33A2C9F41",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313277,34 +313287,34 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (MIROC-ESM r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "C56F1B88-7C29-4E56-B936-25E33A2C9F41",
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
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period.",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research &amp; Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration. This raster contains the modeled change in the average Feddema Moisture Index between the 2041-2070 modeled data (specified in the title) relative to the 1971-2000 Normal period.",
+            "distribution": [],
+            "identifier": "DD107BC2-8BC0-47A5-B66F-2F8005AD88BE",
+            "issued": "2020-01-10",
             "keyword": [
                 "Natural Resources",
                 "Washington",
@@ -313321,34 +313331,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-10",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the average Feddema Moisture Index (multiplied by 1000) between the modeled 2041-2070 period (MRI-CGCM3 r1i1p1 model) and the 1971-2000 Normal period."
         },
-            "identifier": "DD107BC2-8BC0-47A5-B66F-2F8005AD88BE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.854174, 29.335308, -108.071872, 50.664713",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-10",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1901-1910 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "1A2B21BE-21BC-4549-90F6-1B991BCCC364",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313365,35 +313376,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1901-1910 and the 1971-2000 Normal period"
         },
-            "identifier": "1A2B21BE-21BC-4549-90F6-1B991BCCC364",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1901-1930 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "B95CB771-EC86-42F2-867A-3746AC6DB720",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313409,35 +313420,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1901-1930 and the 1971-2000 Normal period"
         },
-            "identifier": "B95CB771-EC86-42F2-867A-3746AC6DB720",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1911-1920 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "FE7D3D0B-8A59-4706-871D-BA8A18A3EEDD",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313453,35 +313464,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1911-1920 and the 1971-2000 Normal period"
         },
-            "identifier": "FE7D3D0B-8A59-4706-871D-BA8A18A3EEDD",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1901-1940 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "37EF547F-F948-499E-AEE7-8E6B5A139D34",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313497,35 +313508,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1901-1940 and the 1971-2000 Normal period"
         },
-            "identifier": "37EF547F-F948-499E-AEE7-8E6B5A139D34",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1921-1930 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "62B9FEE0-2B45-47EA-B599-C659E5BA708B",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313541,35 +313552,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1921-1930 and the 1971-2000 Normal period"
         },
-            "identifier": "62B9FEE0-2B45-47EA-B599-C659E5BA708B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1921-1950 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "1629D486-FE7F-4D34-ACCA-5994AFE83DBF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313585,35 +313596,35 @@
                 "Arizona",
                 "Water"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1921-1950 and the 1971-2000 Normal period"
         },
-            "identifier": "1629D486-FE7F-4D34-ACCA-5994AFE83DBF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1931-1940 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "468308E2-3A04-4CA4-B98A-7B781DA2238C",
+            "issued": "2020-01-13",
             "keyword": [
                 "Washington",
                 "California",
@@ -313630,35 +313641,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1931-1940 and the 1971-2000 Normal period"
         },
-            "identifier": "468308E2-3A04-4CA4-B98A-7B781DA2238C",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1931-1960 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "FA54EE8C-12BD-4853-A959-5D1FFA032725",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313669,35 +313680,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1931-1960 and the 1971-2000 Normal period"
         },
-            "identifier": "FA54EE8C-12BD-4853-A959-5D1FFA032725",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1941-1950 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "DBC58815-F598-47A8-8626-72DE5B27F1D4",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313708,35 +313719,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1941-1950 and the 1971-2000 Normal period"
         },
-            "identifier": "DBC58815-F598-47A8-8626-72DE5B27F1D4",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1941-1970 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "F0060209-CEBA-45F4-8F40-DF93457E7D30",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313747,35 +313758,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1941-1970 and the 1971-2000 Normal period"
         },
-            "identifier": "F0060209-CEBA-45F4-8F40-DF93457E7D30",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1951-1960 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "9881C39F-BE8F-4286-BBCD-B080DE872129",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313786,35 +313797,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1951-1960 and the 1971-2000 Normal period"
         },
-            "identifier": "9881C39F-BE8F-4286-BBCD-B080DE872129",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1951-1980 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "C076B12F-92A3-4734-B792-C7FBBEA71083",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313825,35 +313836,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1951-1980 and the 1971-2000 Normal period"
         },
-            "identifier": "C076B12F-92A3-4734-B792-C7FBBEA71083",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1961-1970 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "A1EB5D68-4907-4D1A-91DF-B3A7A5A4F3A5",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313864,35 +313875,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1961-1970 and the 1971-2000 Normal period"
         },
-            "identifier": "A1EB5D68-4907-4D1A-91DF-B3A7A5A4F3A5",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1961-1990 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "13FB7229-7671-46AE-994F-BE8CB5BE770E",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313903,35 +313914,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1961-1990 and the 1971-2000 Normal period"
         },
-            "identifier": "13FB7229-7671-46AE-994F-BE8CB5BE770E",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1971-1980 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "DEE31549-DB6B-4CC1-BB12-58682F1C83AF",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313942,35 +313953,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1971-1980 and the 1971-2000 Normal period"
         },
-            "identifier": "DEE31549-DB6B-4CC1-BB12-58682F1C83AF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1981-2010 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "DB18F513-3680-448F-AFCD-2EE0ADDE3ED8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -313981,35 +313992,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1981-2010 and the 1971-2000 Normal period"
         },
-            "identifier": "DB18F513-3680-448F-AFCD-2EE0ADDE3ED8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1981-1990 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "AA88AEA7-4F9E-4C62-8026-48D56D930DF0",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314020,35 +314031,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1981-1990 and the 1971-2000 Normal period"
         },
-            "identifier": "AA88AEA7-4F9E-4C62-8026-48D56D930DF0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 1991-2000 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "BC3AAC03-E41D-4A13-A010-9FAC982D9930",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314059,35 +314070,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 1991-2000 and the 1971-2000 Normal period"
         },
-            "identifier": "BC3AAC03-E41D-4A13-A010-9FAC982D9930",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between 2001-2010 and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "1DF49E13-3AD4-410A-9014-15C91C5CD40A",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314098,35 +314109,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between 2001-2010 and the 1971-2000 Normal period"
         },
-            "identifier": "1DF49E13-3AD4-410A-9014-15C91C5CD40A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CanESM2 r5i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "CA5A697C-BB5E-4EB0-ABB5-465205EF0ACE",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314137,35 +314148,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CanESM2 r5i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "CA5A697C-BB5E-4EB0-ABB5-465205EF0ACE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CCSM4 r1i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "2912AC9C-413C-4B55-97AF-D463641EB7E8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314176,35 +314187,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CCSM4 r1i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "2912AC9C-413C-4B55-97AF-D463641EB7E8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CCSM4 r4i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "05F59662-E4D8-4FAC-91DA-59A84855B484",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314215,35 +314226,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CCSM4 r4i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "05F59662-E4D8-4FAC-91DA-59A84855B484",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CESM1 r3i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "6B6E1B82-894A-4878-9FEE-C539C871F269",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314254,35 +314265,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CESM1 r3i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "6B6E1B82-894A-4878-9FEE-C539C871F269",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CSIRO-Mk3-6-0 r5i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "589165D1-229E-480A-9E9A-B6EB83ACD4A4",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314293,35 +314304,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (CSIRO-Mk3-6-0 r5i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "589165D1-229E-480A-9E9A-B6EB83ACD4A4",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (GFDL-CM3 r1i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "A4D9DCD8-464A-496D-A453-86190D123DDC",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314332,37 +314343,37 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
-            },
-            "identifier": "A4D9DCD8-464A-496D-A453-86190D123DDC",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
             "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (GFDL-CM3 r1i1p1) and the 1971-2000 Normal period"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (HadGEM2-AO r1i1p1) and the 1971-2000 Normal period",
-            "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
-            "keyword": [
-                "Environment",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            },
+            "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "553E6A93-79B2-4BC9-AC16-773AF24BE837",
+            "issued": "2020-01-13",
+            "keyword": [
+                "Environment",
                 "Downloadable Data",
                 "020:094",
                 "geospatial",
@@ -314371,35 +314382,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (HadGEM2-AO r1i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "553E6A93-79B2-4BC9-AC16-773AF24BE837",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (INM-CM4 r1i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "255109AB-06FA-4B91-8B8B-2FDE2A9BDF7A",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314410,35 +314421,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (INM-CM4 r1i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "255109AB-06FA-4B91-8B8B-2FDE2A9BDF7A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (MIROC-ESM r1i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "40F62436-215E-44DD-8AD7-AE9A6958BE71",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314449,35 +314460,35 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (MIROC-ESM r1i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "40F62436-215E-44DD-8AD7-AE9A6958BE71",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (MRI-CGCM3 r1i1p1) and the 1971-2000 Normal period",
             "description": "Originators: US Environmental Protection Agency Publisher: US EPA Office of Research & Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL) Publication place: Corvallis, OR Publication date: Time Period of Data: 1900-2010; Projected data for 2041-2070. Data location: GeoPlatform (\"https://www.geoplatform.gov/\") and EPA Environmental Dataset Gateway (https://edg.epa.gov/). Abstract: We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. Projections that are not within two-standard deviations of the historical decadal average contribute to the vulnerability index for each metric. The resulting vulnerability maps show that temperature and potential evapotranspiration are consistently projected to have high vulnerability indices for the western U.S. Precipitation vulnerability is not as spatially-uniform as temperature. The highest elevation areas with snow are projected to experience significant changes in snow accumulation. The seasonality vulnerability map shows that specific mountainous areas in the West are most prone to changes in seasonality, whereas many transitional terrains are moderately susceptible. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. Purpose: These data were created in support of the US EPA\u2019s ACE CIVA 2.3, Task Project (QAPP: E-WED-0030854). However, these climate data and hydrologic landscape summaries should have broad applicability for hydrological, geomorphic, or ecological modeling, management, and restoration.  This raster contains the modeled change in the seasonality of the month of maximum surplus precipitation between the target modeled time period (in title) and the 1971-2000 Normal period (1 = same season, 0 = earlier season, 2 = later season).",
+            "distribution": [],
+            "identifier": "E1CAAA4C-A711-448A-8267-17A5B23E47AD",
+            "issued": "2020-01-13",
             "keyword": [
                 "Environment",
                 "Downloadable Data",
@@ -314488,35 +314499,34 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US EPA, CPHEA/PESD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Modeled change in the Seasonality between the modeled 2041-2070 (MRI-CGCM3 r1i1p1) and the 1971-2000 Normal period"
         },
-            "identifier": "E1CAAA4C-A711-448A-8267-17A5B23E47AD",
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
-            "spatial": "-127.850214, 29.391649, -108.080515, 50.656502",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "accrualPeriodicity": "irregular",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randy Comeleo",
+                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Hydrologic Landscape Classification of the U.S.",
             "description": "We apply the hydrologic landscapes (HL) concept to assess the hydrologic vulnerability of the western United States (U.S.) to projected climate conditions. Our goal is to understand the potential impacts for stakeholder-defined interests across large geographic areas. The basic assumption of the HL approach is that catchments that share similar physical and climatic characteristics are expected to have similar hydrologic characteristics. We map climate vulnerability by integrating the HL approach into a retrospective analysis of historical data to assess variability in future climate projections and hydrology, which includes temperature, precipitation, potential evapotranspiration, snow accumulation, climatic moisture, surplus water, and seasonality of water surplus. This paper illustrates how the HL approach can help assess climatic and hydrologic vulnerability across large spatial scales. By combining the HL concept and climate vulnerability analyses, we provide a planning approach that could allow resource managers to consider how future climate conditions may impact important economic and conservation resources. The data in this data set is specifically for the 1971-2000 normal period.",
+            "distribution": [],
+            "identifier": "DA7BDD3D-C152-4A4F-9621-CF648E748DC8",
+            "issued": "2020-01-13",
             "keyword": [
                 "Natural Resources",
                 "Map Files",
@@ -314528,34 +314538,38 @@
                 "Water",
                 "United States"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2020-01-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USEPA (US EPA, CPHEA/PESD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randy Comeleo",
-                "hasEmail": "mailto:Comeleo.Randy@epa.gov"
+            "spatial": "-127.853157, 29.335308, -108.071786, 50.662617",
+            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
+            "title": "Hydrologic Landscape Classification of the U.S."
         },
-            "identifier": "DA7BDD3D-C152-4A4F-9621-CF648E748DC8",
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
-            "spatial": "-127.853157, 29.335308, -108.071786, 50.662617",
-            "temporal": "1971-01-01T00:00:00/2010-12-31T00:00:00",
-            "issued": "2020-01-13",
-            "distribution": []
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Africa",
             "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Africa.gdb.zip"
+                }
+            ],
+            "identifier": "A2182349-3C2E-436B-B614-7411834E9140",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314572,37 +314586,37 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-19, -35, 55, 38",
+            "title": "GFPLAIN90_Africa"
         },
-            "identifier": "A2182349-3C2E-436B-B614-7411834E9140",
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
-            "spatial": "-19, -35, 55, 38",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Africa.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Artic.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Artic",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "0613679A-82F6-4B01-9CD9-8FADB6B0261D",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314619,37 +314633,37 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
+            "title": "GFPLAIN90_Artic"
         },
-            "identifier": "0613679A-82F6-4B01-9CD9-8FADB6B0261D",
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
-            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Artic.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Asia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Asia",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "CFFC63E6-0205-4B89-8AD2-B6D6CF56AD72",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314666,37 +314680,37 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "57.6083333333334, 1.16666666666669, 150.921488783095, 55.9375",
+            "title": "GFPLAIN90_Asia"
         },
-            "identifier": "CFFC63E6-0205-4B89-8AD2-B6D6CF56AD72",
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
-            "spatial": "57.6083333333334, 1.16666666666669, 150.921488783095, 55.9375",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Asia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Australia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Australia",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "0FAA63D1-4221-42C5-BAD4-660DFF2985AF",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314713,37 +314727,41 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "94.9702158610026, -55.1166666666666, 180, 24.3005296495226",
+            "title": "GFPLAIN90_Australia"
         },
-            "identifier": "0FAA63D1-4221-42C5-BAD4-660DFF2985AF",
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
-            "spatial": "94.9702158610026, -55.1166666666666, 180, 24.3005296495226",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Australia.gdb.zip"
-                }
-            ]
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Europe.gdb.zip"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Europe",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/"
+                }
+            ],
+            "identifier": "3E8ED603-8BF9-4A48-B6B4-732545A204EC",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314760,41 +314778,37 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
+            "title": "GFPLAIN90_Europe"
         },
-            "identifier": "3E8ED603-8BF9-4A48-B6B4-732545A204EC",
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
-            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Europe.gdb.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
             },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Greenland.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Greenland",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "1FA60294-73D5-4C70-B1DE-346B7C49EBBB",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314811,37 +314825,37 @@
                 "non-floodplain",
                 "Greenland"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
+            "title": "GFPLAIN90_Greenland"
         },
-            "identifier": "1FA60294-73D5-4C70-B1DE-346B7C49EBBB",
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
-            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Greenland.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_NorthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_NorthAmerica",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "5920D9C7-9D96-47D1-AE7B-FC5B565AF1D5",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314858,37 +314872,37 @@
                 "non-floodplain",
                 "North America"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-137.9625, 5.49583333333336, -52.6160491943359, 62.742322116428",
+            "title": "GFPLAIN90_NorthAmerica"
         },
-            "identifier": "5920D9C7-9D96-47D1-AE7B-FC5B565AF1D5",
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
-            "spatial": "-137.9625, 5.49583333333336, -52.6160491943359, 62.742322116428",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_NorthAmerica.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Siberia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_Siberia",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "C46BBB99-6215-46A7-AA82-15F861FD34DD",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314905,37 +314919,37 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
+            "title": "GFPLAIN90_Siberia"
         },
-            "identifier": "C46BBB99-6215-46A7-AA82-15F861FD34DD",
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
-            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_Siberia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_SouthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "GFPLAIN90_SouthAmerica",
-            "description": "All floodplains were derived using modified scripts from GFPLAIN v1.0 (https://github.com/fnardi/GFPLAIN).    This data was created by modifying the scripts to work with 90-m data.\nGlobal FloodPLAIN (GFPLAIN) mapping uses a geomorphic algorithm. Geomorphic FloodPLAIN mapping algorithm GFPLAIN is based on Nardi et al. (2006, 2018).  \nThe data is available at the hydrobasin 4 level.  HydroBASINS data provides a series of polygon layers that depict watershed boundaries and sub-basin delineations at a global scale (http://www.hydrosheds.org).   ",
+            ],
+            "identifier": "4627F32C-DAE0-4AB0-AFE5-68DB6753541A",
             "keyword": [
                 "flood-hazard",
                 "global",
@@ -314952,37 +314966,39 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2024-12-06",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "spatial": "-92.0006805419922, -55.9875, -32.3745317247179, 14.8827270507813",
+            "title": "GFPLAIN90_SouthAmerica"
         },
-            "identifier": "4627F32C-DAE0-4AB0-AFE5-68DB6753541A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-92.0006805419922, -55.9875, -32.3745317247179, 14.8827270507813",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Floodplains/GFPlain90_SouthAmerica.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Africa.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands Africa",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "38C9CF74-26EE-4FF4-9F9D-6A14659968E8",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "geographically isolated wetland",
@@ -315001,40 +315017,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-18.1631176418728, -34.8370312160916, 54.5381176418729, 37.5631427341038",
+            "title": "Global Non-Floodplain Wetlands Africa"
         },
-            "identifier": "38C9CF74-26EE-4FF4-9F9D-6A14659968E8",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-18.1631176418728, -34.8370312160916, 54.5381176418729, 37.5631427341038",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Africa.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Artic.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands Arctic",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "21D3846F-5C9B-4A45-B8C6-70AA177B61C4",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315053,40 +315069,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
+            "title": "Global Non-Floodplain Wetlands Arctic"
         },
-            "identifier": "21D3846F-5C9B-4A45-B8C6-70AA177B61C4",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Artic.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Asia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands Asia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "F564ADDB-DCFB-4AA2-AE5C-61656592FE7F",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315105,40 +315121,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "57.6083333333334, 1.16666666666669, 150.921488783095, 55.9375",
+            "title": "Global Non-Floodplain Wetlands Asia"
         },
-            "identifier": "F564ADDB-DCFB-4AA2-AE5C-61656592FE7F",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "57.6083333333334, 1.16666666666669, 150.921488783095, 55.9375",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Asia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Australia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands_Australia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "16759995-A3E0-4174-85D4-1232A4AD3276",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315157,40 +315173,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "94.9702158610026, -55.1166666666666, 180.000642903646, 24.3005296495226",
+            "title": "Global Non-Floodplain Wetlands_Australia"
         },
-            "identifier": "16759995-A3E0-4174-85D4-1232A4AD3276",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "94.9702158610026, -55.1166666666666, 180.000642903646, 24.3005296495226",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Australia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Europe.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands_Europe",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "D9A59666-5CDA-42DB-815B-AC4AB9AFB8C9",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315209,40 +315225,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
+            "title": "Global Non-Floodplain Wetlands_Europe"
         },
-            "identifier": "D9A59666-5CDA-42DB-815B-AC4AB9AFB8C9",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Europe.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Greenland.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands_Greenland",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "0E92440F-DC84-4173-B16B-E173A25C4C37",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315261,40 +315277,40 @@
                 "non-floodplain",
                 "Greenland"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
+            "title": "Global Non-Floodplain Wetlands_Greenland"
         },
-            "identifier": "0E92440F-DC84-4173-B16B-E173A25C4C37",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Greenland.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_NorthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands_NorthAmerica",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "7E269ACC-63AF-4CD8-BE40-D91701787340",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315313,40 +315329,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-137.9625, 5.49583333333336, -52.6160491943359, 62.742322116428",
+            "title": "Global Non-Floodplain Wetlands_NorthAmerica"
         },
-            "identifier": "7E269ACC-63AF-4CD8-BE40-D91701787340",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-137.9625, 5.49583333333336, -52.6160491943359, 62.742322116428",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_NorthAmerica.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Siberia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Non-Floodplain Wetlands Siberia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "C9BE6AF8-55F5-4BBA-B143-7B5D0B0740F1",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315365,40 +315381,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
+            "title": "Global Non-Floodplain Wetlands Siberia"
         },
-            "identifier": "C9BE6AF8-55F5-4BBA-B143-7B5D0B0740F1",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_Siberia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_SouthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WetlandCombo_NFW_SouthAmerica",
-            "description": "This raster GIS dataset contains 30 meter cells depicting non-floodplain wetlands in a hydrobasin. This base dataset is a combination of three globally-available datasets, creating a new dataset that is inclusive of finer-resolution data, while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500-m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019); \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m \u2013 CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies;\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\nA 1-km buffer was applied to the HydroBASINS (Lehner and Grill 2013) coastline area and any wetland partially or completely overlain by the 1-km buffer was removed from analysis. In addition, to avoid including large lakes in  the data, we also applied a mask using HydroLAKES and removed lake systems \u226510 ha (Messager et al. 2016).\n\nThe dataset was then overlain by the GFPlain90 floodplain data (resampled to 30 meters) and wetlands overlain by the floodplain were removed.\n\n",
+            ],
+            "identifier": "D3045338-3296-4471-936C-3294D3B0E24F",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "SouthAmerica",
@@ -315417,40 +315433,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-92.0006805419922, -55.9875, -32.3745317247179, 14.8827270507813",
+            "title": "WetlandCombo_NFW_SouthAmerica"
         },
-            "identifier": "D3045338-3296-4471-936C-3294D3B0E24F",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-92.0006805419922, -55.9875, -32.3745317247179, 14.8827270507813",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_NFWs/Global_NFWs_SouthAmerica.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Africa.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Africa",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "90E9ECF1-561F-42A3-8521-F2B073805442",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "geographically isolated wetland",
@@ -315469,40 +315485,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-18.1631176418728, -34.8370312160916, 54.5381176418729, 37.5631427341038",
+            "title": "Global Wetlands Africa"
         },
-            "identifier": "90E9ECF1-561F-42A3-8521-F2B073805442",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-18.1631176418728, -34.8370312160916, 54.5381176418729, 37.5631427341038",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Africa.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Artic.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Artic",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "D4715E94-ADD4-423B-BC9C-EDA4105F602E",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315521,40 +315537,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
+            "title": "Global Wetlands Artic"
         },
-            "identifier": "D4715E94-ADD4-423B-BC9C-EDA4105F602E",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-180, 51.2083333333334, -61.0993570963541, 83.2172339545356",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Artic.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Asia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Asia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "98966CD2-223E-413F-9B4D-CD4DC6E50916",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315573,40 +315589,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "57.6083333333334, 1.16666666666669, 150.92148878309, 55.9375",
+            "title": "Global Wetlands Asia"
         },
-            "identifier": "98966CD2-223E-413F-9B4D-CD4DC6E50916",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "57.6083333333334, 1.16666666666669, 150.92148878309, 55.9375",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Asia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Australia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Australia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "E7E3FC52-0808-4903-A697-7F2A69A37D65",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315625,40 +315641,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "94.9702158610026, -55.1166666666666, 180, 24.3005296495226",
+            "title": "Global Wetlands Australia"
         },
-            "identifier": "E7E3FC52-0808-4903-A697-7F2A69A37D65",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "94.9702158610026, -55.1166666666666, 180, 24.3005296495226",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Australia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Europe.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Europe",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "5ECDBCD0-94EE-40B2-9126-DB3798CE7760",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315677,40 +315693,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
+            "title": "Global Wetlands Europe"
         },
-            "identifier": "5ECDBCD0-94EE-40B2-9126-DB3798CE7760",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-24.5423221164279, 12.5913133409288, 69.5545199924046, 81.8589760674371",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Europe.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Greenland.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Greenland",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "B85986CC-F478-4D8E-8117-48C019358D22",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315729,40 +315745,40 @@
                 "non-floodplain",
                 "Greenland"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
+            "title": "Global Wetlands Greenland"
         },
-            "identifier": "B85986CC-F478-4D8E-8117-48C019358D22",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-73.0006679958767, 59.7416666666667, -11.3493218315967, 83.6256427764894",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Greenland.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_NorthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands North America",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "4D27AC09-E4C9-4251-8F64-2F9F716F48F4",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315781,40 +315797,40 @@
                 "non-floodplain",
                 "North America"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "-137.9625, 5.49583333333336, -11.3493218315967, 83.6256427764894",
+            "title": "Global Wetlands North America"
         },
-            "identifier": "4D27AC09-E4C9-4251-8F64-2F9F716F48F4",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "-137.9625, 5.49583333333336, -11.3493218315967, 83.6256427764894",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_NorthAmerica.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Siberia.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands Siberia",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "E588295E-D932-4521-B9BD-4159E0894A08",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315833,40 +315849,40 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
+            "rights": "licenseUnrestricted",
+            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
+            "title": "Global Wetlands Siberia"
         },
-            "identifier": "E588295E-D932-4521-B9BD-4159E0894A08",
+        {
+            "@type": "dcat:Dataset",
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
-            "spatial": "58.9583333327298, 45.5625000003308, 179.999884849201, 81.267347208629",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Lane",
+                "hasEmail": "mailto:lane.charles@epa.gov"
+            },
+            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_Siberia.gdb.zip"
+                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_SouthAmerica.gdb.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Global Wetlands South America",
-            "description": "This raster GIS dataset contains 30 meter cells depicting wetlands in a hydrobasin.  \nThis base dataset is a combination of three globally available datasets creating a new dataset is that is inclusive of both finer-resolution data while accounting for a wide range of wetland sizes. \nThe three source datasets are:\n 1) CW-WTD 500 m dataset resampled to 30 m. \u2013 Wetland dataset built from a composite wetland-water table depth (Tootchi 2019), \n 2) CCI (Climate Change Initiative) data resampled from 300 m to 30 m - CCI defined wetlands as \u201c\u2026mixed classes of flooded areas with tree covers, shrubs, or herbaceous covers plus inland water bodies\u201d and\n 3) Global Surface Water (GSW)  30-m (Pekel et al. 2016) \u2013 A pixel was considered a wetland if it had at least one inundation event over a 32-year range.\n\n",
+            ],
+            "identifier": "0DE756B1-475E-4F24-99D9-75F85813ADAE",
+            "issued": "2022-11-08",
             "keyword": [
                 "Wetlands",
                 "watershed",
@@ -315885,90 +315901,39 @@
                 "drought mitigation",
                 "non-floodplain"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2022-11-08",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Lane",
-                "hasEmail": "mailto:lane.charles@epa.gov"
-            },
-            "identifier": "0DE756B1-475E-4F24-99D9-75F85813ADAE",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "licenseUnrestricted",
             "spatial": "-92.0006805419922, -55.9875, -32.3745317247179, 14.8827270507813",
-            "accrualPeriodicity": "irregular",
-            "issued": "2022-11-08",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Global_NonFloodplain_Wetlands/Global_Wetlands/Global_Wetlands_SouthAmerica.gdb.zip"
-                }
-            ]
+            "title": "Global Wetlands South America"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "High Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
-            "keyword": [
-                "New Jersey",
-                "Exposure",
-                "Modeling",
-                "Estuary",
-                "Natural Resources",
-                "Delaware",
-                "Environment",
-                "Downloadable Data",
-                "020:094",
-                "Ecosystem",
-                "Relative Vulnerability",
-                "geospatial",
-                "Coastal Wetland",
-                "Sea Level Rise",
-                "United States"
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2018-02-28",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jordan West",
                 "hasEmail": "mailto:west.jordan@epa.gov"
             },
-            "identifier": "7DB03995-FF00-46E0-B2B7-8A32E1583882",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
-            "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2019-02-01",
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/BDK_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "7DB03995-FF00-46E0-B2B7-8A32E1583882",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -315986,39 +315951,39 @@
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
+            "title": "High Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "9427C992-AF9F-4311-975D-46E098B6B86E",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/BDK_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "9427C992-AF9F-4311-975D-46E098B6B86E",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316036,39 +316001,39 @@
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
+            "title": "Low Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "86AD1088-B422-47FC-9E86-29F03A0D3B4B",
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
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/BDK_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "86AD1088-B422-47FC-9E86-29F03A0D3B4B",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316086,39 +316051,39 @@
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
+            "title": "Total Marsh at Broadkill, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "38A1DD9E-C29A-4FA2-BA7C-70DADF4F0989",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dennis_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain, lost and remaining. Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data, the most recent SLR projections, and site-specific accretion data. These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "38A1DD9E-C29A-4FA2-BA7C-70DADF4F0989",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316136,39 +316101,39 @@
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
+            "title": "High Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "D9A5D462-5ABD-4060-8DDC-280E54FD93B6",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain, lost and remaining. Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories.\n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data, the most recent SLR projections, and site-specific accretion data. These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dennis_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year.\n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "D9A5D462-5ABD-4060-8DDC-280E54FD93B6",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316186,39 +316151,39 @@
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
+            "title": "Low Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "61975990-720B-4F92-AEC6-9B4B18FA67AE",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year.\n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dennis_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "61975990-720B-4F92-AEC6-9B4B18FA67AE",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316236,39 +316201,39 @@
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
+            "title": "Total Marsh at Dennis, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "A388C9C0-6136-46E3-8E3F-6C99E8DC071B",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dividing_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\n Note: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "A388C9C0-6136-46E3-8E3F-6C99E8DC071B",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316286,39 +316251,39 @@
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
+            "title": "High Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "5C6ABF97-2F44-4250-98A9-17F7F61605B3",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\n Note: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dividing_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "5C6ABF97-2F44-4250-98A9-17F7F61605B3",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316336,39 +316301,39 @@
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
+            "title": "Low Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "C7543A89-E234-4C31-AF61-4DB4BC868AFF",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Dividing_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh in the Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh. High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "C7543A89-E234-4C31-AF61-4DB4BC868AFF",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316386,28 +316351,31 @@
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
+            "title": "Total Marsh at Dividing, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "986CD520-B0FB-4250-8804-E587EF7469A2",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh. High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316437,12 +316405,63 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/StJLow_HM.zip"
                 }
-            ]
+            ],
+            "identifier": "986CD520-B0FB-4250-8804-E587EF7469A2",
+            "issued": "2019-02-01",
+            "keyword": [
+                "New Jersey",
+                "Exposure",
+                "Modeling",
+                "Estuary",
+                "Natural Resources",
+                "Delaware",
+                "Environment",
+                "Downloadable Data",
+                "020:094",
+                "Ecosystem",
+                "Relative Vulnerability",
+                "geospatial",
+                "Coastal Wetland",
+                "Sea Level Rise",
+                "United States"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2018-02-28",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
+            },
+            "spatial": "-75.387382, 38.728269, -75.12876, 38.867302",
+            "temporal": "2001-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "High Marsh in the Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ICLUS v1.3 Estimated Percent Impervious Surface for the Conterminous USA",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/iclus/about-iclus",
             "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is available for each scenario by decade to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://www.epa.gov/iclus/iclus-downloads",
+                    "title": "Download"
+                }
+            ],
+            "identifier": "{4D34EB4D-FDD9-4612-98DE-3C723B6B0095}",
+            "issued": "2010-01-01",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316452,45 +316471,45 @@
                 "Climate",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Center for Environmental Assessment, Global Change Research Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2000-01-01/2100-01-01",
+            "title": "ICLUS v1.3 Estimated Percent Impervious Surface for the Conterminous USA"
         },
-            "identifier": "{4D34EB4D-FDD9-4612-98DE-3C723B6B0095}",
+        {
+            "@type": "dcat:Dataset",
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
-            "temporal": "2000-01-01/2100-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/iclus/about-iclus",
-            "issued": "2010-01-01",
-            "language": "en-us",
+            "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is semi-decadally for each scenario to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
+                    "description": "The URL providing direct access to the downloadable dataset. ",
                     "downloadURL": "https://www.epa.gov/iclus/iclus-downloads",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v1.3 Housing Density for the Conterminous USA",
-            "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is semi-decadally for each scenario to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer.",
+            ],
+            "identifier": "{2E953B8B-08A1-42FB-BAAB-1D5C246BC7D0}",
+            "issued": "2010-01-01",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316500,45 +316519,45 @@
                 "Climate",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Center for Environmental Assessment, Global Change Research Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "rights": "Use Constraints: None. Please check sources, scale, accuracy, currentness and other available information. Please confirm that you are using the most recent copy of both data and metadata. Acknowledgement of the EPA would be appreciated.",
+            "spatial": "-138.21454852, 6.65223303, -12.68151645, 61.7110157",
+            "temporal": "2000-01-01/2100-01-01",
+            "title": "ICLUS v1.3 Housing Density for the Conterminous USA"
         },
-            "identifier": "{2E953B8B-08A1-42FB-BAAB-1D5C246BC7D0}",
+        {
+            "@type": "dcat:Dataset",
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
-            "temporal": "2000-01-01/2100-01-01",
-            "accrualPeriodicity": "irregular",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
             "describedBy": "https://www.epa.gov/iclus/about-iclus",
-            "issued": "2010-01-01",
-            "language": "en-us",
+            "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is available for each scenario by decade to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer. This shapefile holds population data for all counties of the conterminous USA for all decades (2010-2100) and SRES population growth scenarios (A1, A2, B1, B2), as well as a 'base case' (BC) scenario, for use in the Integrated Climate and Land Use Scenarios (ICLUS) project.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://www.epa.gov/iclus/iclus-downloads",
-                    "description": "The URL providing direct access to the downloadable dataset. "
+                    "description": "The URL providing direct access to the downloadable dataset. ",
+                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/NCEA/county_pop.zip",
+                    "title": "Download"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v1.3 Population Projections",
-            "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is available for each scenario by decade to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer. This shapefile holds population data for all counties of the conterminous USA for all decades (2010-2100) and SRES population growth scenarios (A1, A2, B1, B2), as well as a 'base case' (BC) scenario, for use in the Integrated Climate and Land Use Scenarios (ICLUS) project.",
+            ],
+            "identifier": "{1BB3ECBD-3EEB-43F3-AF78-B1196ACCC732}",
+            "issued": "2007-01-01",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316547,45 +316566,37 @@
                 "Impact",
                 "Climate"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2007-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Center for Environmental Assessment, Global Change Research Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
-            },
-            "identifier": "{1BB3ECBD-3EEB-43F3-AF78-B1196ACCC732}",
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
             "temporal": "2010-01-01/2100-01-01",
-            "accrualPeriodicity": "irregular",
-            "describedBy": "https://www.epa.gov/iclus/about-iclus",
-            "issued": "2007-01-01",
-            "language": "en-us",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "title": "Download",
-                    "downloadURL": "https://edg.epa.gov/data/Public/ORD/NCEA/county_pop.zip",
-                    "description": "The URL providing direct access to the downloadable dataset. "
-                }
-            ]
+            "title": "ICLUS v1.3 Population Projections"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ICLUS v1.3 Raw Housing Density for the Conterminous USA",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Philip Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
             "description": "Climate and land-use change are major components of global environmental change with feedbacks between these components. The consequences of these interactions show that land use may exacerbate or alleviate climate change effects. Based on these findings it is important to use land-use scenarios that are consistent with the specific assumptions underlying climate-change scenarios. The Integrated Climate and Land-Use Scenarios (ICLUS) project developed land-use outputs that are based on a downscaled version of the Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) social, economic, and demographic storylines. ICLUS outputs are derived from a pair of models. A demographic model generates county-level population estimates that are distributed by a spatial allocation model (SERGoM v3) as housing density across the landscape. Land-use outputs were developed for the four main SRES storylines and a baseline (\"base case\"). The model is run for the conterminous USA and output is semi-decadally for each scenario to 2100. In addition to housing density at a 1 hectare spatial resolution, this project also generated estimates of impervious surface at a resolution of 1 square kilometer.",
+            "distribution": [],
+            "identifier": "{5F363F21-CCC1-4ED5-BF53-1C3657AAD505}",
+            "issued": "2010-01-01",
             "keyword": [
                 "Modeling",
                 "geospatial",
@@ -316593,68 +316604,33 @@
                 "Climate",
                 "United States"
             ],
+            "language": "en-us",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development, National Center for Environmental Assessment (NCEA)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Philip Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
-            },
-            "identifier": "{5F363F21-CCC1-4ED5-BF53-1C3657AAD505}",
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
             "temporal": "2000-01-01/2100-01-01",
-            "accrualPeriodicity": "irregular",
-            "issued": "2010-01-01",
-            "language": "en-us",
-            "distribution": []
+            "title": "ICLUS v1.3 Raw Housing Density for the Conterminous USA"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ICLUS v2.1 land use projections for the Fourth National Climate Assessment (SSP2)",
-            "description": "SSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain consistent with the recent past. This version of the ICLUS model does not include climate change projections to dynamically update location-specific amenities when calculating migration. These projections will include the \u201cnocc\u201d label in the file name to indicate this difference.",
-            "keyword": [
-                "Modeling",
-                "Human",
-                "020:094",
-                "geospatial",
-                "Land",
-                "Climate",
-                "United States"
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
             ],
-            "modified": "2018-02-28",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development-National Center for Environmental Assessment"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Phillip Morefield",
                 "hasEmail": "mailto:morefield.philip@epa.gov"
             },
-            "identifier": "8994C8C5-7398-43C3-A15F-99778DAA0EFA",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
-            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2017-02-28",
+            "description": "SSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain consistent with the recent past. This version of the ICLUS model does not include climate change projections to dynamically update location-specific amenities when calculating migration. These projections will include the \u201cnocc\u201d label in the file name to indicate this difference.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316692,12 +316668,9 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.epa.gov/ord/"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v2.1 land use projections for the Fourth National Climate Assessment (SSP5)",
-            "description": "The SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. This version of the ICLUS model does not include climate change projections to dynamically update location-specific amenities when calculating migration. These projections will include the \u201cnocc\u201d label in the file name to indicate this difference.",
+            ],
+            "identifier": "8994C8C5-7398-43C3-A15F-99778DAA0EFA",
+            "issued": "2017-02-28",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316707,28 +316680,31 @@
                 "Climate",
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
-                "fn": "Phillip Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
+            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "ICLUS v2.1 land use projections for the Fourth National Climate Assessment (SSP2)"
         },
-            "identifier": "7E180905-28E9-4D6C-882C-BD00905CF0B5",
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
-            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
-            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2017-02-28",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phillip Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
+            "description": "The SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. This version of the ICLUS model does not include climate change projections to dynamically update location-specific amenities when calculating migration. These projections will include the \u201cnocc\u201d label in the file name to indicate this difference.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316762,12 +316738,9 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NCEA/ICLUS_v2.1/SSP5/ICLUS_v2.1_land_use_southwest_ssp5_nocc.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v2.1.1 population projections",
-            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nSSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain largely consistent with the recent past, however the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nThe SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. The the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP4.5 assumes that global greenhoue gas emissions increase into the latter part of the century, before leveling off and eventually stabilizing by 2100 as a result of various climate change policies. RCP8.5 assumes that global greenhoue gas emissions increase through the year 2100. ",
+            ],
+            "identifier": "7E180905-28E9-4D6C-882C-BD00905CF0B5",
+            "issued": "2017-02-28",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316777,28 +316750,31 @@
                 "Climate",
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
-                "fn": "Phillip Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
+            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "ICLUS v2.1 land use projections for the Fourth National Climate Assessment (SSP5)"
         },
-            "identifier": "4C6D6B46-8CD3-428D-B238-8FC9ADCBB271",
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
-            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
-            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2017-02-28",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phillip Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
+            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nSSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain largely consistent with the recent past, however the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nThe SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. The the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP4.5 assumes that global greenhoue gas emissions increase into the latter part of the century, before leveling off and eventually stabilizing by 2100 as a result of various climate change policies. RCP8.5 assumes that global greenhoue gas emissions increase through the year 2100. ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316808,12 +316784,9 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.epa.gov/ord/"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v2.1.1 land use projections for SSP2 and RCP4.5 pathways",
-            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nSSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain largely consistent with the recent past, however the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP4.5 assumes that global greenhouse gas emissions increase into the latter part of the century, before leveling off and eventually stabilizing by 2100 as a result of various climate change policies.",
+            ],
+            "identifier": "4C6D6B46-8CD3-428D-B238-8FC9ADCBB271",
+            "issued": "2017-02-28",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316823,28 +316796,31 @@
                 "Climate",
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
-                "fn": "Phillip Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
+            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "ICLUS v2.1.1 population projections"
         },
-            "identifier": "C009CEAD-8841-4268-B13E-7D01C51F6010",
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
-            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
-            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2017-02-28",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phillip Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
+            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nSSP2 is a \u201cmiddle-of-the-road\u201d projection, where social, economic and technological trends do not shift markedly from historical patterns, resulting in a U.S. population of 455 million people by 2100. Domestic migration trends remain largely consistent with the recent past, however the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP4.5 assumes that global greenhouse gas emissions increase into the latter part of the century, before leveling off and eventually stabilizing by 2100 as a result of various climate change policies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316858,12 +316834,9 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.epa.gov/ord/"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ICLUS v2.1.1 land use projections for SSP5 and RCP8.5 pathways",
-            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nThe SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. The the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP8.5 assumes that global greenhouse gas emissions increase through the year 2100.",
+            ],
+            "identifier": "C009CEAD-8841-4268-B13E-7D01C51F6010",
+            "issued": "2017-02-28",
             "keyword": [
                 "Modeling",
                 "Human",
@@ -316873,28 +316846,31 @@
                 "Climate",
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
-                "fn": "Phillip Morefield",
-                "hasEmail": "mailto:morefield.philip@epa.gov"
+            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
+            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "ICLUS v2.1.1 land use projections for SSP2 and RCP4.5 pathways"
         },
-            "identifier": "4e18759e-26f7-11e8-b467-0ed5f89f718b",
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
-            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
-            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
-            "issued": "2017-02-28",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phillip Morefield",
+                "hasEmail": "mailto:morefield.philip@epa.gov"
+            },
+            "description": "The methodology used to produce these projections differs from ICLUS v2.0 (https://cfpub.epa.gov/ncea/iclus/recordisplay.cfm?deid=322479). The demographic components of change (i.e., rates of fertility and mortality) for ICLUS v2.1 were taken directly from the Wittgenstein Centre Data Explorer (http://witt.null2.net/shiny/wic/). These projections were produced more recently than the Census projections used in ICLUS v2.0, and incorporate more recent observations of population change.\n\nThe SSP5 narrative describes a rapidly growing and flourishing global economy that remains heavily dependent on fossil fuels, and a U.S. population that exceeds 730 million by 2100. ICLUS v2.1 land use projections under SSP5 result in a considerably larger expansion of developed lands relative to SSP2. The the amenity value of local climate (average precipitation and temperature for summer and winter) is used in ICLUS v2.1.1 to influence migration patterns. The name of the climate model used as the source of future climate patterns is included at the end of the file name (e.g., \"GISS-E2-R\" or \"HadGEM2-ES\"). The approach for incorporating climate change into the migration model is described in the ICLUS v2.0 documentation.\n\nRCP8.5 assumes that global greenhouse gas emissions increase through the year 2100.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -316908,62 +316884,51 @@
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://www.epa.gov/ord/"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "4e18759e-26f7-11e8-b467-0ed5f89f718b",
+            "issued": "2017-02-28",
             "keyword": [
-                "New Jersey",
-                "Exposure",
                 "Modeling",
-                "Estuary",
-                "Natural Resources",
-                "Delaware",
-                "Environment",
-                "Downloadable Data",
+                "Human",
                 "020:094",
-                "Ecosystem",
-                "Relative Vulnerability",
                 "geospatial",
-                "Coastal Wetland",
-                "Sea Level Rise",
+                "Land",
+                "Climate",
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
+            "spatial": "-124.763068, 24.523096, -66.949895, 49.384358",
+            "temporal": "2000-01-01T00:00:00/2100-12-31T00:00:00",
+            "title": "ICLUS v2.1.1 land use projections for SSP5 and RCP8.5 pathways"
         },
-            "identifier": "E78BBC02-2700-4A86-B004-93A62626CEF1",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/MaurLow_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "E78BBC02-2700-4A86-B004-93A62626CEF1",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -316981,39 +316946,39 @@
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
+            "title": "High Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "12433497-E9A2-46DE-B77D-CE82A15A4E13",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years.\n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/MaurLow_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, gain (value=1), lost (value=-1) and remaining (no change; value=0) These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "12433497-E9A2-46DE-B77D-CE82A15A4E13",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317031,39 +316996,39 @@
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
+            "title": "Low Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "9DE0438E-91F0-49A8-AD9B-FA8CBA6FF679",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, gain (value=1), lost (value=-1) and remaining (no change; value=0) These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/MaurLow_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "9DE0438E-91F0-49A8-AD9B-FA8CBA6FF679",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317081,39 +317046,39 @@
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
+            "title": "Total Marsh at Lower Maurice, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "3334CEC6-6AA7-4F65-9FD9-E2574AA497D8",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Misp_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "3334CEC6-6AA7-4F65-9FD9-E2574AA497D8",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317131,39 +317096,39 @@
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
+            "title": "High Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "F5609639-8432-4E47-83FB-B25DDA00270F",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Misp_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "F5609639-8432-4E47-83FB-B25DDA00270F",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317181,39 +317146,39 @@
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
+            "title": "Low Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "A02DC3D2-4EBA-4157-9B9E-49AE09B8ED8B",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Misp_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\n Note: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "A02DC3D2-4EBA-4157-9B9E-49AE09B8ED8B",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317231,39 +317196,39 @@
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
+            "title": "Total Marsh at Mispillion, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "A90FCABA-155D-4F4C-A707-F5684D5C7F80",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities.\n\n Note: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Reeds_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\n Prior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "A90FCABA-155D-4F4C-A707-F5684D5C7F80",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317281,39 +317246,39 @@
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
+            "title": "High Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "33F0F796-97D4-491B-89E1-0E93CDE756B8",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh).\n\n Prior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Reeds_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "33F0F796-97D4-491B-89E1-0E93CDE756B8",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317331,39 +317296,39 @@
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
+            "title": "Low Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "65ADD2A2-2CD4-4159-A800-B1E90D3E46DA",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of total marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Total marsh (TM) was defined as the sum of low marsh and high marsh [SLAMM category 8 + SLAMM category 7 + SLAMM category 20]. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/Reeds_TM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High Marsh at St. Jones, DE,Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year.\n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "65ADD2A2-2CD4-4159-A800-B1E90D3E46DA",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317381,39 +317346,39 @@
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
+            "title": "Total Marsh at Reeds, NJ, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "E043F6E9-89CB-4F72-80A9-83796DEB6ECD",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of HIGH marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). High marsh (HM) was defined as the aggregation of irregularly-flooded marsh [SLAMM category 7] and transitional salt marsh [SLAMM category 20]. HM is covered by water only sporadically (once per day or less). Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM code equal to 8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year.\n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/StJLow_HM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Low Marsh at St. Jones, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
-            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
+            ],
+            "identifier": "E043F6E9-89CB-4F72-80A9-83796DEB6ECD",
+            "issued": "2019-02-01",
             "keyword": [
                 "New Jersey",
                 "Exposure",
@@ -317431,39 +317396,39 @@
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
+            "title": "High Marsh at St. Jones, DE,Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA"
         },
-            "identifier": "4157F3E9-7C82-4BD8-BD4B-E9888DF70CEA",
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
+            "description": "This raster GIS dataset contains 5-meter-resolution cells depicting the areas of LOW marsh gain (value=1), lost (value=-1) and remaining (no change; value=0). Low marsh (LM) was defined as regularly flooded marsh [SLAMM category 8]. LM is normally inundated by tidal water at least once per day. Based on SLAMM simulation outputs, we generated the gain and loss map by using the \u201cRaster Calculator\u201d tool under \u201cSpatial Analyst Tools\u201d in ArcGIS software. The methodology consists of the three steps listed below (where we use low marsh [LM] as an example). The same process can be applied to other SLAMM land cover categories. \n\n1) Open ArcMap, add SLAMM simulation raster outputs (all SLAMM categories) for baseline year and future years. \n\n2) In Raster Calculator, set the SLAMM codeequal to8 (low marsh = SLAMM category 8) to generate a new raster. Each individual cell in the new raster is assigned a value of \u201c0\u201d or \u201c1\u201d. \u201c1\u201d is low marsh and \u201c0\u201d is any other SLAMM land cover category. Perform this step for both the baseline year and future year. \n\n3) In Raster Calculator, subtract the new raster for the baseline year from the new raster for the future year (formula = new future year raster - new baseline year raster). The calculation generates a new raster, in which each individual cell is assigned a value of \u201c-1\u201d, \u201c0\u201d, or \u201c1\u201d. Based on the calculation, \u201c-1\u201d means low marsh loss in the future (the cell has converted from low marsh to a different SLAMM category), \u201c0\u201d means low marsh is remaining (the cell stays the same), and \u201c1\u201d means low marsh gain in the future (the cell has converted from a different SLAMM category to low marsh). \n\nPrior SLAMM work has been performed in the Delaware Bay, but our methods differ in that we derive results for specific marsh areas and utilize more recent, higher resolution elevation data (2015 USGS CoNED Topobathy Model: New Jersey and Delaware), the most recent SLR projections, and site-specific accretion data (through 2016). These SLAMM simulations were performed as part of a larger project by the USEPA on frameworks and methods for characterizing relative wetland vulnerabilities. \n\nNote: additional raster files from this project are available upon request. These include files from low and high SLR scenarios and different model protection scenarios. For more information, contact Jordan West (West.Jordan@epa.gov).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/SLAMM_DE2019/StJLow_LM.zip"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Total Marsh at St. Jones, DE, Lower Delaware Bay, Intermediate Sea Level Rise Scenario, \u201cProtect Developed Dry Land\u201d model protection scenario, EPA ORD NCEA",
```

