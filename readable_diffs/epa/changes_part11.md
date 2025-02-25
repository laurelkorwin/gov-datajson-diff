# Change History for epa.json (Part 11)

### Changes from 31606f9 to dd2190f (Part 1/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/epa.json b/epa.json
index 3c1d5ec..0425342 100644
--- a/epa.json
+++ b/epa.json
@@ -3,24 +3,39 @@
     "@id": "https://edg.epa.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
-            "title": "Emission & Generation Resource Integrated Database (eGRID)",
-            "description": "The Emissions & Generation Resource Integrated Database (eGRID) is a comprehensive source of data on characteristics of almost all electric power generated in the United States. This data includes capacity; heat input; net generation; associated air emissions of nitrogen oxides, sulfur dioxide, carbon dioxide, methane, nitrous oxide and mercury; emissions rates; resource mix (i.e., generation by fuel type); nonbaseload calculations; line losses (a.k.a., grid gross loss); and many other attributes. The data is provided at the unit and generator levels, as well as, aggregated to the plant, state, balancing authority, eGRID subregion, NERC region, and US levels.\n\nAs of January 2024, the available editions of eGRID contain data for years 2022, 2021, 2020, 2019, 2018, 2016, 2014, 2012, 2010, 2009, 2007, 2005, 2004, and 1996 through 2000.",
             "@type": "dcat:Dataset",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Environmental Protection Agency"
-            },
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Travis Johnson",
                 "hasEmail": "mailto:Johnson.Travis@epa.gov"
             },
-            "bureauCode": [
-                "020:00"
+            "dataQuality": true,
+            "description": "The Emissions & Generation Resource Integrated Database (eGRID) is a comprehensive source of data on characteristics of almost all electric power generated in the United States. This data includes capacity; heat input; net generation; associated air emissions of nitrogen oxides, sulfur dioxide, carbon dioxide, methane, nitrous oxide and mercury; emissions rates; resource mix (i.e., generation by fuel type); nonbaseload calculations; line losses (a.k.a., grid gross loss); and many other attributes. The data is provided at the unit and generator levels, as well as, aggregated to the plant, state, balancing authority, eGRID subregion, NERC region, and US levels.\n\nAs of January 2024, the available editions of eGRID contain data for years 2022, 2021, 2020, 2019, 2018, 2016, 2014, 2012, 2010, 2009, 2007, 2005, 2004, and 1996 through 2000.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/egrid/download-data",
+                    "description": "Most recent year represents 2022 data.",
+                    "format": "Microsoft Office - OOXML - Spreadsheet (.xlsx)",
+                    "mediaType": "text/csv",
+                    "title": "eGRID Data Download"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/egrid/maps",
+                    "description": "The eGRID mapping files include an eGRID subregion image (png), shapefiles (shp), zipped Keyhole Markup Language (kmz) files, and a geodatabase (gdb).",
+                    "title": "eGRID Mapping Files"
+                }
             ],
+            "identifier": "c9a433cb-6754-4a87-a157-9571c054c0ca",
+            "issued": "2024-01-30",
             "keyword": [
                 "Air",
                 "Climate Change",
@@ -87,45 +102,38 @@
                 "emission reductions",
                 "energy efficiency"
             ],
-            "modified": "2024-01-30",
-            "identifier": "c9a433cb-6754-4a87-a157-9571c054c0ca",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2022-01-01/2022-12-31",
-            "issued": "2024-01-30",
-            "accrualPeriodicity": "R/P1Y",
+            "landingPage": "https://www.epa.gov/egrid",
             "language": [
                 "en"
             ],
-            "dataQuality": true,
-            "landingPage": "https://www.epa.gov/egrid",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/egrid/download-data",
-                    "format": "Microsoft Office - OOXML - Spreadsheet (.xlsx)",
-                    "title": "eGRID Data Download",
-                    "description": "Most recent year represents 2022 data.",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/egrid/maps",
-                    "title": "eGRID Mapping Files",
-                    "description": "The eGRID mapping files include an eGRID subregion image (png), shapefiles (shp), zipped Keyhole Markup Language (kmz) files, and a geodatabase (gdb)."
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2024-01-30",
             "programCode": [
                 "020:032"
-            ]
-        },
-        {
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "name": "Environmental Protection Agency"
+            },
+            "temporal": "2022-01-01/2022-12-31",
+            "title": "Emission & Generation Resource Integrated Database (eGRID)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:puchalski.melissa@epa.gov"
+            },
+            "dataQuality": false,
             "description": "This asset provides data on model results for dry and total deposition of sulfur, nitrogen and base cation species. Components include deposition velocities, dry deposition and total deposition for sulfur and nitrogen from 1989 to present",
+            "identifier": "6F9EBF29-C1FD-4B38-99EF-FE0E7B82130C",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -143,38 +151,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Atmospheric Deposition Modeling Results",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6F9EBF29-C1FD-4B38-99EF-FE0E7B82130C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6F9EBF29-C1FD-4B38-99EF-FE0E7B82130C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Atmospheric Deposition Modeling Results"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:puchalski.melissa@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "6F9EBF29-C1FD-4B38-99EF-FE0E7B82130C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:puchalski.melissa@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Nephelometer data (conforms to IMPROVE network standards) from October 1993 to June 2002. This table is no longer updated.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/castnet",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "78745BEC-83F3-434E-849D-4D7BA4D4790C",
+            "issued": "2014-01-01",
             "keyword": [
                 "visibility",
                 "air quality",
@@ -203,45 +218,46 @@
                 "united states",
                 "environment"
             ],
-            "title": "Clean Air Status and Trends Network (CASTNET): Visibility",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/castnet",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B78745BEC-83F3-434E-849D-4D7BA4D4790C%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B78745BEC-83F3-434E-849D-4D7BA4D4790C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Clean Air Status and Trends Network (CASTNET): Visibility"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:puchalski.melissa@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Shaun Ragnauth, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:Ragnauth.Shaun@epa.gov"
             },
-            "identifier": "78745BEC-83F3-434E-849D-4D7BA4D4790C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Marginal abatement curves (MAC) can be downloaded as data annexes to the Global Mitigation of Non-CO2 Greenhouse Gases report. This data allows for improved understanding of the mitigation potential for non-CO2 sources, as well as inclusion of non-CO2 greenhouse gas mitigation in economic modeling of multigas mitigation strategies. The full report at https://www.epa.gov/climatechange/economics/international.html.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/global-mitigation-non-co2-greenhouse-gases/global-non-co2-greenhouse-gas-emission-projections",
+                    "downloadURL": "https://www3.epa.gov/climatechange/Downloads/EPAactivities/DataAnnex_EPA_NonCO2_Projections_2011_draft.zip",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "8EDB1220-D7E2-40F0-9932-2AC9D59B46B7",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "water",
@@ -262,46 +278,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Global Non-CO2 Greenhouse Gas Emission Projections & Mitigation Potential: 2015-2050: Download the Report",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/global-mitigation-non-co2-greenhouse-gases/global-non-co2-greenhouse-gas-emission-projections",
-                    "downloadURL": "https://www3.epa.gov/climatechange/Downloads/EPAactivities/DataAnnex_EPA_NonCO2_Projections_2011_draft.zip",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8EDB1220-D7E2-40F0-9932-2AC9D59B46B7%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8EDB1220-D7E2-40F0-9932-2AC9D59B46B7%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Global Non-CO2 Greenhouse Gas Emission Projections & Mitigation Potential: 2015-2050: Download the Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Ragnauth.Shaun@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Shaun Ragnauth, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "8EDB1220-D7E2-40F0-9932-2AC9D59B46B7",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Paul Gunning, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:gunning.paul@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains the sub-model for EPA's MARKAL model, which tracks methane emissions from the energy system, and limited other sources (landfills and manure handling). This dataset includes projections of future methane emissions from the energy system out to 2030 and potential mitigation levels of methane emissions by energy system component. See the full report at https://www.epa.gov/methane/projections.html.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/cmop",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "2BEBB4ED-2792-4129-B787-70985CCECB5C",
+            "issued": "2014-01-01",
             "keyword": [
                 "research",
                 "analysis & technology",
@@ -319,45 +334,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Methane Tracking and Mitigation Options - EPA CMOP",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/cmop",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2BEBB4ED-2792-4129-B787-70985CCECB5C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2BEBB4ED-2792-4129-B787-70985CCECB5C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Methane Tracking and Mitigation Options - EPA CMOP"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:gunning.paul@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Paul Gunning, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Kevin Culligan, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:culligan.kevin@epa.gov"
             },
-            "identifier": "2BEBB4ED-2792-4129-B787-70985CCECB5C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This asset provides information on policy options in abating SO2, NOx and Greenhouse gases.",
+            "identifier": "0F596FC6-0390-46C8-8B49-0F7D934A6675",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -380,38 +388,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Modeling Results for Policy Analyses",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0F596FC6-0390-46C8-8B49-0F7D934A6675%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0F596FC6-0390-46C8-8B49-0F7D934A6675%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Modeling Results for Policy Analyses"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:culligan.kevin@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Kevin Culligan, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "0F596FC6-0390-46C8-8B49-0F7D934A6675",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Stratospheric Protection Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:spdcomment@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This site includes all of the ozone-depleting substances (ODS) recognized by the Montreal Protocol.  The data include ozone depletion potentials (ODP), global warming potentials (GWP), and CAS numbers for each ODS.  The substances are organized by class.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/ozone-layer-protection/ozone-depleting-substances",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "5E064D95-5BFD-46DE-A4E3-D3D2F702C1F5",
+            "issued": "2014-01-01",
             "keyword": [
                 "substances",
                 "pollutants & contaminants",
@@ -425,45 +440,38 @@
                 "united states",
                 "health"
             ],
-            "title": "Ozone-depleting Substances (ODS)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/ozone-layer-protection/ozone-depleting-substances",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5E064D95-5BFD-46DE-A4E3-D3D2F702C1F5%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B5E064D95-5BFD-46DE-A4E3-D3D2F702C1F5%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Ozone-depleting Substances (ODS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:spdcomment@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Stratospheric Protection Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Paul Gunning,US Environmental Protection Agency Office of Air and Radiation, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:gunning.paul@epa.gov"
             },
-            "identifier": "5E064D95-5BFD-46DE-A4E3-D3D2F702C1F5",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains the output for modeling runs that were performed to investigate the effectiveness of various technologies and lay the groundwork for the formulation of policies for reducing methane emissions. See the full report at https://www.epa.gov/methane/projections.html.",
+            "identifier": "BA99CC05-FFAD-4B2A-B1D5-98552A078C07",
+            "issued": "2014-01-01",
             "keyword": [
                 "research",
                 "analysis & technology",
@@ -481,38 +489,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Analysis of Methane Mitigation Options using the MARKAL Model for the US: Calibration Data for Methane Emissions",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BBA99CC05-FFAD-4B2A-B1D5-98552A078C07%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBA99CC05-FFAD-4B2A-B1D5-98552A078C07%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Analysis of Methane Mitigation Options using the MARKAL Model for the US: Calibration Data for Methane Emissions"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:gunning.paul@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Paul Gunning,US Environmental Protection Agency Office of Air and Radiation, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "BA99CC05-FFAD-4B2A-B1D5-98552A078C07",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:GHGreporting@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The EV-GHG Mobile Source Data asset contains measured mobile source GHG emissions summary compliance information on light-duty vehicles, by model, for certification as required by the 1990 Amendments to the Clean Air Act, and as driven by the 2010 Presidential Memorandum Regarding Fuel Efficiency and the 2005 Supreme Court ruling in Massachusetts v. EPA that supported the regulation of CO2 as a pollutant. Manufacturers submit data on an annual basis, or as needed to document vehicle model changes. This asset will be expanded to include medium and heavy duty vehicles in the future.The EPA performs targeted GHG emissions tests on approximately 15% of vehicles submitted for certification. Confirmatory data on vehicles is associated with its corresponding submission data to verify the accuracy of manufacturer submissions beyond standard business rules.Submitted data comes in XML format or as documents, with the majority of submissions sent in XML, and includes descriptive information on the vehicle itself, emissions information, and the manufacturer's testing approach. This data may contain proprietary information (CBI) such as information on estimated sales or other data elements indicated by the submitter as confidential. CBI data is not publically available; however, CBI data can accessed within EPA under the restrictions of the Office of Transportation and Air Quality (OTAQ) CBI policy [RCS Link]. Pollutants data includes CO2, CH4, N2O. Datasets are divided by vehicle/engine model and/or year with corresponding emission, test, and certification data. Data assets are stored in EPA's Verify system.Coverage began in 2011, with summary light duty data available to the public on request. Raw data is only available to select EPA employees.EV-GHG Mobile Source Data submission documents with metadata, certificate and summary decision information is stored in Verify after it has been quality assured. Where summary data appears inaccurate, OTAQ returns the entries for review to their originator.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/ghgemissions/us-greenhouse-gas-inventory-report-1990-2014",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "1E9534CD-7CE0-4E30-A546-3AEB4793B188",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -532,45 +547,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "National Greenhouse Gas Emission Inventory (EV-GHG)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/ghgemissions/us-greenhouse-gas-inventory-report-1990-2014",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1E9534CD-7CE0-4E30-A546-3AEB4793B188%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1E9534CD-7CE0-4E30-A546-3AEB4793B188%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "National Greenhouse Gas Emission Inventory (EV-GHG)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:GHGreporting@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "John Mearis, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:Mearis.john@epa.gov"
             },
-            "identifier": "1E9534CD-7CE0-4E30-A546-3AEB4793B188",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "All Federal Agencies are required to prescribe an appropriate records maintenance program so that complete records are filed or otherwise preserved, records can be found when needed, the identification and retention of permanent records are facilitated, and permanent and temporary records are physically segregated, or for electronic records, segregable.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/records",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "9B8B1629-6F62-4B5B-A6F2-1E1D4813A05D",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa. oar",
                 "oria",
@@ -582,45 +597,46 @@
                 "united states",
                 "environment"
             ],
-            "title": "Records Management",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/records",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9B8B1629-6F62-4B5B-A6F2-1E1D4813A05D%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9B8B1629-6F62-4B5B-A6F2-1E1D4813A05D%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Records Management"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Mearis.john@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "John Mearis, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "9B8B1629-6F62-4B5B-A6F2-1E1D4813A05D",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Scott Riley, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:riley.scottm@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This asset provides data on the acid-base status of lakes and streams. Key chemical indicators measured include: sulfate, nitrate, ammonium, chloride, Acid Neutralizing Capacity (ANC), pH, base cations, dissolved organic carbon (DOC), total aluminum. TIME and LTM are part of EPA's Environmental Monitoring and Assessment Program (EMAP). Long-term monitoring of the acid-base status (pH, ANC, SO4, NO3, NH4, DOC, base cations, Al) in lakes and streams.  Monitoring is conducted in acid sensitive regions of the Eastern U.S.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/airmarkets/clean-air-markets-monitoring-surface-water-chemistry",
+                    "mediaType": "text/html",
+                    "title": "Clean Air Markets - Monitoring Surface Water Chemistry"
+                }
+            ],
+            "identifier": "7B915AF6-A68A-487B-89D9-D6D89567A36C",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -643,46 +659,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Regional Monitoring of Acidic Lakes and Streams",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/airmarkets/clean-air-markets-monitoring-surface-water-chemistry",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "Clean Air Markets - Monitoring Surface Water Chemistry"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2020-04-16",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B7B915AF6-A68A-487B-89D9-D6D89567A36C%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B7B915AF6-A68A-487B-89D9-D6D89567A36C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Regional Monitoring of Acidic Lakes and Streams"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:riley.scottm@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Scott Riley, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "7B915AF6-A68A-487B-89D9-D6D89567A36C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Paul Gunning, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:gunning.paul@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains relative and absolute forecasts of emissions through 2020 for landfills, natural gas and oil systems, coal mines, manure management and enteric fermentation. See the full report on inventories, projections, and opportunities for reductions at https://www.epa.gov/methane/projections.html.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://nepis.epa.gov/Exe/ZyNET.exe/600009LH.TXT?ZyActionD=ZyDocument&Client=EPA&Index=1995+Thru+1999&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C95thru99%5CTxt%5C00000019%5C600009LH.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "05767852-2EF9-47E8-A89B-0A4799D9896D",
+            "issued": "2014-01-01",
             "keyword": [
                 "research",
                 "analysis & technology",
@@ -700,45 +715,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Report on U.S. Methane Emissions 1990-2020: Inventories, Projections, and Opportunities for Reductions: 2001 Updated emission and cost estimates",
-            "distribution": [
-                {
-                    "accessURL": "https://nepis.epa.gov/Exe/ZyNET.exe/600009LH.TXT?ZyActionD=ZyDocument&Client=EPA&Index=1995+Thru+1999&Docs=&Query=&Time=&EndTime=&SearchMethod=1&TocRestrict=n&Toc=&TocEntry=&QField=&QFieldYear=&QFieldMonth=&QFieldDay=&IntQFieldOp=0&ExtQFieldOp=0&XmlQuery=&File=D%3A%5Czyfiles%5CIndex%20Data%5C95thru99%5CTxt%5C00000019%5C600009LH.txt&User=ANONYMOUS&Password=anonymous&SortMethod=h%7C-&MaximumDocuments=1&FuzzyDegree=0&ImageQuality=r75g8/r75g8/x150y150g16/i425&Display=hpfr&DefSeekPage=x&SearchBack=ZyActionL&Back=ZyActionS&BackDesc=Results%20page&MaximumPages=1&ZyEntry=1&SeekPage=x&ZyPURL",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B05767852-2EF9-47E8-A89B-0A4799D9896D%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B05767852-2EF9-47E8-A89B-0A4799D9896D%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Report on U.S. Methane Emissions 1990-2020: Inventories, Projections, and Opportunities for Reductions: 2001 Updated emission and cost estimates"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:gunning.paul@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Paul Gunning, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Shaun Ragnauth, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:Ragnauth.Shaun@epa.gov"
             },
-            "identifier": "05767852-2EF9-47E8-A89B-0A4799D9896D",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The data in these Appendices to the Global Anthropogenic Emissions of Non-CO2 Greenhouse Gases (1990-2020) report provide historical and projected estimates of emissions from over 90 countries and 8 regions for all major non-CO2 greenhouse gas emission sources. The gases included in this data set are methane (CH4), nitrous oxide (N2O), and the high global warming potential (high GWP) gases (hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), and sulfur hexafluoride (SF6)). See the full report at https://www.epa.gov/climatechange/economics/international.html.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/global-mitigation-non-co2-greenhouse-gases",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "55464D82-8AA5-4225-9DD3-18BEB2B0759A",
+            "issued": "2014-01-01",
             "keyword": [
                 "substances",
                 "pollutants & contaminant",
@@ -757,45 +772,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Global Non-CO2 Greenhouse Gas Emission Projections & Mitigation: 2015-2050",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/global-mitigation-non-co2-greenhouse-gases",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B55464D82-8AA5-4225-9DD3-18BEB2B0759A%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B55464D82-8AA5-4225-9DD3-18BEB2B0759A%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Global Non-CO2 Greenhouse Gas Emission Projections & Mitigation: 2015-2050"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Ragnauth.Shaun@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Shaun Ragnauth, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "55464D82-8AA5-4225-9DD3-18BEB2B0759A",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "CAMPD Support, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:campd-support@camdsupport.com"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Clean Air Markets Program Data (CAMPD) application, accessible at https://campd.epa.gov/, allows users to view Clean Air Markets data through the Custom Data Download Tool and Bulk Data Files. These tools are driven by APIs documented in the CAM API Portal https://www.epa.gov/airmarkets/cam-api-portal, which is accessible through CAMPD. The Custom Data Download Tool and APIs allow users to create custom queries to explore CAMD\u2019s database through different data types: emissions, allowances, compliance, and facility attributes. Prepackaged Bulk Data Files are also available for commonly requested datasets and larger data downloads. EPA's Clean Air Markets Division (CAMD) manages several market-based regulatory programs designed to improve air quality and ecosystems. The most well-known of these programs are EPA's Acid Rain Program and the Cross-State Air Pollution Rule (CSAPR) Programs, which reduce emissions of sulfur dioxide (SO2) and nitrogen oxides (NOx)-compounds that adversely affect air quality, the environment, and public health.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://campd.epa.gov/",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "94AAED23-8775-4A2F-BFB7-74F972F5251C",
+            "issued": "2022-06-27",
             "keyword": [
                 "air quality",
                 "tradeable permits",
@@ -823,45 +838,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Clean Air Markets Program Data Application (CAMPD)",
-            "distribution": [
-                {
-                    "accessURL": "https://campd.epa.gov/",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2022-06-27",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2022-08-23",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B94AAED23-8775-4A2F-BFB7-74F972F5251C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B94AAED23-8775-4A2F-BFB7-74F972F5251C%7D"
             ],
-            "accrualPeriodicity": "R/P1D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Clean Air Markets Program Data Application (CAMPD)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:campd-support@camdsupport.com",
                 "@type": "vcard:Contact",
-                "fn": "CAMPD Support, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "94AAED23-8775-4A2F-BFB7-74F972F5251C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:puchalski.melissa@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The CASTNET Download Data module allows users to select, view, and download CASTNET data (Raw, Aggregate, Modeled & Factual Data) based on user selections.\n  \nCASTNET sites are located in or near rural areas and sensitive ecosystems collecting data on ambient levels of pollutants where urban influences are minimal. CASTNET, which was initiated in 1986, is able to provide data needed to assess and report on geographic patterns and long-term temporal trends in ambient air pollution and dry atmospheric deposition. CASTNET can also be used to track changes in measurements associated with climate change (such as temperature and precipitation).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://java.epa.gov/castnet/clearsession.do",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "5936F352-D87F-4D70-B5C2-1EDA46CD0CF1",
+            "issued": "2014-01-01",
             "keyword": [
                 "ozone",
                 "air quality",
@@ -881,45 +896,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Clean Air Status and Trends Network (CASTNET) Download Data Module",
-            "distribution": [
-                {
-                    "accessURL": "https://java.epa.gov/castnet/clearsession.do",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B5936F352-D87F-4D70-B5C2-1EDA46CD0CF1%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5936F352-D87F-4D70-B5C2-1EDA46CD0CF1%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Clean Air Status and Trends Network (CASTNET) Download Data Module"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:puchalski.melissa@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Melissa Puchalski, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "5936F352-D87F-4D70-B5C2-1EDA46CD0CF1",
-            "@type": "dcat:Dataset"
+                "fn": "Sam Napolitano, Director, Clean Air Markets Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:napolitano.sam@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "8-hour daily maximum ozone concentrations as measured by the Clean Air Status and Trends Network (CASTNET)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/castnet/ozone",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "0192864F-9853-4192-96DE-00ED84376BA1",
+            "issued": "2014-01-01",
             "keyword": [
                 "ozone",
                 "air quality",
@@ -939,45 +954,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Clean Air Status and Trends Network (CASTNET): Ozone",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/castnet/ozone",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0192864F-9853-4192-96DE-00ED84376BA1%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0192864F-9853-4192-96DE-00ED84376BA1%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Clean Air Status and Trends Network (CASTNET): Ozone"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:napolitano.sam@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sam Napolitano, Director, Clean Air Markets Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "0192864F-9853-4192-96DE-00ED84376BA1",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "Stratospheric Protection Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:spdcomment@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This site includes  the global warming potential (GWP) of ozone depleting substance substitutes, their atmospheric lifetime, and uses.",
+            "identifier": "6A69DBD7-5DE5-48B4-8C6D-845878333894",
+            "issued": "2014-01-01",
             "keyword": [
                 "substances",
                 "chemicals",
@@ -991,38 +999,38 @@
                 "united states",
                 "health"
             ],
-            "title": "Global Warming Potentials (GWP) of ODS Substitutes",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6A69DBD7-5DE5-48B4-8C6D-845878333894%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6A69DBD7-5DE5-48B4-8C6D-845878333894%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Global Warming Potentials (GWP) of ODS Substitutes"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:spdcomment@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Stratospheric Protection Division, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "6A69DBD7-5DE5-48B4-8C6D-845878333894",
-            "@type": "dcat:Dataset"
+                "fn": "Gwendolyn Taylor, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:taylor.gwendolyn@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "restricted public",
+            "dataQuality": false,
             "description": "The Integrated Strategic Tracking and Recruiting Database (iSTAR) Data Inventory contains measured and modeled partnership and contact data. It is comprised of basic organization information, their relationship with CPPD, and relative contact information.The statutory authority leading to the collection of this information comes from Title I Section XIV of the Clean Air Act.Sustance classes include CAPs, and data is collected daily.",
+            "identifier": "87793ADF-2B3C-41D2-97F6-873704B58533",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1041,38 +1049,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Integrated Strategic Tracking and Recruiting Database (iSTAR) Data Inventory",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B87793ADF-2B3C-41D2-97F6-873704B58533%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B87793ADF-2B3C-41D2-97F6-873704B58533%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Integrated Strategic Tracking and Recruiting Database (iSTAR) Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:taylor.gwendolyn@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Gwendolyn Taylor, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "87793ADF-2B3C-41D2-97F6-873704B58533",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:GHGreporting@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The National Greenhouse Gas Emission Inventory contains information on direct emissions of greenhouse gases as well as indirect or potential emissions of greenhouse gases through fuels combustion or oxidation, plus releases from storage or sequestration facilities, compiled on an annual basis. Substance classes principally include include CO2, methane, nitrous oxide, and fluorinated gases. The 2008 Consolidated Appropriations Act and the Mandatory Reporting of Greenhouse Gases Act are the statutory basis behind this data. Reporting includes nine sectors. Data is  contributed by reporting industrial and commercial sources of more than 25,000 tons of CO2 equivalent per year. It is also estimated and modeled for transportation and other sources which are geographically distributed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/ghgemissions/us-greenhouse-gas-inventory-report-1990-2014",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "749A4BBB-82A8-4224-9EF4-024C377B459B",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1092,45 +1107,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "National Greenhouse Gas Emission Inventory",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/ghgemissions/us-greenhouse-gas-inventory-report-1990-2014",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B749A4BBB-82A8-4224-9EF4-024C377B459B%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B749A4BBB-82A8-4224-9EF4-024C377B459B%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "National Greenhouse Gas Emission Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:GHGreporting@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "749A4BBB-82A8-4224-9EF4-024C377B459B",
-            "@type": "dcat:Dataset"
+                "fn": "Kevin Culligan, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)",
+                "hasEmail": "mailto:culligan.kevin@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This asset provides information on all operating and planned-committed electricity generation units (used as primary input for IPM)",
+            "identifier": "4805EA49-8426-4DE2-B620-CE5A15373054",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1152,34 +1160,37 @@
                 "united states",
                 "environment"
             ],
-            "title": "Pollution Control Measures and Equipment",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4805EA49-8426-4DE2-B620-CE5A15373054%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4805EA49-8426-4DE2-B620-CE5A15373054%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Pollution Control Measures and Equipment"
+        },
+        {
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:culligan.kevin@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Kevin Culligan, U.S. EPA Office of Air and Radiation (OAR) - Office of Atmospheric Programs (OAP)"
-            },
-            "identifier": "4805EA49-8426-4DE2-B620-CE5A15373054",
-            "@type": "dcat:Dataset"
+                "fn": "Arthur Zuco, U.S. Environmental Protection Agency, Office of Air and Radiation",
+                "hasEmail": "mailto:zuco.arthur@epa.gov"
             },
-        {
-            "title": "Our Nation's Air - annual air trends report, USA, EPA OAR OAQPS",
+            "dataQuality": false,
             "description": "Annual air trends report in the form of an interactive web application. The report features a suite of visualization tools that allow the user to:\n-Learn about air pollution and how it can affect our health and environment.\n-Compare key air emissions to gross domestic product, vehicle miles traveled, population, and energy consumption back to 1970.\n-Take a closer look at how the number of days with unhealthy air has dropped since 2000 in 35 major US cities.\n-Explore how air quality and emissions have changed through time and space for each of the common air pollutants.\n-Check out air trends where you live.\n\nUsers will also be able to share this content across social media, with one-click access to Facebook, Twitter, Pinterest, and other major social media sites.",
+            "identifier": "65276ABE-0D64-4C26-9824-CF0B1752041C",
+            "issued": "2016-07-21",
             "keyword": [
                 "air",
                 "cleanup",
@@ -1209,42 +1220,39 @@
                 "transportation",
                 "utilitiescommunication"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B65276ABE-0D64-4C26-9824-CF0B1752041C%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2017-08-28",
-            "issued": "2016-07-21",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Air and Radiation"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Arthur Zuco, U.S. Environmental Protection Agency, Office of Air and Radiation",
-                "hasEmail": "mailto:zuco.arthur@epa.gov"
-            },
-            "identifier": "65276ABE-0D64-4C26-9824-CF0B1752041C",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B65276ABE-0D64-4C26-9824-CF0B1752041C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B65276ABE-0D64-4C26-9824-CF0B1752041C%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B65276ABE-0D64-4C26-9824-CF0B1752041C%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Our Nation's Air - annual air trends report, USA, EPA OAR OAQPS"
         },
         {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Marc Houyoux, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:houyoux.marc@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Air Emissions Trends site provides national trends of criteria pollutant and precursor emissions data based on the the National Emissions Inventory (NEI) from 1970 - the latest NEI year.",
+            "identifier": "9B89FEF1-068B-4C8E-9A26-D95821871A42",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1254,45 +1262,47 @@
                 "united states",
                 "environment"
             ],
-            "title": "Criteria Air Emissions Trends",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9B89FEF1-068B-4C8E-9A26-D95821871A42%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9B89FEF1-068B-4C8E-9A26-D95821871A42%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Criteria Air Emissions Trends"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:houyoux.marc@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Marc Houyoux, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "9B89FEF1-068B-4C8E-9A26-D95821871A42",
-            "@type": "dcat:Dataset"
+                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
             },
+            "dataQuality": false,
+            "description": "The AirData site provides access to yearly summaries of United States air pollution data, taken from EPA's air pollution databases. AirData has information about where air pollution comes from (emissions) and how much pollution is in the air outside our homes and work places (monitoring).",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4018E3B6-74D1-4F0B-B5D4-E263357D475A%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B4018E3B6-74D1-4F0B-B5D4-E263357D475A%7D"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data"
+                }
             ],
-            "accessLevel": "public",
-            "description": "The AirData site provides access to yearly summaries of United States air pollution data, taken from EPA's air pollution databases. AirData has information about where air pollution comes from (emissions) and how much pollution is in the air outside our homes and work places (monitoring).",
+            "identifier": "4018E3B6-74D1-4F0B-B5D4-E263357D475A",
+            "issued": "2014-01-01",
             "keyword": [
                 "human health",
                 "health risks",
@@ -1308,43 +1318,41 @@
                 "united states",
                 "health"
             ],
-            "title": "AirData",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data",
-                    "@type": "dcat:Distribution"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "4018E3B6-74D1-4F0B-B5D4-E263357D475A",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4018E3B6-74D1-4F0B-B5D4-E263357D475A%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B4018E3B6-74D1-4F0B-B5D4-E263357D475A%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "AirData"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mike Ciolek, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:ciolek.michael@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Emissions factors have long been the fundamental tool in developing national, regional, state, and local emissions inventories for air quality management decisions and in developing emissions control strategies. More recently, emissions factors have been applied in determining site-specific applicability and emissions limitations in operating permits by federal, state, local, and tribal agencies, consultants, and industry. AP-42 is a compendium of EPA recommended emissions factors.",
+            "identifier": "668EB849-93EE-46FD-9C7C-6D50A03BA223",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1366,41 +1374,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "AP-42 Emissions Factors (WebFIRE)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B668EB849-93EE-46FD-9C7C-6D50A03BA223%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B668EB849-93EE-46FD-9C7C-6D50A03BA223%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "AP-42 Emissions Factors (WebFIRE)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:ciolek.michael@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Mike Ciolek, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Ketan Patel, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:patel.ketan@epa.gov"
             },
-            "identifier": "668EB849-93EE-46FD-9C7C-6D50A03BA223",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "EPA regulations codified in 40 CFR Part 60 and 63 require affected sources to perform emissions source tests, conduct continuous emissions monitoring, and submit compliance and emissions reports . EPA is promulgating \"E-Reporting\" rules to require affected sources to electronically submit source test results, emissions monitoring data, compliance reports, and emissions reports to EPA. As a result the EPA has developed the Compliance and Emissions Data Reporting Interface (CEDRI) which is located on EPA's Central Data Exchange (CDX). The CDX Web is the application used by EPA programs and various stakeholders to manage environmental data transmitted to EPA in order to meet EPA's reporting requirements.",
+            "identifier": "10895E74-8139-450B-925E-4A25BA807E7B",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1410,41 +1418,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Compliance and Emissions Data Reporting Interface (CEDRI)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B10895E74-8139-450B-925E-4A25BA807E7B%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B10895E74-8139-450B-925E-4A25BA807E7B%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Compliance and Emissions Data Reporting Interface (CEDRI)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:patel.ketan@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Ketan Patel, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Marc Houyoux, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:houyoux.marc@epa.gov"
             },
-            "identifier": "10895E74-8139-450B-925E-4A25BA807E7B",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Emissions Modeling Clearinghouse (EMCH) supports and promotes emissions modeling activities both internal and external to the EPA.  Through this site, the EPA distributes and documents emissions datasets that are formatted for use in emissions models, which are used for emissions preparation for air quality modeling.  The inventory data on this site are dervied from previous and current versions of the National Emission Inventory (NEI).  This site also distributes the EPA's latest versions of ancillary datasets used to support the temporal, spatial, speciation, and future-year projection of these emissions.",
+            "identifier": "01CD5875-92B2-4DCF-996A-71B09CAC2679",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1454,41 +1462,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Emissions Modeling Clearinghouse",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B01CD5875-92B2-4DCF-996A-71B09CAC2679%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B01CD5875-92B2-4DCF-996A-71B09CAC2679%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Emissions Modeling Clearinghouse"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:houyoux.marc@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Marc Houyoux, EPA/OAR/OAQPS, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "01CD5875-92B2-4DCF-996A-71B09CAC2679",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Joe Steigerwald, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Steigerwald.joe@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "OAR's RACT, BACT, LAER Clearinghouse (RBLC) data asset contains summary information on selected air permitting actions from EPA, state, and local permitting agencies across the U.S., as well as a number of international permit records supplied by air pollution control agencies in Mexico and Canada. The acronyms refer to program requirements of the New Source Review (NSR) program: RACT is Reasonably Available Control Technology and applies to existing sources in areas that are not meeting national ambient air quality standards (i.e., non-attainment areas); BACT is Best Available Control Technology and applies to major new or modified sources in clean areas (i.e., attainment areas). LAER, or Lowest Achievable Emission Rate, is required on major new or modified sources in non-attainment areas. As of 2012, RBLC includes approximately 6,500 entries. With the exception of LAER permit determinations, whose inclusion in RBLC is mandatory, participation is voluntary. Coverage is therefore not complete or necessarily representative.Required under Section 108 of the 1990 Amendments to the Clean Air Act, RBLC provides users  typically permit writers, permit applicants or holders, and the public  with references and personal contacts to support ongoing air pollution control activities. Information is detailed enough for users to know whether a permit is applicable to their needs. Users may then contact the appropriate agency to access the permit or discuss it with agency staff.RBLC-referenced permits cover Criteria Air Pollutants (CAPs) and Hazardous Air Pollutants (HAPs), but the data is also searchable for Greenhouse Gas (GHG) references. Entries are generally provided by the original permitting agency, though EPA Regional Offices may enter data on behalf of state and local agencies to augment coverage. Since 2009, Canadian and Mexican agencies have had access to the RBLC to submit their own permit information; all data is provided in English.There are three main levels of information  Facility, Process, and Pollutant. Facility Data includes but is not limited to: Facility Name, City/Town, State, Permitting Agency, Permit Date, NAICS, SIC, Facility Registry System Number, Permit Number, and Agency Contact Name & Phone Number. Process Data includes but is not limited to: Process Name, Process Type Code, and Throughput. Pollutant Data includes but is not limited to: Pollutant Name, CAS#, Emissions Testing Method(s), Emission Limits, Case-by-Case Basis and any Other Applicable Requirements; and Control Method Description. U.S. geographic coverage includes all states and territories, plus all U.S. permitted facilities within U.S. waters (generally 3 miles for state limits, but further offshore for DOI-permitted oil platforms). Coverage began in 1980, but some historical permits from the 1970s are included. Over the years the data has been converted from paper to searchable digital form. Data is not overwritten, so multiple historical permit references for a single facility may be included. OAQPS manually cross-references RBLC references to the appropriate Facility Registry System (FRS) ID to the extent possible. All RBLC content is public and non-sensitive and available through EPA.gov after it has been quality assured. Data is quality assured by EPA and entered into the RACT, BACT, LAER Clearinghouse (RBLC) data management system (https://cfpub.epa.gov/rblc/index.cfm?action=Home.Home). Where technical summaries appear inaccurate, OAQPS returns entries for review to their originators. All data is edited and approved by the Office of Air and Radiation's Office of Air Quality Permits and Standards (OAQPS) prior to publication.",
+            "identifier": "668AD64A-06E5-4870-B5CB-2FFC45A95A88",
+            "issued": "2014-01-01",
             "keyword": [
                 "rblc",
                 "ract",
@@ -1518,45 +1526,47 @@
                 "united states",
                 "environment"
             ],
-            "title": "RACT_BACT_LAER Clearinghouse (RBLC)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B668AD64A-06E5-4870-B5CB-2FFC45A95A88%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B668AD64A-06E5-4870-B5CB-2FFC45A95A88%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RACT_BACT_LAER Clearinghouse (RBLC)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Steigerwald.joe@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Joe Steigerwald, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "668AD64A-06E5-4870-B5CB-2FFC45A95A88",
-            "@type": "dcat:Dataset"
+                "fn": "Gary Lear,US Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:lear.gary@epa.gov"
             },
+            "dataQuality": false,
+            "description": "This asset provides data on regional air quality, including trace level SO2, nitric acid, ozone, carbon monoxide, and NOy; and particulate sulfate, nitrate, and ammonium from 1989 to present. Precipitation and meteorology are provided from 1989 to 2011.",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7BDE68A445-C389-4C5C-AAC7-D15395BC12D1%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDE68A445-C389-4C5C-AAC7-D15395BC12D1%7D"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/castnet"
+                }
             ],
-            "accessLevel": "public",
-            "description": "This asset provides data on regional air quality, including trace level SO2, nitric acid, ozone, carbon monoxide, and NOy; and particulate sulfate, nitrate, and ammonium from 1989 to present. Precipitation and meteorology are provided from 1989 to 2011.",
+            "identifier": "DE68A445-C389-4C5C-AAC7-D15395BC12D1",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1580,44 +1590,42 @@
                 "united states",
                 "environment"
             ],
-            "title": "Regional Air Quality Data",
+            "landingPage": "https://www.epa.gov/castnet",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/castnet",
-                    "@type": "dcat:Distribution"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.epa.gov/castnet",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:lear.gary@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Gary Lear,US Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "DE68A445-C389-4C5C-AAC7-D15395BC12D1",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/rest/document?id=%7BDE68A445-C389-4C5C-AAC7-D15395BC12D1%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDE68A445-C389-4C5C-AAC7-D15395BC12D1%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Regional Air Quality Data"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Photochemical Assessment Monitoring Stations (PAMS). This file provides information on the numbers and distribution (latitude/longitude) of air monitoring sites  which measure ozone precursors (approximately 60 volatile hydrocarbons and carbonyl), as required by the 1990 Clean Air Act Amendments, in areas with persistently high ozone levels (mostly large metropolitan areas).  In these areas, the States have established ambient air monitoring sites which collect and report detailed data for volatile organic compounds, nitrogen oxides, ozone and meteorological parameters.  This file displays 199 monitoring sites reporting measurements for 2010.  A wide range of related monitoring site attributes is also provided.",
+            "identifier": "F583CC2A-5F0E-411B-A680-4E0CB5382167",
+            "issued": "2014-01-01",
             "keyword": [
                 "air",
                 "environment",
@@ -1627,45 +1635,47 @@
                 "united states",
                 "environment"
             ],
-            "title": "Photochemical Assessment Monitoring Stations (PAMS)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF583CC2A-5F0E-411B-A680-4E0CB5382167%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF583CC2A-5F0E-411B-A680-4E0CB5382167%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Photochemical Assessment Monitoring Stations (PAMS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "F583CC2A-5F0E-411B-A680-4E0CB5382167",
-            "@type": "dcat:Dataset"
+                "fn": "Madeleine Strum, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Strum.madeleine@Epa.gov"
             },
+            "dataQuality": false,
+            "description": "This data exchange allows states to submit data to the US Environmental Protection Agency's National Emissions Inventory (NEI). NEI is a national database of air emissions information including input from numerous State and local air agencies, tribes, and industry.\n(Status: In Transition to the Emission Inventory System)",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B360CA50F-3E1B-4CCF-B32A-85CB293B5A9F%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B360CA50F-3E1B-4CCF-B32A-85CB293B5A9F%7D"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/air-emissions-inventories"
+                }
             ],
-            "accessLevel": "public",
-            "description": "This data exchange allows states to submit data to the US Environmental Protection Agency's National Emissions Inventory (NEI). NEI is a national database of air emissions information including input from numerous State and local air agencies, tribes, and industry.\n(Status: In Transition to the Emission Inventory System)",
+            "identifier": "360CA50F-3E1B-4CCF-B32A-85CB293B5A9F",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -1676,43 +1686,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Air Emisisons Inventories",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/air-emissions-inventories",
-                    "@type": "dcat:Distribution"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:Strum.madeleine@Epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Madeleine Strum, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "360CA50F-3E1B-4CCF-B32A-85CB293B5A9F",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B360CA50F-3E1B-4CCF-B32A-85CB293B5A9F%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B360CA50F-3E1B-4CCF-B32A-85CB293B5A9F%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Air Emisisons Inventories"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Misenheimer, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:misenheimer.david@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The EPA Control Measure Dataset is a collection of documents describing air pollution control available to regulated facilities for the control and abatement of air pollution emissions from a range of regulated source types, whether directly through the use of technical measures, or indirectly through economic or other measures.",
+            "identifier": "92676F0D-0785-40B6-B0CA-4B4D7D7D2132",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1731,41 +1739,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Control Measure Dataset",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B92676F0D-0785-40B6-B0CA-4B4D7D7D2132%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B92676F0D-0785-40B6-B0CA-4B4D7D7D2132%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Control Measure Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:misenheimer.david@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "David Misenheimer, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "92676F0D-0785-40B6-B0CA-4B4D7D7D2132",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Jeff Herring, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:herring.jeff@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Title V Permitting Statistics Inventory contains measured and estimated nationwide statistical data, consisting of counts of permitted sources, types of permits issued, and the timeliness of permit issuance, for the operating permits programs being implemented under CAA authority (40 CFR parts 70 and 71). This data is non-source specific. The statutory authority leading to the collection of this information comes from Title V of the Clean Air Act.Prior to July 2008, data collected on state permit programs (part 70) was not equivalent to that collected when EPA was the permitting agency (part 71).  Current system includes semiannual data from 2006-present; prior data is archived.Data is currently not publicly available, certain statistical data has been made available in the past, but not currently. This data is mostly used for ICR and PART reporting purposes.",
+            "identifier": "2EA64C8B-18B3-4F57-B0C9-5ADAEE3F3D26",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1786,45 +1794,47 @@
                 "united states",
                 "environment"
             ],
-            "title": "Title V Permitting Statistics Inventory",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2EA64C8B-18B3-4F57-B0C9-5ADAEE3F3D26%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2EA64C8B-18B3-4F57-B0C9-5ADAEE3F3D26%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Title V Permitting Statistics Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:herring.jeff@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Jeff Herring, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "2EA64C8B-18B3-4F57-B0C9-5ADAEE3F3D26",
-            "@type": "dcat:Dataset"
+                "fn": "Mike Ciolek, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:info.chief@epa.gov"
             },
+            "dataQuality": false,
+            "description": "The Factor Information Retrieval (FIRE) Data System is a database management system containing EPA's recommended emission estimation factors for criteria and hazardous air pollutants. FIRE includes information about industries and their emitting processes, the chemicals emitted, and the emission factors.",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7BCC90E027-E07A-4D82-9888-DFB6F61308E0%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCC90E027-E07A-4D82-9888-DFB6F61308E0%7D"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://cfpub.epa.gov/webfire/"
+                }
             ],
-            "accessLevel": "public",
-            "description": "The Factor Information Retrieval (FIRE) Data System is a database management system containing EPA's recommended emission estimation factors for criteria and hazardous air pollutants. FIRE includes information about industries and their emitting processes, the chemicals emitted, and the emission factors.",
+            "identifier": "CC90E027-E07A-4D82-9888-DFB6F61308E0",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "air",
@@ -1837,47 +1847,47 @@
                 "united states",
                 "environment"
             ],
-            "title": "WebFIRE",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://cfpub.epa.gov/webfire/",
-                    "@type": "dcat:Distribution"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:info.chief@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Mike Ciolek, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "CC90E027-E07A-4D82-9888-DFB6F61308E0",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7B51984E19-8324-42B6-A73C-54CEACF01F6C%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B51984E19-8324-42B6-A73C-54CEACF01F6C%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7BCC90E027-E07A-4D82-9888-DFB6F61308E0%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCC90E027-E07A-4D82-9888-DFB6F61308E0%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "WebFIRE"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "dataQuality": false,
             "description": "AirCompare contains air quality information that allows a user to compare conditions in different localities over time and compare conditions in the same location at different times of the year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www3.epa.gov/aircompare/"
+                }
+            ],
+            "identifier": "51984E19-8324-42B6-A73C-54CEACF01F6C",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -1887,44 +1897,42 @@
                 "united states",
                 "environment"
             ],
-            "title": "AirCompare",
+            "landingPage": "https://www.epa.gov/aircompare/",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www3.epa.gov/aircompare/",
-                    "@type": "dcat:Distribution"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.epa.gov/aircompare/",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "51984E19-8324-42B6-A73C-54CEACF01F6C",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/rest/document?id=%7B51984E19-8324-42B6-A73C-54CEACF01F6C%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B51984E19-8324-42B6-A73C-54CEACF01F6C%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "AirCompare"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "N/A, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:aqsteam@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Office of Air and Radiation's (OAR) Ambient Air Quality Data (Current) contains ambient air pollution data collected by EPA, other federal agencies, as well as state, local, and tribal air pollution control agencies. Its component data sets have been collected over the years from approximately 10,000 monitoring sites, of which approximately 5,000 are currently active. OAR's Office of Air Quality Planning and Standards (OAQPS) and other internal and external users, rely on this data to assess air quality, assist in Attainment/Non-Attainment designations, evaluate State Implementation Plans for Non-Attainment Areas, perform modeling for permit review analysis, and other air quality management functions.  Air quality information is also used to prepare reports for Congress as mandated by the Clean Air Act. This data covers air quality data collected after 1980, when the Clean Air Act requirements for monitoring were significantly modified. Air quality data from the Agency's early years (1970s) remains available (see OAR PRIMARY DATA ASSET: Ambient Air Quality Data -- Historical), but because of technical and definitional differences the two data assets are not directly comparable. The Clean Air Act of 1970 provided initial authority for monitoring air quality for Conventional Air Pollutants (CAPs) for which EPA has promulgated National Ambient Air Quality Standards (NAAQS). Requirements for monitoring visibility-related parameters were added in 1977. Requirements for monitoring acid deposition and Hazardous Air Pollutants (HAPs) were added in 1990. Most monitoring sites contain multiple instruments. Most also report meteorological data, including wind speed and direction, humidity, atmospheric pressure, inbound solar radiation, precipitation and other factors relevant to air quality analysis. The current system of sites represents a number of independently-defined monitoring networks with different regulatory or scientific purposes, such as the State and Local Air Monitoring System, the National Air Toxics Trends sites, the Urban Air Toxics sites, the IMPROVE visibility monitoring network, the air toxics monitoring sites for schools, and others. (A complete list of air quality monitoring networks is available at https://www.epa.gov/???). Efforts are under way through NCore Multipollutant Monitoring Network (https://www.epa.gov/ttnamti1/ncore/index.html) to streamline and integrate advanced air quality measurement systems to minimize costs of data collection. Measurements and estimates from these networks are collected across the entire U.S., including all states and territories, with emphasis on documenting pollutant exposures in populated areas.Sampling frequencies vary by pollutant (hourly, 3- and 8-hour, daily, monthly, seasonal, and annual measurements), as required by different NAAQS. Some 50,000 measurements per day are added to the EPA's central air quality data repository, the Air Quality System (AQS). All data, including meteorological information, is public and non-confidential and available through the AQS Data Mart (https://www.epa.gov/ttn/airs/aqsdatamart/). Generally, data for one calendar quarter are reported by the end of the following quarter; some values may be subsequently changed due to quality assurance activities.",
+            "identifier": "189B24D8-CFEF-42D1-94F8-41CC3E5A9C1A",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -1949,45 +1957,51 @@
                 "united states",
                 "environment"
             ],
-            "title": "Ambient Air Quality Data Inventory",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B189B24D8-CFEF-42D1-94F8-41CC3E5A9C1A%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B189B24D8-CFEF-42D1-94F8-41CC3E5A9C1A%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Ambient Air Quality Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:aqsteam@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "N/A, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "189B24D8-CFEF-42D1-94F8-41CC3E5A9C1A",
-            "@type": "dcat:Dataset"
+                "fn": "Michael Hamlin, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Hamlin.michael@Epa.gov"
             },
+            "dataQuality": false,
+            "description": "Air Trends provides geographic trend information for specific air pollutants.",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/environmental-topics/air-topics"
                 },
-            "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B3DB6F135-F889-4901-BA61-C4CF4A130D44%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B3DB6F135-F889-4901-BA61-C4CF4A130D44%7D"
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "application/pdf"
+                }
             ],
-            "accessLevel": "public",
-            "description": "Air Trends provides geographic trend information for specific air pollutants.",
+            "identifier": "3DB6F135-F889-4901-BA61-C4CF4A130D44",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -2005,48 +2019,42 @@
                 "united states",
                 "environment"
             ],
-            "title": "Air Trends",
+            "landingPage": "https://www.epa.gov/environmental-topics/air-topics",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/environmental-topics/air-topics",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.epa.gov/environmental-topics/air-topics",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:Hamlin.michael@Epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Michael Hamlin, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "3DB6F135-F889-4901-BA61-C4CF4A130D44",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B3DB6F135-F889-4901-BA61-C4CF4A130D44%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B3DB6F135-F889-4901-BA61-C4CF4A130D44%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Air Trends"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nick Mangus,Scientist, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Ambient ozone concentrations for 2007 from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
+            "identifier": "444FDE7D-E2E8-469E-92C1-766E2CDB73AD",
+            "issued": "2014-01-01",
             "keyword": [
                 "ozone",
                 "air quality",
@@ -2066,41 +2074,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Air Quality System (AQS) ambient observations: 2007 ozone",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B444FDE7D-E2E8-469E-92C1-766E2CDB73AD%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B444FDE7D-E2E8-469E-92C1-766E2CDB73AD%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Air Quality System (AQS) ambient observations: 2007 ozone"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Nick Mangus,Scientist, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "444FDE7D-E2E8-469E-92C1-766E2CDB73AD",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The CMAQ Model Outputs data asset includes current and projected future levels of ambient concentrations and deposition to support regulatory impact analyses.",
+            "identifier": "7FEBA753-FD29-4DE3-860C-61B0A30D2D51",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -2119,41 +2127,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Community Multi-scale Air Quality (CMAQ) Model Outputs",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B7FEBA753-FD29-4DE3-860C-61B0A30D2D51%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B7FEBA753-FD29-4DE3-860C-61B0A30D2D51%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Community Multi-scale Air Quality (CMAQ) Model Outputs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "7FEBA753-FD29-4DE3-860C-61B0A30D2D51",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Barrett Parker, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:parker.barrett@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Monitoring Knowledge Base (MKB) is a compilation of emissions measurement and monitoring techniques associated with air pollution control devices, industrial process descriptions, and permitting techniques, including flexible permit development. Using MKB, one can gain a comprehensive understanding of emissions sources, control devices, and monitoring techniques, enabling one to determine appropriate permit terms and conditions.",
+            "identifier": "8930F377-1F90-43FD-BAC9-CA5C34BED34F",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -2170,41 +2178,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Monitoring Knowledge Base (MKB)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8930F377-1F90-43FD-BAC9-CA5C34BED34F%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8930F377-1F90-43FD-BAC9-CA5C34BED34F%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Monitoring Knowledge Base (MKB)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:parker.barrett@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Barrett Parker, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "8930F377-1F90-43FD-BAC9-CA5C34BED34F",
-            "@type": "dcat:Dataset"
+                "fn": "Tami Laplante, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Laplante.tami@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "OTS is an internal EPA national tribal database to assist the Regions and HQs in tracking tribal performance information.",
+            "identifier": "E994931F-1811-46D6-A41A-A55012108787",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -2225,41 +2233,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "OAR Tribal System",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE994931F-1811-46D6-A41A-A55012108787%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE994931F-1811-46D6-A41A-A55012108787%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "OAR Tribal System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Laplante.tami@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Tami Laplante, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "E994931F-1811-46D6-A41A-A55012108787",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "David Misenheimer, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:misenheimer.david@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The EPA Control Strategy Tool (CoST) is a software tool for projecting potential future control scenarios, their effects on emissions and estimated costs. This tool uses the NEI and the Control Measures Dataset as key inputs. CoST outputs are projections of future control scenarios.",
+            "identifier": "E3AEC827-D8B1-4D0C-AF4B-521AF1B4DF30",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -2277,41 +2285,41 @@
                 "united states",
                 "environment"
             ],
-            "title": "Control Strategy Tool (CoST)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE3AEC827-D8B1-4D0C-AF4B-521AF1B4DF30%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE3AEC827-D8B1-4D0C-AF4B-521AF1B4DF30%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Control Strategy Tool (CoST)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:misenheimer.david@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "David Misenheimer, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "N/A, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:aqsteam@epa.gov"
             },
-            "identifier": "E3AEC827-D8B1-4D0C-AF4B-521AF1B4DF30",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Historical Ambient Air Quality Data Inventory contains measured and estimated data on ambient air pollution for use in assessing air quality, assisting in designating attainment/non-attainment areas, evaluating state implementation plans for non-attainment areas, performing modeling for permit review analysis, and other air quality functionsThe statutory authority leading to the collection of this information comes from Title I, Part A of the  Clean Air Act. Sustance classes include Criteria Air Pollutants, Hazardous Air Pollutants, and Greenhouse Gases. Data no longer collected, current Ambient Air Quality Data Inventory uses higher geographic density and more robust methods of measurement.",
+            "identifier": "651B2300-A3FF-4DE6-AEE7-882751511C5C",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -2336,45 +2344,51 @@
                 "united states",
                 "environment"
             ],
-            "title": "Historical Ambient Air Quality Data Inventory",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B651B2300-A3FF-4DE6-AEE7-882751511C5C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B651B2300-A3FF-4DE6-AEE7-882751511C5C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Historical Ambient Air Quality Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:aqsteam@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "N/A, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "651B2300-A3FF-4DE6-AEE7-882751511C5C",
-            "@type": "dcat:Dataset"
+                "fn": "Phil Dickerson, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Dickerson.Phil@epa.gov"
             },
+            "dataQuality": false,
+            "description": "AirNow is a collaboration between EPA, and othe federal, state and local agencies to provide complete and real-time air quality information.",
+            "distribution": [
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.airnow.gov"
                 },
-            "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9B971C96-B2F3-4A5E-9E4B-D674E174A9F6%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B9B971C96-B2F3-4A5E-9E4B-D674E174A9F6%7D"
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
             ],
-            "accessLevel": "public",
-            "description": "AirNow is a collaboration between EPA, and othe federal, state and local agencies to provide complete and real-time air quality information.",
+            "identifier": "9B971C96-B2F3-4A5E-9E4B-D674E174A9F6",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -2385,52 +2399,52 @@
                 "united states",
                 "environment"
             ],
-            "title": "AirNow",
+            "landingPage": "https://www.airnow.gov",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.airnow.gov",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.airnow.gov",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:Dickerson.Phil@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Phil Dickerson, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "9B971C96-B2F3-4A5E-9E4B-D674E174A9F6",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7B91D36CE9-2321-4EED-B812-AD70A7D7691E%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B91D36CE9-2321-4EED-B812-AD70A7D7691E%7D"
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9B971C96-B2F3-4A5E-9E4B-D674E174A9F6%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B9B971C96-B2F3-4A5E-9E4B-D674E174A9F6%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "AirNow"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert Coats, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Coats.Robert@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The AQS Data Mart is a database that contains all of the information from the AQS system.  It is a storehouse of air quality information that allows users to make queries of unlimited quantities of data.  The Data Mart also includes information from the EPA?s substance and facility registry systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "91D36CE9-2321-4EED-B812-AD70A7D7691E",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "air",
@@ -2443,51 +2457,51 @@
                 "united states",
                 "environment"
             ],
-            "title": "AQS Data Mart",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:Coats.Robert@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Robert Coats, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "91D36CE9-2321-4EED-B812-AD70A7D7691E",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9A27C77A-495A-4E82-B4B9-BDA6F63F9E59%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B9A27C77A-495A-4E82-B4B9-BDA6F63F9E59%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7B91D36CE9-2321-4EED-B812-AD70A7D7691E%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B91D36CE9-2321-4EED-B812-AD70A7D7691E%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "AQS Data Mart"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "dataQuality": false,
             "description": "A REST web service API allowing the retrieval of historical air quality data from EPA.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://aqs.epa.gov/aqsweb/documents/data_api.html"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "9A27C77A-495A-4E82-B4B9-BDA6F63F9E59",
+            "issued": "2014-01-01",
             "keyword": [
                 "air quality",
                 "air pollution",
@@ -2506,73 +2520,53 @@
                 "united states",
                 "environment"
             ],
-            "title": "AirData AQS REST API",
+            "landingPage": "https://www.epa.gov/outdoor-air-quality-data#DMCSV_Format",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://aqs.epa.gov/aqsweb/documents/data_api.html",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.epa.gov/outdoor-air-quality-data#DMCSV_Format",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "9A27C77A-495A-4E82-B4B9-BDA6F63F9E59",
-            "@type": "dcat:Dataset"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
-        {
-            "issued": "2014-01-01",
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7B99AC1621-37DA-4F09-BE81-36262B29BDFF%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B99AC1621-37DA-4F09-BE81-36262B29BDFF%7D"
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9A27C77A-495A-4E82-B4B9-BDA6F63F9E59%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B9A27C77A-495A-4E82-B4B9-BDA6F63F9E59%7D"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "landingPage": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
-            "title": "KMZ files of EPA Ambient Monitors",
-            "temporal": "1990-01/2009-12",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:094"
-            ],
-            "describedBy": "https://www.epa.gov/outdoor-air-quality-data",
-            "description": "KMZ files with the location of all the EPA ambient monitors with the ability to download data from within the description box.",
+            "title": "AirData AQS REST API"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1H",
             "bureauCode": [
                 "020:00"
             ],
             "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            "dataQuality": false,
+            "describedBy": "https://www.epa.gov/outdoor-air-quality-data",
+            "description": "KMZ files with the location of all the EPA ambient monitors with the ability to download data from within the description box.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors"
                 },
-            "language": [
-                "en-US"
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "KML/KMZ"
+                }
             ],
+            "identifier": "99AC1621-37DA-4F09-BE81-36262B29BDFF",
+            "issued": "2014-01-01",
             "keyword": [
                 "criteria pollutants",
                 "air pollution map",
@@ -2594,33 +2588,54 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "accrualPeriodicity": "R/PT1H",
-            "dataQuality": false,
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "KML/KMZ"
-                }
+            "programCode": [
+                "020:094"
             ],
-            "identifier": "99AC1621-37DA-4F09-BE81-36262B29BDFF",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7B15B86480-7A2D-4FBD-9258-090DA358C4F0%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B15B86480-7A2D-4FBD-9258-090DA358C4F0%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7B99AC1621-37DA-4F09-BE81-36262B29BDFF%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B99AC1621-37DA-4F09-BE81-36262B29BDFF%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "temporal": "1990-01/2009-12",
+            "title": "KMZ files of EPA Ambient Monitors"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "https://www.epa.gov/aqs/obtaining-aqs-data",
             "description": "Ambient concentrations of most requested pollutants from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/aqs/obtaining-aqs-data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "15B86480-7A2D-4FBD-9258-090DA358C4F0",
+            "issued": "2014-01-01",
             "keyword": [
                 "air quality",
                 "air pollution",
@@ -2639,53 +2654,52 @@
                 "united states",
                 "environment"
             ],
-            "title": "Web page with Air Quality System (AQS) ambient observation files",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/aqs/obtaining-aqs-data",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "temporal": "1993-01/2009-12",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "describedBy": "https://www.epa.gov/aqs/obtaining-aqs-data",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "R/P1W",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "15B86480-7A2D-4FBD-9258-090DA358C4F0",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB1AB2E31-0835-4C09-9582-38F099C58652%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7BB1AB2E31-0835-4C09-9582-38F099C58652%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7B15B86480-7A2D-4FBD-9258-090DA358C4F0%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B15B86480-7A2D-4FBD-9258-090DA358C4F0%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "temporal": "1993-01/2009-12",
+            "title": "Web page with Air Quality System (AQS) ambient observation files"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "dataQuality": false,
             "description": "A web page that describes and links to EPA systems for accessing and downloading ambient (outdoor) air quality and emissions data",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "B1AB2E31-0835-4C09-9582-38F099C58652",
+            "issued": "2014-01-01",
             "keyword": [
                 "environment",
                 "federal data download",
@@ -2702,52 +2716,53 @@
                 "united states",
                 "environment"
             ],
-            "title": "Web page with links to air quality and emissions data",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/outdoor-air-quality-data",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/html"
-                }
-            ],
-            "temporal": "1990-01/2014-12",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "B1AB2E31-0835-4C09-9582-38F099C58652",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7B200F2DBC-25F2-4F01-A1A9-B50DC1356220%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B200F2DBC-25F2-4F01-A1A9-B50DC1356220%7D"
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB1AB2E31-0835-4C09-9582-38F099C58652%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7BB1AB2E31-0835-4C09-9582-38F099C58652%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "temporal": "1990-01/2014-12",
+            "title": "Web page with links to air quality and emissions data"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.airnowtech.org/Resources/AIRNow-I_AQCSV-Final.pdf",
             "description": "A REST web service API allowing the retrieval of real time air quality index data from AirNow.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://docs.airnowapi.org/"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "200F2DBC-25F2-4F01-A1A9-B50DC1356220",
+            "issued": "2014-01-01",
             "keyword": [
                 "air quality",
                 "real time",
@@ -2774,53 +2789,52 @@
                 "united states",
                 "environment"
             ],
-            "title": "AirNow Real Time Air Quality REST API",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://docs.airnowapi.org/",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "temporal": "1999-01/2014-12",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "describedBy": "http://www.airnowtech.org/Resources/AIRNow-I_AQCSV-Final.pdf",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "R/P1D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Nick Mangus,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "200F2DBC-25F2-4F01-A1A9-B50DC1356220",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/rest/document?id=%7BE87A4099-3793-47D7-A687-969577FFE4F4%7D",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE87A4099-3793-47D7-A687-969577FFE4F4%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7B200F2DBC-25F2-4F01-A1A9-B50DC1356220%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B200F2DBC-25F2-4F01-A1A9-B50DC1356220%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "temporal": "1999-01/2014-12",
+            "title": "AirNow Real Time Air Quality REST API"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Steve Young,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:young.steve@epa.gov"
+            },
+            "dataQuality": false,
             "description": "FuelEconomy.gov provides comprehensive information about vehicles' fuel economy. The official U.S. government site for fuel economy information, it is operated by the Department of Energy and the Environmental Protection Agency. The site provides access to general information, widgets to help car buyers, and fuel economy datasets.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.fueleconomy.gov/"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "E87A4099-3793-47D7-A687-969577FFE4F4",
+            "issued": "2014-01-01",
             "keyword": [
                 "vehicle",
                 "auto",
@@ -2858,53 +2872,53 @@
                 "united states",
                 "environment"
             ],
-            "title": "www.FuelEconomy.gov",
+            "landingPage": "https://www.fueleconomy.gov",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.fueleconomy.gov/",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
-            ],
-            "temporal": "1978-01/2012-12",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.fueleconomy.gov",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:young.steve@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Steve Young,Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "E87A4099-3793-47D7-A687-969577FFE4F4",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B39529785-E7E6-4C46-BE1A-FF37C4D099AA%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B39529785-E7E6-4C46-BE1A-FF37C4D099AA%7D"
+                "https://edg.epa.gov/metadata/rest/document?id=%7BE87A4099-3793-47D7-A687-969577FFE4F4%7D",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE87A4099-3793-47D7-A687-969577FFE4F4%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "temporal": "1978-01/2012-12",
+            "title": "www.FuelEconomy.gov"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert Coats, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:Coats.Robert@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Air Quality System (AQS) database contains measurements of air pollutant concentrations from throughout the United States and its territories. The measurements include both criteria air pollutants and hazardous air pollutants.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/aqs"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "39529785-E7E6-4C46-BE1A-FF37C4D099AA",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -2915,48 +2929,42 @@
                 "united states",
                 "environment"
             ],
-            "title": "Air Quality System (AQS)",
+            "landingPage": "https://www.epa.gov/aqs",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/aqs",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/zip"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://www.epa.gov/aqs",
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:094"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "contactPoint": {
-                "hasEmail": "mailto:Coats.Robert@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Robert Coats, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "39529785-E7E6-4C46-BE1A-FF37C4D099AA",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B39529785-E7E6-4C46-BE1A-FF37C4D099AA%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B39529785-E7E6-4C46-BE1A-FF37C4D099AA%7D"
+            ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Air Quality System (AQS)"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nick Mangus, U.S. EPA Office of Environmental Information (OEI)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "dataQuality": false,
             "description": "A KMZ file with the location of all major facilities that emit pollutants into the atmopshere.",
+            "identifier": "{1799AA6B-66D0-48FD-A380-202D4BEFBB3C}",
+            "issued": "2014-01-01",
             "keyword": [
                 "public health",
                 "environment",
@@ -2972,119 +2980,143 @@
                 "united states",
                 "environment"
             ],
-            "title": "Air Emissions Where You Live KMZ File",
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D",
-            "bureauCode": [
-                "020:00"
-            ],
-            "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D"
-            ],
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,18.0,-66.0,72.0",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Nick Mangus, U.S. EPA Office of Environmental Information (OEI)"
-            },
-            "identifier": "{1799AA6B-66D0-48FD-A380-202D4BEFBB3C}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
             "references": [
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAEFCFBEE-358E-4C8B-8812-868339FC9E91%7D",
-                "https://edg.epa.gov/metadata/rest/document?id=%7BAEFCFBEE-358E-4C8B-8812-868339FC9E91%7D"
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7B1799AA6B-66D0-48FD-A380-202D4BEFBB3C%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Air Emissions Where You Live KMZ File"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "description": "Ambient PM2.5 (particulate matter less than 2.5 microns) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
-            "keyword": [
-                "EPA",
-                "environment"
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "title": "Air Quality System (AQS) ambient observations: 2007 PM2.5",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mangus.nick@epa.gov"
+            },
+            "description": "Ambient PM2.5 (particulate matter less than 2.5 microns) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
             "distribution": [
                 {
-                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "mediaType": "application/zip"
                 }
             ],
-            "modified": "2015-09-23",
+            "identifier": "{AEFCFBEE-358E-4C8B-8812-868339FC9E91}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:mangus.nick@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "{AEFCFBEE-358E-4C8B-8812-868339FC9E91}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
             },
+            "references": [
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAEFCFBEE-358E-4C8B-8812-868339FC9E91%7D",
+                "https://edg.epa.gov/metadata/rest/document?id=%7BAEFCFBEE-358E-4C8B-8812-868339FC9E91%7D"
+            ],
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "Air Quality System (AQS) ambient observations: 2007 PM2.5"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Marc Houyoux",
+                "hasEmail": "mailto:houyoux.marc@epa.gov"
+            },
             "description": "The National Emission Inventory contains measured, modeled, and estimated data for emissions of all known source categories in the US (stationary sources, fires, light duty vehicles and trucks, Heavy duty engines, Motorcycles, ATVs, non-road engines and equipment, locomotives, aircraft, and marine vessels). The statutory authority leading to the collection of this information comes from Title II, Part A of the Clean Air Act.Substance classes include CAPs, HAPs, and some GHG data.Data included in the National Emission Inventory is collected annually, Air Pollutant Trends Data is made available annually, and an National Emissions Inventory of air emissions of both Criteria and Hazardous air pollutants from all air emissions sources is prepared every three years.",
+            "identifier": "{1F3A34AC-1EA3-4E93-95EC-375E559C31A7}",
+            "issued": "2014-01-01",
             "keyword": [
                 "EPA",
                 "environment"
             ],
-            "title": "National Emission Inventory",
-            "issued": "2014-01-01",
-            "modified": "2015-09-23",
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1F3A34AC-1EA3-4E93-95EC-375E559C31A7%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1F3A34AC-1EA3-4E93-95EC-375E559C31A7%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,-90.0,180.0,90.0",
-            "programCode": [
-                "020:072"
+            "title": "National Emission Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:houyoux.marc@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Marc Houyoux"
-            },
-            "identifier": "{1F3A34AC-1EA3-4E93-95EC-375E559C31A7}",
-            "@type": "dcat:Dataset"
+                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS).",
+                "hasEmail": "mailto:mintz.david@epa.gov"
             },
+            "description": "Ambient ozone concentrations for 2008 from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
+            "distribution": [
                 {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "{76724EFD-A302-4774-A318-A72EB6757037}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
@@ -3093,43 +3125,42 @@
                 "https://edg.epa.gov/metadata/rest/document?id=%7B76724EFD-A302-4774-A318-A72EB6757037%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B76724EFD-A302-4774-A318-A72EB6757037%7D"
             ],
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "Air Quality System (AQS) ambient observations: 2008 ozone"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "description": "Ambient ozone concentrations for 2008 from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
-            "keyword": [
-                "EPA",
-                "environment"
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "title": "Air Quality System (AQS) ambient observations: 2008 ozone",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Joe Steigerwald",
+                "hasEmail": "mailto:Steigerwald.joe@epa.gov"
+            },
+            "description": "OAR's RACT, BACT, LAER Clearinghouse (RBLC) data asset contains summary information on selected air permitting actions from EPA, state, and local permitting agencies across the U.S., as well as a number of international permit records supplied by air pollution control agencies in Mexico and Canada. The acronyms refer to program requirements of the New Source Review (NSR) program: RACT is Reasonably Available Control Technology and applies to existing sources in areas that are not meeting national ambient air quality standards (i.e., non-attainment areas); BACT is Best Available Control Technology and applies to major new or modified sources in clean areas (i.e., attainment areas). LAER, or Lowest Achievable Emission Rate, is required on major new or modified sources in non-attainment areas. As of 2012, RBLC includes approximately 6,500 entries. With the exception of LAER permit determinations, whose inclusion in RBLC is mandatory, participation is voluntary. Coverage is therefore not complete or necessarily representative.Required under Section 108 of the 1990 Amendments to the Clean Air Act, RBLC provides users \u00e2?? typically permit writers, permit applicants or holders, and the public \u00e2?? with references and personal contacts to support ongoing air pollution control activities. Information is detailed enough for users to know whether a permit is applicable to their needs. Users may then contact the appropriate agency to access the permit or discuss it with agency staff.RBLC-referenced permits cover Criteria Air Pollutants (CAPs) and Hazardous Air Pollutants (HAPs), but the data is also searchable for Greenhouse Gas (GHG) references. Entries are generally provided by the original permitting agency, though EPA Regional Offices may enter data on behalf of state and local agencies to augment coverage. Since 2009, Canadian and Mexican agencies have had access to the RBLC to submit their own permit information; all data is provided in English.There are three main levels of information \u00e2?? Facility, Process, and Pollutant. Facility Data includes but is not limited to: Facility Name, City/Town, State, Permitting Agency, Permit Date, NAICS, SIC, Facility Registry System Number, Permit Number, and Agency Contact Name & Phone Number. Process Data includes but is not limited to: Process Name, Process Type Code, and Throughput. Pollutant Data includes but is not limited to: Pollutant Name, CAS#, Emissions Testing Method(s), Emission Limits, Case-by-Case Basis and any Other Applicable Requirements; and Control Method Description. U.S. geographic coverage includes all states and territories, plus all U.S. permitted facilities within U.S. waters (generally 3 miles for state limits, but further offshore for DOI-permitted oil platforms). Coverage began in 1980, but some historical permits from the 1970s are included. Over the years the data has been converted from paper to searchable digital form. Data is not overwritten, so multiple historical permit references for a single facility may be included. OAQPS manually cross-references RBLC references to the appropriate Facility Registry System (FRS) ID to the extent possible. All RBLC content is public and non-sensitive and available through EPA.gov after it has been quality assured. Data is quality assured by EPA and entered into the RACT, BACT, LAER Clearinghouse (RBLC) data management system (https://cfpub.epa.gov/rblc/index.cfm?action=Home.Home). Where technical summaries appear inaccurate, OAQPS returns entries for review to their originators. All data is edited and approved by the Office of Air and Radiation\u00e2??s Office of Air Quality Permits and Standards (OAQPS) prior to publication.",
             "distribution": [
                 {
-                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip"
+                    "accessURL": "https://cfpub.epa.gov/rblc/index.cfm?action=Search.BasicSearch&lang=en"
                 }
             ],
-            "modified": "2015-09-23",
+            "identifier": "{76189EF6-FB4F-4292-8970-9AB534088D93}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)."
-            },
-            "identifier": "{76724EFD-A302-4774-A318-A72EB6757037}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
@@ -3138,42 +3169,43 @@
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B76189EF6-FB4F-4292-8970-9AB534088D93%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B76189EF6-FB4F-4292-8970-9AB534088D93%7D"
             ],
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "RACT/BACT/LAER Clearninghouse (RBLC)"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "description": "OAR's RACT, BACT, LAER Clearinghouse (RBLC) data asset contains summary information on selected air permitting actions from EPA, state, and local permitting agencies across the U.S., as well as a number of international permit records supplied by air pollution control agencies in Mexico and Canada. The acronyms refer to program requirements of the New Source Review (NSR) program: RACT is Reasonably Available Control Technology and applies to existing sources in areas that are not meeting national ambient air quality standards (i.e., non-attainment areas); BACT is Best Available Control Technology and applies to major new or modified sources in clean areas (i.e., attainment areas). LAER, or Lowest Achievable Emission Rate, is required on major new or modified sources in non-attainment areas. As of 2012, RBLC includes approximately 6,500 entries. With the exception of LAER permit determinations, whose inclusion in RBLC is mandatory, participation is voluntary. Coverage is therefore not complete or necessarily representative.Required under Section 108 of the 1990 Amendments to the Clean Air Act, RBLC provides users \u00e2?? typically permit writers, permit applicants or holders, and the public \u00e2?? with references and personal contacts to support ongoing air pollution control activities. Information is detailed enough for users to know whether a permit is applicable to their needs. Users may then contact the appropriate agency to access the permit or discuss it with agency staff.RBLC-referenced permits cover Criteria Air Pollutants (CAPs) and Hazardous Air Pollutants (HAPs), but the data is also searchable for Greenhouse Gas (GHG) references. Entries are generally provided by the original permitting agency, though EPA Regional Offices may enter data on behalf of state and local agencies to augment coverage. Since 2009, Canadian and Mexican agencies have had access to the RBLC to submit their own permit information; all data is provided in English.There are three main levels of information \u00e2?? Facility, Process, and Pollutant. Facility Data includes but is not limited to: Facility Name, City/Town, State, Permitting Agency, Permit Date, NAICS, SIC, Facility Registry System Number, Permit Number, and Agency Contact Name & Phone Number. Process Data includes but is not limited to: Process Name, Process Type Code, and Throughput. Pollutant Data includes but is not limited to: Pollutant Name, CAS#, Emissions Testing Method(s), Emission Limits, Case-by-Case Basis and any Other Applicable Requirements; and Control Method Description. U.S. geographic coverage includes all states and territories, plus all U.S. permitted facilities within U.S. waters (generally 3 miles for state limits, but further offshore for DOI-permitted oil platforms). Coverage began in 1980, but some historical permits from the 1970s are included. Over the years the data has been converted from paper to searchable digital form. Data is not overwritten, so multiple historical permit references for a single facility may be included. OAQPS manually cross-references RBLC references to the appropriate Facility Registry System (FRS) ID to the extent possible. All RBLC content is public and non-sensitive and available through EPA.gov after it has been quality assured. Data is quality assured by EPA and entered into the RACT, BACT, LAER Clearinghouse (RBLC) data management system (https://cfpub.epa.gov/rblc/index.cfm?action=Home.Home). Where technical summaries appear inaccurate, OAQPS returns entries for review to their originators. All data is edited and approved by the Office of Air and Radiation\u00e2??s Office of Air Quality Permits and Standards (OAQPS) prior to publication.",
-            "keyword": [
-                "EPA",
-                "environment"
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "title": "RACT/BACT/LAER Clearninghouse (RBLC)",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS).",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "description": "Ambient PM2.5 (particulate matter less than 2.5 microns) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
             "distribution": [
                 {
-                    "accessURL": "https://cfpub.epa.gov/rblc/index.cfm?action=Search.BasicSearch&lang=en",
-                    "@type": "dcat:Distribution"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
+                    "mediaType": "application/zip"
                 }
             ],
-            "modified": "2015-09-23",
+            "identifier": "{214A6E5B-107C-4B0D-9A63-C1858DBEF89B}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:Steigerwald.joe@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Joe Steigerwald"
-            },
-            "identifier": "{76189EF6-FB4F-4292-8970-9AB534088D93}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
@@ -3182,43 +3214,43 @@
                 "https://edg.epa.gov/metadata/rest/document?id=%7B214A6E5B-107C-4B0D-9A63-C1858DBEF89B%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B214A6E5B-107C-4B0D-9A63-C1858DBEF89B%7D"
             ],
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "Air Quality System (AQS) ambient observations: 2008 PM2.5"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "description": "Ambient PM2.5 (particulate matter less than 2.5 microns) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
-            "keyword": [
-                "EPA",
-                "environment"
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "title": "Air Quality System (AQS) ambient observations: 2008 PM2.5",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "description": "Ambient Lead (Pb) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
             "distribution": [
                 {
-                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "mediaType": "application/zip"
                 }
             ],
-            "modified": "2015-09-23",
+            "identifier": "{623F90EA-03C6-4E3A-91E8-9325A617D975}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)."
-            },
-            "identifier": "{214A6E5B-107C-4B0D-9A63-C1858DBEF89B}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
@@ -3227,43 +3259,43 @@
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B623F90EA-03C6-4E3A-91E8-9325A617D975%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B623F90EA-03C6-4E3A-91E8-9325A617D975%7D"
             ],
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "Air Quality System (AQS) ambient observations: 2008 Lead"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "description": "Ambient Lead (Pb) concentrations from the national ambient air quality monitoring networks stored in the Air Quality System (AQS).",
-            "keyword": [
-                "EPA",
-                "environment"
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "title": "Air Quality System (AQS) ambient observations: 2008 Lead",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)",
+                "hasEmail": "mailto:mintz.david@epa.gov"
+            },
+            "description": "A KMZ file with the location of all the EPA ambient ozone monitors with the ability to download data from within the description box.",
             "distribution": [
                 {
-                    "downloadURL": "https://aqs.epa.gov/aqsweb/airdata/download_files.html",
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
                     "mediaType": "application/zip"
                 }
             ],
-            "modified": "2015-09-23",
+            "identifier": "{CA3D3368-EF91-422D-B647-6CCF87FABF10}",
+            "issued": "2014-01-01",
+            "keyword": [
+                "EPA",
+                "environment"
+            ],
             "language": [
                 "en-US"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2015-09-23",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "David Mintz, Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
-            },
-            "identifier": "{623F90EA-03C6-4E3A-91E8-9325A617D975}",
-            "@type": "dcat:Dataset"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
@@ -3272,49 +3304,32 @@
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCA3D3368-EF91-422D-B647-6CCF87FABF10%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BCA3D3368-EF91-422D-B647-6CCF87FABF10%7D"
             ],
-            "accessLevel": "public",
-            "description": "A KMZ file with the location of all the EPA ambient ozone monitors with the ability to download data from within the description box.",
-            "keyword": [
-                "EPA",
-                "environment"
-            ],
-            "title": "KMZ file of EPA Ambient Ozone Monitors",
-            "distribution": [
+            "spatial": "-180.0,-90.0,180.0,90.0",
+            "title": "KMZ file of EPA Ambient Ozone Monitors"
+        },
         {
-                    "downloadURL": "https://www.epa.gov/outdoor-air-quality-data/interactive-map-air-quality-monitors",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "modified": "2015-09-23",
-            "language": [
-                "en-US"
-            ],
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "020:00"
             ],
-            "issued": "2014-01-01",
-            "accrualPeriodicity": "irregular",
-            "spatial": "-180.0,-90.0,180.0,90.0",
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:mintz.david@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "David Mintz, U.S. EPA Office of Air and Radiation (OAR) - Office of Air Quality Planning and Standards (OAQPS)"
+                "fn": "Roy LaPorte,US Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:laporte.roy@epa.gov"
             },
-            "identifier": "{CA3D3368-EF91-422D-B647-6CCF87FABF10}",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "RadNet-Air is a national network of air monitoring stations that regularly collect air samples for near real time analysis of radioactivity. The data is transmitted to NAREL in Montgomery Alabama. The RadNet-Air network has been used to track environmental releases resulting from nuclear emergencies and to provide baseline data during routine conditions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "27663CF9-C37A-40A9-9955-B34DC55F4269",
+            "issued": "2014-01-01",
             "keyword": [
                 "radnet",
                 "radiation",
@@ -3324,45 +3339,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet-Air Near Real Time Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B27663CF9-C37A-40A9-9955-B34DC55F4269%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B27663CF9-C37A-40A9-9955-B34DC55F4269%7D"
             ],
-            "accrualPeriodicity": "R/P1D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet-Air Near Real Time Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:laporte.roy@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Roy LaPorte,US Environmental Protection Agency, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "27663CF9-C37A-40A9-9955-B34DC55F4269",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Quality Data Asset includes all current and historical data on environmental quality with regard to the presence of radiological contamination of all kinds regulated by UMTRA, CERCLA, AEA, CWA, CAA.",
+            "identifier": "5AF9331B-5896-4616-B66B-57E63BEB7372",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3389,38 +3397,57 @@
                 "united states",
                 "environment"
             ],
-            "title": "Environmental Sampling, Monitoring and Site Assessment Data",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-02",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5AF9331B-5896-4616-B66B-57E63BEB7372%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B5AF9331B-5896-4616-B66B-57E63BEB7372%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Environmental Sampling, Monitoring and Site Assessment Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Griggs.john@Epa.gov"
             },
-            "identifier": "5AF9331B-5896-4616-B66B-57E63BEB7372",
-            "@type": "dcat:Dataset"
+            "dataQuality": false,
+            "description": "This RadNet Air Quality Data Asset includes all historical data (prior to 2005, when ERAMS was expanded to become RadNet, name changed to reflect new mission)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://archive.epa.gov/epa/radnet/historical-radiological-event-monitoring.html",
+                    "format": "HyperText Markup Language (HTML) (.html)",
+                    "mediaType": "text/html",
+                    "title": "Historical Radiological Event Monitoring"
                 },
                 {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/chernobyl-epas-radiological-monitoring",
+                    "title": "Chernobyl: EPA's Radiological Monitoring"
                 },
-            "accessLevel": "public",
-            "description": "This RadNet Air Quality Data Asset includes all historical data (prior to 2005, when ERAMS was expanded to become RadNet, name changed to reflect new mission)",
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/fukushima-epas-radiological-monitoring",
+                    "title": "Fukushima: EPA's Radiological Monitoring"
+                }
+            ],
+            "identifier": "2CB3C263-8F42-406E-A0D0-265ECED680E8",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3438,57 +3465,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Historical RadNet Air Quality Data",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://archive.epa.gov/epa/radnet/historical-radiological-event-monitoring.html",
-                    "format": "HyperText Markup Language (HTML) (.html)",
-                    "title": "Historical Radiological Event Monitoring",
-                    "mediaType": "text/html"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/radnet/chernobyl-epas-radiological-monitoring",
-                    "title": "Chernobyl: EPA's Radiological Monitoring"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/radnet/fukushima-epas-radiological-monitoring",
-                    "title": "Fukushima: EPA's Radiological Monitoring"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-03",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2CB3C263-8F42-406E-A0D0-265ECED680E8%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2CB3C263-8F42-406E-A0D0-265ECED680E8%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Historical RadNet Air Quality Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Griggs.john@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "2CB3C263-8F42-406E-A0D0-265ECED680E8",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Griggs.john@Epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The National Radiological Fixed Laboratory Data Asset includes data produced in support of various clients such as other EPA offices, EPA Regional programs, DOE, DOD, state agencies, and tribal support as well as support to other countries when requested. Analytical data for these clients range from support for entire projects to providing QA support only. A wide range of radiochemical and hazardous chemical analyses are performed on a variety of media. Data produced at NAREL are held to strict quality assurance standards and include all supporting documentation for complete data validation.",
+            "identifier": "11D7A1DC-F975-4F88-B67A-C20168536FB1",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3505,38 +3513,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "National Radiological Fixed Lab Data",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-04",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B11D7A1DC-F975-4F88-B67A-C20168536FB1%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B11D7A1DC-F975-4F88-B67A-C20168536FB1%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "National Radiological Fixed Lab Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Griggs.john@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "11D7A1DC-F975-4F88-B67A-C20168536FB1",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The RadNet Real-Time Monitoring Spectrometry Data Inventory contains measured data used to identify and measure specific radioactive materials in the atmosphere at locations across the United States. This data is only collected from the monitors based on a triggered response requirement.The statutory authority leading to the collection of this information comes from Title I Section XII of the Clean Air Act and Title I Chapter XIV of the Atomic Energy Act.Substance classes include Radionuclides and HAPs.Hourly measured data that shows an abnormality is manually downloaded from the monitor the next business day.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "ADEE4B24-5A16-41D6-A655-83401B95AF63",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3556,45 +3571,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet Real-Time Monitoring Spectrometry Data Inventory",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-05",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BADEE4B24-5A16-41D6-A655-83401B95AF63%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BADEE4B24-5A16-41D6-A655-83401B95AF63%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet Real-Time Monitoring Spectrometry Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "ADEE4B24-5A16-41D6-A655-83401B95AF63",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Tom Peake, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Peake.Tom@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "A GIS compiled locational database in Microsoft Access of ~15,000 mines with uranium occurrence or production, primarily in the western United States. The metadata was cooperatively compiled from Federal and State agency data sets and enables the user to conduct geographic and analytical studies on mine impacts on the public and environment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radiation/uranium-mines-and-mills-location-database-0",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "2E4A8313-B6C8-4638-B683-7F8445101725",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3615,45 +3630,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Uranium Location Database",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radiation/uranium-mines-and-mills-location-database-0",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-06",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2E4A8313-B6C8-4638-B683-7F8445101725%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2E4A8313-B6C8-4638-B683-7F8445101725%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Uranium Location Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Peake.Tom@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Tom Peake, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Charles Petko, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:petko.charles@epa.gov"
             },
-            "identifier": "2E4A8313-B6C8-4638-B683-7F8445101725",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Environmental Radiation Data (ERD) is an electronic and print journal compiled and distributed quarterly by the Office of Radiation and Indoor Air's National Air and Radiation Environmental Laboratory (NAREL) in Montgomery, Alabama. It contains data from RadNet (previously known as ERAMS.)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "86A31344-65B1-4BE8-8A9D-A57532F879EA",
+            "issued": "2014-01-01",
             "keyword": [
                 "erams",
                 "radnet",
@@ -3667,45 +3682,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Environmental Radiation Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-07",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B86A31344-65B1-4BE8-8A9D-A57532F879EA%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B86A31344-65B1-4BE8-8A9D-A57532F879EA%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Environmental Radiation Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:petko.charles@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Charles Petko, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "86A31344-65B1-4BE8-8A9D-A57532F879EA",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Sara DeCair, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:decair.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "RadNet is a national network of monitoring stations that regularly collect air, precipitation, drinking water, and milk samples for analysis of radioactivity. The RadNet network, which has stations in each state, has been used to track environmental releases of radioactivity from nuclear weapons tests and nuclear accidents.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "9B282057-4B89-4A1B-AC84-B47930ACF7D2",
+            "issued": "2014-01-01",
             "keyword": [
                 "nuclear",
                 "accidents",
@@ -3737,45 +3752,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet Map Interface for Near-Real-Time Radiation Monitoring Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/near-real-time-and-laboratory-data-state",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-08",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9B282057-4B89-4A1B-AC84-B47930ACF7D2%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9B282057-4B89-4A1B-AC84-B47930ACF7D2%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet Map Interface for Near-Real-Time Radiation Monitoring Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:decair.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara DeCair, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "9B282057-4B89-4A1B-AC84-B47930ACF7D2",
-            "@type": "dcat:Dataset"
+                "fn": "Andrea Cherepy, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Cherepy.andrea@Epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "An Excel database on NRC and Agreement State licensed mills providing status, locational/operational/restoration data, maps, and environmental reports including groundwater and air monitoring information. Developed for support of proposed regulatory revisions supporting UMTRCA and CAA-NESHAPs.",
+            "identifier": "AD8FEC1A-229E-4E23-8084-8B22A407CE45",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3792,38 +3800,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Uranium Mill and ISL Facility Database",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-09",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAD8FEC1A-229E-4E23-8084-8B22A407CE45%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BAD8FEC1A-229E-4E23-8084-8B22A407CE45%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Uranium Mill and ISL Facility Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Cherepy.andrea@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Andrea Cherepy, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "AD8FEC1A-229E-4E23-8084-8B22A407CE45",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Charles Petko, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:petko.charles@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "RadNet, formerly Environmental Radiation Ambient Monitoring System (ERAMS), is a national network of monitoring stations that regularly collect air, precipitation, drinking water, and milk samples for analysis of radioactivity. The RadNet network has been used to track environmental releases resulting from nuclear emergencies and to provide baseline data during routine conditions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "1AE7E64C-4FF1-4CD1-9A0A-57BC454F3A53",
+            "issued": "2014-01-01",
             "keyword": [
                 "erams",
                 "radnet",
@@ -3834,45 +3849,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet (Environmental Radiation Ambient Monitoring System)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-10",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1AE7E64C-4FF1-4CD1-9A0A-57BC454F3A53%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1AE7E64C-4FF1-4CD1-9A0A-57BC454F3A53%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet (Environmental Radiation Ambient Monitoring System)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:petko.charles@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Charles Petko, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "1AE7E64C-4FF1-4CD1-9A0A-57BC454F3A53",
-            "@type": "dcat:Dataset"
+                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Griggs.john@Epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This RadNet Quality Data Asset includes all data since initiation and when ERAMS was expanded to become RadNet, name changed to reflect new mission. This includes the milk, soil, air and water components.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "A94940B9-0CAA-4E0D-923A-49C073792B85",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3890,45 +3905,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Long Term RadNet Quality Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-11",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA94940B9-0CAA-4E0D-923A-49C073792B85%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BA94940B9-0CAA-4E0D-923A-49C073792B85%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Long Term RadNet Quality Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Griggs.john@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "John Griggs, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "A94940B9-0CAA-4E0D-923A-49C073792B85",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Gregg Dempsey, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Dempsey.gregg@Epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Quality Data Asset includes all current and historical emergency radiological response event and incident of national significance data and surveillance, monitoring, and assessment activities, protective action guidelines (PAGS) and environmental sampling and analysis results and other pertinent data to decision makers, modelers, emergency responders, and to the public.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radiation/radiological-emergency-response",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "B1FC8C48-BCE4-4F16-BE79-BF520EB23162",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -3950,45 +3965,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Radiological Emergency Response Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radiation/radiological-emergency-response",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-12",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BB1FC8C48-BCE4-4F16-BE79-BF520EB23162%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB1FC8C48-BCE4-4F16-BE79-BF520EB23162%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Radiological Emergency Response Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Dempsey.gregg@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Gregg Dempsey, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "B1FC8C48-BCE4-4F16-BE79-BF520EB23162",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Michael Messer, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:Messer.michael@Epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "USEPA/National-Based Assets includes current radiological emergency response monitoring and sampling Resource-Type I, II, and III Equipment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radiation/radiological-emergency-response",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "ccc8b51a-c000-11e7-abc4-cec278b6b50a",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4006,45 +4021,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Radiological Emergency Response Data (Equipment Data)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radiation/radiological-emergency-response",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-13",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7Bccc8b51a-c000-11e7-abc4-cec278b6b50a%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7Bccc8b51a-c000-11e7-abc4-cec278b6b50a%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Radiological Emergency Response Data (Equipment Data)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:Messer.michael@Epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Michael Messer, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "ccc8b51a-c000-11e7-abc4-cec278b6b50a",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "RadNet is a national network of monitoring stations that regularly collect air for analysis of radioactivity. The RadNet network, which has stations in each State, has been used to track environmental releases of radioactivity from nuclear weapons tests and nuclear accidents. RadNet also documents the status and trends of environmental radioactivity",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "2B36DCB7-DE2F-4D04-9F62-9A6CD7DDCAE8",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4062,45 +4077,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet Air Quality (Fixed Station) Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-14",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2B36DCB7-DE2F-4D04-9F62-9A6CD7DDCAE8%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2B36DCB7-DE2F-4D04-9F62-9A6CD7DDCAE8%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet Air Quality (Fixed Station) Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "2B36DCB7-DE2F-4D04-9F62-9A6CD7DDCAE8",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Quality Data Asset includes all current and historical data on the quality of water with regard to the presence of water pollutants of all kinds regulated by the Clean Water Act. Under the new Interagency Agreement with the Department of Energy (DOE), the Radiation & Indoor Environments National Laboratory (R&IE), Office of Radiation and Indoor Air (ORIA), EPA, located in Las Vegas, NV, conducts a Long-Term Hydrological Monitoring Program (LTHMP) providing laboratory sampling/analysis and Quality Assurance and Control to measure radioactivity concentrations in the water sources near the sites of former underground nuclear explosions. The results of the LTHMP provide assurance that radioactive material from the tests have not migrated into water supplies.",
+            "identifier": "8B3B62F9-2221-4058-90C5-1C66B2DED831",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4121,38 +4129,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Long Term Hydrological (Radiological) Site Monitoring Data",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-15",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8B3B62F9-2221-4058-90C5-1C66B2DED831%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8B3B62F9-2221-4058-90C5-1C66B2DED831%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Long Term Hydrological (Radiological) Site Monitoring Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Unknown, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "8B3B62F9-2221-4058-90C5-1C66B2DED831",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:contactperson@example.org"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "RadNet Deployable Monitoring is designed to collect radiological and meteorological information and data asset needed to establish the impact of radiation levels on the environment. The RadNet Deployable System has been designed as a tool for radiological emergency response and can be used to support the current fixed stations of the EPA's RadNet monitoring network. It can also be used as a tool for monitoring areas associated with a real or perceived nuclear or radiological threat.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "8A4CE8A4-27AB-4E87-83AE-221C0B648167",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4170,48 +4185,44 @@
                 "united states",
                 "environment"
             ],
-            "title": "RadNet Air Quality (Deployable) Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/radnet/radnet-databases-and-reports",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-16",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8A4CE8A4-27AB-4E87-83AE-221C0B648167%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8A4CE8A4-27AB-4E87-83AE-221C0B648167%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "RadNet Air Quality (Deployable) Data"
+        },
+        {
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "contactPoint": {
-                "hasEmail": "mailto:contactperson@example.org",
                 "@type": "vcard:Contact",
-                "fn": "Scott Telofski, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
-            },
-            "identifier": "8A4CE8A4-27AB-4E87-83AE-221C0B648167",
-            "@type": "dcat:Dataset"
+                "fn": "BASE Workgroup, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
+                "hasEmail": "mailto:BASEworkgroup@epa.gov"
             },
-        {
-            "title": "Building Assessment Survey and Evaluation Data (BASE)",
+            "dataQuality": false,
+            "description": "The Building Assessment Survey and Evaluation (BASE) study was a five year study to characterize determinants of indoor air quality and occupant perceptions in representative public and commercial office buildings across the U.S.  This data source is the raw data from this study about the indoor air quality.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/indoor-air-quality-iaq/building-assessment-survey-and-evaluation-study",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/indoor-air-quality-iaq/building-assessment-survey-and-evaluation-study",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "The Building Assessment Survey and Evaluation (BASE) study was a five year study to characterize determinants of indoor air quality and occupant perceptions in representative public and commercial office buildings across the U.S.  This data source is the raw data from this study about the indoor air quality.",
+            "identifier": "59DB9733-B7C0-45BF-9C16-B3FF7E68E014",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -4224,41 +4235,45 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "BASE Workgroup, U.S. EPA Office of Air and Radiation (OAR) - Office of Radiation and Indoor Air (ORIA)",
-                "hasEmail": "mailto:BASEworkgroup@epa.gov"
-            },
-            "identifier": "59DB9733-B7C0-45BF-9C16-B3FF7E68E014",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B59DB9733-B7C0-45BF-9C16-B3FF7E68E014%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B59DB9733-B7C0-45BF-9C16-B3FF7E68E014%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Building Assessment Survey and Evaluation Data (BASE)"
         },
         {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:EPAFuelsPrograms@epa.gov"
+            },
+            "dataQuality": false,
             "description": "This asset provides identification data on renewable fuel producers, importers, laboratories, and facilities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/fuels-registration-reporting-and-compliance-help",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "DD124B14-9907-49ED-9CB0-9C218FC0FB14",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4273,45 +4288,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Fuels Program Registration",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/fuels-registration-reporting-and-compliance-help",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDD124B14-9907-49ED-9CB0-9C218FC0FB14%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BDD124B14-9907-49ED-9CB0-9C218FC0FB14%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Fuels Program Registration"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:EPAFuelsPrograms@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "General Support Line, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "DD124B14-9907-49ED-9CB0-9C218FC0FB14",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:zarmski.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Fuel Economy Label and CAFE Data asset contains measured summary fuel economy estimates and test data for light-duty vehicle manufacturers by model for certification as required under the Energy Policy and Conservation Act of 1975 (EPCA) and The Energy Independent Security Act of 2007 (EISA) to collect vehicle fuel economy estimates for the creation of Economy Labels and for the calculation of Corporate Average Fuel Economy (CAFE). Manufacturers submit data on an annual basis, or as needed to document vehicle model changes.The EPA performs targeted fuel economy confirmatory tests on approximately 15% of vehicles submitted for validation. Confirmatory data on vehicles is associated with its corresponding submission data to verify the accuracy of manufacturer submissions beyond standard business rules. Submitted data comes in XML format or as documents, with the majority of submissions being sent in XML, and includes descriptive information on the vehicle itself, fuel economy information, and the manufacturer's testing approach. This data may contain proprietary information (CBI) such as information on estimated sales or other data elements indicated by the submitter as confidential. CBI data is not publically available; however, within the EPA data can accessed under the restrictions of the Office of Transportation and Air Quality (OTAQ) CBI policy [RCS Link]. Datasets are segmented by vehicle model/manufacturer and/or year with corresponding fuel economy, test, and certification data. Data assets are stored in EPA's Verify system.Coverage began in 1974 with early records being primarily paper documents which did not go through the same level of validation as primarily digital submissions which started in 2008. Early data is available to the public digitally starting from 1978, but more complete digital certification data is available starting in 2008. Fuel economy submission data prior to 2006 was calculated using an older formula; however, mechanisms exist to make this data comparable to current results.Fuel Economy Label and CAFE Data submission documents with metadata, certificate and summary decision information is utilized and made publically available through the EPA/DOE's Fuel Economy Guide Website (https://www.fueleconomy.gov/) as well as EPA's Smartway Program Website (https://www.epa.gov/smartway/) and Green Vehicle Guide Website (http://ofmpub.epa.gov/greenvehicles/Index.do;jsessionid=3F4QPhhYDYJxv1L3YLYxqh6J2CwL0GkxSSJTl2xgMTYPBKYS00vw!788633877) after it has been quality assured. Where summary data appears inaccurate, OTAQ returns the entries for review to their originator.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.fueleconomy.gov/feg/download.shtml",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "76897A70-0033-452C-BE14-E4107326218F",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4336,45 +4351,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Fuel Economy Label and CAFE Data Inventory",
-            "distribution": [
-                {
-                    "accessURL": "https://www.fueleconomy.gov/feg/download.shtml",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B76897A70-0033-452C-BE14-E4107326218F%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B76897A70-0033-452C-BE14-E4107326218F%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Fuel Economy Label and CAFE Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:zarmski.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "76897A70-0033-452C-BE14-E4107326218F",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:zarmski.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Engine and Vehicle Compliance Certification and Fuel Economy Inventory contains measured emissions and fuel economy compliance information for all types of vehicles (mobile sources of air pollution) excluding snowmobile, marine (diesel), and heavy duty engines whichsummary data is updated on an annual basis. Data is collected by EPA to certify compliance with the applicable fuel economy provisions of the Clean Air Act, Energy Policy and Conservation Act (EPCA) and the Energy Independent Security Act (EISA) of 2007.",
+            "identifier": "87B45AEE-4314-4626-927F-A3C1993510AB",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4399,38 +4407,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Mobile Source Emissions Regulatory Compliance Data",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B87B45AEE-4314-4626-927F-A3C1993510AB%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B87B45AEE-4314-4626-927F-A3C1993510AB%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Mobile Source Emissions Regulatory Compliance Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:zarmski.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "87B45AEE-4314-4626-927F-A3C1993510AB",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:zarmski.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The EV-GHG Mobile Source Data asset contains measured mobile source GHG emissions summary compliance information on light-duty vehicles, by model, for certification as required by the 1990 Amendments to the Clean Air Act, and as driven by the 2010 Presidential Memorandum Regarding Fuel Efficiency and the 2005 Supreme Court ruling in Massachusetts v. EPA that supported the regulation of CO2 as a pollutant. Manufacturers submit data on an annual basis, or as needed to document vehicle model changes. This asset will be expanded to include medium and heavy duty vehicles in the future.The EPA performs targeted GHG emissions tests on approximately 15% of vehicles submitted for certification. Confirmatory data on vehicles is associated with its corresponding submission data to verify the accuracy of manufacturer submissions beyond standard business rules.Submitted data comes in XML format or as documents, with the majority of submissions sent in XML, and includes descriptive information on the vehicle itself, emissions information, and the manufacturer's testing approach. This data may contain proprietary information (CBI) such as information on estimated sales or other data elements indicated by the submitter as confidential. CBI data is not publically available; however, CBI data can accessed within EPA under the restrictions of the Office of Transportation and Air Quality (OTAQ) CBI policy [RCS Link]. Pollutants data includes CO2, CH4, N2O. Datasets are divided by vehicle/engine model and/or year with corresponding emission, test, and certification data. Data assets are stored in EPA's Verify system.Coverage began in 2011, with summary light duty data available to the public on request. Raw data is only available to select EPA employees.EV-GHG Mobile Source Data submission documents with metadata, certificate and summary decision information is stored in Verify after it has been quality assured. Where summary data appears inaccurate, OTAQ returns the entries for review to their originator.",
+            "identifier": "1A180878-78FB-4FA5-B496-08B02D2C69E0",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4451,38 +4459,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "EV-GHG Mobile Source",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1A180878-78FB-4FA5-B496-08B02D2C69E0%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1A180878-78FB-4FA5-B496-08B02D2C69E0%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "EV-GHG Mobile Source"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:zarmski.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "1A180878-78FB-4FA5-B496-08B02D2C69E0",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:zarmski.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Engine and Vehicle Compliance Certification and Fuel Economy Inventory contains measured emissions and fuel economy compliance information for light duty vehicles. Data is collected by EPA to certify compliance with the applicable fuel economy provisions of the Energy Policy and Conservation Act (EPCA) and The Energy Independent Security Act of 2007",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.fueleconomy.gov/feg/download.shtml",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "765D70B8-0151-4BB7-8D60-5AAD5989940C",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4507,45 +4522,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Fuel Economy Label and CAFE Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.fueleconomy.gov/feg/download.shtml",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B765D70B8-0151-4BB7-8D60-5AAD5989940C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B765D70B8-0151-4BB7-8D60-5AAD5989940C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Fuel Economy Label and CAFE Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:zarmski.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "765D70B8-0151-4BB7-8D60-5AAD5989940C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Scott Christian, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:christian.scott@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This asset includes compliance data (registrations and reports), including reports related to reformulated gasoline and conventional gasoline (anti-dumping), gasoline sulfur, mobile source air toxics (including gasoline benzene), sulfur content of on-road and non-road diesel fuel, and renewable fuels under 40 CFR Part 80; and includes registration and compositional information related to fuels and fuel additives under 40 CFR Part 79.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/fuels-registration-reporting-and-compliance-help/reporting-fuel-programs",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "0DC24E22-722B-4C89-862E-3AC401F253D5",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4565,45 +4580,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Fuels Reporting System Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/fuels-registration-reporting-and-compliance-help/reporting-fuel-programs",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0DC24E22-722B-4C89-862E-3AC401F253D5%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0DC24E22-722B-4C89-862E-3AC401F253D5%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Fuels Reporting System Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:christian.scott@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Scott Christian, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "0DC24E22-722B-4C89-862E-3AC401F253D5",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:zarmski.sara@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Mobile Source Emissions Regulatory Compliance Data Inventory data asset contains measured summary compliance information on light-duty, heavy-duty, and non-road engine manufacturers by model, as well as fee payment data required by Title II of the 1990 Amendments to the Clean Air Act, to certify engines for sale in the U.S. and collect compliance certification fees. Data submitted by manufacturers falls into 12 industries: Heavy Duty Compression Ignition, Marine Spark Ignition, Heavy Duty Spark Ignition, Marine Compression Ignition, Snowmobile, Motorcycle & ATV, Non-Road Compression Ignition, Non-Road Small Spark Ignition, Light-Duty, Evaporative Components, Non-Road Large Spark Ignition, and Locomotive. Title II also requires the collection of fees from manufacturers submitting for compliance certification. Manufacturers submit data on an annual basis, to document engine model changes for certification. Manufacturers also submit compliance information on already certified in-use vehicles randomly selected by the EPA (1) year into their life and (4) years into their life to ensure that emissions systems continue to function appropriately over time.The EPA performs targeted confirmatory tests on approximately 15% of vehicles submitted for certification. Confirmatory data on engines is associated with its corresponding submission data to verify the accuracy of manufacturer submission beyond standard business rules.Section 209 of the 1990 Amendments to the Clean Air Act grants the State of California the authority to set its own standards and perform its own compliance certification through the California Air Resources Board (CARB). Currently manufacturers submit compliance information separately to both the EPA and CARB. Currently, data harmonization occurs between EPA data and CARB data only for Motorcycle & ATV submissions.Submitted data comes in XML format or as documents, with the majority of submissions being sent in XML. Data includes descriptive information on the engine itself, as well as on manufacturer testing methods and results. Submissions may include information (CBI) such as information on estimated sales, new technologies, catalysts and calibration, or other data elements indicated by the submitter as confidential. CBI data is not publically available, but it is available within EPA under the restrictions of the Office of Transportation and Air Quality (OTAQ) CBI policy [RCS Link]. Pollution emission data covers a range of Criteria Air Pollutants (CAPs) including carbon monoxide, hydrocarbons, nitrogen oxides, and particulate matter. Datasets are segmented by vehicle/engine model and year, with corresponding emission, test, and certification data. Data assets are primarily stored in EPA's Verify system. Data collected from the Heavy Duty Compression Ignition, Marine Spark Ignition, Heavy Duty Spark Ignition, Marine Compression Ignition, and Snowmobile industries, however, are currently stored in legacy systems the will be migrated to Verify in the future.Coverage began in 1979, with early records being primarily paper documents that did not go through the same level of validation as the digital submissions that began in 2005.Mobile Source Emissions Compliance documents with metadata, certificate and summary decision information is made available to the public through EPA.gov via the OTAQ Document Index System (http://iaspub.epa.gov/otaqpub).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/air-pollution-transportation",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "52A31947-0918-4AFB-8021-411A875C9AE1",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4628,45 +4643,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Mobile Source Emissions Regulatory Compliance Data Inventory",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/air-pollution-transportation",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B52A31947-0918-4AFB-8021-411A875C9AE1%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B52A31947-0918-4AFB-8021-411A875C9AE1%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Mobile Source Emissions Regulatory Compliance Data Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:zarmski.sara@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Sara Zaremski, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "52A31947-0918-4AFB-8021-411A875C9AE1",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Carl Fulper, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:Fulper.Carlr@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Mobile Source Observation Database (MSOD) is a relational database being developed by the Assessment and Standards Division (ASD) of the US Environmental Protection Agency Office of Transportation and Air Quality (formerly the Office of Mobile Sources). The MSOD contains emission test data from in-use mobile air- pollution sources such as cars, trucks, and engines from trucks and nonroad vehicles. Data in the database was collected from 1982 to the present. The data is intended to be representative of in-use vehicle emissions in the United States.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www3.epa.gov/otaq/models/msod/msodannc.htm",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "368EE0F0-011C-4755-982B-022DF2C2EF25",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -4682,45 +4697,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Mobile Source Observation Database (MSOD)",
-            "distribution": [
-                {
-                    "accessURL": "https://www3.epa.gov/otaq/models/msod/msodannc.htm",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B368EE0F0-011C-4755-982B-022DF2C2EF25%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B368EE0F0-011C-4755-982B-022DF2C2EF25%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Mobile Source Observation Database (MSOD)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Fulper.Carlr@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Carl Fulper, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "368EE0F0-011C-4755-982B-022DF2C2EF25",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+                "fn": "Cheryl Bynum, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)",
+                "hasEmail": "mailto:bynum.cheryl@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This asset includes all data collected by EPA in support of this program to address greenhouse gas emissions, fuel consumption, and criteria pollutants (NOx and PM) associated with ground freight transportation operations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/smartway",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "4C23A8B9-60E1-4F6A-BF43-C1CA01E3B55B",
+            "issued": "2014-01-01",
             "keyword": [
                 "epa",
                 "oar",
@@ -4733,45 +4748,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Smartway Transport Partnership Data",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/smartway",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4C23A8B9-60E1-4F6A-BF43-C1CA01E3B55B%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4C23A8B9-60E1-4F6A-BF43-C1CA01E3B55B%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Smartway Transport Partnership Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:bynum.cheryl@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Cheryl Bynum, U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
-            "identifier": "4C23A8B9-60E1-4F6A-BF43-C1CA01E3B55B",
-            "@type": "dcat:Dataset"
+                "fn": "Aaron Hula",
+                "hasEmail": "mailto:hula.aaron@epa.gov"
             },
-        {
-            "title": "The EPA Automotive Trends Report: Greenhouse Gas Emissions, Fuel Economy, and Technology since 1975",
+            "dataQuality": false,
             "description": "This annual report is part of the U.S. Environmental Protection Agency's (EPA) commitment to provide the public with information about new light-duty vehicle greenhouse gas (GHG) emissions, fuel economy, technology data, and auto manufacturers' performance in meeting the agency's GHG emissions standards. EPA has collected data on every new light-duty vehicle model sold in the United States since 1975, either from testing performed by EPA at the National Vehicle and Fuel Emissions Laboratory in Ann Arbor, Michigan, or directly from manufacturers using official EPA test procedures. These data are collected to support several important national programs, including EPA criteria pollutant and GHG standards, the U.S. Department of Transportation's National Highway Traffic Safety Administration (NHTSA) Corporate Average Fuel Economy (CAFE) standards, and vehicle Fuel Economy and Environment labels. The downloadable data are available in the report PDF or spreadsheet (XLS) formats.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
-            },
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/automotive-trends/explore-automotive-trends-data",
+                    "format": "Comma-Separated Values (.csv)",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "743D3E4E-C636-11E6-9D9D-CEC0C932CE01",
             "keyword": [
                 "Climate Change",
                 "Compliance",
@@ -4819,48 +4834,48 @@
                 "trading",
                 "abt"
             ],
+            "landingPage": "https://www.epa.gov/automotive-trends",
+            "language": [
+                "en-us"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2019-03-01",
+            "programCode": [
+                "020:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Air and Radiation (OAR) - Office of Transportation and Air Quality (OTAQ)"
+            },
+            "temporal": "1975-01-01/2018-01-01",
             "theme": [
                 "transportation"
             ],
+            "title": "The EPA Automotive Trends Report: Greenhouse Gas Emissions, Fuel Economy, and Technology since 1975"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "Aaron Hula",
-                "hasEmail": "mailto:hula.aaron@epa.gov"
+                "fn": "Steve Settle, U.S. EPA Office of Administration and Resource Management (OARM)",
+                "hasEmail": "mailto:settle.steve@epa.gov"
             },
-            "@type": "dcat:Dataset",
             "dataQuality": false,
-            "modified": "2019-03-01",
-            "identifier": "743D3E4E-C636-11E6-9D9D-CEC0C932CE01",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "1975-01-01/2018-01-01",
-            "accrualPeriodicity": "R/P1Y",
-            "language": [
-                "en-us"
-            ],
-            "landingPage": "https://www.epa.gov/automotive-trends",
+            "description": "Provide public access using keywords to find technical and scientific research information contained in EPA Publications.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/automotive-trends/explore-automotive-trends-data",
-                    "format": "Comma-Separated Values (.csv)",
+                    "accessURL": "https://www.epa.gov/nscep",
                     "mediaType": "text/csv"
                 }
             ],
-            "programCode": [
-                "020:033"
-            ]
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Administration and Resource Management (OARM)"
-            },
-            "accessLevel": "public",
-            "description": "Provide public access using keywords to find technical and scientific research information contained in EPA Publications.",
+            "identifier": "04401EE1-15B5-41E4-B4FC-75EF4BB0837B",
+            "issued": "2014-01-01",
             "keyword": [
                 "national environmental publications information system",
                 "nep",
@@ -4869,3944 +4884,3913 @@
                 "united states",
                 "environment"
             ],
-            "title": "National Environmental Publications and Information Site",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/nscep",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Administration and Resource Management (OARM)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B04401EE1-15B5-41E4-B4FC-75EF4BB0837B%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:settle.steve@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Steve Settle, U.S. EPA Office of Administration and Resource Management (OARM)"
-            },
-            "identifier": "04401EE1-15B5-41E4-B4FC-75EF4BB0837B",
-            "@type": "dcat:Dataset"
+            "title": "National Environmental Publications and Information Site"
         },
         {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-14",
-            "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Allocation Transfer Agency Identifier",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The allocation agency identifies the department or agency that is receiving funds through an allocation (non-expenditure) transfer.",
-            "programCode": [
-                "020:028"
-            ],
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The allocation agency identifies the department or agency that is receiving funds through an allocation (non-expenditure) transfer.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A appropriations"
                 }
             ],
             "identifier": "21911cdc-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2020-08-05",
+            "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Agency Identifier",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The agency code identifies the department or agency that is responsible for the account.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Allocation Transfer Agency Identifier"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The agency code identifies the department or agency that is responsible for the account.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219120ce-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-14",
+            "issued": "2020-08-05",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Beginning Period Of Availability",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "In annual and multi-year funds, the beginning period of availability identifies the first year of availability under law that an appropriation account may incur new obligations.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Agency Identifier"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "In annual and multi-year funds, the beginning period of availability identifies the first year of availability under law that an appropriation account may incur new obligations.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21912380-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Ending Period Of Availability",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "In annual and multi-year funds, the end period of availability identifies the last year of funds availability under law that an appropriation account may incur new obligations.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Beginning Period Of Availability"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "In annual and multi-year funds, the end period of availability identifies the last year of funds availability under law that an appropriation account may incur new obligations.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219125ec-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Availability Type Code",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "In appropriations accounts, the availability type code identifies an unlimited period to incur new obligations; this is denoted by the letter \"X\".",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Ending Period Of Availability"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "In appropriations accounts, the availability type code identifies an unlimited period to incur new obligations; this is denoted by the letter \"X\".",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21912862-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Main Account Code",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The main account code identifies the account in statute.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Availability Type Code"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The main account code identifies the account in statute.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21912ae2-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Sub Account Code",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "This is a component of the TAS. Identifies a Treasury-defined subdivision of the main account. This field cannot be blank. Subaccount 000 indicates the Parent account.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Main Account Code"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "TAS Component"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "This is a component of the TAS. Identifies a Treasury-defined subdivision of the main account. This field cannot be blank. Subaccount 000 indicates the Parent account.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21913154-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "TAS Component"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "PIID",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The unique identifier of the specific award being reported.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Sub Account Code"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The unique identifier of the specific award being reported.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191350a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Parent Award Id",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The identifier of the procurement award under which the specific award is issued (such as a Federal Supply Schedule). Term currently applies to procurement actions only",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "PIID"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The identifier of the procurement award under which the specific award is issued (such as a Federal Supply Schedule). Term currently applies to procurement actions only",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219137d0-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "FAIN",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The Federal Award Identification Number (FAIN) is the unique ID within the Federal agency for each (non-aggregate) financial assistance award.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Parent Award Id"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The Federal Award Identification Number (FAIN) is the unique ID within the Federal agency for each (non-aggregate) financial assistance award.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21913a3c-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "URI",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "Unique Record Identifier. An agency defined identifier that (when provided) is unique for every reported action.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "FAIN"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "Unique Record Identifier. An agency defined identifier that (when provided) is unique for every reported action.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21913c8a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Program Activity Code",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 200 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nCode of a specific activity or project as listed in the program and financing schedules of the annual budget of the United States Government.  ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "URI"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 200 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nCode of a specific activity or project as listed in the program and financing schedules of the annual budget of the United States Government.  ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21913f14-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Program Activity Name",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 200 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nName of a specific activity or project as listed in the program and financing schedules of the annual budget of the United States Government.  ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Program Activity Code"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 200 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nName of a specific activity or project as listed in the program and financing schedules of the annual budget of the United States Government.  ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21914518-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Object Class",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 83 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nCategories in a classification system that presents obligations by the items or services purchased by the Federal Government.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Program Activity Name"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 83 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nCategories in a classification system that presents obligations by the items or services purchased by the Federal Government.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21914784-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "By Direct Reimbursable Funding Source",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "Holds an attribute flag which specifies that the funding source of the associated data value is either a Direct or Reimbursable Funding Source.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Object Class"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "Holds an attribute flag which specifies that the funding source of the associated data value is either a Direct or Reimbursable Funding Source.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219149e6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances: ID by TAS- Program Activity-Object Class-\nAward-Direct Reimbursable"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Transaction Obligated Amount",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nObligation means a binding agreement that will result in outlays, immediately or in the future. Budgetary resources must be available before obligations can be incurred legally.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "By Direct Reimbursable Funding Source"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Transaction Obligated Amount"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nObligation means a binding agreement that will result in outlays, immediately or in the future. Budgetary resources must be available before obligations can be incurred legally.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21914c34-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Transaction Obligated Amount"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Incurred Total By Award CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Transaction Obligated Amount"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21914e82-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Undelivered Orders Unpaid Total CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Incurred Total By Award CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219150c6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL480100 Undelivered Orders Obligations Unpaid FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received and for which amounts have not been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Undelivered Orders Unpaid Total CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received and for which amounts have not been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21915d28-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL483100 Undelivered Orders Obligations Transferred Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered and obligated in one Treasury Appropriation Fund Symbol (TAFS) and transferred to or from another TAFS, which have not been actually or constructively received and not prepaid or advanced at the time of transfer. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. Although the normal balance for this account is credit, it is acceptable for this account to have a debit balance. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL480100 Undelivered Orders Obligations Unpaid FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered and obligated in one Treasury Appropriation Fund Symbol (TAFS) and transferred to or from another TAFS, which have not been actually or constructively received and not prepaid or advanced at the time of transfer. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. Although the normal balance for this account is credit, it is acceptable for this account to have a debit balance. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21915ff8-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL488100 Upward Adjustments Of Prior Year Undelivered Orders Obligations Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of upward adjustments during the current fiscal year to obligations that were originally recorded in a prior fiscal year in USSGL account 480100,\"Undelivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL483100 Undelivered Orders Obligations Transferred Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of upward adjustments during the current fiscal year to obligations that were originally recorded in a prior fiscal year in USSGL account 480100,\"Undelivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21916264-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Delivered Orders Unpaid Total CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL488100 Upward Adjustments Of Prior Year Undelivered Orders Obligations Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219164d0-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Delivered Orders Unpaid Total FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Delivered Orders Unpaid Total CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191671e-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL490100 Delivered Orders Obligations Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) This account does not close at year-end.  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Delivered Orders Unpaid Total FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) This account does not close at year-end.  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21916d9a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL493100 Delivered Orders Obligations Transferred Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount in USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" transferred during the fiscal year to or from another Treasury Appropriation Fund Symbol. This includes amounts accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. Although the normal balance for this account is credit, it is acceptable in certain instances for this account to have a debit balance. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL490100 Delivered Orders Obligations Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount in USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" transferred during the fiscal year to or from another Treasury Appropriation Fund Symbol. This includes amounts accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. Although the normal balance for this account is credit, it is acceptable in certain instances for this account to have a debit balance. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21917268-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL498100 Upward Adjustments Of Prior Year Delivered Orders Obligations Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of upward adjustments during the fiscal year to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" or USSGL account 490200, \"Delivered Orders - Obligations, Paid,\" that were originally recorded in a prior fiscal year. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL493100 Delivered Orders Obligations Transferred Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of upward adjustments during the fiscal year to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" or USSGL account 490200, \"Delivered Orders - Obligations, Paid,\" that were originally recorded in a prior fiscal year. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219174ac-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlay Amount By Award CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL498100 Upward Adjustments Of Prior Year Delivered Orders Obligations Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191770e-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlay Amount By Award FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlay Amount By Award CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191795c-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlays Undelivered Orders Prepaid Total CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlay Amount By Award FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21917baa-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlays Undelivered Orders Prepaid Total FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
+            "spatial": "USA",
+            "title": "Gross Outlays Undelivered Orders Prepaid Total CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
+            },
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191819a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL480200 Undelivered Orders Obligations Prepaid Advanced CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received but have been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlays Undelivered Orders Prepaid Total FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received but have been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21918474-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL480200 Undelivered Orders Obligations Prepaid Advanced FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received but have been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL480200 Undelivered Orders Obligations Prepaid Advanced CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received but have been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21918744-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL483200 Undelivered Orders Obligations Transferred Prepaid Advanced CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered and obligated in one Treasury Appropriation Fund Symbol (TAFS) and transferred to or from another TAFS, which have not been actually or constructively received but have been prepaid or advanced at the time of transfer. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. Although the normal balance for this account is credit, it is acceptable for this account to have a debit balance.(Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL480200 Undelivered Orders Obligations Prepaid Advanced FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered and obligated in one Treasury Appropriation Fund Symbol (TAFS) and transferred to or from another TAFS, which have not been actually or constructively received but have been prepaid or advanced at the time of transfer. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. Although the normal balance for this account is credit, it is acceptable for this account to have a debit balance.(Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "8c746238-a589-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL488200 Upward Adjustments Of Prior Year Undelivered Orders Obligations Prepaid Advanced CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of upward adjustments during the current fiscal year to obligations that were originally recorded in a prior fiscal year in USSGL account 480200,\"Undelivered Orders - Obligations, Prepaid/Advanced.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL483200 Undelivered Orders Obligations Transferred Prepaid Advanced CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of upward adjustments during the current fiscal year to obligations that were originally recorded in a prior fiscal year in USSGL account 480200,\"Undelivered Orders - Obligations, Prepaid/Advanced.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219189a6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlays Delivered Orders Paid Total CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL488200 Upward Adjustments Of Prior Year Undelivered Orders Obligations Prepaid Advanced CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21918bfe-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlays Delivered Orders Paid Total FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlays Delivered Orders Paid Total CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21918e56-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL490200 Delivered Orders Obligations Paid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount paid/outlayed for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlays Delivered Orders Paid Total FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount paid/outlayed for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219190fe-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL490800 Authority Outlayed Not Yet Disbursed CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of authority outlayed but not yet disbursed. Use only in specific circumstances, such as for interest on certain Bureau of the Fiscal Service securities. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL490200 Delivered Orders Obligations Paid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of authority outlayed but not yet disbursed. Use only in specific circumstances, such as for interest on certain Bureau of the Fiscal Service securities. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191969e-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL490800 Authority Outlayed Not Yet Disbursed FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of authority outlayed but not yet disbursed. Use only in specific circumstances, such as for interest on certain Bureau of the Fiscal Service securities. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL490800 Authority Outlayed Not Yet Disbursed CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of authority outlayed but not yet disbursed. Use only in specific circumstances, such as for interest on certain Bureau of the Fiscal Service securities. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21919914-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Obligations Incurred Total by Award"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL498200 Upward Adjustments Of Prior Year Delivered Orders Obligations Paid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of upward adjustments that were originally recorded in a prior fiscal year paid/outlayed during the fiscal year to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" or USSGL account 490200, \"Delivered Orders - Obligations, Paid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL490800 Authority Outlayed Not Yet Disbursed FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of upward adjustments that were originally recorded in a prior fiscal year paid/outlayed during the fiscal year to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid,\" or USSGL account 490200, \"Delivered Orders - Obligations, Paid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21919b76-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Deobligations Recoveries Refunds Of Prior Year By Award CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of downward adjustments to obligations and outlays incurred resulting from deobligations, recoveries, or refunds collected, at the Award level. The adjustments are to the obligations and outlays which were made in a prior year.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL498200 Upward Adjustments Of Prior Year Delivered Orders Obligations Paid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of downward adjustments to obligations and outlays incurred resulting from deobligations, recoveries, or refunds collected, at the Award level. The adjustments are to the obligations and outlays which were made in a prior year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21919dce-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL487100 Downward Adjustments Of Prior Year Unpaid Undelivered Orders Obligations Recoveries CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of recoveries during the current fiscal year resulting from downward adjustments to obligations originally recorded in a prior fiscal year in USSGL account 480100, \"Undelivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Deobligations Recoveries Refunds Of Prior Year By Award CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of recoveries during the current fiscal year resulting from downward adjustments to obligations originally recorded in a prior fiscal year in USSGL account 480100, \"Undelivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191a03a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL497100 Downward Adjustments Of Prior Year Unpaid Delivered Orders Obligations Recoveries CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of recoveries that were originally recorded in a prior fiscal year during the fiscal year resulting from downward adjustments to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL487100 Downward Adjustments Of Prior Year Unpaid Undelivered Orders Obligations Recoveries CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of recoveries that were originally recorded in a prior fiscal year during the fiscal year resulting from downward adjustments to USSGL account 490100, \"Delivered Orders - Obligations, Unpaid.\" (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191a2d8-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL487200 Downward Adjustments Of Prior Year  Prepaid Advanced Undelivered Orders Obligations Refunds Collected CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of cash refunds during the current fiscal year resulting from downward adjustments to obligations that were originally recorded in a prior fiscal year in USSGL account 480200, \"Undelivered Orders - Obligations, Prepaid/Advanced.\"  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL497100 Downward Adjustments Of Prior Year Unpaid Delivered Orders Obligations Recoveries CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of cash refunds during the current fiscal year resulting from downward adjustments to obligations that were originally recorded in a prior fiscal year in USSGL account 480200, \"Undelivered Orders - Obligations, Prepaid/Advanced.\"  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191a95e-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL497200 Downward Adjustments Of Prior Year Paid Delivered Orders Obligations Refunds Collected CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of cash refunds during the fiscal year resulting from downward adjustments to USSGL account 490200, \"Delivered Orders - Obligations, Paid,\" that were originally recorded in a prior fiscal year. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL487200 Downward Adjustments Of Prior Year  Prepaid Advanced Undelivered Orders Obligations Refunds Collected CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of cash refunds during the fiscal year resulting from downward adjustments to USSGL account 490200, \"Delivered Orders - Obligations, Paid,\" that were originally recorded in a prior fiscal year. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191abca-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Award Balances (by TAS-Program Activity-\nObject Class-award-Direct Reimbursable): Deobligations Recoveries Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Incurred By Program Object Class CPE ",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL497200 Downward Adjustments Of Prior Year Paid Delivered Orders Obligations Refunds Collected CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191d2b2-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Undelivered Orders Unpaid Total FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Incurred By Program Object Class CPE "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below. \n\nA legally binding agreement that will result in outlays, immediately or in the future.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191d82a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL480100 Undelivered Orders Obligations Unpaid CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received and for which amounts have not been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Obligations Undelivered Orders Unpaid Total FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of goods and/or services ordered, which have not been actually or constructively received and for which amounts have not been prepaid or advanced. This includes amounts specified in other contracts or agreements such as grants, program subsidies, undisbursed loans and claims, and similar events for which an advance or prepayment has not occurred. This account does not close at yearend. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191da78-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL490100 Delivered Orders Obligations Unpaid FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) This account does not close at year-end.  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL480100 Undelivered Orders Obligations Unpaid CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount accrued or due for: (1) services performed by employees, contractors, vendors, carriers, grantees, lessors, and other government funds; (2) goods and tangible property received; and (3) programs for which no current service performance is required such as annuities, insurance claims, benefit payments, loans, etc. (Per USSGL TFM Part 2, Section II, Accounts and Definitions.) This account does not close at year-end.  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191f01c-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlay Amount By Program Object Class CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL490100 Delivered Orders Obligations Unpaid FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191f756-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlay Amount By Program Object Class FYB",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlay Amount By Program Object Class CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations",
-                "Program Object Class"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2191fe04-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Obligations",
+                "Program Object Class"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Deobligations Recoveries Refunds Of Prior Year By Program Object Class CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of downward adjustments to obligations and outlays incurred resulting from deobligations, recoveries, or refunds collected, at the TAS / Program Activity / Object Class level. The adjustments are to the obligations and outlays which were made in a prior year.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Gross Outlay Amount By Program Object Class FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Deobligations",
-                "Recoveries",
-                "Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of downward adjustments to obligations and outlays incurred resulting from deobligations, recoveries, or refunds collected, at the TAS / Program Activity / Object Class level. The adjustments are to the obligations and outlays which were made in a prior year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219228fc-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "issued": "2018-08-14",
+            "keyword": [
+                "Deobligations",
+                "Recoveries",
+                "Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "USSGL487200 Downward Adjustments Of Prior Year Prepaid Advanced Undelivered Orders Obligations Refunds Collected CPE",
-            "spatial": "USA",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of cash refunds during the current fiscal year resulting from downward adjustments to obligations that were originally recorded in a prior fiscal year in USSGL account 480200, \"Undelivered Orders - Obligations, Prepaid/Advanced.\"  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "Deobligations Recoveries Refunds Of Prior Year By Program Object Class CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Deobligations",
-                "Recoveries",
-                "Refunds"
-            ],
-            "modified": "2020-08-05",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of cash refunds during the current fiscal year resulting from downward adjustments to obligations that were originally recorded in a prior fiscal year in USSGL account 480200, \"Undelivered Orders - Obligations, Prepaid/Advanced.\"  (Per USSGL TFM Part 2, Section II, Accounts and Definitions.)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21923b8a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-21",
+            "issued": "2018-08-14",
+            "keyword": [
+                "Deobligations",
+                "Recoveries",
+                "Refunds"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Total Budgetary Resources CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "Budgetary resources mean amounts available to incur obligations in a given year. Budgetary resources consist of new budget authority and unobligated balances of budget authority provided in previous years.",
+            "modified": "2020-08-05",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "spatial": "USA",
+            "title": "USSGL487200 Downward Adjustments Of Prior Year Prepaid Advanced Undelivered Orders Obligations Refunds Collected CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "budgetary resources",
-                "budgetary reporting",
-                "current period financial reporting"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "Budgetary resources mean amounts available to incur obligations in a given year. Budgetary resources consist of new budget authority and unobligated balances of budget authority provided in previous years.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21925912-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-22",
+            "issued": "2018-08-21",
+            "keyword": [
+                "budgetary resources",
+                "budgetary reporting",
+                "current period financial reporting"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Budget Authority Appropriated Amount_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nAppropriation means a provision of law (not necessarily in an appropriations act) authorizing the expenditure of funds for a given purpose. Usually, but not always, an appropriation provides budget authority.",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Total Budgetary Resources CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "budget authority appropriated",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nAppropriation means a provision of law (not necessarily in an appropriations act) authorizing the expenditure of funds for a given purpose. Usually, but not always, an appropriation provides budget authority.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21925be2-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-23",
+            "issued": "2018-08-22",
+            "keyword": [
+                "budget authority appropriated",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Budget Authority Unobligated Balance Brought Forward_FYB",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nFor unexpired accounts: Amount of unobligated balance of appropriations or other budgetary resources carried forward from the preceding year and available for obligation without new action by Congress. For expired accounts: Amount of expired unobligated balances available for upward adjustments of obligations. ",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Budget Authority Appropriated Amount_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "fiscal year beginning financial reports",
-                "budget authority unobligated balance brought forward",
-                "budget authority",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nFor unexpired accounts: Amount of unobligated balance of appropriations or other budgetary resources carried forward from the preceding year and available for obligation without new action by Congress. For expired accounts: Amount of expired unobligated balances available for upward adjustments of obligations. ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219261dc-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-24",
+            "issued": "2018-08-23",
+            "keyword": [
+                "fiscal year beginning financial reports",
+                "budget authority unobligated balance brought forward",
+                "budget authority",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Adjustments To Unobligated Balance Brought Forward_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nChanges to unpaid obligations that occurred in a prior fiscal year and that were not recorded in the unpaid obligations as of October 1 of the current fiscal year. \n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Budget Authority Unobligated Balance Brought Forward_FYB"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "adjustments to unobligated balances brought forward",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nChanges to unpaid obligations that occurred in a prior fiscal year and that were not recorded in the unpaid obligations as of October 1 of the current fiscal year. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "2192643e-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-25",
+            "issued": "2018-08-24",
+            "keyword": [
+                "adjustments to unobligated balances brought forward",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Other Budgetary Resources Amount_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nNew borrowing authority, contract authority, and spending authority from offsetting collections provided by Congress in an appropriations act or other legislation, or unobligated balances of budgetary resources made available in previous legislation, to incur obligations and to make outlays.\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Adjustments To Unobligated Balance Brought Forward_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "other budgetary resources",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nNew borrowing authority, contract authority, and spending authority from offsetting collections provided by Congress in an appropriations act or other legislation, or unobligated balances of budgetary resources made available in previous legislation, to incur obligations and to make outlays.\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219266b4-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-26",
+            "issued": "2018-08-25",
+            "keyword": [
+                "other budgetary resources",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Contract Authority Amount Total_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nContract authority is a type of budget authority that permits you to incur obligations in advance of an appropriation, offsetting collections, or receipts to make outlays to liquidate the obligations. Typically, the Congress provides contract authority in an authorizing statute to allow you to incur obligations in anticipation of the collection of receipts or offsetting collections that will be used to liquidate the obligations. ",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Other Budgetary Resources Amount_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "contract authority",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nContract authority is a type of budget authority that permits you to incur obligations in advance of an appropriation, offsetting collections, or receipts to make outlays to liquidate the obligations. Typically, the Congress provides contract authority in an authorizing statute to allow you to incur obligations in anticipation of the collection of receipts or offsetting collections that will be used to liquidate the obligations. ",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21926902-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-27",
+            "issued": "2018-08-26",
+            "keyword": [
+                "contract authority",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Borrowing Authority Amount Total_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nBorrowing authority is a type of budget authority that permits obligations and outlays to be financed by borrowing. \n\n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Contract Authority Amount Total_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Borrowing authority amount",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nBorrowing authority is a type of budget authority that permits obligations and outlays to be financed by borrowing. \n\n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21926b64-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-28",
+            "issued": "2018-08-27",
+            "keyword": [
+                "Borrowing authority amount",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Spending Authority From Offsetting Collections Amount Total_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nSpending authority from offsetting collections is a type of budget authority that permits obligations and outlays to be financed by offsetting collections.\n\nOffsetting collections mean payments to the Government that, by law, are credited directly to expenditure accounts and deducted from gross budget authority and outlays of the expenditure account, rather than added to receipts. Usually, they are authorized to be spent for the purposes of the account without further action by Congress. They usually result from business-like transactions with the public, including payments from the public in exchange for goods and services, reimbursements for damages, and gifts or donations of money to the Government and from intragovernmental transactions with other Government accounts. The authority to spend offsetting collections is a form of budget authority.\n\n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Borrowing Authority Amount Total_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Spending Authority From Offsetting Collections Amount",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nSpending authority from offsetting collections is a type of budget authority that permits obligations and outlays to be financed by offsetting collections.\n\nOffsetting collections mean payments to the Government that, by law, are credited directly to expenditure accounts and deducted from gross budget authority and outlays of the expenditure account, rather than added to receipts. Usually, they are authorized to be spent for the purposes of the account without further action by Congress. They usually result from business-like transactions with the public, including payments from the public in exchange for goods and services, reimbursements for damages, and gifts or donations of money to the Government and from intragovernmental transactions with other Government accounts. The authority to spend offsetting collections is a form of budget authority.\n\n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21926dc6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-29",
+            "issued": "2018-08-28",
+            "keyword": [
+                "Spending Authority From Offsetting Collections Amount",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Status Of Budgetary Resources Total_CPE",
-            "": 43281,
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "This element addresses the status of budgetary resources and includes the total of obligated and unobligated balances, at the reported date. The value should equal the Budget Authority Available Amount Total for the TAS at Current Period End.",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Spending Authority From Offsetting Collections Amount Total_CPE"
+        },
+        {
+            "": 43281,
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Status of Budgetary Resources",
-                "Financial Statements",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "This element addresses the status of budgetary resources and includes the total of obligated and unobligated balances, at the reported date. The value should equal the Budget Authority Available Amount Total for the TAS at Current Period End.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219274e2-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-30",
+            "issued": "2018-08-29",
+            "keyword": [
+                "Status of Budgetary Resources",
+                "Financial Statements",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Obligations Incurred Total By TAS_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.\n\n\n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Status Of Budgetary Resources Total_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
-            },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Obligations Incurred Total by TAS",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Appendix F of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nFor unexpired accounts:\nAmount of obligations incurred from the beginning of the current fiscal year to the end of the reporting period, net of refunds received that pertain to obligations incurred in the current year. Include upward adjustments of prior obligations. \n\nFor expired accounts:\nAmount of upward adjustments of obligations previously incurred. Upward adjustments are limited by the amount available for adjustments. No new obligations may be incurred against expired or canceled accounts.\n\n\n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "219277c6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-08-31",
+            "issued": "2018-08-30",
+            "keyword": [
+                "Obligations Incurred Total by TAS",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Gross Outlay Amount By TAS_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Obligations Incurred Total By TAS_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "Gross outlay amount",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nPayments made to liquidate an obligation (other than the repayment of debt principal or other disbursements that are \u201cmeans of financing\u201d transactions). Outlays generally are equal to cash disbursements but also are recorded for cash-equivalent transactions, such as the issuance of debentures to pay insurance claims, and in a few cases are recorded on an accrual basis such as interest on public issues of the public debt. Outlays are the measure of Government spending. \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21927a5a-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-09-01",
+            "issued": "2018-08-31",
+            "keyword": [
+                "Gross outlay amount",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Unobligated Balance CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nUnobligated balance means the cumulative amount of budget authority that remains available for obligation under law in unexpired accounts. The term \u201cexpired balances available for adjustment only\u201d refers to unobligated amounts in expired accounts.\n \n\n",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Gross Outlay Amount By TAS_CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "unobligated balance",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The definition for this element appears in Section 20 of OMB Circular A-11 issued June 2015; a brief summary from A-11 appears below.\n\nUnobligated balance means the cumulative amount of budget authority that remains available for obligation under law in unexpired accounts. The term \u201cexpired balances available for adjustment only\u201d refers to unobligated amounts in expired accounts.\n \n\n",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21927cc6-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "issued": "2018-09-02",
+            "issued": "2018-09-01",
+            "keyword": [
+                "unobligated balance",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://edg.epa.gov/epa_data_license.html",
-            "title": "Deobligations Recoveries Refunds By TAS_CPE",
-            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "description": "The amount of downward adjustments to obligations and outlays resulting from deobligations, recoveries, or refunds collected, summarized at the TAS level. The adjustments are to the obligations and outlays which were made in a prior year.",
+            "modified": "2018-07-31",
             "programCode": [
                 "020:028"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency"
+            },
+            "title": "Unobligated Balance CPE"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "020:00"
             ],
+            "conformsTo": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
             "contactPoint": {
-                "hasEmail": "mailto:DATAActInquiries@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "US EPA DATA Act Workgroup"
-            },
-            "accessLevel": "public",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency"
+                "fn": "US EPA DATA Act Workgroup",
+                "hasEmail": "mailto:DATAActInquiries@epa.gov"
             },
-            "language": [
-                "en-US"
-            ],
-            "keyword": [
-                "deobligations recoveries refunds",
-                "budgetary reporting",
-                "current period financial reporting",
-                "A-11",
-                "OMB Circular A-11"
-            ],
-            "modified": "2018-07-31",
-            "accrualPeriodicity": "R/P3M",
             "dataQuality": true,
+            "describedBy": "https://www.fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The amount of downward adjustments to obligations and outlays resulting from deobligations, recoveries, or refunds collected, summarized at the TAS level. The adjustments are to the obligations and outlays which were made in a prior year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://api.usaspending.gov",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/environmental-protection-agency",
                     "description": "USAspending.gov is the official source for spending data for the U.S. Government. Its mission is to show the American public what the federal government spends every year and how it spends the money. You can follow the money from the Congressional appropriations to the federal agencies and down to local communities and businesses",
-                    "@type": "dcat:Distribution",
                     "title": "usaspending.gov"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "description": "EPA File A submission to comply with the DATA Act.",
-                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations",
+                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
                     "format": "text/csv",
                     "mediaType": "text/csv",
-                    "downloadURL": "https://www.usaspending.gov/download_center/award_data_archive",
-                    "@type": "dcat:Distribution"
+                    "title": "Raw Quarterly DATA Act Files - Environmental Protection Agency (EPA) / File A, Appropriations"
                 }
             ],
             "identifier": "21927f28-a583-11e8-98d0-529269fb1459",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "title": "List N- Disinfectants for Use Against SARS-CoV-2 (COVID-19)",
-            "description": "EPA-registered antimicrobial products that meet the criteria for inclusion on EPA's List N- Disinfectants for use against SARS-CoV-2 (COVID-19). For each product the dataset includes the EPA registration number, the active ingredient, the primary product name and additional information including how the product should be applied and relevant use sites. ",
-            "modified": "2020-08-20",
+            "issued": "2018-09-02",
+            "keyword": [
+                "deobligations recoveries refunds",
+                "budgetary reporting",
+                "current period financial reporting",
+                "A-11",
+                "OMB Circular A-11"
+            ],
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/epa_data_license.html",
+            "modified": "2018-07-31",
+            "programCode": [
+                "020:028"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "OCSPP, OPP, AD"
+                "name": "U.S. Environmental Protection Agency"
             },
-            "contactPoint": {
-                "fn": "ITRMD Web Team",
-                "hasEmail": "mailto:OPP_ITRMD_WEB_TEAM@epa.gov",
-                "@type": "vcard:Contact"
+            "title": "Deobligations Recoveries Refunds By TAS_CPE"
         },
-            "identifier": "b39dc7ac-dafc-4997-a8e8-2ef10f942ef1",
+        {
             "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "2020-03-05/2021-12-31",
-            "issued": "2020-03-05",
-            "accrualPeriodicity": "R/P1W",
-            "language": [
-                "en-us"
-            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ITRMD Web Team",
+                "hasEmail": "mailto:OPP_ITRMD_WEB_TEAM@epa.gov"
+            },
             "dataQuality": true,
-            "landingPage": "https://www.epa.gov/pesticide-registration/list-n-disinfectants-use-against-sars-cov-2-covid-19",
-            "programCode": [
-                "020:084"
-            ],
+            "description": "EPA-registered antimicrobial products that meet the criteria for inclusion on EPA's List N- Disinfectants for use against SARS-CoV-2 (COVID-19). For each product the dataset includes the EPA registration number, the active ingredient, the primary product name and additional information including how the product should be applied and relevant use sites. ",
+            "identifier": "b39dc7ac-dafc-4997-a8e8-2ef10f942ef1",
+            "issued": "2020-03-05",
             "keyword": [
                 "Biology",
                 "Chemicals",
@@ -8823,23 +8807,53 @@
                 "antimicrobial",
                 "antiviral",
                 "virus"
-            ]
-        },
-        {
-            "title": "Certification Plan and Reporting Database (CPARD)",
-            "description": "CPARD contains (1) EPA-approved State, Tribal and Federal certification plans required by the Federal Insecticide, Fungicide, Rodenticide Act to administer a certification program for applicators of restricted use pesticides; (2) information on plan reviews and approvals; and (3) State, Tribal and Federal annual reports required by 40 CFR 171. ",
+            ],
+            "landingPage": "https://www.epa.gov/pesticide-registration/list-n-disinfectants-use-against-sars-cov-2-covid-19",
+            "language": [
+                "en-us"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2020-08-20",
+            "programCode": [
+                "020:084"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+                "name": "OCSPP, OPP, AD"
             },
+            "temporal": "2020-03-05/2021-12-31",
+            "title": "List N- Disinfectants for Use Against SARS-CoV-2 (COVID-19)"
+        },
+        {
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "conformsTo": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeanne Kasai ",
                 "hasEmail": "mailto:kasai.jeanne@epa.gov"
             },
-            "bureauCode": [
-                "020:00"
+            "dataQuality": true,
+            "describedBy": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
+            "describedByType": "text/html",
+            "description": "CPARD contains (1) EPA-approved State, Tribal and Federal certification plans required by the Federal Insecticide, Fungicide, Rodenticide Act to administer a certification program for applicators of restricted use pesticides; (2) information on plan reviews and approvals; and (3) State, Tribal and Federal annual reports required by 40 CFR 171. ",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
+                    "conformsTo": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
+                    "describedBy": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
+                    "describedByType": "text/html",
+                    "description": "Information required by 40 CFR 171 for each EPA-approved certification plan for applicators of restricted use pesticides. ",
+                    "format": "Information is read directly from webpages.  Where information is sortable, it can be downloaded into a pdf, Excel, html format.",
+                    "title": "Certification Plan and Reporting Database (CPARD)"
+                }
             ],
+            "identifier": "b8228615-fd49-4145-a4eb-31d7ab0cc59d",
+            "issued": "2022",
             "keyword": [
                 "environment",
                 "Management",
@@ -8906,51 +8920,44 @@
                 "restricted use pesticides",
                 "applicators"
             ],
-            "modified": "2021",
-            "identifier": "b8228615-fd49-4145-a4eb-31d7ab0cc59d",
-            "accessLevel": "restricted public",
-            "rights": "EPA Category: Mission Sensitive, NARA Category: Critical Infrastructure",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2005/2022",
-            "issued": "2022",
-            "accrualPeriodicity": "R/P6M",
+            "landingPage": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
             "language": [
                 "en-us"
             ],
-            "dataQuality": true,
-            "conformsTo": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
-            "describedBy": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
-            "describedByType": "text/html",
-            "landingPage": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
-            "references": [
-                "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
-                    "title": "Certification Plan and Reporting Database (CPARD)",
-                    "description": "Information required by 40 CFR 171 for each EPA-approved certification plan for applicators of restricted use pesticides. ",
-                    "format": "Information is read directly from webpages.  Where information is sortable, it can be downloaded into a pdf, Excel, html format.",
-                    "describedBy": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::",
-                    "describedByType": "text/html",
-                    "conformsTo": "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021",
+            "primaryitinvestmentuii": "020-000030302",
             "programCode": [
                 "020:016"
             ],
-            "systemofrecords": "http://www2.epa.gov/privacy/privacy-act-system-records-restricted-use-pesticides-epa-59",
-            "primaryitinvestmentuii": "020-000030302"
-        },
-        {
-            "@type": "dcat:Dataset",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
             },
+            "references": [
+                "https://cpardpub.epa.gov/ords/cpardpub/f?p=154:1::::::"
+            ],
+            "rights": "EPA Category: Mission Sensitive, NARA Category: Critical Infrastructure",
+            "systemofrecords": "http://www2.epa.gov/privacy/privacy-act-system-records-restricted-use-pesticides-epa-59",
+            "temporal": "2005/2022",
+            "title": "Certification Plan and Reporting Database (CPARD)"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dina Castellon, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)",
+                "hasEmail": "mailto:Castellon.dina@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Chemical Search Web Utility is an intuitive web application that allows the public to easily find the chemical that they are interested in using, and which provides a broad array of simple to advanced search options.",
+            "identifier": "77B9868D-A0A9-4F79-83CF-FCFF63CA0DE1",
+            "issued": "2014-01-01",
             "keyword": [
                 "pria",
                 "biopesticide",
@@ -8974,37 +8981,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Chemical Search Web Utility",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B77B9868D-A0A9-4F79-83CF-FCFF63CA0DE1%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B77B9868D-A0A9-4F79-83CF-FCFF63CA0DE1%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Chemical Search Web Utility"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Castellon.dina@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dina Castellon, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+                "fn": "Mark Heflin, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)",
+                "hasEmail": "mailto:heflin.mark@epa.gov"
             },
-            "identifier": "77B9868D-A0A9-4F79-83CF-FCFF63CA0DE1"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Pesticide Product Label System (PPLS) provides a collection of pesticide product labels (Adobe PDF format) that have been approved by EPA under Section 3 of the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA). New labels were added to PPLS on November 21, 2014. Pesticide product labels provide critical information about how to safely handle and use registered pesticide products. An approved pesticide product label represents the full content of EPAs registration decision regarding that product. Pesticide labels contain detailed information on the use, storage, and handling of a product. This information will be found on EPA stamped-approved labels and, in some cases, in subsequent related correspondence, which is also included in PPLS. You may need to review several PDF files for a single product to determine the complete current terms of registration.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://iaspub.epa.gov/apex/pesticides/f?p=PPLS:1",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "F4E8281C-2AD5-4817-BBE5-6EBA55C8DF18",
+            "issued": "2014-01-01",
             "keyword": [
                 "pesticide",
                 "product label",
@@ -9013,45 +9028,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Pesticide Product Label System",
-            "distribution": [
-                {
-                    "accessURL": "https://iaspub.epa.gov/apex/pesticides/f?p=PPLS:1",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF4E8281C-2AD5-4817-BBE5-6EBA55C8DF18%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF4E8281C-2AD5-4817-BBE5-6EBA55C8DF18%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Pesticide Product Label System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:heflin.mark@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Mark Heflin, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
-            },
-            "identifier": "F4E8281C-2AD5-4817-BBE5-6EBA55C8DF18",
-            "@type": "dcat:Dataset"
+                "fn": "Robert Schultz, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)",
+                "hasEmail": "mailto:Schultz.Robert@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "PRISM provides an integrated, web portal for all pesticide related data, communications, registrations and transactions for OPP and its stakeholders, partners and customers. PRISM supports Strategic Goal 4 by automating pesticide registration processes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/pesticide-registration",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "4B03A4C6-94B4-4BE0-89BF-1BA2BDBB1BBD",
+            "issued": "2014-01-01",
             "keyword": [
                 "documentum",
                 "endangered species",
@@ -9066,45 +9081,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Pesticide Registration Information System",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/pesticide-registration",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4B03A4C6-94B4-4BE0-89BF-1BA2BDBB1BBD%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4B03A4C6-94B4-4BE0-89BF-1BA2BDBB1BBD%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Pesticide Registration Information System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Schultz.Robert@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Robert Schultz, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
-            },
-            "identifier": "4B03A4C6-94B4-4BE0-89BF-1BA2BDBB1BBD",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+                "fn": "Mark Heflin, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)",
+                "hasEmail": "mailto:heflin.mark@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Pesticide Product Information System contains information concerning all pesticide products registered in the United States. It includes registrant name and address, chemical ingredients, toxicity category, product names, distributor brand names, site/pest uses, pesticidal type, formulation code, and registration status.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/ingredients-used-pesticide-products/pesticide-product-information-system-ppis",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "4534051E-D8BF-422E-A115-DAD0B4E49BF8",
+            "issued": "2014-01-01",
             "keyword": [
                 "data finder",
                 "substances",
@@ -9115,49 +9130,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Pesticide Product Information System (PPIS)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/ingredients-used-pesticide-products/pesticide-product-information-system-ppis",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4534051E-D8BF-422E-A115-DAD0B4E49BF8%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4534051E-D8BF-422E-A115-DAD0B4E49BF8%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Pesticide Product Information System (PPIS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:heflin.mark@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Mark Heflin, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pesticide Programs (OPP)"
-            },
-            "identifier": "4534051E-D8BF-422E-A115-DAD0B4E49BF8",
-            "@type": "dcat:Dataset"
+                "fn": "Tawanda Maignan, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:maignan.tawanda@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Insecticide, Fungicide, and Rodenticide Act Section 18 Database",
+            "dataQuality": false,
+            "description": "Section 18 of Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) authorizes EPA to allow an unregistered use of a pesticide for a limited time if EPA determines that an emergency condition exists. This database provides information about these emergency exemptions.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/enforcement/federal-insecticide-fungicide-and-rodenticide-act-fifra-and-federal-facilities",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/enforcement/federal-insecticide-fungicide-and-rodenticide-act-fifra-and-federal-facilities",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "Section 18 of Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) authorizes EPA to allow an unregistered use of a pesticide for a limited time if EPA determines that an emergency condition exists. This database provides information about these emergency exemptions.",
+            "identifier": "0390EA72-405A-4534-BB30-37E0FEB4356E",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "water",
@@ -9167,45 +9178,45 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tawanda Maignan, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:maignan.tawanda@epa.gov"
-            },
-            "identifier": "0390EA72-405A-4534-BB30-37E0FEB4356E",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0390EA72-405A-4534-BB30-37E0FEB4356E%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0390EA72-405A-4534-BB30-37E0FEB4356E%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Federal Insecticide, Fungicide, and Rodenticide Act Section 18 Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Aquatic Life Benchmarks",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michelle Thawley, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:thawley.michelle@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "The Aquatic Life Benchmarks is an EPA-developed set of criteria for freshwater species. These benchmarks are based on toxicity values reviewed by EPA and used in the Agency's risk assessments developed as part of the decision-making process for pesticide registration.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/aquatic-life-benchmarks-pesticide-registration",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/aquatic-life-benchmarks-pesticide-registration",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "The Aquatic Life Benchmarks is an EPA-developed set of criteria for freshwater species. These benchmarks are based on toxicity values reviewed by EPA and used in the Agency's risk assessments developed as part of the decision-making process for pesticide registration.",
+            "identifier": "DC8A097C-3206-4717-B20D-55D2BAD74900",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "water",
@@ -9217,41 +9228,45 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michelle Thawley, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:thawley.michelle@epa.gov"
-            },
-            "identifier": "DC8A097C-3206-4717-B20D-55D2BAD74900",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BDC8A097C-3206-4717-B20D-55D2BAD74900%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BDC8A097C-3206-4717-B20D-55D2BAD74900%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Aquatic Life Benchmarks"
         },
         {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Christina Guthrie, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:Guthrie.Christina@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Electronics Environmental Benefits Calculator (EEBC) was developed to assist organizations in estimating the environmental benefits of greening their purchase,  use and disposal of electronics. The EEBC estimates the environmental and economic benefits of: Purchasing Electronic Product Environmental Assessment Tool (EPEAT)-registered products; Enabling power management features on computers and monitors above default percentages;  Extending the life of equipment beyond baseline values;  Reusing computers,  monitors and cell phones; and Recycling computers,  monitors,  cell phones and loads of mixed electronic products. The EEBC may be downloaded as a Microsoft Excel spreadsheet.\nSee https://www.federalelectronicschallenge.net/resources/bencalc.htm for more details.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/fec/publications-and-resources#acquisition",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "B359142D-11A3-4E20-BBCC-DE17E413C699",
+            "issued": "2014-01-01",
             "keyword": [
                 "environment",
                 "energy",
@@ -9260,73 +9275,44 @@
                 "united states",
                 "economy"
             ],
-            "title": "Electronics Environmental Benefits Calculator",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/fec/publications-and-resources#acquisition",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BB359142D-11A3-4E20-BBCC-DE17E413C699%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB359142D-11A3-4E20-BBCC-DE17E413C699%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:Guthrie.Christina@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Christina Guthrie, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "B359142D-11A3-4E20-BBCC-DE17E413C699",
-            "@type": "dcat:Dataset"
+            "title": "Electronics Environmental Benefits Calculator"
         },
         {
-            "title": "Initial Entry Search System",
-            "description": "Dataset contains high-level use information used for new chemical review under TSCA.",
-            "modified": "2021",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Chemical Safety and Pollution Prevention"
-            },
-            "contactPoint": {
-                "fn": "Franklyn Hall",
-                "hasEmail": "mailto:hall.franklyn@epa.gov",
-                "@type": "vcard:Contact"
-            },
-            "identifier": "39350f95-de40-406d-9b81-e24462b4aeac",
             "accessLevel": "non-public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "1999-01-01/2030-01-01",
-            "issued": "1999-01-01",
-            "language": [
-                "en",
-                "en-us"
-            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Franklyn Hall",
+                "hasEmail": "mailto:hall.franklyn@epa.gov"
+            },
+            "description": "Dataset contains high-level use information used for new chemical review under TSCA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "C Source File (.c)",
-                    "title": "Not Applicable",
                     "description": "Dataset contains high-level use information used for new chemical review under TSCA.",
-                    "mediaType": "text/x-c"
+                    "format": "C Source File (.c)",
+                    "mediaType": "text/x-c",
+                    "title": "Not Applicable"
                 }
             ],
+            "identifier": "39350f95-de40-406d-9b81-e24462b4aeac",
+            "issued": "1999-01-01",
             "keyword": [
                 "Chemicals",
                 "Air",
@@ -9345,26 +9331,46 @@
                 "use",
                 "releases"
             ],
+            "language": [
+                "en",
+                "en-us"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021",
             "programCode": [
                 "020:072"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Chemical Safety and Pollution Prevention"
+            },
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "temporal": "1999-01-01/2030-01-01",
+            "title": "Initial Entry Search System"
         },
         {
-            "title": "Inventory Update Rule ",
-            "description": "Information on chemicals manufactured or imported into the United States and listed on the TSCA Chemical Substances Inventory was collected periodically by the EPA as part of the Inventory Update Rule (IUR). This collection began in 1986 and was changed to the Chemical Data Reporting (CDR) rule in 2012.",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": false,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA- Office Of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention (OPPT)"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Santacroce",
                 "hasEmail": "mailto:santacroce.jeffrey@epa.gov"
             },
+            "dataQuality": false,
+            "description": "Information on chemicals manufactured or imported into the United States and listed on the TSCA Chemical Substances Inventory was collected periodically by the EPA as part of the Inventory Update Rule (IUR). This collection began in 1986 and was changed to the Chemical Data Reporting (CDR) rule in 2012.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
+                    "description": "The full IUR data sets are stored on the TSCA CBI LAN.  A public version of the 2006 IUR data is available on the Internet.",
+                    "format": " 2006IUR.zip contains 4 DBF files and an IUR_2006_Readme.doc file. The DBF files store the non-confidential IUR records for 2006.",
+                    "title": "IUR datasets"
+                }
+            ],
+            "identifier": "567dfc76-1bae-43c0-bc6c-a17f99df7979",
+            "issued": "2009-03-09",
             "keyword": [
                 "Chemicals",
                 "environment",
@@ -9440,138 +9446,147 @@
                 "Manufacturer",
                 "TSCA"
             ],
-            "modified": "2009",
-            "identifier": "567dfc76-1bae-43c0-bc6c-a17f99df7979",
-            "accessLevel": "public",
-            "rights": "Only TSCA CBI cleared individuals will be able to access the data asserted as CBI.",
-            "license": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
-            "temporal": "2005/2006",
-            "issued": "2009-03-09",
+            "landingPage": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
             "language": [
                 "en-us"
             ],
-            "landingPage": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
-                    "title": "IUR datasets",
-                    "description": "The full IUR data sets are stored on the TSCA CBI LAN.  A public version of the 2006 IUR data is available on the Internet.",
-                    "format": " 2006IUR.zip contains 4 DBF files and an IUR_2006_Readme.doc file. The DBF files store the non-confidential IUR records for 2006."
-                }
-            ],
+            "license": "https://www.epa.gov/chemical-data-reporting/downloadable-2006-iur-public-database",
+            "modified": "2009",
             "programCode": [
                 "020:072"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Lead-Based Paint Program (FLPP) Database",
-            "description": "The FLPP Database system supports the application process for the accreditation of training providers and the certification of firms and individuals who performs lead based abatements and renovation and repair activities in the United States.",
-            "bureauCode": [
-                "020:00"
             ],
-            "dataQuality": true,
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT) - Existing Chemicals Risk Management Division (ECRMD)"
+                "name": "U.S. EPA- Office Of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention (OPPT)"
             },
-            "contactPoint": {
-                "fn": "Robert Wright",
-                "hasEmail": "mailto:wright.robert@epa.gov",
-                "@type": "vcard:Contact"
+            "rights": "Only TSCA CBI cleared individuals will be able to access the data asserted as CBI.",
+            "temporal": "2005/2006",
+            "title": "Inventory Update Rule "
         },
-            "keyword": [
-                "Environment",
-                "Regulatory",
-                "Toxics",
-                "United States",
-                "FLPP Firm Search",
-                "FLPP Trainer Search",
-                "FLPP Application Process"
-            ],
-            "modified": "2021-11-05",
-            "identifier": "020-000014003",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "temporal": "2006-06-03/2025-12-31",
-            "issued": "2021-11-05",
             "accrualPeriodicity": "R/P1M",
-            "language": [
-                "en-us"
+            "bureauCode": [
+                "020:00"
             ],
             "conformsTo": "https://resources.data.gov/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert Wright",
+                "hasEmail": "mailto:wright.robert@epa.gov"
+            },
+            "dataQuality": true,
             "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
             "describedByType": "application/javascript",
-            "landingPage": "https://javaauth.epa.gov/flpp/",
-            "references": [
-                "https://www.epa.gov/lead"
-            ],
+            "description": "The FLPP Database system supports the application process for the accreditation of training providers and the certification of firms and individuals who performs lead based abatements and renovation and repair activities in the United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://javaauth.epa.gov/flpp/",
-                    "title": "FLPP Database",
                     "description": "The FLPP Database system supports the application process for the accreditation of training providers and the certification of firms and individuals who performs lead based abatements and renovation and repair activities in the United States.",
-                    "format": "API"
+                    "format": "API",
+                    "title": "FLPP Database"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://cfpub.epa.gov/flpp/pub/index.cfm?do=main.firmSearch",
-                    "title": "Find RRP Firms",
                     "description": "Public search tool to locate certified RRP Firms",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Find RRP Firms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://cfpub.epa.gov/flpp/search.cfm?Applicant_Type=firm",
-                    "title": "Find Abatement Firms",
                     "description": "Public search tool to locate certified Abatement firms",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Find Abatement Firms"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://cdxapps.epa.gov/ocspp-oppt-leadhub/training-search?do=main.trainingSearch",
-                    "title": "Find RRP Trainers",
                     "description": "Public search tool to locate accredited RRP Training Providers",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Find RRP Trainers"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://cfpub.epa.gov/flpp/pub/index.cfm?do=main.trainingSearchAbatement",
-                    "title": "Find Abatement Trainers",
                     "description": "Public search tool to locate certified Abatement Training Providers",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Find Abatement Trainers"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://cfpub.epa.gov/flpp/pub/index.cfm?do=main.individualSearch",
-                    "title": "Search for Individual Applicants to locate their information for certification",
                     "description": "Public search tool link to apply for Individual Lead certifications ",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Search for Individual Applicants to locate their information for certification"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/lead/lead-renovationabatement-firm-certification-application-or-update",
-                    "title": "Search for Firm Application Process",
                     "description": "Public search tool link to locate their information for Firm certification",
-                    "format": "API"
+                    "format": "API",
+                    "title": "Search for Firm Application Process"
                 }
             ],
+            "identifier": "020-000014003",
+            "issued": "2021-11-05",
+            "keyword": [
+                "Environment",
+                "Regulatory",
+                "Toxics",
+                "United States",
+                "FLPP Firm Search",
+                "FLPP Trainer Search",
+                "FLPP Application Process"
+            ],
+            "landingPage": "https://javaauth.epa.gov/flpp/",
+            "language": [
+                "en-us"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-05",
+            "primaryitinvestmentuii": "020-000014003",
             "programCode": [
                 "020:013"
             ],
-            "systemofrecords": "http://www2.epa.gov/privacy/privacy-act-system-records-federal-lead-based-paint-program-system-records-epa-5",
-            "primaryitinvestmentuii": "020-000014003"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT) - Existing Chemicals Risk Management Division (ECRMD)"
             },
+            "references": [
+                "https://www.epa.gov/lead"
+            ],
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "systemofrecords": "http://www2.epa.gov/privacy/privacy-act-system-records-federal-lead-based-paint-program-system-records-epa-5",
+            "temporal": "2006-06-03/2025-12-31",
+            "title": "Federal Lead-Based Paint Program (FLPP) Database"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:saxton.dion@epa.gov"
+            },
+            "dataQuality": false,
             "description": "This data extraction tool contains the non confidential identities of chemical substances submitted under the Toxic Substances Control Act (TSCA). TSCA was enacted to ensure that chemicals manufactured,  imported,  processed,  or distributed in commerce,  or used or disposed of in the United States do not pose any unreasonable risks to human health or the environment. EPA adds chemical substances to the TSCA Inventory following EPAs receipt of a Notice of Commencement (NOC) signaling the manufacturers intent to produce a chemical substance that EPA has previously reviewed and approved. Since EPA published the final TSCA Inventory Reporting Rule on December 23,  1977,  the TSCA Inventory has grown to include the identities of over 83, 000 chemical substances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/tsca-inventory",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "4D49A8F7-9B38-44B0-966D-41D7A31856F8",
+            "issued": "2014-01-01",
             "keyword": [
                 "substance inventory",
                 "chemical substance inventory",
@@ -9590,45 +9605,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "TSCA Inventory Data Extraction Tool",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/tsca-inventory",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4D49A8F7-9B38-44B0-966D-41D7A31856F8%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4D49A8F7-9B38-44B0-966D-41D7A31856F8%7D"
             ],
-            "accrualPeriodicity": "R/P6M",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "TSCA Inventory Data Extraction Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:saxton.dion@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "4D49A8F7-9B38-44B0-966D-41D7A31856F8",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Christina Guthrie, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:Guthrie.Christina@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The E3 initiative is designed to help you thrive in a new business era focused on sustainability and,  working together,  to promote sustainable manufacturing and economic growth throughout the United States. Within the E3 framework,  we can: - Drive Innovation - Increase Manufacturing Productivity - Boost Local Economies - Reduce Environmental Impacts - Foster Development - Conserve Energy and Resources This website provides information and tools for E3,  including fact sheets,  contacts,  and calculators.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/e3/about-e3-economy-energy-environment",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "7BECF83A-CE57-48E3-9650-B155DD48A8DF",
+            "issued": "2010-01-01",
             "keyword": [
                 "economy",
                 "economics",
@@ -9648,45 +9663,45 @@
                 "united states",
                 "economy"
             ],
-            "title": "E3: Economy - Energy - Environment; Supporting Manufacturing Leadership through Sustainability",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/e3/about-e3-economy-energy-environment",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2010-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B7BECF83A-CE57-48E3-9650-B155DD48A8DF%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B7BECF83A-CE57-48E3-9650-B155DD48A8DF%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "E3: Economy - Energy - Environment; Supporting Manufacturing Leadership through Sustainability"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Guthrie.Christina@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Christina Guthrie, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "7BECF83A-CE57-48E3-9650-B155DD48A8DF",
-            "@type": "dcat:Dataset"
+                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:saxton.dion@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This tool is intended to aid individuals interested in learning more about chemicals that are manufactured or imported into the United States. Health and safety information on these chemicals,  primarily in the form of paper documents,  are routinely submitted by industry (manufacturers or importers of chemicals) to EPA under the Toxic Substances Control Act (TSCA).  EPA is in the process of converting these documents into electronic form and making non-confidential versions of these documents accessible through this tool.  The tool enables users to conduct both full text and metadata searches of these documents,  and presents these as .pdf for viewing or downloading.  The tool also queries existing EPA legacy database sources of chemical information and presents these data in a consistent format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://java.epa.gov/oppt_chemical_search/",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "2D73C764-6919-404D-8C9B-61869B3330D6",
+            "issued": "2010-01-22",
             "keyword": [
                 "chemicals",
                 "chemical companies",
@@ -9712,45 +9727,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Chemical Data Access Tool",
-            "distribution": [
-                {
-                    "accessURL": "https://java.epa.gov/oppt_chemical_search/",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2010-01-22",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2D73C764-6919-404D-8C9B-61869B3330D6%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2D73C764-6919-404D-8C9B-61869B3330D6%7D"
             ],
-            "accrualPeriodicity": "R/PT1S",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Chemical Data Access Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:saxton.dion@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "2D73C764-6919-404D-8C9B-61869B3330D6",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Chandler Sirmons, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:Sirmons.Chandler@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains information on chemicals that company's produce domestically or import into the United States during the principal reporting year. For the 2012 submission period, reporters provided 2011 manufacturing, processing, and use data and 2010 production volume data for their reportable chemical substances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/chemical-data-reporting",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "91CAEB15-8E6B-48D4-A223-3E2D9B4D4847",
+            "issued": "2009-12-21",
             "keyword": [
                 "substance inventory",
                 "chemical substance inventory",
@@ -9765,45 +9780,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Chemical Data Reporting rule (CDR)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/chemical-data-reporting",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2009-12-21",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B91CAEB15-8E6B-48D4-A223-3E2D9B4D4847%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B91CAEB15-8E6B-48D4-A223-3E2D9B4D4847%7D"
             ],
-            "accrualPeriodicity": "R/P3Y",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Chemical Data Reporting rule (CDR)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Sirmons.Chandler@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Chandler Sirmons, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "91CAEB15-8E6B-48D4-A223-3E2D9B4D4847",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Jeff Santacroce, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:santacroce.jeffrey@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Search tool developed to provide stakeholders access to various TSCA chemicals, and health and safety information. The tool also provides EPA assessments and actions on Chemicals.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/introduction-chemview",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "FE8CC3EA-5D45-43D4-BDBE-4D55C4DFB66A",
+            "issued": "2012-02-11",
             "keyword": [
                 "health and safety data",
                 "tsca chemicals",
@@ -9817,45 +9832,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "ChemView",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca/introduction-chemview",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2012-02-11",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BFE8CC3EA-5D45-43D4-BDBE-4D55C4DFB66A%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFE8CC3EA-5D45-43D4-BDBE-4D55C4DFB66A%7D"
             ],
-            "accrualPeriodicity": "R/PT1S",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "ChemView"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:santacroce.jeffrey@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Jeff Santacroce, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "FE8CC3EA-5D45-43D4-BDBE-4D55C4DFB66A",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:saxton.dion@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains a list of products that carry the Design for the Environment (DfE) label. This mark enables consumers to quickly identify and choose products that can help protect the environment and are safer for families. When you see the DfE logo on a product it means that the DfE scientific review team has screened each ingredient for potential human health and environmental effects and that-based on currently available information,  EPA predictive models,  and expert judgment-the product contains only those ingredients that pose the least concern among chemicals in their class. Product manufacturers who become DfE partners,  and earn the right to display the DfE logo on recognized products,  have invested heavily in research,  development and reformulation to ensure that their ingredients and finished product line up on the green end of the health and environmental spectrum while maintaining or improving product performance. EPA's Design for the Environment Program (DfE) has allowed use of their logo on over 2500 products. These products are formulated from the safest possible ingredients and have reduced the use of \"chemicals of concern\" by hundreds of millions of pounds.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/saferchoice/design-environment-programs-initiatives-and-projects",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "D060AB34-66E2-4BDF-8BC6-6415F55498EF",
+            "issued": "1997-01-01",
             "keyword": [
                 "dfe",
                 "safer product labeling program",
@@ -9885,45 +9900,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Design for the Environment Products (Online Search)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/saferchoice/design-environment-programs-initiatives-and-projects",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "1997-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BD060AB34-66E2-4BDF-8BC6-6415F55498EF%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BD060AB34-66E2-4BDF-8BC6-6415F55498EF%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Design for the Environment Products (Online Search)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:saxton.dion@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "D060AB34-66E2-4BDF-8BC6-6415F55498EF",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:saxton.dion@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains a list of products that carry the Design for the Environment (DfE) label. This mark enables consumers to quickly identify and choose products that can help protect the environment and are safer for families. When you see the DfE logo on a product it means that the DfE scientific review team has screened each ingredient for potential human health and environmental effects and that-based on currently available information,  EPA predictive models,  and expert judgment-the product contains only those ingredients that pose the least concern among chemicals in their class. Product manufacturers who become DfE partners,  and earn the right to display the DfE logo on recognized products,  have invested heavily in research,  development and reformulation to ensure that their ingredients and finished product line up on the green end of the health and environmental spectrum while maintaining or improving product performance. EPA's Design for the Environment Program (DfE) has allowed use of their logo on over 2500 products. These products are formulated from the safest possible ingredients and have reduced the use of \"chemicals of concern\" by hundreds of millions of pounds. A Spanish version of this dataset is available for download at https://www.epa.gov/dfe/pubs/products/list_of_labeled_products.html",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/saferchoice/design-environment-programs-initiatives-and-projects",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "16F788EF-FBC2-463B-9A9F-A4D278B09846",
+            "issued": "1997-01-01",
             "keyword": [
                 "dfe",
                 "safer product labeling program",
@@ -9953,45 +9968,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Design for the Environment Products (Raw Data)",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/saferchoice/design-environment-programs-initiatives-and-projects",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "1997-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B16F788EF-FBC2-463B-9A9F-A4D278B09846%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B16F788EF-FBC2-463B-9A9F-A4D278B09846%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Design for the Environment Products (Raw Data)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:saxton.dion@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "16F788EF-FBC2-463B-9A9F-A4D278B09846",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Gloria Drayton-Miller,US Environmental Protection Agency Office of Chemical Safety and Pollution Prevention, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:Drayton-Miller.Gloria@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The High Production Volume Information System (HPVIS) provides access to select health and environmental effect information on chemicals that are manufactured in exceptionally large amounts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://ofmext.epa.gov/hpvis/ServUserInfo",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "CB6F0D78-3AA8-44EE-ABB4-67A3E72AC76C",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -10005,45 +10020,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "High Production Volume Information System (HPVIS)",
-            "distribution": [
-                {
-                    "accessURL": "https://ofmext.epa.gov/hpvis/ServUserInfo",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BCB6F0D78-3AA8-44EE-ABB4-67A3E72AC76C%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCB6F0D78-3AA8-44EE-ABB4-67A3E72AC76C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "High Production Volume Information System (HPVIS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Drayton-Miller.Gloria@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Gloria Drayton-Miller,US Environmental Protection Agency Office of Chemical Safety and Pollution Prevention, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "CB6F0D78-3AA8-44EE-ABB4-67A3E72AC76C",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)",
+                "hasEmail": "mailto:saxton.dion@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset consists of the non confidential identities of chemical substances submitted under the Toxic Substances Control Act (TSCA).  TSCA was enacted to ensure that chemicals manufactured,  imported,  processed,  or distributed in commerce,  or used or disposed of in the United States do not pose any unreasonable risks to human health or the environment.  EPA adds chemical substances to the TSCA Inventory following EPAs receipt of a Notice of Commencement (NOC) signaling the manufacturers intent to produce a chemical substance that EPA has previously reviewed and approved. Since EPA published the final TSCA Inventory Reporting Rule on December 23,  1977,  the TSCA Inventory has grown to include the identities of over 83, 000 chemical substances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/tsca-inventory",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "8FE10B79-0CA7-403F-92D0-D29FACB0B424",
+            "issued": "2014-08-10",
             "keyword": [
                 "substance inventory",
                 "chemical substance inventory",
@@ -10062,49 +10077,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "TSCA Inventory",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/tsca-inventory",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-08-10",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8FE10B79-0CA7-403F-92D0-D29FACB0B424%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8FE10B79-0CA7-403F-92D0-D29FACB0B424%7D"
             ],
-            "accrualPeriodicity": "R/P6M",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "TSCA Inventory"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:saxton.dion@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dion Saxton, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP) - Office of Pollution Prevention and Toxics (OPPT)"
-            },
-            "identifier": "8FE10B79-0CA7-403F-92D0-D29FACB0B424",
-            "@type": "dcat:Dataset"
+                "fn": "Toni Krasnic, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:Krasnic.Toni@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Toxic Substances Control Act (TSCA) 8(e) Notices and FYI Submissions",
+            "dataQuality": false,
+            "description": "Section 8(e) of the Toxic Substances Control Act (TSCA) requires U.S. chemical manufacturers, importers, processors and distributors to notify EPA within 30 calendar days of new, unpublished information on their chemicals that may lead to a conclusion of substantial risk to human health or to the environment. This data source collects these Section 8(e) notices as well as voluntary submissions (FYI submissions) and organizes them by date.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "Section 8(e) of the Toxic Substances Control Act (TSCA) requires U.S. chemical manufacturers, importers, processors and distributors to notify EPA within 30 calendar days of new, unpublished information on their chemicals that may lead to a conclusion of substantial risk to human health or to the environment. This data source collects these Section 8(e) notices as well as voluntary submissions (FYI submissions) and organizes them by date.",
+            "identifier": "{BD105142-CF54-40DF-9135-5AB7513EFE1B}",
+            "issued": "2014-01-01",
             "keyword": [
                 "substances",
                 "pollutants & contaminants",
@@ -10123,46 +10134,46 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBD105142-CF54-40DF-9135-5AB7513EFE1B%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Toni Krasnic, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:Krasnic.Toni@epa.gov"
-            },
-            "identifier": "{BD105142-CF54-40DF-9135-5AB7513EFE1B}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBD105142-CF54-40DF-9135-5AB7513EFE1B%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BBD105142-CF54-40DF-9135-5AB7513EFE1B%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBD105142-CF54-40DF-9135-5AB7513EFE1B%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Toxic Substances Control Act (TSCA) 8(e) Notices and FYI Submissions"
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
+                "fn": "Mark Seltzer, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:seltzer.mark@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "The Toxic Substances Control Act (TSCA) requires that data be developed on the effect of chemical substances and mixtures on health and the environment. This data source collects the applicable test information on these chemicals submitted by external parties.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/assessing-and-managing-chemicals-under-tsca",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "The Toxic Substances Control Act (TSCA) requires that data be developed on the effect of chemical substances and mixtures on health and the environment. This data source collects the applicable test information on these chemicals submitted by external parties.",
+            "identifier": "{1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D}",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "air",
@@ -10178,46 +10189,46 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Seltzer, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:seltzer.mark@epa.gov"
-            },
-            "identifier": "{1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1CE2B1B7-34E6-49C4-8B13-C7FB8A7C9B1D%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Results of Section 4 Chemical Testing"
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
+                "fn": "Ernest Falke, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:Falke.ernest@Epa.gov"
+            },
+            "dataQuality": false,
+            "description": "The Acute Exposure Guideline Levels Chemical Listing provides a complete listing of risk exposure guidelines from rare exposure to certain chemicals.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/aegl",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/aegl",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "The Acute Exposure Guideline Levels Chemical Listing provides a complete listing of risk exposure guidelines from rare exposure to certain chemicals.",
+            "identifier": "BC3DF16C-9287-454B-92A8-FF7F7788D43D",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "human health",
@@ -10232,42 +10243,46 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2AAE8CF3-F0FB-469A-9264-80EA195C91DF%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ernest Falke, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:Falke.ernest@Epa.gov"
-            },
-            "identifier": "BC3DF16C-9287-454B-92A8-FF7F7788D43D",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BBC3DF16C-9287-454B-92A8-FF7F7788D43D%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBC3DF16C-9287-454B-92A8-FF7F7788D43D%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2AAE8CF3-F0FB-469A-9264-80EA195C91DF%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Acute Exposure Guideline Levels Chemical Listing"
         },
         {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Pamela Johnson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:Johnson.Pam@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Criminal Case Reporting System is designed to record and track criminal case activity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/enforcement/criminal-enforcement",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "1A2BFDAC-A613-4E4F-9B8D-26AC4DA9F686",
+            "issued": "2006-03-06",
             "keyword": [
                 "enforcement",
                 "criminal",
@@ -10276,55 +10291,36 @@
                 "united states",
                 "environment"
             ],
-            "title": "Criminal Case Reporting System",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/enforcement/criminal-enforcement",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2006-03-06",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1A2BFDAC-A613-4E4F-9B8D-26AC4DA9F686%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1A2BFDAC-A613-4E4F-9B8D-26AC4DA9F686%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "contactPoint": {
-                "hasEmail": "mailto:Johnson.Pam@epa.gov",
-                "@type": "vcard:Contact",
-                "fn": "Pamela Johnson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "1A2BFDAC-A613-4E4F-9B8D-26AC4DA9F686",
-            "@type": "dcat:Dataset"
+            "title": "Criminal Case Reporting System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Enforcement and Compliance Information Center - ECIC",
-            "description": "Enforcement and Compliance Information Center - ECIC is a repository of external policy and guidance documents, links to cases and settlements, civil and criminal complaints that are reviewed by HQ and Regional staff.",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": false,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Civil Enforcement (OCE); Office of Criminal Enforcement, Forensics and Training (OCEFT); Office of Site Remediation Enforcement (OSRE); Office of Compliance (OC); Office of Administration and Policy (OAP); Federal Facilities Enforcement Office (FFEO)"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Munsel Norris",
                 "hasEmail": "mailto:norris.munsel@epa.gov"
             },
+            "dataQuality": false,
+            "description": "Enforcement and Compliance Information Center - ECIC is a repository of external policy and guidance documents, links to cases and settlements, civil and criminal complaints that are reviewed by HQ and Regional staff.",
+            "identifier": "4303ff83-2534-4559-adab-3bf3a71ede82",
             "keyword": [
                 "Agriculture",
                 "Air",
@@ -10415,42 +10411,33 @@
                 "names",
                 "offices"
             ],
-            "modified": "2021",
-            "identifier": "4303ff83-2534-4559-adab-3bf3a71ede82",
-            "accessLevel": "public",
             "license": "https://wamssoprd.epa.gov/oam/server/obrareq.cgi?encquery%3DltFBGfd0IFrI%2FiDWE1to9AZRep8fZ0Lj9o82zoaehx5AxOMlQ%2Fy7pxD%2FFpTYEgvC4BlfnOsrTIiEi9GffFdXobe6oB0SkxpItFSBs7roNikWdfd1A1hmkPi81uEavo4RozB%2F%2FEbCslSyMW87LQGcxIV%2F0LqWE3WVXX%2F3DPbM83CexdVVMmea6mlE2OWErEsDgf2%2B1pQ75DeovuGpkSPUzWZVdfhJwlLPQ7NXrqTAvsJrY8nAYC5%2BB%2F1mGvUTcnwi8nb5BGgLt1hrqYrRR1DSuIW5MiiI%2BUU%2Fwnp8C5T6yfCDJfYpAXAZTpi5gDQr%2BQVl%20agentid%3DWebgateEPADomain%20ver%3D1%20crmethod%3D2%26cksum%3Df416c6edf0829fa7f6213bb120f486a9fd42a836",
-            "temporal": "2021-10-01/2022-10-01",
+            "modified": "2021",
+            "primaryitinvestmentuii": "020-000030304",
             "programCode": [
                 "020:000"
             ],
-            "primaryitinvestmentuii": "020-000030304"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Review Framework Manager Database",
-            "description": "The State Review Framework is a primary means by which EPA conducts oversight of three core federal statutes: Clean Air Act, Clean Water Act, and Resource Conservation and Recovery Act. The routine, nationwide review provides a consistent process for evaluating the performance of state, local and EPA compliance and enforcement programs. The overarching goal of the reviews is to ensure fair and consistent enforcement necessary to protect human health and the environment.",
-            "modified": "2021",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "OECA, Office of Compliance"
+                "name": "Office of Civil Enforcement (OCE); Office of Criminal Enforcement, Forensics and Training (OCEFT); Office of Site Remediation Enforcement (OSRE); Office of Compliance (OC); Office of Administration and Policy (OAP); Federal Facilities Enforcement Office (FFEO)"
             },
-            "contactPoint": {
-                "fn": "Jibri Mayo",
-                "hasEmail": "mailto:mayo.jibri@epa.gov",
-                "@type": "vcard:Contact"
+            "temporal": "2021-10-01/2022-10-01",
+            "title": "Enforcement and Compliance Information Center - ECIC"
         },
-            "identifier": "e0b7d4d4-f4d4-4b23-bdd4-72457c3b4a79",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "EPA Category: Mission Sensitive, NARA Category: Critical Infrastructure",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "2021-10-01/2022-09-30",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jibri Mayo",
+                "hasEmail": "mailto:mayo.jibri@epa.gov"
+            },
             "dataQuality": false,
-            "programCode": [
-                "020:000"
-            ],
+            "description": "The State Review Framework is a primary means by which EPA conducts oversight of three core federal statutes: Clean Air Act, Clean Water Act, and Resource Conservation and Recovery Act. The routine, nationwide review provides a consistent process for evaluating the performance of state, local and EPA compliance and enforcement programs. The overarching goal of the reviews is to ensure fair and consistent enforcement necessary to protect human health and the environment.",
+            "identifier": "e0b7d4d4-f4d4-4b23-bdd4-72457c3b4a79",
             "keyword": [
                 "compliance",
                 "Enforcement",
@@ -10458,15 +10445,36 @@
                 "environment",
                 "state oversight",
                 "state framework"
-            ]
-        },
-        {
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021",
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+                "name": "OECA, Office of Compliance"
             },
+            "rights": "EPA Category: Mission Sensitive, NARA Category: Critical Infrastructure",
+            "temporal": "2021-10-01/2022-09-30",
+            "title": "State Review Framework Manager Database"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Moshay Simpson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:simpson.moshay@epa.gov"
+            },
+            "dataQuality": false,
             "description": "This dataset contains selected cases involving EPA's Regional Judicial Officers (RJOs) from 2005 to present. EPA's Regional Judicial Officers (RJOs) perform adjudicatory functions and act as Agency neutrals in administrative cases. EPA's RJOs are senior attorneys with backgrounds in EPA enforcement, general law, or both.",
+            "identifier": "55B4937C-5B14-48B1-BEF7-D248D99F3196",
+            "issued": "2014-01-01",
             "keyword": [
                 "office of enforcement and compliance assurance",
                 "oeca",
@@ -10487,38 +10495,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Selected Regional Judicial Officer Cases, 2005 - Present",
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B55B4937C-5B14-48B1-BEF7-D248D99F3196%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B55B4937C-5B14-48B1-BEF7-D248D99F3196%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Selected Regional Judicial Officer Cases, 2005 - Present"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:simpson.moshay@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Moshay Simpson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "55B4937C-5B14-48B1-BEF7-D248D99F3196",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+                "fn": "Munsel Norris, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:Norris.Munsel@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The Environmental Protection Agency's Enforcement and Compliance History Online (ECHO) website provides customizable and downloadable information about environmental inspections, violations, and enforcement actions for EPA-regulated facilities, like power plants and factories. ECHO advances public information by sharing data related to facility compliance with and regulatory agency activity related to air, hazardous waste, clean water, and drinking water regulations. ECHO offers many user-friendly options to explore data, including:\n1. Facility Search (https://echo.epa.gov/facilities/facility-search?mediaSelected=all): ECHO information is searchable by varied criteria, including location, facility type, and compliance status related to the Clean Air Act, Clean Water Act, Resource Conservation and Recovery Act, and Safe Drinking Water Act. Search results are customizable and downloadable.\n2. Comparative Maps (https://echo.epa.gov/maps/state-comparative-maps) and State Dashboards (https://echo.epa.gov/trends/comparative-maps-dashboards/state-air-dashboard): These tools offer aggregated information about facility compliance status and regulatory agency compliance monitoring and enforcement activity at the national and state level.\n3. Bulk Data Downloads (https://echo.epa.gov/resources/echo-data/data-downloads): One of ECHO's most popular features is the ability to work offline by downloading large data sets. Users can take advantage of the ECHO Exporter, which provides summary information about each facility in a comma-separated format. Additionally, data sets by program also are available as zip files. These are updated weekly as part of the ECHO data refresh.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/enforcement/policy-guidance-publications",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "BF52D6F1-0816-49A1-8F86-C04923D9FBF2",
+            "issued": "2014-01-01",
             "keyword": [
                 "echo",
                 "enforcement",
@@ -10551,45 +10566,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Civil Penalty Policies",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/enforcement/policy-guidance-publications",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BBF52D6F1-0816-49A1-8F86-C04923D9FBF2%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BBF52D6F1-0816-49A1-8F86-C04923D9FBF2%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Civil Penalty Policies"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Norris.Munsel@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Munsel Norris, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+                "fn": "Moshay Simpson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:simpson.moshay@epa.gov"
             },
-            "identifier": "BF52D6F1-0816-49A1-8F86-C04923D9FBF2",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "EPAs Office of Enforcement and Compliance Assurance (OECA)  cases and settlements webpage contains links to selected settlements resolving civil enforcement cases and, in some cases, complaints filed initiating civil judicial and administrative enforcement actions.  Typically, the links are to settlements about which we have issued a press release.  This is not a complete repository of all enforcement actions taken by or on behalf of EPA.  Rather, it represents a subset of enforcement cases, taken civil judicially or administratively, which may be of national interest.  Most of the settlements are civil judicial consent decrees resolving alleged violations of environmental laws (e.g., the Clean Air Act, the Clean Water Act).  In some instances, the website includes significant enforcement actions resolved by the Environmental Appeals Board (EAB). In addition, please note that the cases and settlements webpage does not include:Most administrative enforcement actions; Most civil judicial cases resolving liability under CERCLA; Criminal enforcement matters.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://cfpub.epa.gov/enforcement/cases/",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "4EDAD0CE-D8CB-4C47-B264-8326B468CEC3",
+            "issued": "2014-01-01",
             "keyword": [
                 "office of enforcement and compliance assurance",
                 "oeca",
@@ -10625,45 +10640,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Consent Decrees",
-            "distribution": [
-                {
-                    "accessURL": "https://cfpub.epa.gov/enforcement/cases/",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4EDAD0CE-D8CB-4C47-B264-8326B468CEC3%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4EDAD0CE-D8CB-4C47-B264-8326B468CEC3%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Consent Decrees"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:simpson.moshay@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Moshay Simpson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "4EDAD0CE-D8CB-4C47-B264-8326B468CEC3",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+                "fn": "Mike Hanson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:Hanson.Michael@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The EPA Administrative Enforcement Dockets database contains the electronic dockets for administrative penalty cases filed by EPA Regions and Headquarters. Visitors can browse the dockets by year, by statute, EPA region, or a via a free text search. It should be noted that in some cases, particularly prior to 2008, dockets have not yet been published electronically. For users looking for information not included on the website, please contact the Regional Hearing Clerk where the case was filed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://yosemite.epa.gov/OA/rhc/EPAAdmin.nsf",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "EC25FE3F-183E-41E1-AFCD-62A2417EBB5C",
+            "issued": "2014-01-01",
             "keyword": [
                 "dockets",
                 "enforcement",
@@ -10690,45 +10705,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "EPA Administrative Enforcement Dockets",
-            "distribution": [
-                {
-                    "accessURL": "https://yosemite.epa.gov/OA/rhc/EPAAdmin.nsf",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BEC25FE3F-183E-41E1-AFCD-62A2417EBB5C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BEC25FE3F-183E-41E1-AFCD-62A2417EBB5C%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "EPA Administrative Enforcement Dockets"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Hanson.Michael@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Mike Hanson, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "EC25FE3F-183E-41E1-AFCD-62A2417EBB5C",
-            "@type": "dcat:Dataset"
+                "fn": "Lisa Knight, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:knight.lisa@epa.gov"
             },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "This dataset contains Decisions and Orders originating from EPAs Office of Administrative Law Judges (OALJ), which is an independent office in the Office of the Administrator of the EPA. The Administrative Law Judges conduct hearings and render decisions in proceedings between the EPA and persons, businesses, government entities, and other organizations which are or are alleged to be regulated under environmental laws. Administrative Law Judges preside in enforcement and permit proceedings in accordance with the Administrative Procedure Act. Most enforcement actions initiated by the EPA are for the assessment of civil penalties. The Decisions and Orders are organized into three categories: (1) alphabetical listing by the respondent involved, (2) reverse chronological listing by date, and (3) Decisions and Orders under FIFRA Section 6. This dataset includes Decisions and Orders dating back to 1989 in the Reverse Chronological list, Decisions and Orders dating back to 1997 in the Alphabetical list, and a few Decisions and Orders dating back to 1974 under FIFRA Section 6.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/alj",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "61D37827-1470-453A-BCCD-AB1F32A45B97",
+            "issued": "2014-01-01",
             "keyword": [
                 "office of administrative law judges",
                 "oalj",
@@ -10750,45 +10765,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "EPA Administrative Law Judge Legal Documents",
-            "distribution": [
-                {
-                    "accessURL": "https://www.epa.gov/alj",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B61D37827-1470-453A-BCCD-AB1F32A45B97%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B61D37827-1470-453A-BCCD-AB1F32A45B97%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "EPA Administrative Law Judge Legal Documents"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:knight.lisa@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Lisa Knight, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "61D37827-1470-453A-BCCD-AB1F32A45B97",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+                "fn": "Glendora Spinelli, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:spinelli.glendora@epa.gov"
             },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "The purpose of ICIS is to meet evolving Enforcement and Compliance business needs for EPA and State users by integrating information into a single integrated data system that supports both management and programmatic requirements of the Enforcement and Compliance programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www3.epa.gov/enviro/facts/pcs-icis/search.html",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "E95156F3-39BE-4734-9999-0DFAEE036BA6",
+            "issued": "2002-06-24",
             "keyword": [
                 "icis",
                 "pcs modernization",
@@ -10798,49 +10813,45 @@
                 "united states",
                 "environment"
             ],
-            "title": "Integrated Compliance Information System (ICIS)",
-            "distribution": [
-                {
-                    "accessURL": "https://www3.epa.gov/enviro/facts/pcs-icis/search.html",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "issued": "2002-06-24",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE95156F3-39BE-4734-9999-0DFAEE036BA6%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE95156F3-39BE-4734-9999-0DFAEE036BA6%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Integrated Compliance Information System (ICIS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:spinelli.glendora@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Glendora Spinelli, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
-            },
-            "identifier": "E95156F3-39BE-4734-9999-0DFAEE036BA6",
-            "@type": "dcat:Dataset"
+                "fn": "Kathy Dockery, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
+                "hasEmail": "mailto:Dockery.Kathy@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Permit Compliance System (PCS)",
+            "dataQuality": false,
+            "description": "The Permit Compliance System (PCS) provides information on companies which have been issued permits to discharge waste water into rivers.",
             "distribution": [
                 {
-                    "accessURL": "https://www3.epa.gov/enviro/facts/pcs-icis/search.html",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www3.epa.gov/enviro/facts/pcs-icis/search.html",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "The Permit Compliance System (PCS) provides information on companies which have been issued permits to discharge waste water into rivers.",
+            "identifier": "{E2533854-DAF0-4774-909F-6554F74E4BFD}",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "regulatory & industrial topics",
@@ -10858,39 +10869,38 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2533854-DAF0-4774-909F-6554F74E4BFD%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Enforcement and Compliance Assurance (OECA)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kathy Dockery, U.S. EPA Office of Enforcement and Compliance Assurance (OECA)",
-                "hasEmail": "mailto:Dockery.Kathy@epa.gov"
-            },
-            "identifier": "{E2533854-DAF0-4774-909F-6554F74E4BFD}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE2533854-DAF0-4774-909F-6554F74E4BFD%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2533854-DAF0-4774-909F-6554F74E4BFD%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2533854-DAF0-4774-909F-6554F74E4BFD%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Permit Compliance System (PCS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA iComplaints",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Renee Clark, U.S. EPA Office of Environmental Information (OEI)",
+                "hasEmail": "mailto:Clark.Renee@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The iComplaints system is an enterprise-level COTS (Commercial Off-The-Shelf) product that provides all of the funtionality required to collect, track, manage, process and report on information regarding internal EEO complaints in accordance with several civil rights laws and regulations, to include but not limited to, Title VII of the Civil Rights Act.",
+            "identifier": "51E75568-7D4B-4731-A35F-444CFCFE10C5",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "eeo",
@@ -10900,54 +10910,48 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B51E75568-7D4B-4731-A35F-444CFCFE10C5%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Environmental Information (OEI)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Renee Clark, U.S. EPA Office of Environmental Information (OEI)",
-                "hasEmail": "mailto:Clark.Renee@epa.gov"
-            },
-            "identifier": "51E75568-7D4B-4731-A35F-444CFCFE10C5",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B51E75568-7D4B-4731-A35F-444CFCFE10C5%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B51E75568-7D4B-4731-A35F-444CFCFE10C5%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B51E75568-7D4B-4731-A35F-444CFCFE10C5%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "EPA iComplaints"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "COMPLY Grantee Compliance Database",
-            "description": "The Grantee Compliance Database Comply App is a comprehensive database for summarizing a wide range of grant recipient related activities. In addition to providing an overview of award information related to each grantee recipient, this database also stores historical information related to the recipient's training activities, indirect cost rate negotiations, pre-award certifications, post award monitoring plans, as well as on-site review, off-site review, and technical assistance activities. All advanced monitoring activities must be recorded in the system with an attached report to count as part of the Grantee Compliance Assistance Initiative as outlined in EPA Order 5700.6. The database tracks information on planned and actual On-Site Evaluative, off-Site Evaluative and/or On-Site Technical Assistance Visits conducted by each Grants Management and Program Office in the Agency. The primary objective of this database is to provide accurate information to EPA staff in Headquarters, Regional Program, and Grants Management Offices regarding compliance activities that each Program and Grants Management Office performs or plans to perform during any given calendar year.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Grants and Debarment (OMS/OGD)"
-            },
+            "accessLevel": "non-public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Etheredge",
                 "hasEmail": "mailto:etheredge.william@epa.gov"
             },
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
             "dataQuality": false,
+            "description": "The Grantee Compliance Database Comply App is a comprehensive database for summarizing a wide range of grant recipient related activities. In addition to providing an overview of award information related to each grantee recipient, this database also stores historical information related to the recipient's training activities, indirect cost rate negotiations, pre-award certifications, post award monitoring plans, as well as on-site review, off-site review, and technical assistance activities. All advanced monitoring activities must be recorded in the system with an attached report to count as part of the Grantee Compliance Assistance Initiative as outlined in EPA Order 5700.6. The database tracks information on planned and actual On-Site Evaluative, off-Site Evaluative and/or On-Site Technical Assistance Visits conducted by each Grants Management and Program Office in the Agency. The primary objective of this database is to provide accurate information to EPA staff in Headquarters, Regional Program, and Grants Management Offices regarding compliance activities that each Program and Grants Management Office performs or plans to perform during any given calendar year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
+                    "description": "Overview of award information related to each grantee recipient, this database also stores historical information related to the recipient's\ntraining activities, indirect cost rate negotiations, pre-award certifications, post award monitoring plans, as well as on-site review, off-site review, and technical assistance activities. All advanced monitoring activities must be recorded in the system with an attached report to count as part of the Grantee\nCompliance Assistance Initiative as outlined in EPA Order 5700.6. The database tracks information on planned and actual On-Site Evaluative, off-Site Evaluative and/or On-Site Technical Assistance Visits conducted by each Grants Management and Program Office in the Agency.",
+                    "format": "SharePoint App",
+                    "title": "COMPLY Application URL"
+                }
+            ],
+            "identifier": "f06f7a30-f5e5-4ded-bc3e-767e4c2f6504",
+            "issued": "2021-06-01",
             "keyword": [
                 "Compliance",
                 "environment",
@@ -10958,45 +10962,37 @@
                 "Financial",
                 "Business Data"
             ],
-            "modified": "2022-01-10",
-            "identifier": "f06f7a30-f5e5-4ded-bc3e-767e4c2f6504",
-            "accessLevel": "non-public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "license": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
-            "temporal": "2015-10-01/2022-01-10",
-            "issued": "2021-06-01",
-            "accrualPeriodicity": "R/P1D",
+            "landingPage": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
             "language": [
                 "en-us"
             ],
-            "landingPage": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
-                    "title": "COMPLY Application URL",
-                    "description": "Overview of award information related to each grantee recipient, this database also stores historical information related to the recipient's\ntraining activities, indirect cost rate negotiations, pre-award certifications, post award monitoring plans, as well as on-site review, off-site review, and technical assistance activities. All advanced monitoring activities must be recorded in the system with an attached report to count as part of the Grantee\nCompliance Assistance Initiative as outlined in EPA Order 5700.6. The database tracks information on planned and actual On-Site Evaluative, off-Site Evaluative and/or On-Site Technical Assistance Visits conducted by each Grants Management and Program Office in the Agency.",
-                    "format": "SharePoint App"
-                }
-            ]
+            "license": "https://usepa-7291dac51b2899.sharepoint.com/sites/OARM/comply/comply-sp/#/home",
+            "modified": "2022-01-10",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Grants and Debarment (OMS/OGD)"
+            },
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
+            "temporal": "2015-10-01/2022-01-10",
+            "title": "COMPLY Grantee Compliance Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Environmental Protection Agency Acquisition System",
-            "description": "Automated contract writing and management system with configurable workflow.  EAS is built using a Commercial Off The Shelf Product (PRISM)that also includes the purchase request form and workflow.",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": true,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office Of Mission Support (OMS) - Office of Acquisition Solutions (OAS)"
-            },
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Richard Belles",
-                "hasEmail": "mailto:belles.richard@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:belles.richard@epa.gov"
             },
+            "dataQuality": true,
+            "description": "Automated contract writing and management system with configurable workflow.  EAS is built using a Commercial Off The Shelf Product (PRISM)that also includes the purchase request form and workflow.",
+            "identifier": "e4a720e3-1ce2-4cc3-82cf-646f633a5b3e",
             "keyword": [
                 "Cleanup",
                 "Emergency Response",
@@ -11015,41 +11011,33 @@
                 "purchase request",
                 "requisition"
             ],
-            "modified": "2021-11-24",
-            "identifier": "e4a720e3-1ce2-4cc3-82cf-646f633a5b3e",
-            "accessLevel": "public",
             "license": "https://easinfo.epa.gov/",
-            "temporal": "2010-03/2021-12",
+            "modified": "2021-11-24",
+            "primaryitinvestmentuii": "020-000016231",
             "programCode": [
                 "020:001"
             ],
-            "primaryitinvestmentuii": "020-000016231"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Cross-Media Electronic Reporting Rule",
-            "description": "This system centralizes all data and reporting functions associated with applicants seeking to obtain Cross Media Electronic Reporting Rule CROMERR) certification for systems submitting data to EPA which require an electronic signature , facilitates agency review of those applications, increases accessibility to program information, and increases transparency in program management. This system is implemented as a workflow within the EPA\u2019s Business Application Platform (BAP) and exclusively uses its native capabilities.",
-            "modified": "2021-12-17",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "EPA-OMS-OIM-IEPB"
+                "name": "U.S. EPA Office Of Mission Support (OMS) - Office of Acquisition Solutions (OAS)"
             },
-            "contactPoint": {
-                "fn": "Shirley Miller",
-                "hasEmail": "mailto:miller.shirley@epa.gov",
-                "@type": "vcard:Contact"
+            "temporal": "2010-03/2021-12",
+            "title": "Environmental Protection Agency Acquisition System"
         },
-            "identifier": "75f41ff9-881c-4b42-bafa-204357bb2799",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "2005-10-13/2021-12-17",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shirley Miller",
+                "hasEmail": "mailto:miller.shirley@epa.gov"
+            },
             "dataQuality": false,
-            "programCode": [
-                "020:072"
-            ],
+            "description": "This system centralizes all data and reporting functions associated with applicants seeking to obtain Cross Media Electronic Reporting Rule CROMERR) certification for systems submitting data to EPA which require an electronic signature , facilitates agency review of those applications, increases accessibility to program information, and increases transparency in program management. This system is implemented as a workflow within the EPA\u2019s Business Application Platform (BAP) and exclusively uses its native capabilities.",
+            "identifier": "75f41ff9-881c-4b42-bafa-204357bb2799",
             "keyword": [
                 "Regulatory",
                 "Permits",
@@ -11059,25 +11047,33 @@
                 "CROMERR",
                 "Cross-Media Electronic Reporting Rule",
                 "Electronic Reporting"
-            ]
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021-12-17",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "EPA-OMS-OIM-IEPB"
+            },
+            "temporal": "2005-10-13/2021-12-17",
+            "title": "Cross-Media Electronic Reporting Rule"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EPA Acquisition Forecast Database",
-            "description": "The EPA Acquisition Forecast Database was developed and is used to post the Agency's anticipated requirements and applicable acquisition strategies. ",
+            "accessLevel": "non-public",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": true,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office Of Mission Support (OMS) - Office of Acquisition Solutions (OAS)"
-            },
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Richard Belles",
-                "hasEmail": "mailto:belles.richard@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:belles.richard@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The EPA Acquisition Forecast Database was developed and is used to post the Agency's anticipated requirements and applicable acquisition strategies. ",
+            "identifier": "74b6f85f-2d8a-41f6-8fb9-10f66f2f0353",
             "keyword": [
                 "Cleanup",
                 "Emergency Response",
@@ -11097,34 +11093,38 @@
                 "planning",
                 "contracts"
             ],
-            "modified": "2021-12-15",
-            "identifier": "74b6f85f-2d8a-41f6-8fb9-10f66f2f0353",
-            "accessLevel": "non-public",
-            "rights": "EPA Category: Source Selection Information, NARA Category: Proprietary-Source Selection",
             "license": "https://ofmpub.epa.gov/apex/forecast/f?p=forecast",
-            "temporal": "2017-06/2021-12",
+            "modified": "2021-12-15",
+            "primaryitinvestmentuii": "020-000000088",
             "programCode": [
                 "020:001"
             ],
-            "primaryitinvestmentuii": "020-000000088"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Advanced Utility Metering",
-            "description": "The National Advanced Utility Metering (NAUM) system is used to monitor utility consumption of EPA managed facilities required by the Energy Policy Act of 2005 (EPAct 2005), the Energy Independence and Security Act of 2007 (EISA 2007) and Executive Order 13514, along with other Presidential Memorandums that have established the need for additional water and utility metering.",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "OMS/OA"
+                "name": "U.S. EPA Office Of Mission Support (OMS) - Office of Acquisition Solutions (OAS)"
+            },
+            "rights": "EPA Category: Source Selection Information, NARA Category: Proprietary-Source Selection",
+            "temporal": "2017-06/2021-12",
+            "title": "EPA Acquisition Forecast Database"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
+            "conformsTo": "https://project-open-data.cio.gov/v1.1/schema/",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mr. Jackie Brown",
                 "hasEmail": "mailto:brown.jackie@epa.gov"
             },
-            "bureauCode": [
-                "020:00"
-            ],
             "dataQuality": false,
+            "describedByType": "text/html",
+            "description": "The National Advanced Utility Metering (NAUM) system is used to monitor utility consumption of EPA managed facilities required by the Energy Policy Act of 2005 (EPAct 2005), the Energy Independence and Security Act of 2007 (EISA 2007) and Executive Order 13514, along with other Presidential Memorandums that have established the need for additional water and utility metering.",
+            "identifier": "fc56c95c-e68d-41b6-8686-61cc6796b9cd",
+            "issued": "2020-11-16",
             "keyword": [
                 "Air",
                 "Energy",
@@ -11134,31 +11134,50 @@
                 "Electric",
                 "GAS"
             ],
-            "modified": "2021-11-16",
-            "identifier": "fc56c95c-e68d-41b6-8686-61cc6796b9cd",
-            "accessLevel": "non-public",
-            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2020-11-16/2022-11-16",
-            "issued": "2020-11-16",
-            "accrualPeriodicity": "R/P1D",
+            "landingPage": "https://v18h1n-naum033.aa.ad.epa.gov/Web/Auth?ReturnUrl=/Web/",
             "language": [
                 "en"
             ],
-            "conformsTo": "https://project-open-data.cio.gov/v1.1/schema/",
-            "describedByType": "text/html",
-            "landingPage": "https://v18h1n-naum033.aa.ad.epa.gov/Web/Auth?ReturnUrl=/Web/",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021-11-16",
+            "programCode": [
+                "020:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OMS/OA"
+            },
             "references": [
                 "https://v18h1n-naum033.aa.ad.epa.gov/Web/Auth?ReturnUrl=/Web/"
             ],
-            "programCode": [
-                "020:000"
-            ]
+            "rights": "EPA Category: Confidential Business Information, NARA Category: Proprietary-Manufacturer",
+            "temporal": "2020-11-16/2022-11-16",
+            "title": "National Advanced Utility Metering"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Tribal Consultation Tracking System",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Elias Abunassar, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:abunassar.elias@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Tribal Consultation Opportunities Tracking System (TCOTS) publicizes upcoming and current EPA consultation opportunities for tribal governments and Alaska Native Corporations. The goal of TCOTS is to provide early notification and transparency on EPA consultations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://tcots.epa.gov",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "6B8E6259-95FF-4CFD-AD43-3FBD9E6D0A6C",
+            "issued": "2001-07-25",
             "keyword": [
                 "tcots",
                 "tribal consultation",
@@ -11169,48 +11188,40 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://tcots.epa.gov",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2001-07-25",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Elias Abunassar, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:abunassar.elias@epa.gov"
-            },
-            "identifier": "6B8E6259-95FF-4CFD-AD43-3FBD9E6D0A6C",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://www.epa.gov/tribal",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6B8E6259-95FF-4CFD-AD43-3FBD9E6D0A6C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6B8E6259-95FF-4CFD-AD43-3FBD9E6D0A6C%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://tcots.epa.gov",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://tcots.epa.gov",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
-                }
-            ],
-            "dataQuality": false
+            "title": "Tribal Consultation Tracking System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Fast International Approval and Tracking System",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Sergio Schwimmer, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:schwimmer.sergio@epa.gov"
+            },
+            "dataQuality": false,
             "description": "FIAT, a BAP based database, is the electronic process that tracks and monitors the international travel approval process.",
+            "identifier": "58F6D56D-65EB-479D-B630-3C550C400FA6",
+            "issued": "2014-01-01",
             "keyword": [
                 "travel",
                 "international",
@@ -11221,40 +11232,58 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B58F6D56D-65EB-479D-B630-3C550C400FA6%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Sergio Schwimmer, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:schwimmer.sergio@epa.gov"
-            },
-            "identifier": "58F6D56D-65EB-479D-B630-3C550C400FA6",
-            "accessLevel": "public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B58F6D56D-65EB-479D-B630-3C550C400FA6%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B58F6D56D-65EB-479D-B630-3C550C400FA6%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B58F6D56D-65EB-479D-B630-3C550C400FA6%7D",
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Fast International Approval and Tracking System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "General Assistance Program",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Elias Abunassar, US Environmental Protection Agency",
+                "hasEmail": "mailto:abunassar.elias@epa.gov"
+            },
+            "dataQuality": false,
             "description": "GAP Online is a grant work plan development and reporting information system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://gaponline.epa.gov/ords/gap/f?p=139:4",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/tribal/indian-environmental-general-assistance-program-gap",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/tribal/indian-environmental-general-assistance-program-gap",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "74A869D9-818A-43FB-885F-3CEA0DE3AB2D",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "aieo",
@@ -11271,58 +11300,40 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B74A869D9-818A-43FB-885F-3CEA0DE3AB2D%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Environmental Protection Agency"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Elias Abunassar, US Environmental Protection Agency",
-                "hasEmail": "mailto:abunassar.elias@epa.gov"
-            },
-            "identifier": "74A869D9-818A-43FB-885F-3CEA0DE3AB2D",
-            "accessLevel": "public",
-            "rights": "EPA Category: Deliberative Process Privilege, NARA Category: Legal-Privilege",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B74A869D9-818A-43FB-885F-3CEA0DE3AB2D%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B74A869D9-818A-43FB-885F-3CEA0DE3AB2D%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B74A869D9-818A-43FB-885F-3CEA0DE3AB2D%7D",
+            "rights": "EPA Category: Deliberative Process Privilege, NARA Category: Legal-Privilege",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://gaponline.epa.gov/ords/gap/f?p=139:4",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/tribal/indian-environmental-general-assistance-program-gap",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "title": "General Assistance Program"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/tribal/indian-environmental-general-assistance-program-gap",
-                    "mediaType": "application/octet-stream"
-                }
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "dataQuality": false
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Sergio Schwimmer, U.S. EPA Office of Environmental Information (OEI)",
+                "hasEmail": "mailto:Schwimmer.Sergio@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "International Visitors Reservation and Screening",
+            "dataQuality": false,
             "description": "IVRS collects and tracks dates, times and topics of stateside meetings with International organizations and visitors.",
+            "identifier": "4CF1380B-D515-4D49-905A-66A84F7D110C",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "meetings",
@@ -11334,52 +11345,46 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4CF1380B-D515-4D49-905A-66A84F7D110C%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Environmental Information (OEI)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Sergio Schwimmer, U.S. EPA Office of Environmental Information (OEI)",
-                "hasEmail": "mailto:Schwimmer.Sergio@epa.gov"
-            },
-            "identifier": "4CF1380B-D515-4D49-905A-66A84F7D110C",
-            "accessLevel": "public",
-            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4CF1380B-D515-4D49-905A-66A84F7D110C%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4CF1380B-D515-4D49-905A-66A84F7D110C%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4CF1380B-D515-4D49-905A-66A84F7D110C%7D",
+            "rights": "EPA Category: Personally Identifiable Information (PII), NARA Category: Privacy",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "International Visitors Reservation and Screening"
         },
         {
-            "title": "State Grant Information Technology Application (SGITA)",
-            "description": "The State Grant IT Application (SGITA) was created in response to Grants Policy Issuance (GPI) 11-03, State Grant Workplans and Progress Reports. The policy was developed by the State Grant Workplan Workgroup and was designed 1) enhance accountability for achieving grant performance objectives; 2) ensure that State grants are aligned with the Agency 2019 Strategic Plan; and 3) provide for more consistent performance reporting. To achieve those objectives, the GPI requires that workplans and associated progress reports prominently display three Essential Elements the EPA Strategic Plan Goal; the EPA Strategic Plan Objective; and Workplan Commitments plus time frame. The GPI applies to the fourteen State grant programs previously subject to the State Grant Performance Measures Template. It supplements, but in no way supersedes, existing workplan requirements in 40 C.F.R. Part 35 Subpart A. The effective date of the GPI is October 1, 2012. Awards made under Program Code for State and Tribal Underground Storage Tanks Program utilizing STAG funds are required to submit workplans and progress reports in SGITA. Those awards funded using LUST funds are not applicable to GPI 11-03. If an award has both STAG and LUST funds, those workplans and progress reports must be entered into SGITA. SGITA was developed from a requirement in the GPI stating that an application needed to be created to electronically store workplans and progress reports for the applicable programs. EPA Project Officers are to enter the information into SGITA as frequently as workplans and progress reports are required per the terms and conditions of the grant award. The application is accessible to EPA Personnel, OMB, and State users.",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P4M",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": true,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Mission Support\u202f(OMS)  -- Office of Grants and Debarment"
-            },
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Olayori Oluwo",
-                "hasEmail": "mailto:oluwo.olayori@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:oluwo.olayori@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The State Grant IT Application (SGITA) was created in response to Grants Policy Issuance (GPI) 11-03, State Grant Workplans and Progress Reports. The policy was developed by the State Grant Workplan Workgroup and was designed 1) enhance accountability for achieving grant performance objectives; 2) ensure that State grants are aligned with the Agency 2019 Strategic Plan; and 3) provide for more consistent performance reporting. To achieve those objectives, the GPI requires that workplans and associated progress reports prominently display three Essential Elements the EPA Strategic Plan Goal; the EPA Strategic Plan Objective; and Workplan Commitments plus time frame. The GPI applies to the fourteen State grant programs previously subject to the State Grant Performance Measures Template. It supplements, but in no way supersedes, existing workplan requirements in 40 C.F.R. Part 35 Subpart A. The effective date of the GPI is October 1, 2012. Awards made under Program Code for State and Tribal Underground Storage Tanks Program utilizing STAG funds are required to submit workplans and progress reports in SGITA. Those awards funded using LUST funds are not applicable to GPI 11-03. If an award has both STAG and LUST funds, those workplans and progress reports must be entered into SGITA. SGITA was developed from a requirement in the GPI stating that an application needed to be created to electronically store workplans and progress reports for the applicable programs. EPA Project Officers are to enter the information into SGITA as frequently as workplans and progress reports are required per the terms and conditions of the grant award. The application is accessible to EPA Personnel, OMB, and State users.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://sgita.epa.gov/ords/sgitapub/f?p=SGITAPUB:Home:",
+                    "description": "The State Grant IT Application (SGITA) was created in response to Grants Policy Issuance (GPI) 11-03, State Grant Workplans and Progress Reports. The policy was developed by the State Grant Workplan Workgroup and was designed 1) enhance accountability for achieving grant performance objectives; 2) ensure that State grants are aligned with the Agency 2019 Strategic Plan; and 3) provide for more consistent performance reporting. To achieve those objectives, the GPI requires that workplans and associated progress reports prominently display three Essential Elements: the EPA Strategic Plan Goal; the EPA Strategic Plan Objective; and Workplan Commitments plus time frame. The GPI applies to the fourteen State grant programs previously subject to the State Grant Performance Measures Template. It supplements, but in no way supersedes, existing workplan requirements in 40 C.F.R. Part 35 Subpart A. The effective date of the GPI is October 1, 2012. Awards made under Program Code for State and Tribal Underground Storage Tanks Program utilizing STAG funds are required to submit workplans and progress reports in SGITA. Those awards funded using LUST funds are not applicable to GPI 11-03. If an award has both STAG and LUST funds, those workplans and progress reports must be entered into SGITA\n\nSGITA was developed from a requirement in the GPI stating that an application needed to be created to electronically store workplans and progress reports for the applicable programs. EPA Project Officers are to enter the information into SGITA as frequently as workplans and progress reports are required per the terms and conditions of the grant award. The application is accessible to EPA Personnel, OMB, and State users.",
+                    "title": "SGITA Home"
+                }
+            ],
+            "identifier": "fd45d11c-b236-455a-8ff6-380cc4ff5664",
             "keyword": [
                 "environment",
                 "Washington DC",
@@ -11390,75 +11395,50 @@
                 "EPA Personnel",
                 "State users"
             ],
-            "modified": "2021-08-14",
-            "identifier": "fd45d11c-b236-455a-8ff6-380cc4ff5664",
-            "accessLevel": "public",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "license": "https://sgita.epa.gov/ords/sgitapub/f?p=SGITAPUB:Home:",
-            "temporal": "2020-10-01/2021-10-01",
-            "accrualPeriodicity": "R/P4M",
             "landingPage": "https://sgita.epa.gov/ords/sgitapub/f?p=SGITAPUB:Home:",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://sgita.epa.gov/ords/sgitapub/f?p=SGITAPUB:Home:",
-                    "title": "SGITA Home",
-                    "description": "The State Grant IT Application (SGITA) was created in response to Grants Policy Issuance (GPI) 11-03, State Grant Workplans and Progress Reports. The policy was developed by the State Grant Workplan Workgroup and was designed 1) enhance accountability for achieving grant performance objectives; 2) ensure that State grants are aligned with the Agency 2019 Strategic Plan; and 3) provide for more consistent performance reporting. To achieve those objectives, the GPI requires that workplans and associated progress reports prominently display three Essential Elements: the EPA Strategic Plan Goal; the EPA Strategic Plan Objective; and Workplan Commitments plus time frame. The GPI applies to the fourteen State grant programs previously subject to the State Grant Performance Measures Template. It supplements, but in no way supersedes, existing workplan requirements in 40 C.F.R. Part 35 Subpart A. The effective date of the GPI is October 1, 2012. Awards made under Program Code for State and Tribal Underground Storage Tanks Program utilizing STAG funds are required to submit workplans and progress reports in SGITA. Those awards funded using LUST funds are not applicable to GPI 11-03. If an award has both STAG and LUST funds, those workplans and progress reports must be entered into SGITA\n\nSGITA was developed from a requirement in the GPI stating that an application needed to be created to electronically store workplans and progress reports for the applicable programs. EPA Project Officers are to enter the information into SGITA as frequently as workplans and progress reports are required per the terms and conditions of the grant award. The application is accessible to EPA Personnel, OMB, and State users."
-                }
-            ],
+            "license": "https://sgita.epa.gov/ords/sgitapub/f?p=SGITAPUB:Home:",
+            "modified": "2021-08-14",
             "programCode": [
                 "020:072"
-            ]
-        },
-        {
-            "title": "Laws and Regulations Services (LRS)",
-            "description": "LRS is a catalog of laws relevant to EPA, the regulations that implement those laws, and the EPA programs that oversee those regulations",
-            "modified": "2021",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "United States Environmental Protection Agency (EPA)"
+                "name": "Office of Mission Support\u202f(OMS)  -- Office of Grants and Debarment"
             },
-            "contactPoint": {
-                "fn": "Justin Mattison",
-                "hasEmail": "mailto:mattison.justin@epa.gov",
-                "@type": "vcard:Contact"
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "temporal": "2020-10-01/2021-10-01",
+            "title": "State Grant Information Technology Application (SGITA)"
         },
-            "identifier": "0d18d90b-a358-4948-8fb5-2b72a728b061",
+        {
             "accessLevel": "public",
-            "rights": "LRS is available to the public via web services ",
-            "license": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "2021/2025",
-            "issued": "2015",
-            "accrualPeriodicity": "R/P1W",
-            "language": [
-                "en-us"
-            ],
-            "dataQuality": false,
             "conformsTo": "https://sor.epa.gov/sor_internet/registry/lawsreg/home/overview/home.jsp",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Justin Mattison",
+                "hasEmail": "mailto:mattison.justin@epa.gov"
+            },
+            "dataQuality": false,
             "describedBy": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
             "describedByType": "text/html",
-            "landingPage": "https://sor.epa.gov/sor_internet/registry/lawsreg/home/overview/home.jsp",
-            "references": [
-                "https://sor.epa.gov/sor_internet/registry/lawsreg/home/overview/home.jsp"
-            ],
+            "description": "LRS is a catalog of laws relevant to EPA, the regulations that implement those laws, and the EPA programs that oversee those regulations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
-                    "title": "LRS Web Services",
-                    "description": "The LRS Web Services provide an interface to the System of Registries' Laws and Regulations Registry (LRS). LRS is a catalog of laws relevant to EPA, the regulations that implement those laws, and the EPA programs that oversee those regulations.The statutory and regulatory information is gleaned from the Code of Federal Regulations (CFR), published annually by the Government Publishing Office (GPO).",
-                    "format": "API",
+                    "conformsTo": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
                     "describedBy": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
                     "describedByType": "text/html",
-                    "conformsTo": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2"
+                    "description": "The LRS Web Services provide an interface to the System of Registries' Laws and Regulations Registry (LRS). LRS is a catalog of laws relevant to EPA, the regulations that implement those laws, and the EPA programs that oversee those regulations.The statutory and regulatory information is gleaned from the Code of Federal Regulations (CFR), published annually by the Government Publishing Office (GPO).",
+                    "format": "API",
+                    "title": "LRS Web Services"
                 }
             ],
-            "programCode": [
-                "020:072"
-            ],
+            "identifier": "0d18d90b-a358-4948-8fb5-2b72a728b061",
+            "issued": "2015",
             "keyword": [
                 "Chemicals",
                 "Pesticides",
@@ -11477,46 +11457,51 @@
                 "CFR",
                 "government publishing office",
                 "GPO"
-            ]
-        },
-        {
-            "title": "Reference Data for Analytics",
-            "description": "Collection of reference datasets for analytics applications.  These are lookup tables, crosswalks, and other useful datasets for connecting tables for analytics",
-            "modified": "2021-01-28",
+            ],
+            "landingPage": "https://sor.epa.gov/sor_internet/registry/lawsreg/home/overview/home.jsp",
+            "language": [
+                "en-us"
+            ],
+            "license": "https://sor-lrs-api.epa.gov/lrswebservices/swaggerV2",
+            "modified": "2021",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "OMS-EI/OIM/IAASD"
+                "name": "United States Environmental Protection Agency (EPA)"
             },
-            "contactPoint": {
-                "fn": "David G. Smith",
-                "hasEmail": "mailto:smith.davidg@epa.gov",
-                "@type": "vcard:Contact"
+            "references": [
+                "https://sor.epa.gov/sor_internet/registry/lawsreg/home/overview/home.jsp"
+            ],
+            "rights": "LRS is available to the public via web services ",
+            "temporal": "2021/2025",
+            "title": "Laws and Regulations Services (LRS)"
         },
-            "identifier": "3e6f9173-790f-44a1-93e6-662662bcf67d",
+        {
             "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "bureauCode": [
                 "020:00"
             ],
-            "temporal": "2020/2021",
-            "issued": "2021-01-28",
-            "language": [
-                "en-us"
-            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David G. Smith",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
+            },
             "dataQuality": false,
+            "description": "Collection of reference datasets for analytics applications.  These are lookup tables, crosswalks, and other useful datasets for connecting tables for analytics",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://edap-oms-data-commons.s3.amazonaws.com/analytics-refdata/ACE-Ports.csv",
-                    "format": "C Source File (.c)",
-                    "title": "Data Commons",
                     "description": "Data Commons Reference Datasets",
-                    "mediaType": "text/x-c"
+                    "format": "C Source File (.c)",
+                    "mediaType": "text/x-c",
+                    "title": "Data Commons"
                 }
             ],
-            "programCode": [
-                "020:053"
-            ],
+            "identifier": "3e6f9173-790f-44a1-93e6-662662bcf67d",
+            "issued": "2021-01-28",
             "keyword": [
                 "Boundaries and Base Data",
                 "United States",
@@ -11530,12 +11515,38 @@
                 "Ports",
                 "Codesets",
                 "reference"
-            ]
+            ],
+            "language": [
+                "en-us"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021-01-28",
+            "programCode": [
+                "020:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OMS-EI/OIM/IAASD"
+            },
+            "temporal": "2020/2021",
+            "title": "Reference Data for Analytics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Superfund Query",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:knipschild.shane@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Superfund Query allows users to retrieve data from the Comprehensive Environmental Response, Compensation, and Liability Information System (CERCLIS) database.",
+            "identifier": "F26474DB-5364-4173-89CB-3561096F8D9E",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "emergencies and cleanup topics",
@@ -11548,39 +11559,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF26474DB-5364-4173-89CB-3561096F8D9E%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:knipschild.shane@epa.gov"
-            },
-            "identifier": "F26474DB-5364-4173-89CB-3561096F8D9E",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF26474DB-5364-4173-89CB-3561096F8D9E%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF26474DB-5364-4173-89CB-3561096F8D9E%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF26474DB-5364-4173-89CB-3561096F8D9E%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Superfund Query"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Toxics Release Inventory Chemical Hazard Information Profiles (TRI-CHIP) Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Turk, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:Turk.David@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Toxics Release Inventory (TRI) Chemical Hazard Information Profiles (TRI-CHIP) dataset contains hazard information about the chemicals reported in TRI. Users can use this XML-format dataset to create their own databases and hazard analyses of TRI chemicals. The hazard information is compiled from a series of authoritative sources including the Integrated Risk Information System (IRIS). The dataset is provided as a downloadable .zip file that when extracted provides XML files and schemas for the hazard information tables.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chip-download-page",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chemical-hazard-information-profiles",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chemical-hazard-information-profiles",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "2DA57844-7EC1-4BAC-B521-3017862A1E70",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "chemical",
@@ -11605,57 +11634,68 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2DA57844-7EC1-4BAC-B521-3017862A1E70%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Turk, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:Turk.David@epa.gov"
-            },
-            "identifier": "2DA57844-7EC1-4BAC-B521-3017862A1E70",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2DA57844-7EC1-4BAC-B521-3017862A1E70%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2DA57844-7EC1-4BAC-B521-3017862A1E70%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Toxics Release Inventory Chemical Hazard Information Profiles (TRI-CHIP) Dataset"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2DA57844-7EC1-4BAC-B521-3017862A1E70%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michelle Torreano, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:torreano.michelle@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "Federal Docket Management System.  Includes all information published in rulemaking and non-rulemaking dockets.  Dockets are posted at Regulations.gov.  FDMS is hosted by the eRulemaking PMO at GSA and used by most Federal agencies (including EPA). The eRulemaking PMO had previously been housed in EPA. Was transferred in to GSA in mid-2010s.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chip-download-page",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.fdms.gov",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chemical-hazard-information-profiles",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.fdms.gov",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/toxics-release-inventory-tri-program/tri-chemical-hazard-information-profiles",
+                    "accessURL": "https://www.epa.gov/dockets",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Federal Docket Management System",
-            "description": "Federal Docket Management System.  Includes all information published in rulemaking and non-rulemaking dockets.  Dockets are posted at Regulations.gov.  FDMS is hosted by the eRulemaking PMO at GSA and used by most Federal agencies (including EPA). The eRulemaking PMO had previously been housed in EPA. Was transferred in to GSA in mid-2010s.",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.fdms.gov",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/dockets",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "E2381C0A-1269-4E90-A78F-BACF80409D0C",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "fdms",
@@ -11666,69 +11706,58 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2381C0A-1269-4E90-A78F-BACF80409D0C%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michelle Torreano, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:torreano.michelle@epa.gov"
-            },
-            "identifier": "E2381C0A-1269-4E90-A78F-BACF80409D0C",
-            "accessLevel": "public",
-            "rights": "epa/govt-2: federal docket management system (fdms)",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2381C0A-1269-4E90-A78F-BACF80409D0C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE2381C0A-1269-4E90-A78F-BACF80409D0C%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE2381C0A-1269-4E90-A78F-BACF80409D0C%7D",
+            "rights": "epa/govt-2: federal docket management system (fdms)",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fdms.gov",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "title": "Federal Docket Management System"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fdms.gov",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:smith.davidg@epa.gov"
             },
+            "dataQuality": false,
+            "description": "Brownfields are real property, the expansion, redevelopment, or reuse of which may be complicated by the presence or potential presence of a hazardous substance, pollutant or contaminant.  This dataset shows the locations of sites, facilities and properties that have been contaminated by hazardous materials and are being, or have been, cleaned up under EPA Brownfields cleanup programs.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/dockets",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/enviro/geospatial-data-download-service",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.fdms.gov",
+                    "accessURL": "https://www.epa.gov/brownfields/brownfields-grantee-reporting-assessment-cleanup-and-redevelopment-exchange-system-acres",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/dockets",
+                    "downloadURL": "https://www.epa.gov/brownfields/brownfields-grantee-reporting-assessment-cleanup-and-redevelopment-exchange-system-acres",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACRES - Brownfields Properties",
-            "description": "Brownfields are real property, the expansion, redevelopment, or reuse of which may be complicated by the presence or potential presence of a hazardous substance, pollutant or contaminant.  This dataset shows the locations of sites, facilities and properties that have been contaminated by hazardous materials and are being, or have been, cleaned up under EPA Brownfields cleanup programs.",
+            "identifier": "681ECFBA-5BB4-421F-85F9-4F5CA963F8A3",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "epa",
@@ -11755,57 +11784,51 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B681ECFBA-5BB4-421F-85F9-4F5CA963F8A3%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:smith.davidg@epa.gov"
-            },
-            "identifier": "681ECFBA-5BB4-421F-85F9-4F5CA963F8A3",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B681ECFBA-5BB4-421F-85F9-4F5CA963F8A3%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B681ECFBA-5BB4-421F-85F9-4F5CA963F8A3%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "ACRES - Brownfields Properties"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B681ECFBA-5BB4-421F-85F9-4F5CA963F8A3%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/enviro/geospatial-data-download-service",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Chiu.Kong@epa.gov"
             },
+            "dataQuality": false,
+            "description": "These files contain the publicly available data from the GHG Reporting Program for 2010. This data includes non-confidential data reported by facilities that directly emit GHGs. The files also contain non-confidential information reported by suppliers of fossil fuels and industrial gases.  The files include data in both HTML (human readable) and XML format.   For more information on the GHG Reporting Program and this data, please visit http://epa.gov/ghgreporting",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/brownfields/brownfields-grantee-reporting-assessment-cleanup-and-redevelopment-exchange-system-acres",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/brownfields/brownfields-grantee-reporting-assessment-cleanup-and-redevelopment-exchange-system-acres",
+                    "downloadURL": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Complete 2010 Greenhouse Gas Data",
-            "description": "These files contain the publicly available data from the GHG Reporting Program for 2010. This data includes non-confidential data reported by facilities that directly emit GHGs. The files also contain non-confidential information reported by suppliers of fossil fuels and industrial gases.  The files include data in both HTML (human readable) and XML format.   For more information on the GHG Reporting Program and this data, please visit http://epa.gov/ghgreporting",
+            "identifier": "907B4527-3C65-4782-B438-9402B6AA4012",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "epa",
@@ -11839,51 +11862,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Chiu.Kong@epa.gov"
-            },
-            "identifier": "907B4527-3C65-4782-B438-9402B6AA4012",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B907B4527-3C65-4782-B438-9402B6AA4012%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B907B4527-3C65-4782-B438-9402B6AA4012%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Complete 2010 Greenhouse Gas Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:knipschild.shane@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "The Envirofacts Data Warehouse contains information from select EPA Environmental program office databases and provides access about environmental activities that may affect air, water, and land anywhere in the United States. The Envirofacts Warehouse supports its own web enabled tools as well as a host of other EPA applications.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www3.epa.gov/enviro/",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/ghgreporting/ghg-reporting-program-data-sets",
+                    "accessURL": "https://www3.epa.gov/enviro/",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Envirofacts Data Warehouse",
-            "description": "The Envirofacts Data Warehouse contains information from select EPA Environmental program office databases and provides access about environmental activities that may affect air, water, and land anywhere in the United States. The Envirofacts Warehouse supports its own web enabled tools as well as a host of other EPA applications.",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www3.epa.gov/enviro/",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "715D19E9-E38B-4C55-B250-E0E92E297D42",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "datafinder",
@@ -11914,57 +11943,51 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www3.epa.gov/enviro/",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:knipschild.shane@epa.gov"
-            },
-            "identifier": "715D19E9-E38B-4C55-B250-E0E92E297D42",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B715D19E9-E38B-4C55-B250-E0E92E297D42%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B715D19E9-E38B-4C55-B250-E0E92E297D42%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Envirofacts Data Warehouse"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://www3.epa.gov/enviro/",
-            "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www3.epa.gov/enviro/",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Hessling, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Hessling.Michael@epa.gov"
             },
+            "dataQuality": false,
+            "description": "EPA's Web Taxonomy is a faceted hierarchical vocabulary used to tag web pages with terms from a controlled vocabulary. Tagging enables search and discovery of EPA's Web based information assests. EPA's Web Taxonomy is being provided in Simple Knowledge Organization System (SKOS) format. SKOS is a standard for sharing and linking knowledge organization systems that promises to make Federal terminology resources more interoperable.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www3.epa.gov/enviro/",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www3.epa.gov/enviro/",
+                    "downloadURL": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Web Taxonomy",
-            "description": "EPA's Web Taxonomy is a faceted hierarchical vocabulary used to tag web pages with terms from a controlled vocabulary. Tagging enables search and discovery of EPA's Web based information assests. EPA's Web Taxonomy is being provided in Simple Knowledge Organization System (SKOS) format. SKOS is a standard for sharing and linking knowledge organization systems that promises to make Federal terminology resources more interoperable.",
+            "identifier": "9FC56CC1-2532-455A-9FA9-A58B0B35D304",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "regulatory",
@@ -11988,51 +12011,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Hessling, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Hessling.Michael@epa.gov"
-            },
-            "identifier": "9FC56CC1-2532-455A-9FA9-A58B0B35D304",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9FC56CC1-2532-455A-9FA9-A58B0B35D304%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9FC56CC1-2532-455A-9FA9-A58B0B35D304%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "title": "EPA Web Taxonomy"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/webguide/epas-information-architecture-and-web-taxonomy",
-                    "mediaType": "application/octet-stream"
-                }
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "dataQuality": false
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Zach Scott, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Scott.Zachary@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Grand Traverse Overall Supply Air Monitoring",
+            "dataQuality": false,
             "description": "EPA is conducting soil remediation: contaminated soils are being excavated and hauled offsite to an approved landfill. During soil excavation and backfill activities, we will collect air samples each day to monitor the ambient air for volatile organic compounds (VOCs). At the end of each day, the four summa canisters that have been taking readings will be sent to a lab for analysis. We are measuring approximately 30 different VOCs using the standard lab method TO-15. Results will be compared to the Michigan ambient air standards. Acronyms: AA: Ambient Air EA: Excavation Area PN: Perimeter North PNW: Perimeter Northwest PS: Perimeter South PSW: Perimeter Southwest ppb: Parts per billion RPD: Relative Percent Difference RL: Reporting Limit MDL: Method Detection Limit Qualifier definitions: *: Recovery or RPD exceeds control limits B: Compound was found in the blank and sample. J: Result is less than the RL but greater than or equal to the MDL and the concentration is an approximate value. U: Indicates the analyte was analyzed for but not detected.",
+            "identifier": "F5B83FA8-3382-417B-A0D7-FFE38C37CFD2",
+            "issued": "2014-01-01",
             "keyword": [
                 "superfund",
                 "grand traverse",
@@ -12047,39 +12058,51 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF5B83FA8-3382-417B-A0D7-FFE38C37CFD2%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Zach Scott, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Scott.Zachary@epa.gov"
-            },
-            "identifier": "F5B83FA8-3382-417B-A0D7-FFE38C37CFD2",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF5B83FA8-3382-417B-A0D7-FFE38C37CFD2%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF5B83FA8-3382-417B-A0D7-FFE38C37CFD2%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF5B83FA8-3382-417B-A0D7-FFE38C37CFD2%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Grand Traverse Overall Supply Air Monitoring"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Information Collection Rule Federal Database",
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Water Resources Center, U.S. EPA Office of Water (OW)",
+                "hasEmail": "mailto:center.water-resources@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Information Collection Rule (ICR) Federal database includes research data from an 18-month study of disinfection byproducts and microbial contaminants.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "8F6A6113-925B-405A-BC73-392CB7BFF0B6",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "substances",
@@ -12094,51 +12117,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Water Resources Center, U.S. EPA Office of Water (OW)",
-                "hasEmail": "mailto:center.water-resources@epa.gov"
-            },
-            "identifier": "8F6A6113-925B-405A-BC73-392CB7BFF0B6",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8F6A6113-925B-405A-BC73-392CB7BFF0B6%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8F6A6113-925B-405A-BC73-392CB7BFF0B6%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Information Collection Rule Federal Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Smith.DavidG@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "Error Tracking System is a database used to store & track error notifications sent by users of EPA's web site. ETS is managed by OIC/OEI. OECA's ECHO & OEI Envirofacts use it. Error notifications from EPA's home Page under \"Contact Us\" also uses it.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://archive.epa.gov/enviro/html/icr/web/html/index.html",
+                    "accessURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Error Tracking System",
-            "description": "Error Tracking System is a database used to store & track error notifications sent by users of EPA's web site. ETS is managed by OIC/OEI. OECA's ECHO & OEI Envirofacts use it. Error notifications from EPA's home Page under \"Contact Us\" also uses it.",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "2A9E5357-B564-42E8-AB2A-0DD75DCE4D4F",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "error notifications",
@@ -12149,57 +12178,51 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Smith, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Smith.DavidG@epa.gov"
-            },
-            "identifier": "2A9E5357-B564-42E8-AB2A-0DD75DCE4D4F",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2A9E5357-B564-42E8-AB2A-0DD75DCE4D4F%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2A9E5357-B564-42E8-AB2A-0DD75DCE4D4F%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Error Tracking System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
-            "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Harman, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:harman.john@epa.gov"
             },
+            "dataQuality": false,
+            "description": "The Substance Registry Services (SRS) is the authoritative resource for basic information about substances of interest to the U.S. EPA and its state and tribal partners.  Substances, particularly chemicals, can have many valid synonyms.  For example, toluene, methyl benzene, and phenyl methane, are commonly used names for the same chemical.  EPA programs collect environmental data for this chemical using each of these names, plus others.  This diversity leads to problems when a user is looking for programmatic data for toluene but is unaware that the data is stored under the synonym methyl benzene.  For each substance, the SRS identifies the statutes, EPA programs, as well as organization external to EPA, that track or regulate that substance and the synonym used by that statute, EPA program or external organization.  Besides standardized information for each chemical, such as the Chemical Abstracts Services name and the Chemical Abstracts Number and the EPA Registry Name (the EPA standard name), the SRS also includes additional information, such as molecular weight and molecular formula.  Additionally, an SRS Internal Tracking Number uniquely identifies each substance, enabling cross-walking between synonyms. \n\nEPA is providing a large .ZIP file providing the SRS data in CSV format, and a separate small metadata file in XML containing the field names and definitions.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://oaspub.epa.gov/enviro/ets_grab_error.smart_form",
+                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Substance Identification Information from EPA's Substance Registry",
-            "description": "The Substance Registry Services (SRS) is the authoritative resource for basic information about substances of interest to the U.S. EPA and its state and tribal partners.  Substances, particularly chemicals, can have many valid synonyms.  For example, toluene, methyl benzene, and phenyl methane, are commonly used names for the same chemical.  EPA programs collect environmental data for this chemical using each of these names, plus others.  This diversity leads to problems when a user is looking for programmatic data for toluene but is unaware that the data is stored under the synonym methyl benzene.  For each substance, the SRS identifies the statutes, EPA programs, as well as organization external to EPA, that track or regulate that substance and the synonym used by that statute, EPA program or external organization.  Besides standardized information for each chemical, such as the Chemical Abstracts Services name and the Chemical Abstracts Number and the EPA Registry Name (the EPA standard name), the SRS also includes additional information, such as molecular weight and molecular formula.  Additionally, an SRS Internal Tracking Number uniquely identifies each substance, enabling cross-walking between synonyms. \n\nEPA is providing a large .ZIP file providing the SRS data in CSV format, and a separate small metadata file in XML containing the field names and definitions.",
+            "identifier": "0AEA7FA5-98C2-4175-AE3E-E70947456E86",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "biological",
@@ -12242,51 +12265,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Harman, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:harman.john@epa.gov"
-            },
-            "identifier": "0AEA7FA5-98C2-4175-AE3E-E70947456E86",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0AEA7FA5-98C2-4175-AE3E-E70947456E86%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0AEA7FA5-98C2-4175-AE3E-E70947456E86%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Substance Identification Information from EPA's Substance Registry"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Chiu.Kong@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "This file contains a summary of the publicly available data from the GHG Reporting Program for 2010. This data includes non-confidential data reported by facilities that directly emit GHGs. The files also contain non-confidential information reported by suppliers of fossil fuels and industrial gases. This excel file contains the same information available in the Data Publication Tool. The file contains the most important, high-level information reported by direct emitters and suppliers and can be easily sorted to respond to many common queries.  Please visit https://www.epa.gov/ghgreporting for more information on the data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/sites/production/files/2015-10/ghgp_data_2010_10_7_15.xlsx",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
+                    "accessURL": "https://www.epa.gov/ghgreporting/ghgrp-reported-data",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Summary 2010 Greenhouse Gas Data",
-            "description": "This file contains a summary of the publicly available data from the GHG Reporting Program for 2010. This data includes non-confidential data reported by facilities that directly emit GHGs. The files also contain non-confidential information reported by suppliers of fossil fuels and industrial gases. This excel file contains the same information available in the Data Publication Tool. The file contains the most important, high-level information reported by direct emitters and suppliers and can be easily sorted to respond to many common queries.  Please visit https://www.epa.gov/ghgreporting for more information on the data.",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/ghgreporting/ghgrp-reported-data",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "59A02659-36C4-4B19-B5F5-2E0852C0F929",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "epa",
@@ -12320,57 +12349,51 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B59A02659-36C4-4B19-B5F5-2E0852C0F929%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Chiu.Kong@epa.gov"
-            },
-            "identifier": "59A02659-36C4-4B19-B5F5-2E0852C0F929",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B59A02659-36C4-4B19-B5F5-2E0852C0F929%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B59A02659-36C4-4B19-B5F5-2E0852C0F929%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Summary 2010 Greenhouse Gas Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B59A02659-36C4-4B19-B5F5-2E0852C0F929%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/sites/production/files/2015-10/ghgp_data_2010_10_7_15.xlsx",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Zach Scott, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Scott.Zachary@epa.gov"
             },
+            "dataQuality": false,
+            "description": "The U.S. Environmental Protection Agency (EPA) has collected and reported data on the generation and disposal of waste in the United States for more than 30 years. We use this information to measure the success of waste reduction and recycling programs across the country. Our trash, or municipal solid waste (MSW), is made up of the things we commonly use and then throw away. These materials include items such as packaging, food scraps, grass clippings, sofas, computers, tires, and refrigerators. MSW does not include industrial, hazardous, or construction waste. The data on Materials Discarded in the Municipal Waste Stream, 1960 to 2009, provides estimated data in thousands of tons discarded after recycling and compost recovery for the years 1960, 1970, 1980, 1990, 2000, 2005, 2007, 2008, and 2009. In this data set, discards include combustion with energy recovery. This data table does not include construction & demolition debris, industrial process wastes, or certain other wastes. The \"Other\" category includes electrolytes in batteries and fluff pulp, feces, and urine in disposable diapers. Details may not add to totals due to rounding.",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/ghgreporting/ghgrp-reported-data",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/transforming-waste-tool",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/ghgreporting/ghgrp-reported-data",
+                    "downloadURL": "https://www.epa.gov/transforming-waste-tool",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Materials Discarded in the U.S. Municipal Waste Stream, 1960 to 2009 (in tons)",
-            "description": "The U.S. Environmental Protection Agency (EPA) has collected and reported data on the generation and disposal of waste in the United States for more than 30 years. We use this information to measure the success of waste reduction and recycling programs across the country. Our trash, or municipal solid waste (MSW), is made up of the things we commonly use and then throw away. These materials include items such as packaging, food scraps, grass clippings, sofas, computers, tires, and refrigerators. MSW does not include industrial, hazardous, or construction waste. The data on Materials Discarded in the Municipal Waste Stream, 1960 to 2009, provides estimated data in thousands of tons discarded after recycling and compost recovery for the years 1960, 1970, 1980, 1990, 2000, 2005, 2007, 2008, and 2009. In this data set, discards include combustion with energy recovery. This data table does not include construction & demolition debris, industrial process wastes, or certain other wastes. The \"Other\" category includes electrolytes in batteries and fluff pulp, feces, and urine in disposable diapers. Details may not add to totals due to rounding.",
+            "identifier": "E5DE559C-4258-496E-AA1D-71FCBA48161F",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "materials generation",
@@ -12400,51 +12423,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www.epa.gov/transforming-waste-tool",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Zach Scott, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Scott.Zachary@epa.gov"
-            },
-            "identifier": "E5DE559C-4258-496E-AA1D-71FCBA48161F",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BE5DE559C-4258-496E-AA1D-71FCBA48161F%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BE5DE559C-4258-496E-AA1D-71FCBA48161F%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Materials Discarded in the U.S. Municipal Waste Stream, 1960 to 2009 (in tons)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://www.epa.gov/transforming-waste-tool",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Chiu.Kong@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "This tool to gives you access to greenhouse gas data reported to EPA by large facilities and suppliers in the United States through EPA's Greenhouse Gas Reporting Program. The tool allows you to view data in several formats including maps, tables, charts and graphs for individual facilities or groups of facilities. You can search the data set for individual facilities by name or location or filter the data set by state or county, industry sectors and sub-sectors, annual facility emission thresholds, and greenhouse gas type.  For more information on the GHG Reporting Program and this data, please visit https://www.epa.gov/ghgreporting",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/transforming-waste-tool",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://ghgdata.epa.gov/ghgp/main.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/transforming-waste-tool",
+                    "accessURL": "https://www.epa.gov/ghgreporting",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Greenhouse Gas Data Publication Tool",
-            "description": "This tool to gives you access to greenhouse gas data reported to EPA by large facilities and suppliers in the United States through EPA's Greenhouse Gas Reporting Program. The tool allows you to view data in several formats including maps, tables, charts and graphs for individual facilities or groups of facilities. You can search the data set for individual facilities by name or location or filter the data set by state or county, industry sectors and sub-sectors, annual facility emission thresholds, and greenhouse gas type.  For more information on the GHG Reporting Program and this data, please visit https://www.epa.gov/ghgreporting",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.epa.gov/ghgreporting",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "FE489855-C43D-493B-BF08-6CE2B5E69330",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "epa",
@@ -12476,57 +12505,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFE489855-C43D-493B-BF08-6CE2B5E69330%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kong Chiu, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Chiu.Kong@epa.gov"
-            },
-            "identifier": "FE489855-C43D-493B-BF08-6CE2B5E69330",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFE489855-C43D-493B-BF08-6CE2B5E69330%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BFE489855-C43D-493B-BF08-6CE2B5E69330%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Greenhouse Gas Data Publication Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFE489855-C43D-493B-BF08-6CE2B5E69330%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Harman, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Harman.John@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "The Substance Registry System (SRS) is EPA's central system for information about regulated and monitored substances.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://ghgdata.epa.gov/ghgp/main.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/ghgreporting",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/LandingPage.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/ghgreporting",
+                    "downloadURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/LandingPage.do",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Substance Registry Services (SRS)",
-            "description": "The Substance Registry System (SRS) is EPA's central system for information about regulated and monitored substances.",
+            "identifier": "6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "datafinder",
@@ -12538,57 +12567,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Harman, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Harman.John@epa.gov"
-            },
-            "identifier": "6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Substance Registry Services (SRS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6786D3DA-E9A5-43BD-A5E9-2EEC2E75E78E%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:knipschild.shane@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "Envirofacts integrates information from a variety of EPA's environmental databases. Each of these databases contains information about facilities that are required to report activity to a state or federal system. Using this API, you can retrieve information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/home/overview/home.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/enviro/web-services",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/LandingPage.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://www.epa.gov/enviro/envirofacts-data-service-api",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://ofmpub.epa.gov/sor_internet/registry/substreg/LandingPage.do",
+                    "downloadURL": "https://www.epa.gov/enviro/envirofacts-data-service-api",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EPA Envirofacts API",
-            "description": "Envirofacts integrates information from a variety of EPA's environmental databases. Each of these databases contains information about facilities that are required to report activity to a state or federal system. Using this API, you can retrieve information.",
+            "identifier": "A4EBFA50-EC19-4F00-9866-C09D01B951E0",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "envirofacts",
@@ -12614,57 +12643,62 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://www.epa.gov/enviro/web-services",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Shane Knipschild, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:knipschild.shane@epa.gov"
-            },
-            "identifier": "A4EBFA50-EC19-4F00-9866-C09D01B951E0",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BA4EBFA50-EC19-4F00-9866-C09D01B951E0%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA4EBFA50-EC19-4F00-9866-C09D01B951E0%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "EPA Envirofacts API"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://www.epa.gov/enviro/web-services",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Angelina Hurst, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:hurst.angelina@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "Terminology Services provides tools and services that enable vocabulary development, maintenance and provisioning for the enterprise.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/enviro/web-services",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/searchandretrieve/termsandacronyms/search.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/enviro/envirofacts-data-service-api",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/home/whatisterminology/",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/enviro/envirofacts-data-service-api",
+                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/searchandretrieve/termsandacronyms/search.do",
                     "mediaType": "application/octet-stream"
-                }
-            ],
-            "dataQuality": false
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "Terminology Services",
-            "description": "Terminology Services provides tools and services that enable vocabulary development, maintenance and provisioning for the enterprise.",
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/home/whatisterminology/",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "F180B542-3D54-4CBA-BD71-47EC423ECE65",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "etss",
@@ -12685,62 +12719,57 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF180B542-3D54-4CBA-BD71-47EC423ECE65%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Angelina Hurst, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:hurst.angelina@epa.gov"
-            },
-            "identifier": "F180B542-3D54-4CBA-BD71-47EC423ECE65",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF180B542-3D54-4CBA-BD71-47EC423ECE65%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF180B542-3D54-4CBA-BD71-47EC423ECE65%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Terminology Services"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF180B542-3D54-4CBA-BD71-47EC423ECE65%7D",
-            "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/searchandretrieve/termsandacronyms/search.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Pendleton, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:pendleton.michael@epa.gov"
             },
+            "dataQuality": false,
+            "description": "READ is EPA's authoritative source for information about Agency information resources, including applications/systems, datasets and models. READ is one component of the System of Registries (SoR).",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/home/whatisterminology/",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/systmreg/searchandretrieve/basic/search.do",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/searchandretrieve/termsandacronyms/search.do",
+                    "accessURL": "https://www.epa.gov/read/",
+                    "format": "API",
                     "mediaType": "application/octet-stream"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://iaspub.epa.gov/sor_internet/registry/termreg/home/whatisterminology/",
+                    "downloadURL": "https://www.epa.gov/read/",
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Registry of EPA Applications, Models, and Databases",
-            "description": "READ is EPA's authoritative source for information about Agency information resources, including applications/systems, datasets and models. READ is one component of the System of Registries (SoR).",
+            "identifier": "101513F0-7F51-4CAB-966B-15E7794EA775",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "it system",
@@ -12758,57 +12787,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://ofmpub.epa.gov/sor_internet/registry/systmreg/searchandretrieve/basic/search.do",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Pendleton, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:pendleton.michael@epa.gov"
-            },
-            "identifier": "101513F0-7F51-4CAB-966B-15E7794EA775",
-            "accessLevel": "public",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B101513F0-7F51-4CAB-966B-15E7794EA775%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B101513F0-7F51-4CAB-966B-15E7794EA775%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://ofmpub.epa.gov/sor_internet/registry/systmreg/searchandretrieve/basic/search.do",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://ofmpub.epa.gov/sor_internet/registry/systmreg/searchandretrieve/basic/search.do",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/read/",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
+            "title": "Registry of EPA Applications, Models, and Databases"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/read/",
-                    "mediaType": "application/octet-stream"
-                }
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
             ],
-            "dataQuality": false
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mirza Baig, U.S. EPA Office of Mission Support (OMS)",
+                "hasEmail": "mailto:Baig.Mirza@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Visual Power Data Files for Equal Employment Opportunity (EEO)",
+            "dataQuality": false,
             "description": "The Visual Powerfiles for EEO is an information management and reporting system designed to meet Federal requirements for the agency's Equal Employment Opportunity (EEO) function in accordance with several civil rights laws and regulations. EPA OCR is responsible for monitoring and evaluating the effectiveness of affirmative programs, conducting workforce ad hoc anlysis and summaries for data related to applicant flow, new hires, promotions, awards, training, disciplinary actions, and selection procedures., and developing plans and actions for an annual Management Directive 715.",
+            "identifier": "B31A8D34-444C-4FE9-B6B4-58818D5902B6",
+            "issued": "2014-01-01",
             "keyword": [
                 "eeo",
                 "environment",
@@ -12817,39 +12828,58 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB31A8D34-444C-4FE9-B6B4-58818D5902B6%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Mission Support (OMS)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mirza Baig, U.S. EPA Office of Mission Support (OMS)",
-                "hasEmail": "mailto:Baig.Mirza@epa.gov"
-            },
-            "identifier": "B31A8D34-444C-4FE9-B6B4-58818D5902B6",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB31A8D34-444C-4FE9-B6B4-58818D5902B6%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BB31A8D34-444C-4FE9-B6B4-58818D5902B6%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
```

