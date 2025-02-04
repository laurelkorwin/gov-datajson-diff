# Change History for epa.json (Part 12)

### Changes from 31606f9 to dd2190f (Part 2/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB31A8D34-444C-4FE9-B6B4-58818D5902B6%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Visual Power Data Files for Equal Employment Opportunity (EEO)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Facility Registry Service (FRS)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Smith, US Environmental Protection Agency",
+                "hasEmail": "mailto:Smith.DavidG@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Facility Registry Service (FRS) provides an integrated source of comprehensive (air, water, and waste) environmental information about facilities across EPA, states, tribes and other \"places\" of environmental interest such as schools and landfills.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/frs",
+                    "title": "FRS Home Page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/frs/frs-data-resources",
+                    "description": "Links to FRS data available as Web Services, Prepackaged Downloads, and Custom Downloads.",
+                    "title": "FRS Data Resources Page"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/frs/frs-documentation",
+                    "description": "Information about data sources, flows, schemas, dictionaries, and standards.",
+                    "title": "FRS Documentation Page"
+                }
+            ],
+            "identifier": "B158161D-F639-4A93-BF7C-D454C80F7C92",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -12865,66 +12895,50 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB158161D-F639-4A93-BF7C-D454C80F7C92%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2013-09-24",
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
-                "fn": "David Smith, US Environmental Protection Agency",
-                "hasEmail": "mailto:Smith.DavidG@epa.gov"
-            },
-            "identifier": "B158161D-F639-4A93-BF7C-D454C80F7C92",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB158161D-F639-4A93-BF7C-D454C80F7C92%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BB158161D-F639-4A93-BF7C-D454C80F7C92%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB158161D-F639-4A93-BF7C-D454C80F7C92%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/frs",
-                    "title": "FRS Home Page"
+            "title": "Facility Registry Service (FRS)"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/frs/frs-data-resources",
-                    "title": "FRS Data Resources Page",
-                    "description": "Links to FRS data available as Web Services, Prepackaged Downloads, and Custom Downloads."
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Justin Mattison",
+                "hasEmail": "mailto:mattison.justin@epa.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset provides authoritative names for federally recognized tribes as defined by the Bureau of Indian Affairs.  EPA maintains this data (1978 - Present) and makes it available via the TRIBES Names Services",
+            "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/frs/frs-documentation",
-                    "title": "FRS Documentation Page",
-                    "description": "Information about data sources, flows, schemas, dictionaries, and standards."
+                    "describedBy": "https://www.epa.gov/sites/production/files/2015-06/documents/tribalidenversion2.2a_10_02_14.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "List of BIA tribe names, BIA codes (where we have them), and EPA identifiers",
+                    "downloadURL": "https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx",
+                    "format": "This is a link to a spreadsheet that contains the BIA Tribe Names, BIA tribe codes, and EPA internal identifiers for each tribe.  Tribe names are tracked from 1978 - present.",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tribe Entity Mapping"
                 }
             ],
-            "dataQuality": false
-        },
-        {
-            "title": "Federally Recognized Tribes",
-            "description": "This dataset provides authoritative names for federally recognized tribes as defined by the Bureau of Indian Affairs.  EPA maintains this data (1978 - Present) and makes it available via the TRIBES Names Services",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "EPA Office of Mission Support "
-            },
-            "contactPoint": {
-                "fn": "Justin Mattison",
-                "hasEmail": "mailto:mattison.justin@epa.gov",
-                "@type": "vcard:Contact"
-            },
+            "identifier": "3f4bd197-b312-4a0c-b179-6ea798f52ac4",
+            "issued": "2021-01-28",
             "keyword": [
                 "Human",
                 "Management",
@@ -12935,48 +12949,42 @@
                 "tribes",
                 "indian"
             ],
-            "modified": "2021-02-11",
-            "identifier": "3f4bd197-b312-4a0c-b179-6ea798f52ac4",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
-            "bureauCode": [
-                "020:00"
-            ],
-            "temporal": "1978-01-01/2021-04-13",
-            "issued": "2021-01-28",
-            "accrualPeriodicity": "R/P1Y",
+            "landingPage": "https://www.epa.gov/data-standards/tribes-services-tribal-identifier-data-standard#file-150427",
             "language": [
                 "en-us"
             ],
-            "dataQuality": true,
-            "landingPage": "https://www.epa.gov/data-standards/tribes-services-tribal-identifier-data-standard#file-150427",
-            "references": [
-                "http://www.exchangenetwork.net/data-exchange/epa-tribal-identification-tribes/"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx",
-                    "format": "This is a link to a spreadsheet that contains the BIA Tribe Names, BIA tribe codes, and EPA internal identifiers for each tribe.  Tribe names are tracked from 1978 - present.",
-                    "title": "Tribe Entity Mapping",
-                    "description": "List of BIA tribe names, BIA codes (where we have them), and EPA identifiers",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "describedBy": "https://www.epa.gov/sites/production/files/2015-06/documents/tribalidenversion2.2a_10_02_14.pdf",
-                    "describedByType": "application/pdf"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
+            "modified": "2021-02-11",
+            "primaryitinvestmentuii": "020-000016006",
             "programCode": [
                 "020:042"
             ],
-            "primaryitinvestmentuii": "020-000016006"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. EPA Office of General Counsel (OGC)"
+                "name": "EPA Office of Mission Support "
+            },
+            "references": [
+                "http://www.exchangenetwork.net/data-exchange/epa-tribal-identification-tribes/"
+            ],
+            "temporal": "1978-01-01/2021-04-13",
+            "title": "Federally Recognized Tribes"
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
+                "fn": "Andrew Salzman, U.S. EPA Office of General Counsel (OGC)",
+                "hasEmail": "mailto:salzman.andrew@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Office of General Counsel (OGC) has an ongoing business process engineering and business process automation initiative which has helped the office reduce administrative labor costs while increasing employee effectiveness. Supporting this effort is a system of automated routines accessible through a \"portal' interface called \"OGC Dashboard.\" The dashboard helps OGC track work progress, legal case load, written work products such as legal briefs and advice, and scheduling processes such as employee leave plans (via calendar) and travel compensatory time off.",
+            "identifier": "836352F6-A37C-4FDD-9C98-F7501C454273",
+            "issued": "2014-01-01",
             "keyword": [
                 "legal",
                 "environment",
@@ -12984,38 +12992,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "OGC Dashboard",
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
+                "name": "U.S. EPA Office of General Counsel (OGC)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B836352F6-A37C-4FDD-9C98-F7501C454273%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B836352F6-A37C-4FDD-9C98-F7501C454273%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "OGC Dashboard"
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
-                "hasEmail": "mailto:salzman.andrew@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Andrew Salzman, U.S. EPA Office of General Counsel (OGC)"
+                "fn": "Michael P Murphy, U.S. EPA Office of General Counsel (OGC)",
+                "hasEmail": "mailto:Murphy.MichaelP@epa.gov"
             },
-            "identifier": "836352F6-A37C-4FDD-9C98-F7501C454273",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of General Counsel (OGC)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "Case and Administrative Support Tools (CAST) is the secure portion of the Office of General Counsel (OGC) Dashboard business process automation tool used to help reduce office administrative labor costs while increasing employee effectiveness. CAST supports business functions which rely on and store Privacy Act sensitive data (PII). Specific business processes included in CAST (and respective PII) are: -Civil Rights Cast Tracking (name, partial medical history, summary of case, and case correspondance). -Employment Law Case Tracking (name, summary of case). -Federal Tort Claims Act Incident Tracking (name, summary of incidents). -Ethics Program Support Tools and Tracking (name, partial financial history). -Summer Honors Application Tracking (name, home address, telephone number, employment history). -Workforce Flexibility Initiative Support Tools (name, alternative workplace phone number). -Resource and Personnel Management Support Tools (name, partial employment and financial history).",
+            "identifier": "4296E18F-AC00-4F64-929A-34173D146387",
+            "issued": "2014-01-01",
             "keyword": [
                 "legal",
                 "environment",
@@ -13023,35 +13031,38 @@
                 "united states",
                 "environment"
             ],
-            "title": "Case and Administrative Support Tools",
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
+                "name": "U.S. EPA Office of General Counsel (OGC)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B4296E18F-AC00-4F64-929A-34173D146387%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B4296E18F-AC00-4F64-929A-34173D146387%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Case and Administrative Support Tools"
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
-                "hasEmail": "mailto:Murphy.MichaelP@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Michael P Murphy, U.S. EPA Office of General Counsel (OGC)"
-            },
-            "identifier": "4296E18F-AC00-4F64-929A-34173D146387",
-            "@type": "dcat:Dataset"
+                "fn": "Matt Martin, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:martin.matt@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Toxicity Reference Database",
+            "dataQuality": false,
             "description": "The Toxicity Reference Database (ToxRefDB) contains approximately 30 years and $2 billion worth of animal studies. ToxRefDB allows scientists and the interested public to search and download thousands of animal toxicity testing results for hundreds of chemicals that were previously found only in paper documents. Currently, there are 474 chemicals in ToxRefDB, primarily the data rich pesticide active ingredients, but the number will continue to expand.",
+            "identifier": "8D1F4382-424A-492E-8D2E-ADC046140BBB",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -13064,74 +13075,37 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Matt Martin, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:martin.matt@epa.gov"
-            },
-            "identifier": "8D1F4382-424A-492E-8D2E-ADC046140BBB",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8D1F4382-424A-492E-8D2E-ADC046140BBB%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8D1F4382-424A-492E-8D2E-ADC046140BBB%7D"
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
+            "title": "Toxicity Reference Database"
         },
         {
-            "title": "Characterization Factors for Construction Material EPD Indicators (ISO21930-LCIA-US) v0.1",
-            "description": "This dataset contains characterization factors (CFs) for the five mandatory life cycle impact assessment (LCIA) categories required in ISO 21930:2017: \n1.\tGreenhouse gases (GHG), which is incorrectly named \u2018GWP\u2019 in the standard,\n2.\tOzone Depletion Potential (ODP),\n3.\tEutrophication Potential (EP),\n4.\tAcidification Potential (AP), and\n5.\tPhotochemical Ozone Formation Potential (POCP)\nThese CFs are appropriate for use with life cycle inventory data for activities occurring within the United States. \nThe short name for the dataset is ISO21930-LCIA-US v0.1.\nThe characterization factors, with the exception of GHGs, are identical to the those currently in TRACI v2.1 for the corresponding impact categories. The four TRACI v2.1 impact categories have the same names as ISO 21930:2017 with the exception of POCP, which is called \u201csmog formation\u201d in TRACI v2.1. The characterization factors for GHGs are the 100-year (GWP-100) GWPs from the International Panel for Climate Change (IPCC)\u2019s 5th Assessment Report (AR5) report. \nThe names for the chemicals, release contexts, units and IDs are from the Federal LCA Elementary Flow List (FEDEFL) v1.2. These datasets were created using the LCIA Formatter v1.1.2 (https://github.com/USEPA/LCIAformatter).\nFormats\nDatasets are provided in simple tables in Excel, in the openLCA JSON-LD format using Federal LCA Commons standards, and in Apache parquet format.  The fields in the Excel and identical parquet versions use the LCIAmethod format fields: https://github.com/USEPA/LCIAformatter/blob/master/format%20specs/LCIAmethod.md\n1.\tZip archives of JSON files in the JSON-LD schema: a file type associated with the openLCA schema. Two JSON-LD versions are provided. \na.\t\u201cISO21930-LCIA-USv0.1_noflows_json-ld.zip\u201d is without flow objects. \nb.\t\u201cISO21930-LCIA-USv0.1_wprefflows_json-ld.zip\u201d is with flow objects of preferred flows from the FEDEFL.\nSee usage notes below. \n2.\tExcel and parquet: tabular format according to schema from the LCIA formatter, with additional fields added:\no\t\u201csource_method\u201d: indicates the original method source for the indicator (e.g., TRACI 2.1 or IPCC)\no\t\u201csource_indicator\u201d: indicates the name of the indicator in its original form (e.g. Smog Formation)\no\t\u201ccategory\u201d: indicates the desired parent folder name for the impact category (shown as \u201cEPA EPD in Figure 1)\nUsage\nGenerally, in all formats, the CFs can be multiplied by kg (or unit specified in the denominator) of the relevant chemical emitted to calculate the potential impact value for a given impact category for that relevant chemical. If no CF exists for a chemical in a given impact category, it is not considered to have an impact in that category.\nThe parquet format is most efficient for import into applications or scripts using languages like Python and R.\nThe Zip archives of JSON-LD files can be loaded into openLCA or other LCA or EPD software supporting that format. When loaded into openLCA (via JSON-LD), the method shows as a separate impact assessment method. Individual indicators are categorized within the EPA EPD category.\nFor introduction to importing a dataset into openLCA we recommend this training video from the National Renewable Energy Laboratory. https://youtu.be/YLao5jC5b_0?si=H0SNZ_ufOwInkgCF&t=48\nThe version with no flows is designed to import in a database that already has FEDEFL elementary flows or no more modeling is to be done that would use any new flows. It will only create the LCIA method.\nThe version with flows can be imported into a new \u2018empty\u2019 database and it will create not just the LCIA method but all associated flows and more basic objects like units and flow properties. It can be used when no process data that you wish to model has been created yet and/or if you want to have a full import of all relevant elementary flows.\n",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "020:00"
             ],
-            "dataQuality": true,
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Chemical Safety and Pollution Prevention"
-            },
+            "conformsTo": "https://greendelta.github.io/olca-schema/",
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Low Embodied Carbon Team",
-                "hasEmail": "mailto:embodiedcarbon@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:embodiedcarbon@epa.gov"
             },
-            "keyword": [
-                "Air",
-                "Water",
-                "Impact",
-                "United States",
-                "environment",
-                "LCIA",
-                "Environmental product declarations",
-                "Low embodied carbon",
-                "carbon label"
-            ],
-            "modified": "2024-04-26",
-            "identifier": "9bf03ab6-dd13-4d5a-a92e-b33f9d77a100",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2000-01-01/2030-01-01",
-            "issued": "2024-04",
-            "accrualPeriodicity": "R/P6M",
-            "language": [
-                "en-us"
-            ],
-            "conformsTo": "https://greendelta.github.io/olca-schema/",
+            "dataQuality": true,
             "describedBy": "https://github.com/USEPA/LCIAformatter/blob/master/format%20specs/LCIAmethod.md",
-            "landingPage": "https://www.epa.gov/greenerproducts/tools-resources",
+            "description": "This dataset contains characterization factors (CFs) for the five mandatory life cycle impact assessment (LCIA) categories required in ISO 21930:2017: \n1.\tGreenhouse gases (GHG), which is incorrectly named \u2018GWP\u2019 in the standard,\n2.\tOzone Depletion Potential (ODP),\n3.\tEutrophication Potential (EP),\n4.\tAcidification Potential (AP), and\n5.\tPhotochemical Ozone Formation Potential (POCP)\nThese CFs are appropriate for use with life cycle inventory data for activities occurring within the United States. \nThe short name for the dataset is ISO21930-LCIA-US v0.1.\nThe characterization factors, with the exception of GHGs, are identical to the those currently in TRACI v2.1 for the corresponding impact categories. The four TRACI v2.1 impact categories have the same names as ISO 21930:2017 with the exception of POCP, which is called \u201csmog formation\u201d in TRACI v2.1. The characterization factors for GHGs are the 100-year (GWP-100) GWPs from the International Panel for Climate Change (IPCC)\u2019s 5th Assessment Report (AR5) report. \nThe names for the chemicals, release contexts, units and IDs are from the Federal LCA Elementary Flow List (FEDEFL) v1.2. These datasets were created using the LCIA Formatter v1.1.2 (https://github.com/USEPA/LCIAformatter).\nFormats\nDatasets are provided in simple tables in Excel, in the openLCA JSON-LD format using Federal LCA Commons standards, and in Apache parquet format.  The fields in the Excel and identical parquet versions use the LCIAmethod format fields: https://github.com/USEPA/LCIAformatter/blob/master/format%20specs/LCIAmethod.md\n1.\tZip archives of JSON files in the JSON-LD schema: a file type associated with the openLCA schema. Two JSON-LD versions are provided. \na.\t\u201cISO21930-LCIA-USv0.1_noflows_json-ld.zip\u201d is without flow objects. \nb.\t\u201cISO21930-LCIA-USv0.1_wprefflows_json-ld.zip\u201d is with flow objects of preferred flows from the FEDEFL.\nSee usage notes below. \n2.\tExcel and parquet: tabular format according to schema from the LCIA formatter, with additional fields added:\no\t\u201csource_method\u201d: indicates the original method source for the indicator (e.g., TRACI 2.1 or IPCC)\no\t\u201csource_indicator\u201d: indicates the name of the indicator in its original form (e.g. Smog Formation)\no\t\u201ccategory\u201d: indicates the desired parent folder name for the impact category (shown as \u201cEPA EPD in Figure 1)\nUsage\nGenerally, in all formats, the CFs can be multiplied by kg (or unit specified in the denominator) of the relevant chemical emitted to calculate the potential impact value for a given impact category for that relevant chemical. If no CF exists for a chemical in a given impact category, it is not considered to have an impact in that category.\nThe parquet format is most efficient for import into applications or scripts using languages like Python and R.\nThe Zip archives of JSON-LD files can be loaded into openLCA or other LCA or EPD software supporting that format. When loaded into openLCA (via JSON-LD), the method shows as a separate impact assessment method. Individual indicators are categorized within the EPA EPD category.\nFor introduction to importing a dataset into openLCA we recommend this training video from the National Renewable Energy Laboratory. https://youtu.be/YLao5jC5b_0?si=H0SNZ_ufOwInkgCF&t=48\nThe version with no flows is designed to import in a database that already has FEDEFL elementary flows or no more modeling is to be done that would use any new flows. It will only create the LCIA method.\nThe version with flows can be imported into a new \u2018empty\u2019 database and it will create not just the LCIA method but all associated flows and more basic objects like units and flow properties. It can be used when no process data that you wish to model has been created yet and/or if you want to have a full import of all relevant elementary flows.\n",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13154,21 +13128,65 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "references": [
-                "https://downloads.regulations.gov/EPA-HQ-OPPT-2024-0075-0002/content.pdf"
+            "identifier": "9bf03ab6-dd13-4d5a-a92e-b33f9d77a100",
+            "issued": "2024-04",
+            "keyword": [
+                "Air",
+                "Water",
+                "Impact",
+                "United States",
+                "environment",
+                "LCIA",
+                "Environmental product declarations",
+                "Low embodied carbon",
+                "carbon label"
+            ],
+            "landingPage": "https://www.epa.gov/greenerproducts/tools-resources",
+            "language": [
+                "en-us"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2024-04-26",
+            "primaryitinvestmentuii": "020-000030304",
             "programCode": [
                 "020:085"
             ],
-            "primaryitinvestmentuii": "020-000030304"
-        },
-        {
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development"
+                "name": "Office of Chemical Safety and Pollution Prevention"
+            },
+            "references": [
+                "https://downloads.regulations.gov/EPA-HQ-OPPT-2024-0075-0002/content.pdf"
+            ],
+            "temporal": "2000-01-01/2030-01-01",
+            "title": "Characterization Factors for Construction Material EPD Indicators (ISO21930-LCIA-US) v0.1"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Linda Harwell",
+                "hasEmail": "mailto:Harwell.linda@epa.gov"
+            },
+            "dataQuality": true,
+            "describedByType": "text/csv",
             "description": "The Environmental Monitoring and Assessment Program (EMAP) was a national research program run by EPA\u2019s Office of Research and Development from 1990 to 2008 to develop the tools necessary to monitor and assess the status and trends of national ecological resources. Initially, resources included estuaries and coastal waters, wadeable streams, lakes, wetlands, forests, agroecosystems, arid areas, and landscape ecology. Later, this was narrowed down to just the aquatic resources. EMAP collected field data from 1990 to 2006. EMAP's goal was to develop the scientific understanding for translating environmental monitoring data from multiple spatial and temporal scales into assessments of current ecological condition and forecasts of future risks to our natural resources. EMAP aimed to advance the science of ecological monitoring and ecological risk assessment, guide national monitoring with improved scientific understanding of ecosystem integrity and dynamics, and demonstrate multi-agency monitoring through large regional projects. EMAP developed indicators to monitor the condition of ecological resources. EMAP also investigated designs that addressed the acquisition, aggregation, and analysis of multiscale and multitier data. Monitoring of the nation\u2019s aquatic resources is now being routinely conducted by the National Aquatic Resource Surveys, run by EPA\u2019s Office of Water.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data from the US EPA's Environmental Monitoring and Assessment Program, 1990-2006",
+                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/NHEERL/EMAP_archive1990-2006.zip",
+                    "format": "text/csv",
+                    "mediaType": "application/zip",
+                    "title": "EMAP_archive1990-2006"
+                }
+            ],
+            "identifier": "40C37FCC-7D79-4FD6-BDBF-29127BD9B606",
+            "issued": "2006-12-31",
             "keyword": [
                 "environmental monitoring",
                 "environmental assessment",
@@ -13179,24 +13197,23 @@
                 "wetlands",
                 "U.S."
             ],
-            "title": "Environmental Monitoring and Assessment Program (EMAP)",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "description": "Data from the US EPA's Environmental Monitoring and Assessment Program, 1990-2006",
-                    "title": "EMAP_archive1990-2006",
-                    "format": "text/csv",
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://edg.epa.gov/data/PUBLIC/ORD/NHEERL/EMAP_archive1990-2006.zip",
-                    "@type": "dcat:Distribution"
-                }
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2008-06-30",
+            "programCode": [
+                "020:079"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Research and Development"
+            },
+            "references": [
+                "https://archive.epa.gov/emap/archive-emap/web/html/index.html"
             ],
+            "spatial": "USA",
             "temporal": "1990/2006",
-            "describedByType": "text/csv",
-            "modified": "2008-06-30",
-            "dataQuality": true,
             "theme": [
                 "monitoring",
                 "estuaries",
@@ -13205,39 +13222,22 @@
                 " lakes",
                 " wetlands"
             ],
+            "title": "Environmental Monitoring and Assessment Program (EMAP)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "020:00"
             ],
-            "issued": "2006-12-31",
-            "references": [
-                "https://archive.epa.gov/emap/archive-emap/web/html/index.html"
-            ],
-            "spatial": "USA",
-            "programCode": [
-                "020:079"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:Harwell.linda@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Linda Harwell"
-            },
-            "identifier": "40C37FCC-7D79-4FD6-BDBF-29127BD9B606",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Surplus Precipitation",
-            "description": "Surplus Precipitation (mm): precipitation minus potential evaporation within catchment",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
-            },
-            "contactPoint": {
                 "fn": "Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:weber.marc@epa.gov"
             },
+            "dataQuality": true,
+            "description": "Surplus Precipitation (mm): precipitation minus potential evaporation within catchment",
+            "identifier": "04760b79-3aae-407a-a830-f0dd04c90739",
             "keyword": [
                 "Ecosystem",
                 "environment",
@@ -13299,23 +13299,34 @@
                 "NHDPlus V21",
                 "Precipitation"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "dataQuality": true,
-            "modified": "2021",
-            "identifier": "04760b79-3aae-407a-a830-f0dd04c90739",
-            "accessLevel": "public",
             "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2021-09-09/2021-09-09",
+            "modified": "2021",
             "programCode": [
                 "020:096"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Environmental Protection Agency, Office of Research and Development, National Health and Environmental Effects Research Laboratory (NHEERL)"
+            },
+            "temporal": "2021-09-09/2021-09-09",
+            "title": "Surplus Precipitation"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ToxCast Phase I",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:judson.richard@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Background: Chemical toxicity testing is being transformed by advances in biology and computer modeling,  concerns over animal use and the thousands of environmental chemicals lacking toxicity data. EPA's ToxCast program aims to address these concerns by screening and prioritizing chemicals for potential human toxicity using in vitro assays and in silico approaches. Objectives: This project aims to evaluate the use of in vitro assays for understanding the types of molecular and pathway perturbations caused by environmental chemicals and to build initial prioritization models of in vivo toxicity. Methods: We tested 309 mostly pesticide active chemicals in 467 assays across 9 technologies,  including high-throughput cell-free assays and cell-based assays in multiple human primary cells and cell lines,  plus rat primary hepatocytes. Both individual and composite scores for effects on genes and pathways were analyzed. Results: Chemicals display a broad spectrum of activity at the molecular and pathway levels. Many expected interactions are seen,  including endocrine and xenobiotic metabolism enzyme activity. Chemicals range in promiscuity across pathways,  from no activity to affecting dozens of pathways. We find a statistically significant inverse association between the number of pathways perturbed by a chemical at low in vitro concentrations and the lowest in vivo dose at which a chemical causes toxicity. We also find associations between a small set in vitro assays and rodent liver lesion formation. Conclusions: This approach promises to provide meaningful data on the thousands of untested environmental chemicals,  and to guide targeted testing of environmental contaminants.",
+            "identifier": "227B16A3-AEE1-4724-A91B-D4119F5A2C1B",
+            "issued": "2014-01-01",
             "keyword": [
                 "chemical safety",
                 "chemical safety research",
@@ -13334,38 +13345,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "identifier": "227B16A3-AEE1-4724-A91B-D4119F5A2C1B",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B227B16A3-AEE1-4724-A91B-D4119F5A2C1B%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B227B16A3-AEE1-4724-A91B-D4119F5A2C1B%7D"
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
+            "title": "ToxCast Phase I"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Interactive Chemical Safety for Sustainablity Toxicity Forecaster Dashboard",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Matt Martin, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:martin.matt@epa.gov"
+            },
+            "dataQuality": false,
             "description": "EPA researchers have been using advances in computational toxicology to address lack of data on the thousands of chemicals. EPA released chemical data on 1,800 chemicals. The 1,800 chemicals were screened in more than 800 rapid, automated tests (called high-throughput screening assays) to determine potential human health effects.  The data is available through the interactive Chemical Safety for Sustainability Dashboards (iCSS dashboard) and the complete data sets are also available for download.",
+            "identifier": "9E05E004-0752-4881-B1EF-27456E0EE6CA",
+            "issued": "2014-01-01",
             "keyword": [
                 "chemical safety",
                 "chemical safety research",
@@ -13387,38 +13398,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Matt Martin, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:martin.matt@epa.gov"
-            },
-            "identifier": "9E05E004-0752-4881-B1EF-27456E0EE6CA",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9E05E004-0752-4881-B1EF-27456E0EE6CA%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9E05E004-0752-4881-B1EF-27456E0EE6CA%7D"
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
+            "title": "Interactive Chemical Safety for Sustainablity Toxicity Forecaster Dashboard"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Exposure Forecaster",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Wambaugh, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:wambaugh.john@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Exposure Forecaster Database (ExpoCastDB) is EPA's database for aggregating chemical exposure information and can be used to help with chemical exposure predictions. The database currently includes biomonitoring exposure data from three studies: the American Healthy Homes Survey, the First National Environmental Health Survey of Child Care Centers and the Children's Total Exposure to Persistent Pesticides and Other Persistent Organic Pollutants study. Data include the amounts of chemicals found in food, drinking water, air, dust indoor surfaces and urine. The database will eventually include high-throughput exposure predictions for thousands of chemicals based on manufacture and use information. EPA researchers developed high-throughput exposure models to predict exposures for 1,763 chemicals using production volume, environmental fate and transport models, and a simple indicator of consumer product use.The model is being improved by adding more refined indoor and consumer use information since these are also large determinants of exposure. As these models are refined and more exposure data is collected, it will be added to ExpoCastDB.",
+            "identifier": "33778226-2C82-4EFE-A310-1225F2911A07",
+            "issued": "2014-01-01",
             "keyword": [
                 "chemical safety",
                 "chemical safety research",
@@ -13442,38 +13453,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John Wambaugh, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:wambaugh.john@epa.gov"
-            },
-            "identifier": "33778226-2C82-4EFE-A310-1225F2911A07",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B33778226-2C82-4EFE-A310-1225F2911A07%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B33778226-2C82-4EFE-A310-1225F2911A07%7D"
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
+            "title": "Exposure Forecaster"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Distributed Structure Searchable Toxicity",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Tony Williams, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:williams.antony@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Distributed Structure Searchable Toxicity (DSSTox) online resource provides high quality chemical structures and annotations in association with toxicity data. It helps to build a data foundation for improved structure-activity relationships and predictive toxicology. DSSTox publishes summarized chemical activity representations for structure-activity modeling and provides a structure browser. This tool also houses the chemical inventories for the ToxCast and Tox21 projects.",
+            "identifier": "0E749283-2A82-489B-A90D-067686928631",
+            "issued": "2014-01-01",
             "keyword": [
                 "chemical safety",
                 "chemical safety research",
@@ -13501,38 +13512,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tony Williams, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:williams.antony@epa.gov"
-            },
-            "identifier": "0E749283-2A82-489B-A90D-067686928631",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B0E749283-2A82-489B-A90D-067686928631%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B0E749283-2A82-489B-A90D-067686928631%7D"
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
+            "title": "Distributed Structure Searchable Toxicity"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Consumer Product Category Database",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:judson.richard@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Chemical and Product Categories database (CPCat) catalogs the use of over 40,000 chemicals and their presence in different consumer products. The chemical use information is compiled from multiple sources while product information is gathered from publicly available Material Safety Data Sheets (MSDS). EPA researchers are evaluating the possibility of expanding the database with additional product and use information.",
+            "identifier": "90CDFB11-E94E-4E84-942C-5B3D2B5ED0CD",
+            "issued": "2014-01-01",
             "keyword": [
                 "sample",
                 "chemical safety",
@@ -13559,38 +13570,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "identifier": "90CDFB11-E94E-4E84-942C-5B3D2B5ED0CD",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B90CDFB11-E94E-4E84-942C-5B3D2B5ED0CD%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B90CDFB11-E94E-4E84-942C-5B3D2B5ED0CD%7D"
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
+            "title": "Consumer Product Category Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Aggregated Computational Toxicology Online Resource",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
+                "hasEmail": "mailto:judson.richard@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Aggregated Computational Toxicology Online Resource (AcTOR) is EPA's online aggregator of all the public sources of chemical toxicity data. ACToR aggregates data from over 1,000 public sources on over 500,000 chemicals and is searchable by chemical name, other identifiers and by chemical structure. It can be used to query a specific chemical and find all publicly available hazard, exposure and risk assessment data. It also provides access to EPA's ToxCast, ToxRefDB, DSSTox, Dashboard and DSSTox data.",
+            "identifier": "46942636-82FB-46BD-B044-52EFEC632D00",
+            "issued": "2014-01-01",
             "keyword": [
                 "chemical safety",
                 "chemical safety research",
@@ -13614,38 +13625,38 @@
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
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Richard Judson, U.S. EPA Office of Research and Development (ORD) - National Center for Computational Toxicology (NCCT)",
-                "hasEmail": "mailto:judson.richard@epa.gov"
-            },
-            "identifier": "46942636-82FB-46BD-B044-52EFEC632D00",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B46942636-82FB-46BD-B044-52EFEC632D00%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B46942636-82FB-46BD-B044-52EFEC632D00%7D"
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
+            "title": "Aggregated Computational Toxicology Online Resource"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Ecotoxicology Database (ECOTOX)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jennifer Olker, ORD-CCTE-GLTED-TTB",
+                "hasEmail": "mailto:olker.jennifer@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Ecotoxicology Database (ECOTOX) provides information on effects of single chemicals to ecologically-relevant species.",
+            "identifier": "B68D31D1-D035-4678-8B0C-324CC433DBD4",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -13660,46 +13671,46 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB68D31D1-D035-4678-8B0C-324CC433DBD4%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jennifer Olker, ORD-CCTE-GLTED-TTB",
-                "hasEmail": "mailto:olker.jennifer@epa.gov"
-            },
-            "identifier": "B68D31D1-D035-4678-8B0C-324CC433DBD4",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BB68D31D1-D035-4678-8B0C-324CC433DBD4%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB68D31D1-D035-4678-8B0C-324CC433DBD4%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BB68D31D1-D035-4678-8B0C-324CC433DBD4%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Ecotoxicology Database (ECOTOX)"
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
+                "fn": "Katie Paul-Friedman, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
+                "hasEmail": "mailto:CCTE@epa.gov"
+            },
+            "dataQuality": false,
+            "description": "ToxCast is used as a cost-effective approach for efficiently prioritizing the toxicity testing of thousands of chemicals. It uses data from state-of-the-art high throughput screening (HTS) bioassay and builds computational models to forecast potential chemical toxicity in humans. ToxRefDB stores data related to ToxCast.",
             "distribution": [
                 {
-                    "accessURL": "https://www.epa.gov/comptox-tools/exploring-toxcast-data",
                     "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/comptox-tools/exploring-toxcast-data",
                     "mediaType": "text/csv"
                 }
             ],
-            "description": "ToxCast is used as a cost-effective approach for efficiently prioritizing the toxicity testing of thousands of chemicals. It uses data from state-of-the-art high throughput screening (HTS) bioassay and builds computational models to forecast potential chemical toxicity in humans. ToxRefDB stores data related to ToxCast.",
+            "identifier": "94ADB175-265C-494D-A25A-1BAF8501A274",
+            "issued": "2014-01-01",
             "keyword": [
                 "substances",
                 "chemicals",
@@ -13715,39 +13726,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B94ADB175-265C-494D-A25A-1BAF8501A274%7D",
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
-                "fn": "Katie Paul-Friedman, U.S. EPA Office of Chemical Safety and Pollution Prevention (OCSPP)",
-                "hasEmail": "mailto:CCTE@epa.gov"
-            },
-            "identifier": "94ADB175-265C-494D-A25A-1BAF8501A274",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B94ADB175-265C-494D-A25A-1BAF8501A274%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B94ADB175-265C-494D-A25A-1BAF8501A274%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B94ADB175-265C-494D-A25A-1BAF8501A274%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "ToxCast/ToxRefDB"
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
+                "fn": "ECOTOX Support, U.S. EPA Office of Research and Development (ORD)",
+                "hasEmail": "mailto:ecotox.support@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The PCB Residue Effects (PCBRes) Database was developed to assist scientists and risk assessors in correlating PCB and dioxin-like compound residues with toxic effects. The purpose is to develop PCB critical residue values for fish, mammals and birds, especially as these relate to aquatic and aquatic-dependent species.",
+            "identifier": "C01775F2-A45E-4367-BE93-9629C82F6872",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -13762,39 +13773,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC01775F2-A45E-4367-BE93-9629C82F6872%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ECOTOX Support, U.S. EPA Office of Research and Development (ORD)",
-                "hasEmail": "mailto:ecotox.support@epa.gov"
-            },
-            "identifier": "C01775F2-A45E-4367-BE93-9629C82F6872",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BC01775F2-A45E-4367-BE93-9629C82F6872%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC01775F2-A45E-4367-BE93-9629C82F6872%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC01775F2-A45E-4367-BE93-9629C82F6872%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
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
+                "fn": "TSCA Hotline, U.S. EPA Office of Solid Waste and Emergency Response (OSWER)",
+                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Polychlorinated Biphenyls (PCB) Transformer Registration Database tracks geographic and dated information of registered PCB transformers.",
+            "identifier": "CDE0CD61-4C9A-4288-92C4-7D9BAAAD480D",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "environmental media topics",
@@ -13807,39 +13818,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCDE0CD61-4C9A-4288-92C4-7D9BAAAD480D%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Solid Waste and Emergency Response (OSWER)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "TSCA Hotline, U.S. EPA Office of Solid Waste and Emergency Response (OSWER)",
-                "hasEmail": "mailto:tsca-hotline@epamail.epa.gov"
-            },
-            "identifier": "CDE0CD61-4C9A-4288-92C4-7D9BAAAD480D",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCDE0CD61-4C9A-4288-92C4-7D9BAAAD480D%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BCDE0CD61-4C9A-4288-92C4-7D9BAAAD480D%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BCDE0CD61-4C9A-4288-92C4-7D9BAAAD480D%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Polychlorinated Biphenyls (PCB) Transformer Registration Database"
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
+                "fn": "Chad Thompson, U.S. EPA Office of Research and Development (ORD)",
+                "hasEmail": "mailto:thompson.chad@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Physiological Parameters Database for Older Adults is available for download and contains physiological parameters values for healthy older human adults (age 60 and older), as well as data for some individuals with adverse health conditions that may relate to environmental exposure.  The information in this database was collected from review of peer-review published papers.",
+            "identifier": "864CD515-C7A4-48FF-9DBC-7C4164DC2FBD",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "human health",
@@ -13851,39 +13862,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B864CD515-C7A4-48FF-9DBC-7C4164DC2FBD%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Chad Thompson, U.S. EPA Office of Research and Development (ORD)",
-                "hasEmail": "mailto:thompson.chad@epa.gov"
-            },
-            "identifier": "864CD515-C7A4-48FF-9DBC-7C4164DC2FBD",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B864CD515-C7A4-48FF-9DBC-7C4164DC2FBD%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B864CD515-C7A4-48FF-9DBC-7C4164DC2FBD%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B864CD515-C7A4-48FF-9DBC-7C4164DC2FBD%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Physiological Parameters Database for Older Adults"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Health and Environmental Research Online (HERO) database",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "US EPA - HERO, U.S. EPA Office of Research and Development (ORD)",
+                "hasEmail": "mailto:hero@epa.gov"
+            },
+            "dataQuality": false,
             "description": "HERO contains the key studies EPA uses to develop environmental risk assessments for the public. EPA uses risk assessments to characterize the nature and magnitude of health risks to humans and the ecosystem from pollutants and chemicals in the environment.",
+            "identifier": "8E982CE9-B802-4A3B-A4FB-7BD7785A9813",
+            "issued": "2014-01-01",
             "keyword": [
                 "environment",
                 "environment",
@@ -13891,42 +13902,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8E982CE9-B802-4A3B-A4FB-7BD7785A9813%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "US EPA - HERO, U.S. EPA Office of Research and Development (ORD)",
-                "hasEmail": "mailto:hero@epa.gov"
-            },
-            "identifier": "8E982CE9-B802-4A3B-A4FB-7BD7785A9813",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8E982CE9-B802-4A3B-A4FB-7BD7785A9813%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8E982CE9-B802-4A3B-A4FB-7BD7785A9813%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8E982CE9-B802-4A3B-A4FB-7BD7785A9813%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Health and Environmental Research Online (HERO) database"
         },
         {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
-            },
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bob Sonawane, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)",
+                "hasEmail": "mailto:sonawane.bob@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Database of Physiological Parameters for Early Life Rats and Mice provides information based on scientific literature about physiological parameters.  Modelers are encouraged to use the database as a starting point for researching age-specific parameter values needed in their models.",
+            "identifier": "8059DD6E-85B6-43F6-B042-4A889D2CE1F7",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "research",
@@ -13942,41 +13950,41 @@
                 "united states",
                 "health"
             ],
-            "title": "Database of Physiological Parameters for Early Life Rats and Mice",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2009-06-23",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B8059DD6E-85B6-43F6-B042-4A889D2CE1F7%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B8059DD6E-85B6-43F6-B042-4A889D2CE1F7%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Database of Physiological Parameters for Early Life Rats and Mice"
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
-                "hasEmail": "mailto:sonawane.bob@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Bob Sonawane, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
+                "fn": "Dahnish Shams, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)",
+                "hasEmail": "mailto:shams.dahnish@epa.gov"
             },
-            "identifier": "8059DD6E-85B6-43F6-B042-4A889D2CE1F7",
-            "@type": "dcat:Dataset"
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
-            },
-            "accessLevel": "public",
+            "dataQuality": false,
             "description": "EPA?s Integrated Risk Information System (IRIS) is a compilation of electronic reports on specific substances found in the environment and their potential to cause human health effects.",
+            "identifier": "6D68C3EC-8136-40AA-893E-13407355302A",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "human health",
@@ -13988,38 +13996,41 @@
                 "united states",
                 "health"
             ],
-            "title": "Integrated Risk Information System (IRIS)",
             "language": [
                 "en-US"
             ],
-            "issued": "2014-01-01",
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-31",
-            "dataQuality": false,
-            "bureauCode": [
-                "020:00"
+            "programCode": [
+                "020:072"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
+            },
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6D68C3EC-8136-40AA-893E-13407355302A%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6D68C3EC-8136-40AA-893E-13407355302A%7D"
             ],
-            "accrualPeriodicity": "irregular",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "programCode": [
-                "020:072"
+            "title": "Integrated Risk Information System (IRIS)"
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
-                "hasEmail": "mailto:shams.dahnish@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Dahnish Shams, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
-            },
-            "identifier": "6D68C3EC-8136-40AA-893E-13407355302A",
-            "@type": "dcat:Dataset"
+                "fn": "Technical Information Staff, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)",
+                "hasEmail": "mailto:nceadc.comment@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Database of Sources of Environmental Releases of Dioxin-Like Compounds in the United States",
+            "dataQuality": false,
             "description": "The Database of Sources of Environmental Releases of Dioxin-like Compounds in the United States was developed by EPA to be a repository of certain specific chlorinated dibenzo-p-dioxin/dibenzofuran (CDD/CDF) emissions data from all known sources in the US.  The database contains information that can be analyzed to track emissions of CDD/CDF over time, compare specific profiles between and among source categories, and develop source specific emission factors that can then be used to develop emission estimates.",
+            "identifier": "{5454AA68-9042-467D-B323-02D30FB2F50A}",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -14031,39 +14042,39 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5454AA68-9042-467D-B323-02D30FB2F50A%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Technical Information Staff, U.S. EPA Office of Research and Development (ORD) - National Center for Environmental Assessment (NCEA)",
-                "hasEmail": "mailto:nceadc.comment@epa.gov"
-            },
-            "identifier": "{5454AA68-9042-467D-B323-02D30FB2F50A}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B5454AA68-9042-467D-B323-02D30FB2F50A%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5454AA68-9042-467D-B323-02D30FB2F50A%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B5454AA68-9042-467D-B323-02D30FB2F50A%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Database of Sources of Environmental Releases of Dioxin-Like Compounds in the United States"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Human Exposure Database System (HEDS)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Carry Croghan, U.S. EPA Office of Research and Development (ORD) - Center for Environmental Measurement and Modeling",
+                "hasEmail": "mailto:Croghan.Carry@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Human Exposure Database System (HEDS) provides public access to data sets, documents, and metadata from EPA on human exposure. It is primarily intended for scientists involved in human exposure studies or work requiring such data.",
+            "identifier": "47138AA0-2BCA-4E6F-84F8-6741C5BFFB2C",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "substances",
@@ -14076,38 +14087,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2011-11-30",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD) - Center for Environmental Measurement and Modeling"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Carry Croghan, U.S. EPA Office of Research and Development (ORD) - Center for Environmental Measurement and Modeling",
-                "hasEmail": "mailto:Croghan.Carry@epa.gov"
-            },
-            "identifier": "47138AA0-2BCA-4E6F-84F8-6741C5BFFB2C",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B47138AA0-2BCA-4E6F-84F8-6741C5BFFB2C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B47138AA0-2BCA-4E6F-84F8-6741C5BFFB2C%7D"
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
+            "title": "Human Exposure Database System (HEDS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Consolidated Human Activities Database (CHAD)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kristin Isaacs, U.S. EPA Office of Research and Development (ORD) - National Exposure Research Laboratory (NERL)",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Consolidated Human Activity Database (CHAD) contains data obtained from human activity studies that were collected at city, state, and national levels. CHAD is intended to be an input file for exposure/intake dose modeling and/or statistical analysis.",
+            "identifier": "{25B6EC2E-51D5-4691-A4C6-8249268DBEB3}",
+            "issued": "2014-01-01",
             "keyword": [
                 "datafinder",
                 "human health",
@@ -14119,39 +14130,47 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B25B6EC2E-51D5-4691-A4C6-8249268DBEB3%7D",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Exposure Research Laboratory (NERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kristin Isaacs, U.S. EPA Office of Research and Development (ORD) - National Exposure Research Laboratory (NERL)",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "identifier": "{25B6EC2E-51D5-4691-A4C6-8249268DBEB3}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B25B6EC2E-51D5-4691-A4C6-8249268DBEB3%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B25B6EC2E-51D5-4691-A4C6-8249268DBEB3%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B25B6EC2E-51D5-4691-A4C6-8249268DBEB3%7D",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Consolidated Human Activities Database (CHAD)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Toxicity/Residue Database",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Colleen Elonen, U.S. EPA Office of Research and Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)",
+                "hasEmail": "mailto:elonen.colleen@epa.gov"
+            },
+            "dataQuality": false,
             "description": "A toxicity/tissue residue database for aquatic organisms exposed to inorganic and organic chemicals. This database is a resource for use in the systematic investigation of hypotheses related to effect/residue relationships.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://archive.epa.gov/med/med_archive_03/web/html/tox_residue.html",
+                    "format": "API",
+                    "mediaType": "application/octet-stream"
+                }
+            ],
+            "identifier": "20A061F0-3B16-4C4D-AC1C-397FA2F152F8",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "air",
@@ -14162,47 +14181,62 @@
                 "united states",
                 "environment"
             ],
+            "landingPage": "https://archive.epa.gov/med/med_archive_03/web/html/tox_residue.html",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "1905-07-06",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Research and Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Colleen Elonen, U.S. EPA Office of Research and Development (ORD) - National Health and Environmental Effects Research Laboratory (NHEERL)",
-                "hasEmail": "mailto:elonen.colleen@epa.gov"
-            },
-            "identifier": "20A061F0-3B16-4C4D-AC1C-397FA2F152F8",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B20A061F0-3B16-4C4D-AC1C-397FA2F152F8%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B20A061F0-3B16-4C4D-AC1C-397FA2F152F8%7D"
             ],
+            "spatial": "-180.0,18.0,-66.0,72.0",
+            "title": "Toxicity/Residue Database"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "landingPage": "https://archive.epa.gov/med/med_archive_03/web/html/tox_residue.html",
-            "spatial": "-180.0,18.0,-66.0,72.0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the population and housing unit density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the 2010 US Census data (See Supplementary Info for Glossary of Terms). Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit.   The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://archive.epa.gov/med/med_archive_03/web/html/tox_residue.html",
-                    "mediaType": "application/octet-stream",
-                    "format": "API"
-                }
-            ],
-            "dataQuality": false
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
+                    "format": "API",
+                    "title": "LakeCat Dataset"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Housing Unit and Population Density",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "This dataset represents the population and housing unit density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the 2010 US Census data (See Supplementary Info for Glossary of Terms). Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit.   The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
+                    "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                    "format": "Comma-Separated Values (.csv)",
+                    "mediaType": "text/csv",
+                    "title": "2010 US Census Housing Unit and Population Density"
+                }
+            ],
+            "identifier": "BA42DA59-6F0F-4F21-9306-CEDBD29ADE63",
+            "issued": "2015-04-23",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14264,70 +14298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=BA42DA59-6F0F-4F21-9306-CEDBD29ADE63"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Housing Unit and Population Density"
         },
-            "identifier": "BA42DA59-6F0F-4F21-9306-CEDBD29ADE63",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the road density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the road density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "2010 US Census Housing Unit and Population Density",
-                    "description": "This dataset represents the population and housing unit density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the 2010 US Census data (See Supplementary Info for Glossary of Terms). Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit.   The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "2010 US Census Road Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "D3FDB46C-9EF8-4848-AE53-495DB3F058A9",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=BA42DA59-6F0F-4F21-9306-CEDBD29ADE63"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Road Density",
-            "description": "This dataset represents the road density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14389,70 +14423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=D3FDB46C-9EF8-4848-AE53-495DB3F058A9"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Road Density"
         },
-            "identifier": "D3FDB46C-9EF8-4848-AE53-495DB3F058A9",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the application of nitrogen within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based data published in EPA EnviroAtlas. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the application of nitrogen within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based data published in EPA EnviroAtlas. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "2010 US Census Road Density",
-                    "description": "This dataset represents the road density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Agricultural Nitrogen Inputs"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "799414E7-AE12-4785-B444-7786AE9D6489",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=D3FDB46C-9EF8-4848-AE53-495DB3F058A9"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Nitrogen Inputs",
-            "description": "This dataset represents the application of nitrogen within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based data published in EPA EnviroAtlas. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14514,70 +14548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=799414E7-AE12-4785-B444-7786AE9D6489"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Nitrogen Inputs"
         },
-            "identifier": "799414E7-AE12-4785-B444-7786AE9D6489",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the base flow index values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The bfi (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the base flow index values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The bfi (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Agricultural Nitrogen Inputs",
-                    "description": "This dataset represents the application of nitrogen within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based data published in EPA EnviroAtlas. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Base Flow Index"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "F50445F4-99B8-46E7-BF1B-A75D3320E52A",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=799414E7-AE12-4785-B444-7786AE9D6489"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Base Flow Index",
-            "description": "This dataset represents the base flow index values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The bfi (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14639,70 +14673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=F50445F4-99B8-46E7-BF1B-A75D3320E52A"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Base Flow Index"
         },
-            "identifier": "F50445F4-99B8-46E7-BF1B-A75D3320E52A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents canal density within individual, local and accumulated upstream catchments for NHDPlusV2 Waterbodies.  Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents canal density within individual, local and accumulated upstream catchments for NHDPlusV2 Waterbodies.  Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Base Flow Index",
-                    "description": "This dataset represents the base flow index values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The bfi (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Canal Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "e0398045-0643-492e-960c-d882b6519585",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=F50445F4-99B8-46E7-BF1B-A75D3320E52A"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Canal Density",
-            "description": "This dataset represents canal density within individual, local and accumulated upstream catchments for NHDPlusV2 Waterbodies.  Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14764,70 +14798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
-            "modified": "2023-11-13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
-            },
-            "identifier": "e0398045-0643-492e-960c-d882b6519585",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2023-11-13",
             "programCode": [
                 "020:072"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
+            },
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=e0398045-0643-492e-960c-d882b6519585"
+            ],
             "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
             "spatial": "-125.0,24.5,-66.5,49.5",
             "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Canal Density"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Inventory of Dams (NID). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The NID database contains information about the dam2019s location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams).   The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Inventory of Dams (NID). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The NID database contains information about the dam2019s location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams).   The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Canal Density",
-                    "description": "This dataset represents canal density within individual, local and accumulated upstream catchments for NHDPlusV2 Waterbodies.  Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Dam Density and Storage Volume"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "52F2F469-AC5D-40B9-B1FD-0DFD8AC53B47",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=e0398045-0643-492e-960c-d882b6519585"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Dam Density and Storage Volume",
-            "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Inventory of Dams (NID). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The NID database contains information about the dam2019s location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams).   The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -14889,70 +14923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=52F2F469-AC5D-40B9-B1FD-0DFD8AC53B47"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Dam Density and Storage Volume"
         },
-            "identifier": "52F2F469-AC5D-40B9-B1FD-0DFD8AC53B47",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the estimated density of georeferenced sites within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the EPA's Facility Registry Services (FRS) geodatabase. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting . Csv. The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the estimated density of georeferenced sites within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the EPA's Facility Registry Services (FRS) geodatabase. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting . Csv. The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Dam Density and Storage Volume",
-                    "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Inventory of Dams (NID). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The NID database contains information about the dam2019s location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams).   The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "AEC40436-E5D1-4AD9-BFF4-0654966EC3BF",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=52F2F469-AC5D-40B9-B1FD-0DFD8AC53B47"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites",
-            "description": "This dataset represents the estimated density of georeferenced sites within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the EPA's Facility Registry Services (FRS) geodatabase. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting . Csv. The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15014,70 +15048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=AEC40436-E5D1-4AD9-BFF4-0654966EC3BF"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites"
         },
-            "identifier": "AEC40436-E5D1-4AD9-BFF4-0654966EC3BF",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Global Forest Change 2000, 2013, 2013. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, 201313, representing loss detected primarily in the year 2001, 2013, 2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Global Forest Change 2000, 2013, 2013. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, 201313, representing loss detected primarily in the year 2001, 2013, 2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites",
-                    "description": "This dataset represents the estimated density of georeferenced sites within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the EPA's Facility Registry Services (FRS) geodatabase. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting . Csv. The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Forest Loss By Year 2001 to 2013"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "F8BED808-A2F6-4F47-AB21-4E3C37F6D9C4",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=AEC40436-E5D1-4AD9-BFF4-0654966EC3BF"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Forest Loss By Year 2001 to 2013",
-            "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Global Forest Change 2000, 2013, 2013. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, 201313, representing loss detected primarily in the year 2001, 2013, 2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15139,70 +15173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=F8BED808-A2F6-4F47-AB21-4E3C37F6D9C4"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Forest Loss By Year 2001 to 2013"
         },
-            "identifier": "F8BED808-A2F6-4F47-AB21-4E3C37F6D9C4",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Forest Loss By Year 2001 to 2013",
-                    "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Global Forest Change 2000, 2013, 2013. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, 201313, representing loss detected primarily in the year 2001, 2013, 2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "GeoChemPhys"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "DC063B04-19B9-4172-9D07-37B118DB935A",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=F8BED808-A2F6-4F47-AB21-4E3C37F6D9C4"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: GeoChemPhys",
-            "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15264,70 +15298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=DC063B04-19B9-4172-9D07-37B118DB935A"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: GeoChemPhys"
         },
-            "identifier": "DC063B04-19B9-4172-9D07-37B118DB935A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents mine density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on mine plants and operations monitored by the USGS National Minerals Information Center. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents mine density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on mine plants and operations monitored by the USGS National Minerals Information Center. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "GeoChemPhys",
-                    "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Mine Density: Active Mines and Mineral Plants in the US"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "79e843a5-dd98-41c1-9dd6-914706b75a48",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=DC063B04-19B9-4172-9D07-37B118DB935A"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mine Density: Active Mines and Mineral Plants in the US",
-            "description": "This dataset represents mine density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on mine plants and operations monitored by the USGS National Minerals Information Center. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15389,70 +15423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=79e843a5-dd98-41c1-9dd6-914706b75a48"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mine Density: Active Mines and Mineral Plants in the US"
         },
-            "identifier": "79e843a5-dd98-41c1-9dd6-914706b75a48",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Anthropogenic Barrier Dataset (NABD). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Anthropogenic Barrier Dataset (NABD). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Mine Density: Active Mines and Mineral Plants in the US",
-                    "description": "This dataset represents mine density within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on mine plants and operations monitored by the USGS National Minerals Information Center. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table.  The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Anthropogenic Barrier Dataset"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "8A4F8423-0D37-4F28-938A-E5522BFEAA96",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=79e843a5-dd98-41c1-9dd6-914706b75a48"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Anthropogenic Barrier Dataset",
-            "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Anthropogenic Barrier Dataset (NABD). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15514,70 +15548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=8A4F8423-0D37-4F28-938A-E5522BFEAA96"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Anthropogenic Barrier Dataset"
         },
-            "identifier": "8A4F8423-0D37-4F28-938A-E5522BFEAA96",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents deposition estimates of nutrients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Atmospheric Deposition Program. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents deposition estimates of nutrients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Atmospheric Deposition Program. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Anthropogenic Barrier Dataset",
-                    "description": "This dataset represents the dam density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Anthropogenic Barrier Dataset (NABD). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "49DA91A5-0D29-41E4-96BD-93987FF85979",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=8A4F8423-0D37-4F28-938A-E5522BFEAA96"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition",
-            "description": "This dataset represents deposition estimates of nutrients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Atmospheric Deposition Program. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15639,70 +15673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=49DA91A5-0D29-41E4-96BD-93987FF85979"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition"
         },
-            "identifier": "49DA91A5-0D29-41E4-96BD-93987FF85979",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents coal mine density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Coal Resource Dataset System (NCRDS). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents coal mine density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Coal Resource Dataset System (NCRDS). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition",
-                    "description": "This dataset represents deposition estimates of nutrients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Atmospheric Deposition Program. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Coal Resource Dataset System"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "a440e12b-9875-4b88-b7af-f095c79f891b",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=49DA91A5-0D29-41E4-96BD-93987FF85979"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Coal Resource Dataset System",
-            "description": "This dataset represents coal mine density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Coal Resource Dataset System (NCRDS). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15764,70 +15798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=a440e12b-9875-4b88-b7af-f095c79f891b"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Coal Resource Dataset System"
         },
-            "identifier": "a440e12b-9875-4b88-b7af-f095c79f891b",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the elevation values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Elevation Dataset. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16 The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the elevation values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Elevation Dataset. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16 The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Coal Resource Dataset System",
-                    "description": "This dataset represents coal mine density and storage volumes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Coal Resource Dataset System (NCRDS). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Elevation Dataset"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "FD387D2B-CCD3-4D17-ACDE-A9A8426CA1CA",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=a440e12b-9875-4b88-b7af-f095c79f891b"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Elevation Dataset",
-            "description": "This dataset represents the elevation values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Elevation Dataset. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16 The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -15889,70 +15923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FD387D2B-CCD3-4D17-ACDE-A9A8426CA1CA"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Elevation Dataset"
         },
-            "identifier": "FD387D2B-CCD3-4D17-ACDE-A9A8426CA1CA",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the land cover data within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the NLCD. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the NLCD raster composed of 16 land cover classes (categorical data type) for the conterminous USA. Four classes of the NLCD were excluded as they were specific to Alaska land covers.  This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the land cover data within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the NLCD. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the NLCD raster composed of 16 land cover classes (categorical data type) for the conterminous USA. Four classes of the NLCD were excluded as they were specific to Alaska land covers.  This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Elevation Dataset",
-                    "description": "This dataset represents the elevation values within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Elevation Dataset. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16 The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Land Cover Database"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "65264DD6-6227-4732-8162-3E4F194C4913",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FD387D2B-CCD3-4D17-ACDE-A9A8426CA1CA"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database",
-            "description": "This dataset represents the land cover data within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the NLCD. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the NLCD raster composed of 16 land cover classes (categorical data type) for the conterminous USA. Four classes of the NLCD were excluded as they were specific to Alaska land covers.  This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16014,70 +16048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=65264DD6-6227-4732-8162-3E4F194C4913"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database"
         },
-            "identifier": "65264DD6-6227-4732-8162-3E4F194C4913",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the impervious surface coefficients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Land Cover Data. AOI boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-AOI boundaries and then links them through an off-network flow table. This data set is derived from the NLCD Impervious Surfaces raster which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the impervious surface coefficients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Land Cover Data. AOI boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-AOI boundaries and then links them through an off-network flow table. This data set is derived from the NLCD Impervious Surfaces raster which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Land Cover Database",
-                    "description": "This dataset represents the land cover data within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the NLCD. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the NLCD raster composed of 16 land cover classes (categorical data type) for the conterminous USA. Four classes of the NLCD were excluded as they were specific to Alaska land covers.  This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Land Cover Database - Impervious Surfaces"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "43F2C9A2-4F0F-4603-928B-5DF138EDDB96",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=65264DD6-6227-4732-8162-3E4F194C4913"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database - Impervious Surfaces",
-            "description": "This dataset represents the impervious surface coefficients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Land Cover Data. AOI boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-AOI boundaries and then links them through an off-network flow table. This data set is derived from the NLCD Impervious Surfaces raster which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16139,70 +16173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=43F2C9A2-4F0F-4603-928B-5DF138EDDB96"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database - Impervious Surfaces"
         },
-            "identifier": "43F2C9A2-4F0F-4603-928B-5DF138EDDB96",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the average height of the dominant vegetation for a 30-m grid cell within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on field reference data and Landsat, elevation, and ancillary data. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The Existing Vegetation Type (EVT) layer represents the species composition currently present at a given site. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, which is a nationally consistent set of mid-scale ecological units. Additional units are derived from NLCD, National Vegetation Classification Standard (NVCS) Alliances, and LANDFIRE specific types. - Reclassified into introduced managed vegetation cover - IntrodManagVeg class - reclass from EVT - groups (EVT_GP) = (701,702,703,704,705,706,707,708,709,711,731) Canopy height is generated separately for tree, shrub and herbaceous lifeforms using training data and other layers. EVH is determined by the average height weighted by species cover and based on the existing vegetation type (EVT) lifeform. Decision tree models using field reference data and Landsat, elevation, and ancillary data are developed separately for each lifeform. Decision tree relationships are used to generate lifeform specific height class layers, which are merged into a single composite EVH layer. The vegetation characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the average height of the dominant vegetation for a 30-m grid cell within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on field reference data and Landsat, elevation, and ancillary data. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The Existing Vegetation Type (EVT) layer represents the species composition currently present at a given site. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, which is a nationally consistent set of mid-scale ecological units. Additional units are derived from NLCD, National Vegetation Classification Standard (NVCS) Alliances, and LANDFIRE specific types. - Reclassified into introduced managed vegetation cover - IntrodManagVeg class - reclass from EVT - groups (EVT_GP) = (701,702,703,704,705,706,707,708,709,711,731) Canopy height is generated separately for tree, shrub and herbaceous lifeforms using training data and other layers. EVH is determined by the average height weighted by species cover and based on the existing vegetation type (EVT) lifeform. Decision tree models using field reference data and Landsat, elevation, and ancillary data are developed separately for each lifeform. Decision tree relationships are used to generate lifeform specific height class layers, which are merged into a single composite EVH layer. The vegetation characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Land Cover Database - Impervious Surfaces",
-                    "description": "This dataset represents the impervious surface coefficients within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the National Land Cover Data. AOI boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-AOI boundaries and then links them through an off-network flow table. This data set is derived from the NLCD Impervious Surfaces raster which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Nonnative LANDFIRE Vegetation"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "B995906F-9B18-4B1F-B0D1-D13122A80C85",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=43F2C9A2-4F0F-4603-928B-5DF138EDDB96"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nonnative LANDFIRE Vegetation",
-            "description": "This dataset represents the average height of the dominant vegetation for a 30-m grid cell within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on field reference data and Landsat, elevation, and ancillary data. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The Existing Vegetation Type (EVT) layer represents the species composition currently present at a given site. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, which is a nationally consistent set of mid-scale ecological units. Additional units are derived from NLCD, National Vegetation Classification Standard (NVCS) Alliances, and LANDFIRE specific types. - Reclassified into introduced managed vegetation cover - IntrodManagVeg class - reclass from EVT - groups (EVT_GP) = (701,702,703,704,705,706,707,708,709,711,731) Canopy height is generated separately for tree, shrub and herbaceous lifeforms using training data and other layers. EVH is determined by the average height weighted by species cover and based on the existing vegetation type (EVT) lifeform. Decision tree models using field reference data and Landsat, elevation, and ancillary data are developed separately for each lifeform. Decision tree relationships are used to generate lifeform specific height class layers, which are merged into a single composite EVH layer. The vegetation characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16264,70 +16298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B995906F-9B18-4B1F-B0D1-D13122A80C85"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nonnative LANDFIRE Vegetation"
         },
-            "identifier": "B995906F-9B18-4B1F-B0D1-D13122A80C85",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the pesticide use within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the pesticide use within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Nonnative LANDFIRE Vegetation",
-                    "description": "This dataset represents the average height of the dominant vegetation for a 30-m grid cell within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on field reference data and Landsat, elevation, and ancillary data. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The Existing Vegetation Type (EVT) layer represents the species composition currently present at a given site. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, which is a nationally consistent set of mid-scale ecological units. Additional units are derived from NLCD, National Vegetation Classification Standard (NVCS) Alliances, and LANDFIRE specific types. - Reclassified into introduced managed vegetation cover - IntrodManagVeg class - reclass from EVT - groups (EVT_GP) = (701,702,703,704,705,706,707,708,709,711,731) Canopy height is generated separately for tree, shrub and herbaceous lifeforms using training data and other layers. EVH is determined by the average height weighted by species cover and based on the existing vegetation type (EVT) lifeform. Decision tree models using field reference data and Landsat, elevation, and ancillary data are developed separately for each lifeform. Decision tree relationships are used to generate lifeform specific height class layers, which are merged into a single composite EVH layer. The vegetation characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Pesticide"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "7D1FE157-43CD-4AA6-A1D3-37B4FC41065A",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B995906F-9B18-4B1F-B0D1-D13122A80C85"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Pesticide",
-            "description": "This dataset represents the pesticide use within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16389,70 +16423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7D1FE157-43CD-4AA6-A1D3-37B4FC41065A"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Pesticide"
         },
-            "identifier": "7D1FE157-43CD-4AA6-A1D3-37B4FC41065A",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents climate observations within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the PRISM Climate Group. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents climate observations within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the PRISM Climate Group. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Pesticide",
-                    "description": "This dataset represents the pesticide use within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "PRISM Normals Data"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "C1AED92E-568B-47C6-9B51-272462155A76",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7D1FE157-43CD-4AA6-A1D3-37B4FC41065A"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: PRISM Normals Data",
-            "description": "This dataset represents climate observations within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the PRISM Climate Group. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16514,70 +16548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=C1AED92E-568B-47C6-9B51-272462155A76"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: PRISM Normals Data"
         },
-            "identifier": "C1AED92E-568B-47C6-9B51-272462155A76",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the density of road and stream crossings within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the density of road and stream crossings within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "PRISM Normals Data",
-                    "description": "This dataset represents climate observations within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the PRISM Climate Group. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Road and Stream Intersections"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "BFB01111-7676-4E96-B9BD-7DC4E5A3168B",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=C1AED92E-568B-47C6-9B51-272462155A76"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Road and Stream Intersections",
-            "description": "This dataset represents the density of road and stream crossings within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16639,70 +16673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=BFB01111-7676-4E96-B9BD-7DC4E5A3168B"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Road and Stream Intersections"
         },
-            "identifier": "BFB01111-7676-4E96-B9BD-7DC4E5A3168B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the estimated surface water runoff within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month.   The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the estimated surface water runoff within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month.   The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Road and Stream Intersections",
-                    "description": "This dataset represents the density of road and stream crossings within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Runoff"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "15669D84-E7E5-4E53-9FC3-0E022B6F40C0",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=BFB01111-7676-4E96-B9BD-7DC4E5A3168B"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Runoff",
-            "description": "This dataset represents the estimated surface water runoff within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month.   The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16764,70 +16798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=15669D84-E7E5-4E53-9FC3-0E022B6F40C0"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Runoff"
         },
-            "identifier": "15669D84-E7E5-4E53-9FC3-0E022B6F40C0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the soil characteristics within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the STATSGO landscape rasters. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the soil characteristics within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the STATSGO landscape rasters. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Runoff",
-                    "description": "This dataset represents the estimated surface water runoff within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month.   The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "State Soil Geographic Database (STATSGO) (KFFACT)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "AA3ADCFD-0758-47FC-A069-31E95A116A3D",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=15669D84-E7E5-4E53-9FC3-0E022B6F40C0"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: State Soil Geographic Database (STATSGO) (KKACT)",
-            "description": "This dataset represents the soil characteristics within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the STATSGO landscape rasters. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -16889,70 +16923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=AA3ADCFD-0758-47FC-A069-31E95A116A3D"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: State Soil Geographic Database (STATSGO) (KKACT)"
         },
-            "identifier": "AA3ADCFD-0758-47FC-A069-31E95A116A3D",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the density of 18 USGS lithology classes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the density of 18 USGS lithology classes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "State Soil Geographic Database (STATSGO) (KFFACT)",
-                    "description": "This dataset represents the soil characteristics within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the STATSGO landscape rasters. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Surficial Lithology in Watershed"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "70CB7CB9-A915-48F6-A3DE-BE62446A454E",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=AA3ADCFD-0758-47FC-A069-31E95A116A3D"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surficial Lithology in Watershed",
-            "description": "This dataset represents the density of 18 USGS lithology classes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17014,70 +17048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=70CB7CB9-A915-48F6-A3DE-BE62446A454E"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surficial Lithology in Watershed"
         },
-            "identifier": "70CB7CB9-A915-48F6-A3DE-BE62446A454E",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents total fresh surface-water withdrawals in agricultural land (L/day) within individual, local NHDPlusV2 catchments and upstream, contributing watersheds as described in DOI: 10.1016/j.scitotenv.2020.137661",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents total fresh surface-water withdrawals in agricultural land (L/day) within individual, local NHDPlusV2 catchments and upstream, contributing watersheds as described in DOI: 10.1016/j.scitotenv.2020.137661",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Surficial Lithology in Watershed",
-                    "description": "This dataset represents the density of 18 USGS lithology classes within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "wdrw_LD"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "26bfe85d-64e1-41d8-b871-79914e59f788",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=70CB7CB9-A915-48F6-A3DE-BE62446A454E"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: wdrw_LD",
-            "description": "This dataset represents total fresh surface-water withdrawals in agricultural land (L/day) within individual, local NHDPlusV2 catchments and upstream, contributing watersheds as described in DOI: 10.1016/j.scitotenv.2020.137661",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17139,70 +17173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=26bfe85d-64e1-41d8-b871-79914e59f788"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: wdrw_LD"
         },
-            "identifier": "26bfe85d-64e1-41d8-b871-79914e59f788",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the calculated wetness index value within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The westness index is calculated using the Composite Topographic Index (CTI) which is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the calculated wetness index value within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The westness index is calculated using the Composite Topographic Index (CTI) which is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "wdrw_LD",
-                    "description": "This dataset represents total fresh surface-water withdrawals in agricultural land (L/day) within individual, local NHDPlusV2 catchments and upstream, contributing watersheds as described in DOI: 10.1016/j.scitotenv.2020.137661",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wet Index"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "2717d2c3-32d3-41a5-89f5-60a8d7f04965",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=26bfe85d-64e1-41d8-b871-79914e59f788"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wet Index",
-            "description": "This dataset represents the calculated wetness index value within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The westness index is calculated using the Composite Topographic Index (CTI) which is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17264,70 +17298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2717d2c3-32d3-41a5-89f5-60a8d7f04965"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wet Index"
         },
-            "identifier": "2717d2c3-32d3-41a5-89f5-60a8d7f04965",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wet Index",
-                    "description": "This dataset represents the calculated wetness index value within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. The westness index is calculated using the Composite Topographic Index (CTI) which is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildfire Burn Percent 1984-2018 (MTBS)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "bdfdd237-06ef-41c3-8024-23a385d44a6b",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2717d2c3-32d3-41a5-89f5-60a8d7f04965"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Percent 1984-2018 (MTBS)",
-            "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17389,70 +17423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=bdfdd237-06ef-41c3-8024-23a385d44a6b"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Percent 1984-2018 (MTBS)"
         },
-            "identifier": "bdfdd237-06ef-41c3-8024-23a385d44a6b",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildfire Burn Percent 1984-2018 (MTBS)",
-                    "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildfire Burn Severity Class 1984-2018 (MTBS)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "7ffbc84f-8903-4aca-a9d4-f04e2e801595",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=bdfdd237-06ef-41c3-8024-23a385d44a6b"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Severity Class 1984-2018 (MTBS)",
-            "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17514,70 +17548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7ffbc84f-8903-4aca-a9d4-f04e2e801595"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Severity Class 1984-2018 (MTBS)"
         },
-            "identifier": "7ffbc84f-8903-4aca-a9d4-f04e2e801595",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the historical fire perimeters within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "LakeCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the historical fire perimeters within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildfire Burn Severity Class 1984-2018 (MTBS)",
-                    "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildland Fire Perimeters By Year 2000 - 2010"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "7988E3BC-FD77-47F6-B098-77A686C55B7F",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7ffbc84f-8903-4aca-a9d4-f04e2e801595"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildland Fire Perimeters By Year 2000 - 2010",
-            "description": "This dataset represents the historical fire perimeters within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17639,70 +17673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7988E3BC-FD77-47F6-B098-77A686C55B7F"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The LakeCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildland Fire Perimeters By Year 2000 - 2010"
         },
-            "identifier": "7988E3BC-FD77-47F6-B098-77A686C55B7F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the population and housing unit density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on 2010 US Census data. Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit. The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-                    "title": "LakeCat Dataset",
-                    "description": "LakeCat currently contains over 300 metrics that include local catchment (Cat), watershed (Ws), and special metrics. See Geospatial Framework and Terms in the ReadMe for definitions of the terms \u2018catchment\u2019 and \u2018watershed\u2019 as used with the LakeCat Dataset. An additional metric, inStreamCat, indicates whether the variable was pulled from the StreamCat Dataset or calculated with a geospatial framework that was developed for LakeCat.\n\nThese metrics are available for 378,088 lakes and their associated catchments across the conterminous US. LakeCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the population and housing unit density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on 2010 US Census data. Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit. The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
+                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildland Fire Perimeters By Year 2000 - 2010",
-                    "description": "This dataset represents the historical fire perimeters within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Catchment boundaries in LakeCat are defined in one of two ways, on-network or off-network. The on-network catchment boundaries follow the catchments provided in the NHDPlusV2 and the metrics for these lakes mirror metrics from StreamCat, but will substitute the COMID of the NHDWaterbody for that of the NHDFlowline. The off-network catchment framework uses the NHDPlusV2 flow direction rasters to define non-overlapping lake-catchment boundaries and then links them through an off-network flow table. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "2010 US Census Housing Unit and Population Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "DF3DB5FE-C99A-4DA4-8339-8698B5D7D801",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/lakecat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/epadatacommons/ORD/NHDPlusLandscapeAttributes/LakeCat/FinalTables/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7988E3BC-FD77-47F6-B098-77A686C55B7F"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Housing Unit and Population Density",
-            "description": "This dataset represents the population and housing unit density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on 2010 US Census data. Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit. The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17764,70 +17798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=DF3DB5FE-C99A-4DA4-8339-8698B5D7D801"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Housing Unit and Population Density"
         },
-            "identifier": "DF3DB5FE-C99A-4DA4-8339-8698B5D7D801",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the road density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the road density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "2010 US Census Housing Unit and Population Density",
-                    "description": "This dataset represents the population and housing unit density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on 2010 US Census data. Densities are calculated for every block group and watershed averages are calculated for every local NHDPlusV2 catchment. This data set is derived from The TIGER/Line Files and related database (.dbf) files for the conterminous USA. It was downloaded as Block Group-Level Census 2010 SF1 Data in File Geodatabase Format (ArcGIS version 10.0). The landscape raster (LR) was produced based on the data compiled from the questions asked of all people and about every housing unit. The (block-group population / block group area) and (block-group housing units / block group area) were summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "2010 US Census Road Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "20AC52F2-251B-49F7-8328-2FC8EA6FE18B",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=DF3DB5FE-C99A-4DA4-8339-8698B5D7D801"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Road Density",
-            "description": "This dataset represents the road density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -17889,70 +17923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=20AC52F2-251B-49F7-8328-2FC8EA6FE18B"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: 2010 US Census Road Density"
         },
-            "identifier": "20AC52F2-251B-49F7-8328-2FC8EA6FE18B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents % of land with agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents % of land with agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "2010 US Census Road Density",
-                    "description": "This dataset represents the road density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from TIGER/Line Files of roads in the conterminous United States. Road density describes how many kilometers of road exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of road/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Agricultural Drainage"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "1aae5df2-b9e9-4dd1-996a-c2b08e75d806",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=20AC52F2-251B-49F7-8328-2FC8EA6FE18B"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Drainage",
-            "description": "This dataset represents % of land with agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18014,70 +18048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1aae5df2-b9e9-4dd1-996a-c2b08e75d806"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Drainage"
         },
-            "identifier": "1aae5df2-b9e9-4dd1-996a-c2b08e75d806",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661 ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661 ",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Agricultural Drainage",
-                    "description": "This dataset represents % of land with agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Agricultural Fresh Surface-Water Withdraw"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "c6c7743b-7ed4-4e40-b023-a576fba18e9d",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1aae5df2-b9e9-4dd1-996a-c2b08e75d806"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Fresh Surface-Water Withdraw",
-            "description": "This dataset represents total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661 ",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18139,70 +18173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c6c7743b-7ed4-4e40-b023-a576fba18e9d"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Fresh Surface-Water Withdraw"
         },
-            "identifier": "c6c7743b-7ed4-4e40-b023-a576fba18e9d",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents density of total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents density of total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Agricultural Fresh Surface-Water Withdraw",
-                    "description": "This dataset represents total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661 ",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Agricultural Fresh Surface-Water Withdraw Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "2771a7fa-bcbd-460c-af71-3c607712565c",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c6c7743b-7ed4-4e40-b023-a576fba18e9d"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Fresh Surface-Water Withdraw Density",
-            "description": "This dataset represents density of total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18264,70 +18298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2771a7fa-bcbd-460c-af71-3c607712565c"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Fresh Surface-Water Withdraw Density"
         },
-            "identifier": "2771a7fa-bcbd-460c-af71-3c607712565c",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the application of nitrogen within individual,\u00a0 local NHDPlusV2 catchments and upstream, contributing watersheds based data published in EPA EnviroAtlas. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the application of nitrogen within individual,\u00a0 local NHDPlusV2 catchments and upstream, contributing watersheds based data published in EPA EnviroAtlas. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Agricultural Fresh Surface-Water Withdraw Density",
-                    "description": "This dataset represents density of total fresh surface-water withdrawals in agricultural land within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  Measured as L/day as described in DOI: 10.1016/j.scitotenv.2020.137661",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Agricultural Nitrogen Inputs"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "9eae0ab2-0861-4e0f-8c77-b0033af1eecf",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2771a7fa-bcbd-460c-af71-3c607712565c"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Nitrogen Inputs",
-            "description": "This dataset represents the application of nitrogen within individual,\u00a0 local NHDPlusV2 catchments and upstream, contributing watersheds based data published in EPA EnviroAtlas. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18389,70 +18423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
-            },
-            "identifier": "9eae0ab2-0861-4e0f-8c77-b0033af1eecf",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=9eae0ab2-0861-4e0f-8c77-b0033af1eecf"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
             "spatial": "-125.0,24.5,-66.5,49.5",
             "temporal": "2015/2030",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
-                    "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
-                    "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Agricultural Nitrogen Inputs"
         },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                    "format": "Comma-Separated Values (.csv)",
-                    "title": "Agricultural Nitrogen Inputs",
-                    "description": "This dataset represents the application of nitrogen within individual,\u00a0 local NHDPlusV2 catchments and upstream, contributing watersheds based data published in EPA EnviroAtlas. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. These data are based on county-scale estimates of N in the form of fertilizer, manure, or cultivated biological nitrogen fixation. The rasters used for this analysis were prepared for EnviroAtlas published datasets on agricultural nitrogen inputs. Links to data in each raster can be found in Data Sources below. The nitrogen characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
-                    "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
-                }
-            ],
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
             "dataQuality": true,
             "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
             "describedByType": "text/html",
-            "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=9eae0ab2-0861-4e0f-8c77-b0033af1eecf"
-            ],
-            "theme": [
-                "environment"
-            ]
+            "description": "This dataset represents net anthropogenic Nitrogen within AOI: farm fertilizer + urban fertilizer + NOx deposition + CBNF + Human and Livestock food - crop N content - livestock N content within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
+                    "format": "API",
+                    "title": "StreamCat Dataset"
                 },
                 {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Anthropogenic Nitrogen",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "This dataset represents net anthropogenic Nitrogen within AOI: farm fertilizer + urban fertilizer + NOx deposition + CBNF + Human and Livestock food - crop N content - livestock N content within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
+                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                    "format": "Comma-Separated Values (.csv)",
+                    "mediaType": "text/csv",
+                    "title": "Anthropogenic Nitrogen"
+                }
+            ],
+            "identifier": "1ab197c0-2cca-4fe0-a935-fb7b6be379c7",
+            "issued": "2015-04-23",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18514,70 +18548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1ab197c0-2cca-4fe0-a935-fb7b6be379c7"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Anthropogenic Nitrogen"
         },
-            "identifier": "1ab197c0-2cca-4fe0-a935-fb7b6be379c7",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents net anthropogenic Nitrogen within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents net anthropogenic Nitrogen within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Anthropogenic Nitrogen",
-                    "description": "This dataset represents net anthropogenic Nitrogen within AOI: farm fertilizer + urban fertilizer + NOx deposition + CBNF + Human and Livestock food - crop N content - livestock N content within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Anthropogenic Nitrogen per AOI within AOI"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "63669882-c84b-43d5-bd21-7143ce486ab6",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1ab197c0-2cca-4fe0-a935-fb7b6be379c7"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Anthropogenic Nitrogen per AOI within AOI",
-            "description": "This dataset represents net anthropogenic Nitrogen within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18639,70 +18673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=63669882-c84b-43d5-bd21-7143ce486ab6"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Anthropogenic Nitrogen per AOI within AOI"
         },
-            "identifier": "63669882-c84b-43d5-bd21-7143ce486ab6",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents percent area consisting of carbonate-rock aquifers, igneous and metamorphic-rock, sandstone, sandstone and carbonate-rock, semiconsolidated sand, and unconsolidated sand and gravel aquifers within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents percent area consisting of carbonate-rock aquifers, igneous and metamorphic-rock, sandstone, sandstone and carbonate-rock, semiconsolidated sand, and unconsolidated sand and gravel aquifers within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Anthropogenic Nitrogen per AOI within AOI",
-                    "description": "This dataset represents net anthropogenic Nitrogen within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Aquifers"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "f9a68367-e950-4dca-a626-17d8907afddb",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=63669882-c84b-43d5-bd21-7143ce486ab6"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Aquifers",
-            "description": "This dataset represents percent area consisting of carbonate-rock aquifers, igneous and metamorphic-rock, sandstone, sandstone and carbonate-rock, semiconsolidated sand, and unconsolidated sand and gravel aquifers within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18764,70 +18798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=f9a68367-e950-4dca-a626-17d8907afddb"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Aquifers"
         },
-            "identifier": "f9a68367-e950-4dca-a626-17d8907afddb",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the base flow index values within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The BFI (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the base flow index values within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The BFI (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Aquifers",
-                    "description": "This dataset represents percent area consisting of carbonate-rock aquifers, igneous and metamorphic-rock, sandstone, sandstone and carbonate-rock, semiconsolidated sand, and unconsolidated sand and gravel aquifers within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Base Flow Index"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "66C0ED41-2707-4732-A906-E9D89E8F5A6B",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=f9a68367-e950-4dca-a626-17d8907afddb"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Base Flow Index",
-            "description": "This dataset represents the base flow index values within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The BFI (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -18889,70 +18923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=66C0ED41-2707-4732-A906-E9D89E8F5A6B"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Base Flow Index"
         },
-            "identifier": "66C0ED41-2707-4732-A906-E9D89E8F5A6B",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the canal density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the canal density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Base Flow Index",
-                    "description": "This dataset represents the base flow index values within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The base-flow index (BFI) grid for the conterminous United States was developed to estimate (1) BFI values for ungaged streams, and (2) ground-water recharge throughout the conterminous United States (see Source_Information). Estimates of BFI values at ungaged streams and BFI-based ground-water recharge estimates are useful for interpreting relations between land use and water quality in surface and ground water. The BFI (%) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Canal Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "6B8EB461-6624-4B62-B163-D01A65669EE1",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=66C0ED41-2707-4732-A906-E9D89E8F5A6B"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Canal Density",
-            "description": "This dataset represents the canal density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19014,70 +19048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=6B8EB461-6624-4B62-B163-D01A65669EE1"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Canal Density"
         },
-            "identifier": "6B8EB461-6624-4B62-B163-D01A65669EE1",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on National Inventory of Dams (NID) data. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics.(See Supplementary Info for Glossary of Terms). The NID database contains information about the dams location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams) . The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on National Inventory of Dams (NID) data. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics.(See Supplementary Info for Glossary of Terms). The NID database contains information about the dams location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams) . The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Canal Density",
-                    "description": "This dataset represents the canal density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from NHDPlusV2 line features classified as canal, ditch, or pipeline in the conterminous United States. Canal density describes how many kilometers of canal exist in a square kilometer. A raster was produced using the ArcGIS Line Density Tool to form the landscape layer for analysis. The (kilometer of canal/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Dam Density and Storage Volume"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "C64137B3-B0C3-428D-A7A0-62DF27816CA9",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=6B8EB461-6624-4B62-B163-D01A65669EE1"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Dam Density and Storage Volume",
-            "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on National Inventory of Dams (NID) data. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics.(See Supplementary Info for Glossary of Terms). The NID database contains information about the dams location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams) . The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19139,70 +19173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=C64137B3-B0C3-428D-A7A0-62DF27816CA9"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Dam Density and Storage Volume"
         },
-            "identifier": "C64137B3-B0C3-428D-A7A0-62DF27816CA9",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the estimated density of georeferenced sites within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the EPA's Facility Registry Services (FRS) geodatabase. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting .csv. (see Data Sources for links to NHDPlusV2 data and FRS data) The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the estimated density of georeferenced sites within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the EPA's Facility Registry Services (FRS) geodatabase. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting .csv. (see Data Sources for links to NHDPlusV2 data and FRS data) The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Dam Density and Storage Volume",
-                    "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on National Inventory of Dams (NID) data. Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics.(See Supplementary Info for Glossary of Terms). The NID database contains information about the dams location, size, purpose, type, last inspection, regulatory facts, and other technical data. Structures on streams reduce the longitudinal and lateral hydrologic connectivity of the system. For example, impoundments above dams slow stream flow, cause deposition of sediment and reduce peak flows. Dams change both the discharge and sediment supply of streams, causing channel incision and bed coarsening downstream. Downstream areas are often sediment deprived, resulting in degradation, i.e., erosion of the stream bed and stream banks. This database was improved upon by locations verified by work from the USGS National Map (Jeff Simley Group). It was observed that some dams, some of them major and which do exist, were not part of the 2009 NID, but were represented in the USGS National Map dataset, and had been in the 2006 NID.  Approximately 1,100 such dams were added, based on the USGS National Map lat/long and the 2006 NID attributes (dam height, storage, etc.) Finally, as clean-up, a) about 600 records with duplicate NIDID were removed, and b) about 300 records were removed which represented the same location of the same dam but with a different NIDID, for the largest dams (did visual check of dams with storage above 5000 acre feet and are likely duplicated - about the 10,000 largest dams) . The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "630C3CAA-B678-45FC-8641-E91C591BE13F",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=C64137B3-B0C3-428D-A7A0-62DF27816CA9"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites",
-            "description": "This dataset represents the estimated density of georeferenced sites within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the EPA's Facility Registry Services (FRS) geodatabase. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting .csv. (see Data Sources for links to NHDPlusV2 data and FRS data) The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19264,70 +19298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=630C3CAA-B678-45FC-8641-E91C591BE13F"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites"
         },
-            "identifier": "630C3CAA-B678-45FC-8641-E91C591BE13F",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Global Forest Change 2000-2013. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, representing loss detected primarily in the year 2000-2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Global Forest Change 2000-2013. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, representing loss detected primarily in the year 2000-2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Facility Registry Services (FRS) : Toxic Release Inventory (TRI) , National Pollutant Discharge Elimination System (NPDES) , and Superfund Sites",
-                    "description": "This dataset represents the estimated density of georeferenced sites within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the EPA's Facility Registry Services (FRS) geodatabase. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The FRS geodatabase is a collection of point locations of facilities or sites subject to environmental regulation. TRI, NPDES, and Superfund sites were extracted individually to summarize for each in the resulting .csv. (see Data Sources for links to NHDPlusV2 data and FRS data) The (site locations / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a points data type (see Data Structure and Attribute Information for a description of each metric).",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Forest Loss By Year 2001 to 2013"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "14889232-F9DE-468E-854D-9C11A25238D5",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=630C3CAA-B678-45FC-8641-E91C591BE13F"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Forest Loss By Year 2001 to 2013",
-            "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Global Forest Change 2000-2013. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, representing loss detected primarily in the year 2000-2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19389,70 +19423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=14889232-F9DE-468E-854D-9C11A25238D5"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Forest Loss By Year 2001 to 2013"
         },
-            "identifier": "14889232-F9DE-468E-854D-9C11A25238D5",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metric. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metric. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Forest Loss By Year 2001 to 2013",
-                    "description": "This dataset represents the characterization of global forest extent and change by year from 2001 through 2013 within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Global Forest Change 2000-2013. These data are based on global tree cover loss for the period from 2001 to 2013 at a spatial resolution of 30m. The analysis used to create the landscape layer is based on Landsat data. Forest loss was defined as a stand-replacement disturbance or the complete removal of tree cover canopy at the Landsat pixel scale. This landscape layer is a disaggregation of total forest loss to annual time scales. Encoded as either 0 (no loss) or else a value in the range 1, representing loss detected primarily in the year 2000-2013, respectively. The forest loss by year characteristics (%) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "GeoChemPhys"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "61F319E2-0048-4FEE-A3BF-4B1298EB93FE",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=14889232-F9DE-468E-854D-9C11A25238D5"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: GeoChemPhys",
-            "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metric. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19514,70 +19548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=61F319E2-0048-4FEE-A3BF-4B1298EB93FE"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: GeoChemPhys"
         },
-            "identifier": "61F319E2-0048-4FEE-A3BF-4B1298EB93FE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on 23 other StreamCat metrics. The Index of Watershed Integrity (IWI) is based on first order approximations of relationships between stressors and six watershed functions: hydrologic regulation, regulation of water chemistry, sediment regulation, hydrologic connectivity, temperature regulation, and habitat provision. Link to paper: https://doi.org/10.1016/j.ecolind.2017.10.070\\\\nThe Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on 23 other StreamCat metrics. The Index of Watershed Integrity (IWI) is based on first order approximations of relationships between stressors and six watershed functions: hydrologic regulation, regulation of water chemistry, sediment regulation, hydrologic connectivity, temperature regulation, and habitat provision. Link to paper: https://doi.org/10.1016/j.ecolind.2017.10.070\\\\nThe Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "GeoChemPhys",
-                    "description": "This dataset represents geochemical or geophysical attributes in surface or near surface geology within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metric. For information regarding how the Landscape layers were created see https://www.sciencebase.gov/catalog/item/53481333e4b06f6ce034aae7. Landscape Layers are partitioned into 4 tables based on the location of no-data cells within their rasters to correctly reflect the PctFull attributes within each table.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "520397B1-342A-45EA-B8F9-B05694C0A194",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=61F319E2-0048-4FEE-A3BF-4B1298EB93FE"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI)",
-            "description": "This dataset represents the Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on 23 other StreamCat metrics. The Index of Watershed Integrity (IWI) is based on first order approximations of relationships between stressors and six watershed functions: hydrologic regulation, regulation of water chemistry, sediment regulation, hydrologic connectivity, temperature regulation, and habitat provision. Link to paper: https://doi.org/10.1016/j.ecolind.2017.10.070\\\\nThe Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19639,70 +19673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=520397B1-342A-45EA-B8F9-B05694C0A194"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI)"
         },
-            "identifier": "520397B1-342A-45EA-B8F9-B05694C0A194",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents mean hillslope percent within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents mean hillslope percent within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI)",
-                    "description": "This dataset represents the Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on 23 other StreamCat metrics. The Index of Watershed Integrity (IWI) is based on first order approximations of relationships between stressors and six watershed functions: hydrologic regulation, regulation of water chemistry, sediment regulation, hydrologic connectivity, temperature regulation, and habitat provision. Link to paper: https://doi.org/10.1016/j.ecolind.2017.10.070\\\\nThe Index of Watershed Integrity / Index of Catchment Integrity (IWI/ICI) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Mean Hillslope"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "352d021d-56b5-4826-8831-202fdfa4e31d",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=520397B1-342A-45EA-B8F9-B05694C0A194"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mean Hillslope",
-            "description": "This dataset represents mean hillslope percent within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19764,70 +19798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=352d021d-56b5-4826-8831-202fdfa4e31d"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mean Hillslope"
         },
-            "identifier": "352d021d-56b5-4826-8831-202fdfa4e31d",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the mine density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on mine plants and operations monitored by the USGS National Minerals Information Center. The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the mine density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on mine plants and operations monitored by the USGS National Minerals Information Center. The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Mean Hillslope",
-                    "description": "This dataset represents mean hillslope percent within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Mine Density  Active Mines and Mineral Plants in the US"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "E195B424-0A8A-4836-BE03-C48C122AF701",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=352d021d-56b5-4826-8831-202fdfa4e31d"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mine Density  Active Mines and Mineral Plants in the US",
-            "description": "This dataset represents the mine density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on mine plants and operations monitored by the USGS National Minerals Information Center. The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -19889,70 +19923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=E195B424-0A8A-4836-BE03-C48C122AF701"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Mine Density  Active Mines and Mineral Plants in the US"
         },
-            "identifier": "E195B424-0A8A-4836-BE03-C48C122AF701",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Anthropogenic Barrier Dataset (NABD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Anthropogenic Barrier Dataset (NABD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Mine Density  Active Mines and Mineral Plants in the US",
-                    "description": "This dataset represents the mine density within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on mine plants and operations monitored by the USGS National Minerals Information Center. The National Minerals Information Center canvasses the nonfuel mining and mineral-processing industry in the United States for data on mineral production, consumption, recycling, stocks, and shipments. Mine plants and operations for commodities are expressed as points in a shapefile that was downloaded from the USGS directly. The (mines / catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Anthropogenic Barrier Dataset (NABD)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "83E6ECD0-1BC3-4182-B1A1-DDFF5804E405",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=E195B424-0A8A-4836-BE03-C48C122AF701"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Anthropogenic Barrier Dataset (NABD)",
-            "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Anthropogenic Barrier Dataset (NABD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20014,70 +20048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=83E6ECD0-1BC3-4182-B1A1-DDFF5804E405"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Anthropogenic Barrier Dataset (NABD)"
         },
-            "identifier": "83E6ECD0-1BC3-4182-B1A1-DDFF5804E405",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents deposition estimates of nutrients within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Atmospheric Deposition Program. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents deposition estimates of nutrients within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Atmospheric Deposition Program. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Anthropogenic Barrier Dataset (NABD)",
-                    "description": "This dataset represents the dam density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Anthropogenic Barrier Dataset (NABD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The main objective of this project was to develop a dataset of large, anthropogenic barriers that are spatially linked to the National Hydrography Dataset Plus Version 1 (NHDPlusV1) for the conterminous U.S. to facilitate GIS analyses based on the NHDPlusV1/NHD and NID datasets. To meet this objective, Michigan State University conducted a spatial linkage of the point dataset of the 2009 National Inventory of Dams (NID) created by the U.S. Army Corps of Engineers (USACE) to the NHDPlusV1/NHD. The pool of dam data included were modified based on 1) dam removals that occurred after development of the 2009 NID and 2) the identification of duplicate dam records along state boundaries (cases where more than one state reported the same dam). The US Geological Survey (USGS) Aquatic GAP Program supported this work. The (dams/catchment) and (dam_storage/catchment) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition (NADP)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "42B3C5E0-7FF9-47E4-B00B-9AAE56E42102",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=83E6ECD0-1BC3-4182-B1A1-DDFF5804E405"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition (NADP)",
-            "description": "This dataset represents deposition estimates of nutrients within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Atmospheric Deposition Program. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20139,70 +20173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=42B3C5E0-7FF9-47E4-B00B-9AAE56E42102"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition (NADP)"
         },
-            "identifier": "42B3C5E0-7FF9-47E4-B00B-9AAE56E42102",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the coal mine density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Coal Resource Dataset System (NCRDS). Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the coal mine density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Coal Resource Dataset System (NCRDS). Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Atmospheric Deposition Program National Trends Network - Nitrogen Deposition (NADP)",
-                    "description": "This dataset represents deposition estimates of nutrients within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Atmospheric Deposition Program. The National Trends Network provides long-term records of precipitation chemistry across the United States. Individual rasters describe ammonium, nitrate, inorganic nitrogen, and average sulfur/nitrogen deposition per year. See Source Info for links to NADP. The nitrogen and sulfur characteristics (kg N/ha/yr) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Coal Resource Dataset System"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "087CFE54-7465-410E-B2DF-07B5F94FCC15",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=42B3C5E0-7FF9-47E4-B00B-9AAE56E42102"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Coal Resource Dataset System",
-            "description": "This dataset represents the coal mine density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Coal Resource Dataset System (NCRDS). Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20264,70 +20298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
-            },
-            "identifier": "087CFE54-7465-410E-B2DF-07B5F94FCC15",
-            "accessLevel": "public",
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=087CFE54-7465-410E-B2DF-07B5F94FCC15"
             ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
             "spatial": "-125.0,24.5,-66.5,49.5",
             "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Coal Resource Dataset System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the elevation values within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Elevation Dataset (see Data Sources for links to NHDPlusV2 data and NED data). NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16. The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the elevation values within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Elevation Dataset (see Data Sources for links to NHDPlusV2 data and NED data). NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16. The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Coal Resource Dataset System",
-                    "description": "This dataset represents the coal mine density and storage volumes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Coal Resource Dataset System (NCRDS). Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. The National Coal Resources Data System (NCRDS) began as a cooperative venture between the USGS and State geological agencies in 1975 and focused on the stratigraphy and chemistry of coal. Web pages have been developed to query data within both the USCOAL database and a subset of the USCHEM database. The USTRAT database, due to its size and complexity, was first made available in 2011 for direct query through web pages. The (coal mine sites/AreaSqKm) were summarized and accumulated into watersheds to produce local catchment-level and watershed-level metrics as a point data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Elevation Dataset"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "1730F0BC-7019-4821-8B31-4A6E7B3DA625",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=087CFE54-7465-410E-B2DF-07B5F94FCC15"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Elevation Dataset",
-            "description": "This dataset represents the elevation values within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Elevation Dataset (see Data Sources for links to NHDPlusV2 data and NED data). NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16. The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20389,70 +20423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1730F0BC-7019-4821-8B31-4A6E7B3DA625"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Elevation Dataset"
         },
-            "identifier": "1730F0BC-7019-4821-8B31-4A6E7B3DA625",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated watershed to provide watershed-level metrics for classes within the NLCD. This data set is derived from the NLCD raster composed of 16 of the modified Anderson land cover classes (categorical data type) for the conterminous USA (excluding the  four Alaska-specific land cover classes). Additional agriculture on slope  metrics were derived using slope based on  National elevation DEMs delivered with NHDplusV2 for agriculture NLCD classes. The NLCD raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data (see Data Structure and Attribute Information for a description of each metric). This dataset will include additional years as they become available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated watershed to provide watershed-level metrics for classes within the NLCD. This data set is derived from the NLCD raster composed of 16 of the modified Anderson land cover classes (categorical data type) for the conterminous USA (excluding the  four Alaska-specific land cover classes). Additional agriculture on slope  metrics were derived using slope based on  National elevation DEMs delivered with NHDplusV2 for agriculture NLCD classes. The NLCD raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data (see Data Structure and Attribute Information for a description of each metric). This dataset will include additional years as they become available.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Elevation Dataset",
-                    "description": "This dataset represents the elevation values within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the National Elevation Dataset (see Data Sources for links to NHDPlusV2 data and NED data). NHDPlusV2 records NED snapshot dates as follows: August 2010 - VPU04 February 2011 - VPUs 05, 06 June 2011 - VPU 17 August 2011 - VPUs 07, 10L, 10U, 11, 18 December 2011 - VPUs 01, 02, 03N, 03S, 03W, 08, 09, 12, 13, 14, 15, 16. The elevation characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Land Cover Database"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "E6436B49-3888-476D-8F2E-9415FBCCF850",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1730F0BC-7019-4821-8B31-4A6E7B3DA625"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database",
-            "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated watershed to provide watershed-level metrics for classes within the NLCD. This data set is derived from the NLCD raster composed of 16 of the modified Anderson land cover classes (categorical data type) for the conterminous USA (excluding the  four Alaska-specific land cover classes). Additional agriculture on slope  metrics were derived using slope based on  National elevation DEMs delivered with NHDplusV2 for agriculture NLCD classes. The NLCD raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data (see Data Structure and Attribute Information for a description of each metric). This dataset will include additional years as they become available.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20514,70 +20548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=E6436B49-3888-476D-8F2E-9415FBCCF850"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database"
         },
-            "identifier": "E6436B49-3888-476D-8F2E-9415FBCCF850",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated upstream catchments to provide watershed-level metrics for imperviousness values within the NLCD.  This data set is derived from the NLCD Impervious Surfaces raster, which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated upstream catchments to provide watershed-level metrics for imperviousness values within the NLCD.  This data set is derived from the NLCD Impervious Surfaces raster, which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Land Cover Database",
-                    "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated watershed to provide watershed-level metrics for classes within the NLCD. This data set is derived from the NLCD raster composed of 16 of the modified Anderson land cover classes (categorical data type) for the conterminous USA (excluding the  four Alaska-specific land cover classes). Additional agriculture on slope  metrics were derived using slope based on  National elevation DEMs delivered with NHDplusV2 for agriculture NLCD classes. The NLCD raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data (see Data Structure and Attribute Information for a description of each metric). This dataset will include additional years as they become available.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "National Land Cover Database - Impervious Surfaces"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "B68DABF6-7883-41B0-A6B2-8AFB5BB230F3",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=E6436B49-3888-476D-8F2E-9415FBCCF850"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database - Impervious Surfaces",
-            "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated upstream catchments to provide watershed-level metrics for imperviousness values within the NLCD.  This data set is derived from the NLCD Impervious Surfaces raster, which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20639,70 +20673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B68DABF6-7883-41B0-A6B2-8AFB5BB230F3"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: National Land Cover Database - Impervious Surfaces"
         },
-            "identifier": "B68DABF6-7883-41B0-A6B2-8AFB5BB230F3",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents Nitrogen from rock weathering (kg/ km2) within AOI",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents Nitrogen from rock weathering (kg/ km2) within AOI",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "National Land Cover Database - Impervious Surfaces",
-                    "description": "This dataset represents data derived from the NLCD dataset and the National Hydrography Dataset version 2.1(NHDPlusV2) (see Data Sources for links to NHDPlusV2 data and NLCD). Attributes were calculated for every local NHDPlusV2 catchment and accumulated upstream catchments to provide watershed-level metrics for imperviousness values within the NLCD.  This data set is derived from the NLCD Impervious Surfaces raster, which describes percent imperviousness (continuous data type). Values indicate the degree to which the area is composed of impervious anthropogenic materials (e.g., parking surfaces, roads, building roofs). This raster was produced based on a decision-tree classification of 2001, 2004, 2006, 2008, 2011, 2013, 2016, and 2019 Landsat satellite data. This dataset will include additional years as they become available. ",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Nitrogen From Rock Weathering"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "2475fce5-6deb-4121-8216-30872e63ca41",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B68DABF6-7883-41B0-A6B2-8AFB5BB230F3"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nitrogen From Rock Weathering",
-            "description": "This dataset represents Nitrogen from rock weathering (kg/ km2) within AOI",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20764,70 +20798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2475fce5-6deb-4121-8216-30872e63ca41"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nitrogen From Rock Weathering"
         },
-            "identifier": "2475fce5-6deb-4121-8216-30872e63ca41",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the density of nitrogen surplus as kg N / yr, excluding biological N Fixation, within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the density of nitrogen surplus as kg N / yr, excluding biological N Fixation, within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Nitrogen From Rock Weathering",
-                    "description": "This dataset represents Nitrogen from rock weathering (kg/ km2) within AOI",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Nitrogen Surplus Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "5d7e2a7a-d7ef-40d2-99b9-101b2af9d8b6",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2475fce5-6deb-4121-8216-30872e63ca41"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nitrogen Surplus Density",
-            "description": "This dataset represents the density of nitrogen surplus as kg N / yr, excluding biological N Fixation, within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -20889,70 +20923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=5d7e2a7a-d7ef-40d2-99b9-101b2af9d8b6"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Nitrogen Surplus Density"
         },
-            "identifier": "5d7e2a7a-d7ef-40d2-99b9-101b2af9d8b6",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents % of land without agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents % of land without agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Nitrogen Surplus Density",
-                    "description": "This dataset represents the density of nitrogen surplus as kg N / yr, excluding biological N Fixation, within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "No Agricultural Drainage"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "2c91949a-00eb-4196-8b10-dbe9a1191d05",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=5d7e2a7a-d7ef-40d2-99b9-101b2af9d8b6"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: No Agricultural Drainage",
-            "description": "This dataset represents % of land without agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21014,70 +21048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2c91949a-00eb-4196-8b10-dbe9a1191d05"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: No Agricultural Drainage"
         },
-            "identifier": "2c91949a-00eb-4196-8b10-dbe9a1191d05",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the percent of non-agricultural, non-native vegetation based on LANDFIRE existing vegetation type (EVT) for a 30-m grid cell within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on field reference data and Landsat, elevation, and ancillary data. EVTs are mapped using decision tree models, field data, Landsat imagery, elevation, and biophysical gradient data. Decision tree models are developed separately for each of the three lifeforms -tree, shrub, and herbaceous and are then used to generate lifeform specific EVT layers.  The LF-GAP Map Units Descriptions provide descriptions for each LF EVT including species, distribution and classification information. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, alliances of the U.S. National Vegetation Classification (USNVC), and the National Land Cover Database and LF specific types. LANDFIRE EVT groups were reclassified into introduced managed vegetation cover where EVT_GP = (701,702,703,704,705,706,707,708,709,711,731).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the percent of non-agricultural, non-native vegetation based on LANDFIRE existing vegetation type (EVT) for a 30-m grid cell within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on field reference data and Landsat, elevation, and ancillary data. EVTs are mapped using decision tree models, field data, Landsat imagery, elevation, and biophysical gradient data. Decision tree models are developed separately for each of the three lifeforms -tree, shrub, and herbaceous and are then used to generate lifeform specific EVT layers.  The LF-GAP Map Units Descriptions provide descriptions for each LF EVT including species, distribution and classification information. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, alliances of the U.S. National Vegetation Classification (USNVC), and the National Land Cover Database and LF specific types. LANDFIRE EVT groups were reclassified into introduced managed vegetation cover where EVT_GP = (701,702,703,704,705,706,707,708,709,711,731).",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "No Agricultural Drainage",
-                    "description": "This dataset represents % of land without agricultural drainage, described in DOI: 10.1016/j.scitotenv.2020.137661,  within individual, local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Non-agricultural Introduced Managed Vegetation"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "B3B702B9-1A95-4C4D-B296-1365FAA7E8FE",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=2c91949a-00eb-4196-8b10-dbe9a1191d05"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Non-agricultural Introduced Managed Vegetation",
-            "description": "This dataset represents the percent of non-agricultural, non-native vegetation based on LANDFIRE existing vegetation type (EVT) for a 30-m grid cell within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on field reference data and Landsat, elevation, and ancillary data. EVTs are mapped using decision tree models, field data, Landsat imagery, elevation, and biophysical gradient data. Decision tree models are developed separately for each of the three lifeforms -tree, shrub, and herbaceous and are then used to generate lifeform specific EVT layers.  The LF-GAP Map Units Descriptions provide descriptions for each LF EVT including species, distribution and classification information. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, alliances of the U.S. National Vegetation Classification (USNVC), and the National Land Cover Database and LF specific types. LANDFIRE EVT groups were reclassified into introduced managed vegetation cover where EVT_GP = (701,702,703,704,705,706,707,708,709,711,731).",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21139,70 +21173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B3B702B9-1A95-4C4D-B296-1365FAA7E8FE"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Non-agricultural Introduced Managed Vegetation"
         },
-            "identifier": "B3B702B9-1A95-4C4D-B296-1365FAA7E8FE",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the pesticide use within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. (see Data Sources for links to NHDPlusV2 data and USGS Data). The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the pesticide use within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. (see Data Sources for links to NHDPlusV2 data and USGS Data). The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Non-agricultural Introduced Managed Vegetation",
-                    "description": "This dataset represents the percent of non-agricultural, non-native vegetation based on LANDFIRE existing vegetation type (EVT) for a 30-m grid cell within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on field reference data and Landsat, elevation, and ancillary data. EVTs are mapped using decision tree models, field data, Landsat imagery, elevation, and biophysical gradient data. Decision tree models are developed separately for each of the three lifeforms -tree, shrub, and herbaceous and are then used to generate lifeform specific EVT layers.  The LF-GAP Map Units Descriptions provide descriptions for each LF EVT including species, distribution and classification information. Vegetation map units are primarily derived from NatureServe's Ecological Systems classification, alliances of the U.S. National Vegetation Classification (USNVC), and the National Land Cover Database and LF specific types. LANDFIRE EVT groups were reclassified into introduced managed vegetation cover where EVT_GP = (701,702,703,704,705,706,707,708,709,711,731).",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Pesticide"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "FF4DC154-0BEE-4818-8417-331705B40A12",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B3B702B9-1A95-4C4D-B296-1365FAA7E8FE"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Pesticide",
-            "description": "This dataset represents the pesticide use within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. (see Data Sources for links to NHDPlusV2 data and USGS Data). The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21264,70 +21298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FF4DC154-0BEE-4818-8417-331705B40A12"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Pesticide"
         },
-            "identifier": "FF4DC154-0BEE-4818-8417-331705B40A12",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset consists of predicted probabilities of good biological condition based in the US EPA 2008/2009 National Rivers and Streams Assessment (NRSA). NRSA assesses the biological condition of rivers and streams using several approaches, including a benthic invertebrate multimetric index (BMMI). The development of the NRSA BMMI is documented in the 2008/2009 NRSA Report (https://www.epa.gov/national-aquatic-resource-surveys/national-rivers-and-streams-assessment-2008-2009-results) and by Stoddard et al. (2008) (http://www.bioone.org/doi/abs/10.1899/08-053.1). This assessment resulted in the classification of 1,380 streams as being in good or poor biological condition. These sites were paired with StreamCat data and a random forest model was developed to predict the probable condition of streams based on the binary response of condition to catchment and watershed features. This model was then applied to NHDPlusV2 stream segments that were within the NRSA sampling frame, i.e., streams that were candidates for sampling during the 2008/2009 NRSA (~1.1 million stream segments). Model development was documented in Fox et al. (2017) (https://link.springer.com/article/10.1007/s10661-017-6025-0) and Hill et al. (2017)(http://onlinelibrary.wiley.com/doi/10.1002/eap.1617/full).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset consists of predicted probabilities of good biological condition based in the US EPA 2008/2009 National Rivers and Streams Assessment (NRSA). NRSA assesses the biological condition of rivers and streams using several approaches, including a benthic invertebrate multimetric index (BMMI). The development of the NRSA BMMI is documented in the 2008/2009 NRSA Report (https://www.epa.gov/national-aquatic-resource-surveys/national-rivers-and-streams-assessment-2008-2009-results) and by Stoddard et al. (2008) (http://www.bioone.org/doi/abs/10.1899/08-053.1). This assessment resulted in the classification of 1,380 streams as being in good or poor biological condition. These sites were paired with StreamCat data and a random forest model was developed to predict the probable condition of streams based on the binary response of condition to catchment and watershed features. This model was then applied to NHDPlusV2 stream segments that were within the NRSA sampling frame, i.e., streams that were candidates for sampling during the 2008/2009 NRSA (~1.1 million stream segments). Model development was documented in Fox et al. (2017) (https://link.springer.com/article/10.1007/s10661-017-6025-0) and Hill et al. (2017)(http://onlinelibrary.wiley.com/doi/10.1002/eap.1617/full).",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Pesticide",
-                    "description": "This dataset represents the pesticide use within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from 219, 1-kilometer (km) resolution grids depicting estimated agricultural use of each pesticide in the conterminous United States. Each grid cell value in the national grids of this dataset is the estimated total kilograms (kg) of pesticides applied to row crops, small grain crops and fallow land, pasture and hay crops, and orchard and vineyard crops within the 1- by 1-km area. A single raster was produced using the Raster Calculator Tool adding all 219 grids to form the landscape layer for analysis. (see Data Sources for links to NHDPlusV2 data and USGS Data). The (kilograms of pesticides/square kilometer) was summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Predicted Biological Condition"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "347BAA74-DA58-4F3D-BD51-7A424CAA8EBD",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FF4DC154-0BEE-4818-8417-331705B40A12"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Predicted Biological Condition",
-            "description": "This dataset consists of predicted probabilities of good biological condition based in the US EPA 2008/2009 National Rivers and Streams Assessment (NRSA). NRSA assesses the biological condition of rivers and streams using several approaches, including a benthic invertebrate multimetric index (BMMI). The development of the NRSA BMMI is documented in the 2008/2009 NRSA Report (https://www.epa.gov/national-aquatic-resource-surveys/national-rivers-and-streams-assessment-2008-2009-results) and by Stoddard et al. (2008) (http://www.bioone.org/doi/abs/10.1899/08-053.1). This assessment resulted in the classification of 1,380 streams as being in good or poor biological condition. These sites were paired with StreamCat data and a random forest model was developed to predict the probable condition of streams based on the binary response of condition to catchment and watershed features. This model was then applied to NHDPlusV2 stream segments that were within the NRSA sampling frame, i.e., streams that were candidates for sampling during the 2008/2009 NRSA (~1.1 million stream segments). Model development was documented in Fox et al. (2017) (https://link.springer.com/article/10.1007/s10661-017-6025-0) and Hill et al. (2017)(http://onlinelibrary.wiley.com/doi/10.1002/eap.1617/full).",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21389,70 +21423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=347BAA74-DA58-4F3D-BD51-7A424CAA8EBD"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Predicted Biological Condition"
         },
-            "identifier": "347BAA74-DA58-4F3D-BD51-7A424CAA8EBD",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents predicted channel widths and depths from Doyle et al. 2023. Values include: Predicted wetted width: distance of the water\\\\u2019s edge from left to right bank, Predicted thalweg depth: deepest point in the channel cross section from the bottom substrate to the water surface, Predicted bankfull width: distance from left to right bank at bankfull stage where the potential water height would spill outside of the channel and into the floodplain, and Predicted bankfull depth: thalweg depth plus bankfull height, which is the height from the water surface to the bankfull stage.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents predicted channel widths and depths from Doyle et al. 2023. Values include: Predicted wetted width: distance of the water\\\\u2019s edge from left to right bank, Predicted thalweg depth: deepest point in the channel cross section from the bottom substrate to the water surface, Predicted bankfull width: distance from left to right bank at bankfull stage where the potential water height would spill outside of the channel and into the floodplain, and Predicted bankfull depth: thalweg depth plus bankfull height, which is the height from the water surface to the bankfull stage.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Predicted Biological Condition",
-                    "description": "This dataset consists of predicted probabilities of good biological condition based in the US EPA 2008/2009 National Rivers and Streams Assessment (NRSA). NRSA assesses the biological condition of rivers and streams using several approaches, including a benthic invertebrate multimetric index (BMMI). The development of the NRSA BMMI is documented in the 2008/2009 NRSA Report (https://www.epa.gov/national-aquatic-resource-surveys/national-rivers-and-streams-assessment-2008-2009-results) and by Stoddard et al. (2008) (http://www.bioone.org/doi/abs/10.1899/08-053.1). This assessment resulted in the classification of 1,380 streams as being in good or poor biological condition. These sites were paired with StreamCat data and a random forest model was developed to predict the probable condition of streams based on the binary response of condition to catchment and watershed features. This model was then applied to NHDPlusV2 stream segments that were within the NRSA sampling frame, i.e., streams that were candidates for sampling during the 2008/2009 NRSA (~1.1 million stream segments). Model development was documented in Fox et al. (2017) (https://link.springer.com/article/10.1007/s10661-017-6025-0) and Hill et al. (2017)(http://onlinelibrary.wiley.com/doi/10.1002/eap.1617/full).",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Predicted Channel Widths and Depths"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "7a44ee19-0620-4be9-b82d-e2a42943c067",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=347BAA74-DA58-4F3D-BD51-7A424CAA8EBD"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Predicted Channel Widths and Depths",
-            "description": "This dataset represents predicted channel widths and depths from Doyle et al. 2023. Values include: Predicted wetted width: distance of the water\\\\u2019s edge from left to right bank, Predicted thalweg depth: deepest point in the channel cross section from the bottom substrate to the water surface, Predicted bankfull width: distance from left to right bank at bankfull stage where the potential water height would spill outside of the channel and into the floodplain, and Predicted bankfull depth: thalweg depth plus bankfull height, which is the height from the water surface to the bankfull stage.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21514,70 +21548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7a44ee19-0620-4be9-b82d-e2a42943c067"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Predicted Channel Widths and Depths"
         },
-            "identifier": "7a44ee19-0620-4be9-b82d-e2a42943c067",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents climate observations within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents climate observations within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Predicted Channel Widths and Depths",
-                    "description": "This dataset represents predicted channel widths and depths from Doyle et al. 2023. Values include: Predicted wetted width: distance of the water\\\\u2019s edge from left to right bank, Predicted thalweg depth: deepest point in the channel cross section from the bottom substrate to the water surface, Predicted bankfull width: distance from left to right bank at bankfull stage where the potential water height would spill outside of the channel and into the floodplain, and Predicted bankfull depth: thalweg depth plus bankfull height, which is the height from the water surface to the bankfull stage.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "PRISM Normals Data"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "CE7978C6-6F61-4643-9BAB-695FA4478364",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=7a44ee19-0620-4be9-b82d-e2a42943c067"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: PRISM Normals Data",
-            "description": "This dataset represents climate observations within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21639,70 +21673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=CE7978C6-6F61-4643-9BAB-695FA4478364"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: PRISM Normals Data"
         },
-            "identifier": "CE7978C6-6F61-4643-9BAB-695FA4478364",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents predictions made to individual, local NHDPlusV2 stream segments. Attributes were calculated for every local NHDPlusV2 stream segment. (See Supplementary Info for Glossary of Terms). These predictions were made to provide estimates of reference-condition stream temperatures in support of the 2008-2009 and 2013-2014 (forthcoming) National Rivers and Streams Assessments. These predictions were based on a set of published models (Hill et al. 2013; http://www.journals.uchicago.edu/doi/abs/10.1899/12-009.1). From Hill et al. (2013): \"We modeled 3 ecologically important elements of the thermal regime: mean summer, mean winter, and mean annual stream temperature. These models used a set of least-disturbed USGS stations and sites to model stream temperatures from a set of landscape metrics. To build reference-condition models, we used daily mean ST data obtained from several thousand US Geological Survey temperature sites distributed across the conterminous USA and iteratively modeled ST with Random Forests to identify sites in reference condition. These data are summarized to produce local stream segment-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents predictions made to individual, local NHDPlusV2 stream segments. Attributes were calculated for every local NHDPlusV2 stream segment. (See Supplementary Info for Glossary of Terms). These predictions were made to provide estimates of reference-condition stream temperatures in support of the 2008-2009 and 2013-2014 (forthcoming) National Rivers and Streams Assessments. These predictions were based on a set of published models (Hill et al. 2013; http://www.journals.uchicago.edu/doi/abs/10.1899/12-009.1). From Hill et al. (2013): \"We modeled 3 ecologically important elements of the thermal regime: mean summer, mean winter, and mean annual stream temperature. These models used a set of least-disturbed USGS stations and sites to model stream temperatures from a set of landscape metrics. To build reference-condition models, we used daily mean ST data obtained from several thousand US Geological Survey temperature sites distributed across the conterminous USA and iteratively modeled ST with Random Forests to identify sites in reference condition. These data are summarized to produce local stream segment-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "PRISM Normals Data",
-                    "description": "This dataset represents climate observations within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. PRISM is a set of monthly, yearly, and single-event gridded data products of mean temperature and precipitation, max/min temperatures, and dewpoints, primarily for the United States. In-situ point measurements are ingested into the PRISM (Parameter elevation Regression on Independent Slopes Model) statistical mapping system. The PRISM products use a weighted regression scheme to account for complex climate regimes associated with orography, rain shadows, temperature inversions, slope aspect, coastal proximity, and other factors. These data are summarized by local catchment and by watershed to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Reference Stream Temperature Predictions"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "B93A5967-949A-4075-AA3D-EA60105D2E86",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=CE7978C6-6F61-4643-9BAB-695FA4478364"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Reference Stream Temperature Predictions",
-            "description": "This dataset represents predictions made to individual, local NHDPlusV2 stream segments. Attributes were calculated for every local NHDPlusV2 stream segment. (See Supplementary Info for Glossary of Terms). These predictions were made to provide estimates of reference-condition stream temperatures in support of the 2008-2009 and 2013-2014 (forthcoming) National Rivers and Streams Assessments. These predictions were based on a set of published models (Hill et al. 2013; http://www.journals.uchicago.edu/doi/abs/10.1899/12-009.1). From Hill et al. (2013): \"We modeled 3 ecologically important elements of the thermal regime: mean summer, mean winter, and mean annual stream temperature. These models used a set of least-disturbed USGS stations and sites to model stream temperatures from a set of landscape metrics. To build reference-condition models, we used daily mean ST data obtained from several thousand US Geological Survey temperature sites distributed across the conterminous USA and iteratively modeled ST with Random Forests to identify sites in reference condition. These data are summarized to produce local stream segment-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21764,70 +21798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B93A5967-949A-4075-AA3D-EA60105D2E86"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Reference Stream Temperature Predictions"
         },
-            "identifier": "B93A5967-949A-4075-AA3D-EA60105D2E86",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the density of road and stream crossings within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the density of road and stream crossings within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Reference Stream Temperature Predictions",
-                    "description": "This dataset represents predictions made to individual, local NHDPlusV2 stream segments. Attributes were calculated for every local NHDPlusV2 stream segment. (See Supplementary Info for Glossary of Terms). These predictions were made to provide estimates of reference-condition stream temperatures in support of the 2008-2009 and 2013-2014 (forthcoming) National Rivers and Streams Assessments. These predictions were based on a set of published models (Hill et al. 2013; http://www.journals.uchicago.edu/doi/abs/10.1899/12-009.1). From Hill et al. (2013): \"We modeled 3 ecologically important elements of the thermal regime: mean summer, mean winter, and mean annual stream temperature. These models used a set of least-disturbed USGS stations and sites to model stream temperatures from a set of landscape metrics. To build reference-condition models, we used daily mean ST data obtained from several thousand US Geological Survey temperature sites distributed across the conterminous USA and iteratively modeled ST with Random Forests to identify sites in reference condition. These data are summarized to produce local stream segment-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Road and Stream Intersections"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "FBBEB21F-62C9-4ECA-BE95-EC3F387CE584",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=B93A5967-949A-4075-AA3D-EA60105D2E86"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Road and Stream Intersections",
-            "description": "This dataset represents the density of road and stream crossings within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -21889,70 +21923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FBBEB21F-62C9-4ECA-BE95-EC3F387CE584"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Road and Stream Intersections"
         },
-            "identifier": "FBBEB21F-62C9-4ECA-BE95-EC3F387CE584",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the estimated surface water runoff within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics.(see Data Sources for links to NHDPlusV2 data and metadata) The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month. The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the estimated surface water runoff within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics.(see Data Sources for links to NHDPlusV2 data and metadata) The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month. The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Road and Stream Intersections",
-                    "description": "This dataset represents the density of road and stream crossings within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics. The landscape layer (raster) was developed by James Falcone of the USGS. US Census TIGER 2000 line files of roads and the NHDPlusV1 line files of all streams were converted to 30-meter grids where the presence of a street or stream was a 1 and everything else a 0.  These were intersected and anything that was a 1 in both grids is the result. The density of road and stream crossings (crossings / square kilometer) were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Runoff"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "01927611-2FD4-4AA1-9C11-3FFC24415867",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FBBEB21F-62C9-4ECA-BE95-EC3F387CE584"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Runoff",
-            "description": "This dataset represents the estimated surface water runoff within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics.(see Data Sources for links to NHDPlusV2 data and metadata) The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month. The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22014,70 +22048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=01927611-2FD4-4AA1-9C11-3FFC24415867"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Runoff"
         },
-            "identifier": "01927611-2FD4-4AA1-9C11-3FFC24415867",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents density of septic systems within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  The data is based on the 1990 U.S. Census.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents density of septic systems within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  The data is based on the 1990 U.S. Census.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Runoff",
-                    "description": "This dataset represents the estimated surface water runoff within individual, local NHDPlusV2 catchments and upstream, contributing watersheds. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics.(see Data Sources for links to NHDPlusV2 data and metadata) The landscape layer (raster) was developed with a water-balance model developed by Dave Wolock of the USGS and is detailed further in the paper \"Independent effects of temperature and precipitation on modeled runoff in the conterminous United States\". McCabe and Wolock[2011] Runoff is defined as the flow per unit area delivered to streams and rivers in units of millimeters per month. The runoff estimates were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Septic System Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "decccf96-783c-4e0e-962c-27da23c0289b",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=01927611-2FD4-4AA1-9C11-3FFC24415867"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Septic System Density",
-            "description": "This dataset represents density of septic systems within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  The data is based on the 1990 U.S. Census.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22139,70 +22173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
-            "modified": "2023-11-13",
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=decccf96-783c-4e0e-962c-27da23c0289b"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Septic System Density"
         },
-            "identifier": "decccf96-783c-4e0e-962c-27da23c0289b",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents slope percent along stream within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents slope percent along stream within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Septic System Density",
-                    "description": "This dataset represents density of septic systems within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.  The data is based on the 1990 U.S. Census.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Slope Along Stream"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "105c1dc2-0360-4681-a4f0-c579463d5a79",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=decccf96-783c-4e0e-962c-27da23c0289b"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Slope Along Stream",
-            "description": "This dataset represents slope percent along stream within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22264,70 +22298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=105c1dc2-0360-4681-a4f0-c579463d5a79"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Slope Along Stream"
         },
-            "identifier": "105c1dc2-0360-4681-a4f0-c579463d5a79",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the soil characteristic within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the STATSGO landscape rasters. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the soil characteristic within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the STATSGO landscape rasters. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Slope Along Stream",
-                    "description": "This dataset represents slope percent along stream within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "State Soil Geographic Database (STATSGO) (KFFACT)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "EBB945ED-0151-4DBF-8FE0-806165A58973",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=105c1dc2-0360-4681-a4f0-c579463d5a79"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: State Soil Geographic Database (STATSGO) (KFFACT)",
-            "description": "This dataset represents the soil characteristic within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the STATSGO landscape rasters. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22389,70 +22423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=EBB945ED-0151-4DBF-8FE0-806165A58973"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: State Soil Geographic Database (STATSGO) (KFFACT)"
         },
-            "identifier": "EBB945ED-0151-4DBF-8FE0-806165A58973",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents estimated surface water TN flux within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg N/km2.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents estimated surface water TN flux within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg N/km2.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "State Soil Geographic Database (STATSGO) (KFFACT)",
-                    "description": "This dataset represents the soil characteristic within individual, local NHDPlusV2 catchments and upstream, contributing watersheds based on the STATSGO landscape rasters. Attributes of the landscape layer were calculated for every local NHDPlusV2 catchment and accumulated to provide watershed-level metrics. This data set is derived from the STATSGO landscape rasters for the conterminous USA. Individual rasters (Landscape Layers) of depth to bedrock (rckdep), organic material (om), percent clay (clay), percent sand (sand), permeability (perm), soil erodibility (KFFACT/KFACT), and water table depth (wtdep) were used to calculate soil characteristics for each NHDPlusV2 catchment.  The soil characteristics were summarized to produce local catchment-level and watershed-level metrics as a continuous data type. The STATSGO data are distributed in two sets, STATSGO_Set1 and STATSGO_Set2, based on common NoData locations in each set of soil GIS layers.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Surface Water Nitrogen Flux"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "956964c5-b117-49b7-b469-35b90d95574a",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=EBB945ED-0151-4DBF-8FE0-806165A58973"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surface Water Nitrogen Flux",
-            "description": "This dataset represents estimated surface water TN flux within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg N/km2.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22514,70 +22548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=956964c5-b117-49b7-b469-35b90d95574a"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surface Water Nitrogen Flux"
         },
-            "identifier": "956964c5-b117-49b7-b469-35b90d95574a",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents estimated surface water TN load within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg Nitrogen.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents estimated surface water TN load within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg Nitrogen.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Surface Water Nitrogen Flux",
-                    "description": "This dataset represents estimated surface water TN flux within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg N/km2.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Surface Water Nitrogen Load"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "4ab1a8a0-1413-48df-a25f-316f6812c0af",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=956964c5-b117-49b7-b469-35b90d95574a"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surface Water Nitrogen Load",
-            "description": "This dataset represents estimated surface water TN load within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg Nitrogen.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22639,70 +22673,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=4ab1a8a0-1413-48df-a25f-316f6812c0af"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surface Water Nitrogen Load"
         },
-            "identifier": "4ab1a8a0-1413-48df-a25f-316f6812c0af",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the density of 18 USGS lithology classes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds(see Data Sources for links to NHDPlusV2 data and USGS). Attributes were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics for USGS lithology data. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the density of 18 USGS lithology classes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds(see Data Sources for links to NHDPlusV2 data and USGS). Attributes were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics for USGS lithology data. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Surface Water Nitrogen Load",
-                    "description": "This dataset represents estimated surface water TN load within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as kg Nitrogen.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Surficial Lithology in Watershed"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "33D3BE86-634D-43F8-984E-FAA8A29861FD",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=4ab1a8a0-1413-48df-a25f-316f6812c0af"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surficial Lithology in Watershed",
-            "description": "This dataset represents the density of 18 USGS lithology classes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds(see Data Sources for links to NHDPlusV2 data and USGS). Attributes were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics for USGS lithology data. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22764,70 +22798,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=33D3BE86-634D-43F8-984E-FAA8A29861FD"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surficial Lithology in Watershed"
         },
-            "identifier": "33D3BE86-634D-43F8-984E-FAA8A29861FD",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents surplus precipitation (mm): precipitation minus potential evaporation described in DOI: 10.1016/j.scitotenv.2020.137661 within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents surplus precipitation (mm): precipitation minus potential evaporation described in DOI: 10.1016/j.scitotenv.2020.137661 within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Surficial Lithology in Watershed",
-                    "description": "This dataset represents the density of 18 USGS lithology classes within individual, local NHDPlusV2 catchments and upstream, contributing watersheds(see Data Sources for links to NHDPlusV2 data and USGS). Attributes were calculated for every local NHDPlusV2 catchment and then accumulated to provide watershed-level metrics for USGS lithology data. This data set is derived from the USGS raster map of 18 lithology classes (categorical data type) for the conterminous USA. The map was produced based on texture, internal structure, thickness, and environment of deposition or formation of materials. These 18 lithology classes were summarized by local catchment and by watershed to produce 18 local catchment-level and watershed-level metrics as a categorical data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Surplus Precipitation"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "348ecacb-d9ba-491d-bcc4-3518540488f7",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=33D3BE86-634D-43F8-984E-FAA8A29861FD"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surplus Precipitation",
-            "description": "This dataset represents surplus precipitation (mm): precipitation minus potential evaporation described in DOI: 10.1016/j.scitotenv.2020.137661 within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -22889,70 +22923,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=348ecacb-d9ba-491d-bcc4-3518540488f7"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Surplus Precipitation"
         },
-            "identifier": "348ecacb-d9ba-491d-bcc4-3518540488f7",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents density of all wastewater treatment plants within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as number/ km2.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents density of all wastewater treatment plants within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as number/ km2.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Surplus Precipitation",
-                    "description": "This dataset represents surplus precipitation (mm): precipitation minus potential evaporation described in DOI: 10.1016/j.scitotenv.2020.137661 within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wastewater Treatment Density"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "c698cf93-23ed-4854-9749-757acf3b8a82",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=348ecacb-d9ba-491d-bcc4-3518540488f7"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wastewater Treatment Density",
-            "description": "This dataset represents density of all wastewater treatment plants within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as number/ km2.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23014,70 +23048,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c698cf93-23ed-4854-9749-757acf3b8a82"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wastewater Treatment Density"
         },
-            "identifier": "c698cf93-23ed-4854-9749-757acf3b8a82",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents water input, measured as km2/cm: Ratio of the total area of irrigated land to precipitation within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents water input, measured as km2/cm: Ratio of the total area of irrigated land to precipitation within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wastewater Treatment Density",
-                    "description": "This dataset represents density of all wastewater treatment plants within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds. Measured as number/ km2.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Water Input"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "478be3b3-3c4e-4028-94a3-5a26e9c922a8",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c698cf93-23ed-4854-9749-757acf3b8a82"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Water Input",
-            "description": "This dataset represents water input, measured as km2/cm: Ratio of the total area of irrigated land to precipitation within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23139,70 +23173,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=478be3b3-3c4e-4028-94a3-5a26e9c922a8"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Water Input"
         },
-            "identifier": "478be3b3-3c4e-4028-94a3-5a26e9c922a8",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the wetness index within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). The Composite Topographic Index (CTI) is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the wetness index within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). The Composite Topographic Index (CTI) is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Water Input",
-                    "description": "This dataset represents water input, measured as km2/cm: Ratio of the total area of irrigated land to precipitation within individual,  local NHDPlusV2 catchments and upstream, contributing watersheds.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wetness Index"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "FAACFBF4-4C14-42A3-8D3C-7C9E5546BDF0",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=478be3b3-3c4e-4028-94a3-5a26e9c922a8"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wetness Index",
-            "description": "This dataset represents the wetness index within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). The Composite Topographic Index (CTI) is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23264,70 +23298,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FAACFBF4-4C14-42A3-8D3C-7C9E5546BDF0"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wetness Index"
         },
-            "identifier": "FAACFBF4-4C14-42A3-8D3C-7C9E5546BDF0",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wetness Index",
-                    "description": "This dataset represents the wetness index within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the Composite Topographic Index (See Supplementary Info for Glossary of Terms). The Composite Topographic Index (CTI) is based on contributing area, slope, and overland flow and has been developed internally at the EPA for the EnviroAtls (http://edg.epa.gov/data/Public/ORD/EnviroAtlas/National/). As defined for use in EnviroAtlas datasets and as used here, wet areas are typically created by runoff from natural land cover when rain falls on saturated soil. Surface and rill (or small channel) runoff carries excess water to lowland depressions or wet areas. Runoff collects in wet areas until they fill and overflow downstream. In this way, stream networks can be extended into new areas that would not be hydrologically connected during drier times. Wet area expansion and watershed hydrological connectivity differ between humid temperate and semi-arid and arid climates (where drought and soil crusts limit infiltration and produce flashier runoff) (from https://enviroatlas.epa.gov/enviroatlas/datafactsheets/pdf/ESN/PercentForestonWetAreas.pdf). The Mean Composite Topographic Index (CTI)[Wetness Index] were summarized to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildfire Burn Percent 1984-2018 (MTBS)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "4c505425-5e38-48dd-9064-b19baeafef9f",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=FAACFBF4-4C14-42A3-8D3C-7C9E5546BDF0"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Percent 1984-2018 (MTBS)",
-            "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23389,70 +23423,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=4c505425-5e38-48dd-9064-b19baeafef9f"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Percent 1984-2018 (MTBS)"
         },
-            "identifier": "4c505425-5e38-48dd-9064-b19baeafef9f",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildfire Burn Percent 1984-2018 (MTBS)",
-                    "description": "This dataset represents mean percent are burned from wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018. The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildfire Burn Severity Class 1984-2018 (MTBS)"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "c92338f3-6d37-4425-9fde-e24780759ebe",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=4c505425-5e38-48dd-9064-b19baeafef9f"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Severity Class 1984-2018",
-            "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23514,70 +23548,70 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c92338f3-6d37-4425-9fde-e24780759ebe"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildfire Burn Severity Class 1984-2018"
         },
-            "identifier": "c92338f3-6d37-4425-9fde-e24780759ebe",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3Y",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
+                "hasEmail": "mailto:weber.marc@epa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+            "describedByType": "text/html",
+            "description": "This dataset represents the historical fire perimeters within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
                     "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
                     "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "StreamCat Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
+                    "describedByType": "text/html",
+                    "description": "This dataset represents the historical fire perimeters within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
                     "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
                     "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildfire Burn Severity Class 1984-2018 (MTBS)",
-                    "description": "This dataset represents percent area burned in each burn severity class for wildfires within individual local and accumulated upstream catchments for NHDPlusV2 Waterbodies for each year for 1984-2018.The Monitoring Trends in Burn Severity MTBS project assesses the frequency, extent, and magnitude (size and severity) of all large wildland fires (includes wildfire, wildland fire use, and prescribed fire) in the conterminous United States (CONUS), Alaska, Hawaii, and Puerto Rico from the beginning of the Landsat Thematic Mapper archive to the present.  See: https://catalog.data.gov/dataset/monitoring-trends-in-burn-severity-burned-area-boundaries-feature-layer-27201 and https://www.mtbs.gov/product-descriptions",
                     "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "title": "Wildland Fire Perimeters By Year 2000 - 2010"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
+            "identifier": "1179C18B-1EDF-4102-A93A-F77F2772E769",
             "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=c92338f3-6d37-4425-9fde-e24780759ebe"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildland Fire Perimeters By Year 2000 - 2010",
-            "description": "This dataset represents the historical fire perimeters within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
             "keyword": [
                 "inlandwaters",
                 "ecosystem",
@@ -23639,76 +23673,58 @@
                 "wisconsin",
                 "wyoming"
             ],
+            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-11-13",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), "
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "U.S. Environmental Protection Agency, Office of Research and Development (ORD), Center for Public Health and Environmental Assessment (CPHEA), Pacific Ecological Systems Division (PESD), Marc Weber",
-                "hasEmail": "mailto:weber.marc@epa.gov"
+            "references": [
+                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
+                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1179C18B-1EDF-4102-A93A-F77F2772E769"
+            ],
+            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
+            "spatial": "-125.0,24.5,-66.5,49.5",
+            "temporal": "2015/2030",
+            "theme": [
+                "environment"
+            ],
+            "title": "The StreamCat Dataset: Accumulated Attributes for NHDPlusV2 (Version 2.1) Catchments for the Conterminous United States: Wildland Fire Perimeters By Year 2000 - 2010"
         },
-            "identifier": "1179C18B-1EDF-4102-A93A-F77F2772E769",
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "rights": "public (Data asset is or could be made publicly available to all without restrictions)",
-            "spatial": "-125.0,24.5,-66.5,49.5",
-            "temporal": "2015/2030",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ann Vega",
+                "hasEmail": "mailto:vega.ann@epa.gov"
+            },
+            "dataQuality": true,
+            "description": "PubMed Central (PMC) is a full-text, online archive of journal literature operated by the National Library of Medicine. The EPA is using PMC to permanently preserve and provide easy public access to the peer-reviewed papers resulting from EPA-funded research.\u00a0",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-                    "title": "StreamCat Dataset",
-                    "description": "StreamCat currently contains over 600 metrics that include local catchment (Cat), watershed (Ws), and special metrics. The special metrics were derived through modeling or by combining other StreamCat metrics. These variables include predicted water temperature, predicted biological condition, and the indexes of catchment and watershed integrity. See Geospatial Framework and Terms below for definitions of catchment and watershed as used with the StreamCat Dataset.\n\nThese metrics are available for ~2.65 million stream segments and their associated catchments across the conterminous US. StreamCat metrics represent both natural (e.g., soils and geology) and anthropogenic (e.g, urban areas and agriculture) landscape information.",
-                    "format": "API",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                    "format": "Comma-Separated Values (.csv)",
-                    "title": "Wildland Fire Perimeters By Year 2000 - 2010",
-                    "description": "This dataset represents the historical fire perimeters within individual local NHDPlusV2 catchments and upstream, contributing watersheds based on the GeoMAC (Geospatial Multi-Agency Coordination) mapping tool. Fire perimeters contain data as they are submitted by field offices to GeoMAC (Geospatial Multi-Agency Coordination) in a polygon format. Fire perimeter data is based on input from incident intelligence sources, GPS data, infrared (IR) imagery from fixed wing and satellite platforms. Polygons are selected by year and then converted into a binary raster format where values of 1 represent fire perimeters of the given year and 0 describes the remaining areas across the CONUS, leaving No Data to be anything outside the CONUS border. The wildland fire characteristics (% forest loss to fire) were summarized by year to produce local catchment-level and watershed-level metrics as a continuous data type.",
-                    "mediaType": "text/csv",
-                    "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-                    "describedByType": "text/html"
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa",
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P3Y",
-            "dataQuality": true,
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-metrics-and-definitions",
-            "describedByType": "text/html",
-            "issued": "2015-04-23",
-            "language": [
-                "en-US"
-            ],
-            "landingPage": "https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset",
-            "references": [
-                "https://gaftp.epa.gov/EPADataCommons/ORD/NHDPlusLandscapeAttributes/StreamCat/HydroRegions/",
-                "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=1179C18B-1EDF-4102-A93A-F77F2772E769"
-            ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Environmental Protection Agency"
-            },
-            "references": [
-                "https://www.ncbi.nlm.nih.gov/pmc/about/public-access/"
-            ],
-            "accessLevel": "public",
-            "description": "PubMed Central (PMC) is a full-text, online archive of journal literature operated by the National Library of Medicine. The EPA is using PMC to permanently preserve and provide easy public access to the peer-reviewed papers resulting from EPA-funded research.\u00a0",
+            "identifier": "00bf8c5a-dc57-11e7-9296-cec278b6b50a",
+            "issued": "2017-04-17",
             "keyword": [
                 "EPA Pub Central",
                 "PMC Funders",
@@ -23718,49 +23734,44 @@
                 "EPA Articles on PMC",
                 "EPA Research Papers"
             ],
-            "title": "Environmental Protection Agency - EPA Pub Central",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa/",
             "language": [
                 "en-US"
             ],
-            "distribution": [
-                {
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa",
-                    "@type": "dcat:Distribution"
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2014-04-17",
+            "programCode": [
+                "020:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Environmental Protection Agency"
             },
-                {
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa",
-                    "@type": "dcat:Distribution",
-                    "mediaType": "text/plain"
-                }
+            "references": [
+                "https://www.ncbi.nlm.nih.gov/pmc/about/public-access/"
             ],
-            "modified": "2014-04-17",
+            "spatial": "-80.542601,36.666691,-74.580735,42.987042",
             "theme": [
                 "environment"
             ],
-            "dataQuality": true,
-            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/funder/epa/",
+            "title": "Environmental Protection Agency - EPA Pub Central"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "020:00"
             ],
-            "issued": "2017-04-17",
-            "accrualPeriodicity": "R/P1D",
-            "spatial": "-80.542601,36.666691,-74.580735,42.987042",
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "contactPoint": {
-                "hasEmail": "mailto:vega.ann@epa.gov",
                 "@type": "vcard:Contact",
-                "fn": "Ann Vega"
-            },
-            "identifier": "00bf8c5a-dc57-11e7-9296-cec278b6b50a",
-            "@type": "dcat:Dataset"
+                "fn": "Thomas Speth, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:Speth.Thomas@epa.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Drinking Water Treatability Database (TDB)",
+            "dataQuality": false,
             "description": "The Drinking Water Treatability Database (TDB) presents referenced information on the control of contaminants in drinking water. It allows drinking water utilities, first responders to spills or emergencies, treatment process designers, research organizations, regulators and others to access referenced information gathered from thousands of literature sources on regulated and unregulated contaminants.",
+            "identifier": "{05F6B3E7-ED0F-468D-8D74-DA40D48DD100}",
+            "issued": "2014-01-01",
             "keyword": [
                 "human health",
                 "health risks",
@@ -23772,46 +23783,43 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Speth, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:Speth.Thomas@epa.gov"
-            },
-            "identifier": "{05F6B3E7-ED0F-468D-8D74-DA40D48DD100}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B05F6B3E7-ED0F-468D-8D74-DA40D48DD100%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B05F6B3E7-ED0F-468D-8D74-DA40D48DD100%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Drinking Water Treatability Database (TDB)"
         },
         {
-            "title": "Office of Water Linked Data",
-            "description": "The Office of Water Linked Data (OWLD) dataset stores EPA Water program information indexed to several National Hydrography Dataset frameworks. Indexing may be accomplished by catchment, reach or hydrologic unit referencing and includes a curated set of relevant program data attributes. OWLD is closely related to the NHD Event Data model with extensions added to cover catchment-based indexing.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. EPA Office of Water (OW)"
-            },
+            "accessLevel": "public",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WATERS Support",
                 "hasEmail": "mailto:waters_support@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Water Linked Data (OWLD) dataset stores EPA Water program information indexed to several National Hydrography Dataset frameworks. Indexing may be accomplished by catchment, reach or hydrologic unit referencing and includes a curated set of relevant program data attributes. OWLD is closely related to the NHD Event Data model with extensions added to cover catchment-based indexing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://watersgeo.epa.gov/arcgis/rest/services/owld",
+                    "format": "API",
+                    "title": "Office of Water GIS Services for OWLD datasets"
+                }
+            ],
+            "identifier": "d4ae8812-b921-40ee-96b5-ba9829b96568",
             "keyword": [
                 "environment",
                 "Surface Water",
@@ -23824,42 +23832,34 @@
                 "stream network",
                 "NHDPlus"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "modified": "2024-05-14",
-            "identifier": "d4ae8812-b921-40ee-96b5-ba9829b96568",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2000-01-01/2024-05-14",
-            "dataQuality": true,
             "landingPage": "https://www.epa.gov/waterdata/waters-watershed-assessment-tracking-environmental-results-system/",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://watersgeo.epa.gov/arcgis/rest/services/owld",
-                    "title": "Office of Water GIS Services for OWLD datasets",
-                    "format": "API"
-                }
-            ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2024-05-14",
+            "primaryitinvestmentuii": "020-000000087",
             "programCode": [
                 "020:112"
             ],
-            "primaryitinvestmentuii": "020-000000087"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Water Contaminant Information Tool",
-            "description": "The Water Contaminant Information Tool (WCIT) is a secure, on-line database that provides current, reliable information on chemical, biological, and radiological contaminants of concern for water security. The WCIT database assists in planning for and responding to drinking water and wastewater (water) contamination threats and incidents. As a planning tool, WCIT supports vulnerability assessments, emergency response plans, and site-specific response guidelines. As a response tool, WCIT provides contaminant data to help responders (including utilities) make appropriate response decisions. WCIT also helps EPA to identify gaps in contaminant data, which will, in turn, help inform future research efforts.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW)"
             },
+            "temporal": "2000-01-01/2024-05-14",
+            "title": "Office of Water Linked Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Veronica Aponte-Morales",
                 "hasEmail": "mailto:aponte-morales.veronica@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The Water Contaminant Information Tool (WCIT) is a secure, on-line database that provides current, reliable information on chemical, biological, and radiological contaminants of concern for water security. The WCIT database assists in planning for and responding to drinking water and wastewater (water) contamination threats and incidents. As a planning tool, WCIT supports vulnerability assessments, emergency response plans, and site-specific response guidelines. As a response tool, WCIT provides contaminant data to help responders (including utilities) make appropriate response decisions. WCIT also helps EPA to identify gaps in contaminant data, which will, in turn, help inform future research efforts.",
+            "identifier": "c3b1fc8c-3966-46b4-84ba-92cb4529ccfd",
             "keyword": [
                 "Chemicals",
                 "Drinking Water",
@@ -23870,34 +23870,35 @@
                 "Drinking Water Utilities",
                 "Water Security"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "modified": "2021",
-            "identifier": "c3b1fc8c-3966-46b4-84ba-92cb4529ccfd",
-            "accessLevel": "non-public",
             "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "temporal": "2005/2021",
-            "dataQuality": true,
+            "modified": "2021",
+            "primaryitinvestmentuii": "020-000000087",
             "programCode": [
                 "020:038"
             ],
-            "systemofrecords": "https://www.epa.gov/privacy/privacy-act-system-records-epa-central-data-exchange-customer-registration-subsystem-epa-52",
-            "primaryitinvestmentuii": "020-000000087"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WIFIA Vault",
-            "description": "The Water Infrastructure Finance and Innovation Act of 2014 (WIFIA) established a federal credit program administered by EPA. WIFIA authorizes EPA to provide loans to eligible water infrastructure projects. After a loan is closed, WIFIA\u2019s portfolio management team leads individual transactions from closing to final maturity (this can be 35+ years). Portfolio management responsibilities are numerous but generally are intended to achieve the following critical objectives:\n\u2022\tmonitor portfolio risk and compliance, \n\u2022\ttrack key loan requirements, information and status, \n\u2022\tdocument and track disbursements, repayments, and related accounting actions, \n\u2022\tmaintain and document borrower communication, and \n\u2022\tmaintain robust loan-specific and portfolio-wide metrics reporting capabilities.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW)"
             },
+            "systemofrecords": "https://www.epa.gov/privacy/privacy-act-system-records-epa-central-data-exchange-customer-registration-subsystem-epa-52",
+            "temporal": "2005/2021",
+            "title": "Water Contaminant Information Tool"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Kudzai Mukushi",
-                "hasEmail": "mailto:Mukushi.Kudzai@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:Mukushi.Kudzai@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The Water Infrastructure Finance and Innovation Act of 2014 (WIFIA) established a federal credit program administered by EPA. WIFIA authorizes EPA to provide loans to eligible water infrastructure projects. After a loan is closed, WIFIA\u2019s portfolio management team leads individual transactions from closing to final maturity (this can be 35+ years). Portfolio management responsibilities are numerous but generally are intended to achieve the following critical objectives:\n\u2022\tmonitor portfolio risk and compliance, \n\u2022\ttrack key loan requirements, information and status, \n\u2022\tdocument and track disbursements, repayments, and related accounting actions, \n\u2022\tmaintain and document borrower communication, and \n\u2022\tmaintain robust loan-specific and portfolio-wide metrics reporting capabilities.",
+            "identifier": "7a9c7c95-3f18-4ece-aad0-dc748a206d89",
             "keyword": [
                 "Water",
                 "Drinking Water",
@@ -23908,34 +23909,34 @@
                 "Finance",
                 "Infrastructure"
             ],
-            "identifier": "7a9c7c95-3f18-4ece-aad0-dc748a206d89",
-            "accessLevel": "non-public",
             "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "bureauCode": [
-                "020:00"
-            ],
-            "temporal": "2019/2021",
-            "accrualPeriodicity": "R/P1D",
-            "dataQuality": true,
+            "modified": "2021-12-14",
+            "primaryitinvestmentuii": "020-000000104",
             "programCode": [
                 "020:000"
             ],
-            "primaryitinvestmentuii": "020-000000104",
-            "modified": "2021-12-14"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Data on Aquatic Resources Tracking for Effective Regulation",
-            "description": "DARTER is EPA's system to manage its workflow in the Clean Water Act Section 404 permit program. Section 404 requires a permit from the U.S. Army Corps of Engineers, or EPA-approved State, for the discharge of dredged or fill material into waters of the United States. EPA plays a number of roles in the Section 404 permit program including developing and interpreting policy, guidance and environmental criteria used in evaluating permit applications, determining the scope of geographic jurisdiction and reviewing and commenting on proposed Section 404 permits. DARTER allows EPA staff to: \n- Track agency involvement in pre-application coordination, review of public notices for proposed permits, review of third party mitigation projects and proposed jurisdictional determinations;\n- Prepare and share EPA-generated jurisdictional determinations; and\n- Access shared data from the U.S. Army Corps of Engineers\u2019 national regulatory program data management system known as OMBIL Regulatory Module (ORM2)\n",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW)"
             },
+            "temporal": "2019/2021",
+            "title": "WIFIA Vault"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Brian Topping",
-                "hasEmail": "mailto:Topping.Brian@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:Topping.Brian@epa.gov"
             },
+            "dataQuality": true,
+            "description": "DARTER is EPA's system to manage its workflow in the Clean Water Act Section 404 permit program. Section 404 requires a permit from the U.S. Army Corps of Engineers, or EPA-approved State, for the discharge of dredged or fill material into waters of the United States. EPA plays a number of roles in the Section 404 permit program including developing and interpreting policy, guidance and environmental criteria used in evaluating permit applications, determining the scope of geographic jurisdiction and reviewing and commenting on proposed Section 404 permits. DARTER allows EPA staff to: \n- Track agency involvement in pre-application coordination, review of public notices for proposed permits, review of third party mitigation projects and proposed jurisdictional determinations;\n- Prepare and share EPA-generated jurisdictional determinations; and\n- Access shared data from the U.S. Army Corps of Engineers\u2019 national regulatory program data management system known as OMBIL Regulatory Module (ORM2)\n",
+            "identifier": "c916f0ad-d87b-4b60-8d33-80e0f093fa15",
             "keyword": [
                 "Surface Water",
                 "United States",
@@ -23949,34 +23950,34 @@
                 "Mitigation",
                 "Jurisdictional determinations"
             ],
-            "identifier": "c916f0ad-d87b-4b60-8d33-80e0f093fa15",
-            "accessLevel": "restricted public",
             "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "bureauCode": [
-                "020:00"
-            ],
-            "temporal": "1987/2021",
-            "accrualPeriodicity": "R/P1D",
-            "dataQuality": true,
+            "modified": "2023-02-28",
+            "primaryitinvestmentuii": "020-000000087",
             "programCode": [
                 "020:112"
             ],
-            "primaryitinvestmentuii": "020-000000087",
-            "modified": "2023-02-28"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Water Quality Portal",
-            "description": "The Water Quality Portal (WQP) is the premiere source of discrete water-quality data in the United States and beyond. This cooperative service integrates publicly available water-quality data from the United States Geological Survey (USGS), the Environmental Protection Agency (EPA), and over 400 state, federal, tribal, and local agencies.",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "U.S. Geological Survey and U.S. EPA Office of Water (OW)"
+                "name": "U.S. EPA Office of Water (OW)"
+            },
+            "temporal": "1987/2021",
+            "title": "Data on Aquatic Resources Tracking for Effective Regulation"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "020:00"
+            ],
             "contactPoint": {
+                "@type": "vcard:Contact",
                 "fn": "Kevin Christian",
-                "hasEmail": "mailto:christian.kevin@epa.gov",
-                "@type": "vcard:Contact"
+                "hasEmail": "mailto:christian.kevin@epa.gov"
             },
+            "dataQuality": true,
+            "description": "The Water Quality Portal (WQP) is the premiere source of discrete water-quality data in the United States and beyond. This cooperative service integrates publicly available water-quality data from the United States Geological Survey (USGS), the Environmental Protection Agency (EPA), and over 400 state, federal, tribal, and local agencies.",
+            "identifier": "28bc151c-da9c-4daa-a45d-cb92141cb6a2",
             "keyword": [
                 "Waste",
                 "Surface Water",
@@ -23994,26 +23995,36 @@
                 "NWIS",
                 "Stewards"
             ],
-            "identifier": "28bc151c-da9c-4daa-a45d-cb92141cb6a2",
-            "accessLevel": "public",
-            "license": "https://edg.epa.gov/EPA_Data_License.html",
-            "bureauCode": [
-                "020:00"
-            ],
-            "temporal": "1987/2021",
-            "accrualPeriodicity": "R/P1D",
-            "dataQuality": true,
             "landingPage": "https://www.waterqualitydata.us/",
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
+            "modified": "2021-12-14",
+            "primaryitinvestmentuii": "020-000000103",
             "programCode": [
                 "020:112"
             ],
-            "primaryitinvestmentuii": "020-000000103",
-            "modified": "2021-12-14"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Geological Survey and U.S. EPA Office of Water (OW)"
+            },
+            "temporal": "1987/2021",
+            "title": "Water Quality Portal"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State-Specific Water Quality Standards Effective under the Clean Water Act (CWA)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Gregory Stapleton, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
+                "hasEmail": "mailto:stapleton.gregory@epa.gov"
+            },
+            "dataQuality": false,
             "description": " EPA has compiled state, territorial, and authorized tribal water quality standards that EPA has approved or are otherwise in effect for Clean Water Act purposes.  This compilation is continuously updated as EPA approves new or revised WQS.Please note the water quality standards may contain additional provisions outside the scope of the Clean Water Act, its implementing federal regulations, or EPA's authority. In some cases, these additional provisions have been included as supplementary information. EPA is posting the water quality standards as a convenience to users and has made a reasonable effort to assure their accuracy. Additionally, EPA has made a reasonable effort to identify parts of the standards that are approved, disapproved, or are otherwise not in effect for Clean Water Act purposes.",
+            "identifier": "{6D51530E-0EFF-4126-8404-36C00A8F1548}",
+            "issued": "2014-01-01",
             "keyword": [
                 "environmental media topics",
                 "water",
@@ -24033,39 +24044,39 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2014-01-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Gregory Stapleton, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
-                "hasEmail": "mailto:stapleton.gregory@epa.gov"
-            },
-            "identifier": "{6D51530E-0EFF-4126-8404-36C00A8F1548}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://www.epa.gov/wqs-tech/state-specific-water-quality-standards-effective-under-clean-water-act-cwa",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B6D51530E-0EFF-4126-8404-36C00A8F1548%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B6D51530E-0EFF-4126-8404-36C00A8F1548%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "State-Specific Water Quality Standards Effective under the Clean Water Act (CWA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Wetland Program Pilot Grants",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
+                "hasEmail": "mailto:price.myra@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Wetland Grant Database (WGD) houses grant data for Wetland Program Development Grants (created by EPA in 1990 under the Clean Water Act Section 104(b)(3) authority).   The Wetland Grants Database contains further information on Wetland Program Pilot Grants that were awarded in past years.",
+            "identifier": "{A719BA4D-91AC-45AC-BFFD-46EF90AC7F9C}",
+            "issued": "2014-01-01",
             "keyword": [
                 "wetlands",
                 "grants",
@@ -24081,38 +24092,38 @@
                 "united states",
                 "inlandwaters"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-01",
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
-                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
-                "hasEmail": "mailto:price.myra@epa.gov"
-            },
-            "identifier": "{A719BA4D-91AC-45AC-BFFD-46EF90AC7F9C}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BA719BA4D-91AC-45AC-BFFD-46EF90AC7F9C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BA719BA4D-91AC-45AC-BFFD-46EF90AC7F9C%7D"
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
+            "title": "Wetland Program Pilot Grants"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Wetland Program Development Grants (WPDGs) Case Studies",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
+                "hasEmail": "mailto:price.myra@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Wetland Grant Database (WGD) houses grant data for Wetland Program Development Grants (created by EPA in 1990 under the Clean Water Act Section 104(b)(3) authority).   The Wetland Grants Database contains further information on WPDG Case Studies that were awarded in past years.",
+            "identifier": "{FDA9BF78-09CC-4E36-B74D-04F770973E57}",
+            "issued": "2014-01-01",
             "keyword": [
                 "wetlands",
                 "grants",
@@ -24128,38 +24139,38 @@
                 "united states",
                 "inlandwaters"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-01",
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
-                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
-                "hasEmail": "mailto:price.myra@epa.gov"
-            },
-            "identifier": "{FDA9BF78-09CC-4E36-B74D-04F770973E57}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BFDA9BF78-09CC-4E36-B74D-04F770973E57%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BFDA9BF78-09CC-4E36-B74D-04F770973E57%7D"
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
+            "title": "Wetland Program Development Grants (WPDGs) Case Studies"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Wetland Program Development Grants (WPDGs)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
+                "hasEmail": "mailto:price.myra@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Wetland Grant Database (WGD) houses grant data for Wetland Program Development Grants (created by EPA in 1990 under the Clean Water Act Section 104(b)(3) authority).   The Wetland Grants Database contains further information on Wetland Program Development Grants that were awarded in past years.",
+            "identifier": "{1893AF89-489E-4D8B-9308-DC401A4F716A}",
+            "issued": "2014-01-01",
             "keyword": [
                 "wetlands",
                 "grants",
@@ -24175,38 +24186,38 @@
                 "united states",
                 "inlandwaters"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-01",
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
-                "fn": "Myra Price, U.S. EPA Office of Water (OW)",
-                "hasEmail": "mailto:price.myra@epa.gov"
-            },
-            "identifier": "{1893AF89-489E-4D8B-9308-DC401A4F716A}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1893AF89-489E-4D8B-9308-DC401A4F716A%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1893AF89-489E-4D8B-9308-DC401A4F716A%7D"
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
+            "title": "Wetland Program Development Grants (WPDGs)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unregulated Contaminant Monitoring Program Data",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "EPA uses the Unregulated Contaminant Monitoring (UCM) program to collect data for contaminants suspected to be present in drinking water, but that do not have health-based standards set under the Safe Drinking Water Act (SDWA). Every five years EPA reviews the list of contaminants, largely based on the Contaminant Candidate List.",
+            "identifier": "{F31D0AC6-A317-41D9-A0B2-06304478185C}",
+            "issued": "2014-01-01",
             "keyword": [
                 "pollution prevention",
                 "pollution prevention",
@@ -24215,38 +24226,38 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "modified": "2012-05-02",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{F31D0AC6-A317-41D9-A0B2-06304478185C}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF31D0AC6-A317-41D9-A0B2-06304478185C%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF31D0AC6-A317-41D9-A0B2-06304478185C%7D"
             ],
-            "bureauCode": [
-                "020:00"
-            ],
-            "programCode": [
-                "020:072"
-            ],
-            "license": "https://edg.epa.gov/EPA_Data_License.htm",
             "spatial": "-180.0,18.0,-66.0,72.0",
-            "dataQuality": false
+            "title": "Unregulated Contaminant Monitoring Program Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unregulated Contaminant Monitoring Rule 3 (UCMR 3), (2013-2015) Occurrence Data",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The third Unregulated Contaminant Monitoring Rule (UCMR 3), conducted under EPA oversight, was published in the Federal Register on May 2, 2012. UCMR 3 requires monitoring for 30 contaminants: 28 chemicals and 2 viruses.",
+            "identifier": "{C590EF66-7551-4959-BFE1-1D37D329A517}",
+            "issued": "2014-01-01",
             "keyword": [
                 "unregulated contaminants",
                 "contaminants",
@@ -24261,38 +24272,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2012-05-02",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{C590EF66-7551-4959-BFE1-1D37D329A517}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BC590EF66-7551-4959-BFE1-1D37D329A517%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BC590EF66-7551-4959-BFE1-1D37D329A517%7D"
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
+            "title": "Unregulated Contaminant Monitoring Rule 3 (UCMR 3), (2013-2015) Occurrence Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unregulated Contaminant Monitoring Rule 2 (UCMR 2), (2008-2010) Occurrence Data",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Unregulated Contaminant Monitoring Rule supporting the second cycle (UCMR 2) of monitoring, conducted under EPA oversight, was published in the Federal Register on January 4, 2007. The UCMR 2 required monitoring for 25 contaminants using five analytical methods.",
+            "identifier": "{9ADCB4EC-B670-4989-8F1E-1237B510F462}",
+            "issued": "2014-01-01",
             "keyword": [
                 "unregulated contaminants",
                 "contaminants",
@@ -24306,38 +24317,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2007-01-04",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{9ADCB4EC-B670-4989-8F1E-1237B510F462}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B9ADCB4EC-B670-4989-8F1E-1237B510F462%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B9ADCB4EC-B670-4989-8F1E-1237B510F462%7D"
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
+            "title": "Unregulated Contaminant Monitoring Rule 2 (UCMR 2), (2008-2010) Occurrence Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Summary of Annual Beach Notifications",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bill Kramer, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
+                "hasEmail": "mailto:kramer.bill@epa.gov"
+            },
+            "dataQuality": false,
             "description": "To help beachgoers make informed decisions about swimming at U.S. beaches, EPA gathers state-by-state data about beach closings and advisories. Between 1999 and 2012, EPA published a national summary report about the previous year's swimming season data.",
+            "identifier": "{AFC8F1AD-0DF4-496C-842A-1E85FE0462BD}",
+            "issued": "2023-06-22",
             "keyword": [
                 "beach",
                 "swimming",
@@ -24349,38 +24360,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2023-06-22",
-            "issued": "2023-06-22",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bill Kramer, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
-                "hasEmail": "mailto:kramer.bill@epa.gov"
-            },
-            "identifier": "{AFC8F1AD-0DF4-496C-842A-1E85FE0462BD}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7BAFC8F1AD-0DF4-496C-842A-1E85FE0462BD%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BAFC8F1AD-0DF4-496C-842A-1E85FE0462BD%7D"
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
+            "title": "Summary of Annual Beach Notifications"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State National Pollutant Discharge Elimination System (NPDES) Program Withdrawal Petitions",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jackie Clark, U.S. EPA Office of Water (OW) - Office of Wastewater Management (OWM)",
+                "hasEmail": "mailto:clark.jackie@epa.gov"
+            },
+            "dataQuality": false,
             "description": "Search for pending and resolved NPDES withdrawal petitions by state, region, date, or keyword.  \"Pending\" means EPA has received the petition and is working with the state and petitioner to resolve it. \"Withdrew petition\" means that the petitioner has withdrawn the petition they submitted. \"Resolved\" means that EPA has resolved the issues raised in the petition and has denied the petition. \"Partially resolved\" means that EPA has partially denied the petition by resolving some of the issues, while continuing to work with the state and petitioner on other pending issues. \"Program withdrawn\" would apply if, after conducting investigations, EPA withdrew a state's NPDES authority.",
+            "identifier": "{90E487AE-AE70-4692-BA27-D1CCD06C6B55}",
+            "issued": "2014-01-01",
             "keyword": [
                 "ndpes",
                 "permits",
@@ -24393,38 +24404,38 @@
                 "united states",
                 "inlandwaters"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2012-12-12",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Wastewater Management (OWM)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jackie Clark, U.S. EPA Office of Water (OW) - Office of Wastewater Management (OWM)",
-                "hasEmail": "mailto:clark.jackie@epa.gov"
-            },
-            "identifier": "{90E487AE-AE70-4692-BA27-D1CCD06C6B55}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B90E487AE-AE70-4692-BA27-D1CCD06C6B55%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B90E487AE-AE70-4692-BA27-D1CCD06C6B55%7D"
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
+            "title": "State National Pollutant Discharge Elimination System (NPDES) Program Withdrawal Petitions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Six-Year Review Contaminant Occurrence Data",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Safe Drinking Water Act (SDWA) requires EPA to review each National Primary Drinking Water Regulation (NPDWR) at least once every six years and revise them, if appropriate.  The purpose of the review, called the Six-Year Review, is to identify those NPDWRs for which current health effects assessments, changes in technology, and/or other factors provide a health or technical basis to support a regulatory revision that will maintain or strengthen public health protection. To support the national contaminant occurrence and exposure assessments performed under the Six-Year Review process, EPA analyzes SDWA compliance monitoring data from public water supplies for regulated drinking water contaminants.  This analysis allows EPA to characterize the national occurrence of contaminants to help the Agency determine if there may be a meaningful opportunity to improve public health protection.",
+            "identifier": "{616538BA-B7B5-4D4E-B1F8-A5A441F275D1}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "sdwa",
@@ -24439,38 +24450,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2010-03-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{616538BA-B7B5-4D4E-B1F8-A5A441F275D1}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B616538BA-B7B5-4D4E-B1F8-A5A441F275D1%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B616538BA-B7B5-4D4E-B1F8-A5A441F275D1%7D"
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
+            "title": "Six-Year Review Contaminant Occurrence Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "SDWISFED Drinking Water Data",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "SDWIS/FED is EPA's national regulatory compliance database for the drinking water program. It includes information on the nation's 160,000 public water systems and violations of drinking water regulations. Access aggregated information on all violations reported in an EPA region, state, and county since 1993 using the MS Excel PivotTables. These multidimensional tables contain aggregated information on water systems; violations reported by violation type and by contaminant/rule, and GPRA data, for each year since 1993; and current Envirofacts data. Sort, categorize, and analyze the data across several dimensions.",
+            "identifier": "{10CF7CDC-83C5-46FF-8581-342DD8ADE202}",
+            "issued": "2014-01-01",
             "keyword": [
                 "pwss",
                 "drinking water",
@@ -24484,38 +24495,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2014-10-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{10CF7CDC-83C5-46FF-8581-342DD8ADE202}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B10CF7CDC-83C5-46FF-8581-342DD8ADE202%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B10CF7CDC-83C5-46FF-8581-342DD8ADE202%7D"
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
+            "title": "SDWISFED Drinking Water Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National List of Beaches",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bill Kramer, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
+                "hasEmail": "mailto:kramer.bill@epa.gov"
+            },
+            "dataQuality": false,
             "description": "EPA has published a list of coastal recreation waters adjacent to beaches (or similar points of access) used by the public in the U.S.  The list, required by the Beaches Environmental Assessment and Coastal Health Act (BEACH Act), identifies waters that are subject to a state beach water quality monitoring and public notification program consistent with the National Beach Guidance and Required Performance Criteria for BEACH Act Grants.",
+            "identifier": "{F1EA07EA-7243-49F1-A50E-682B90DF4741}",
+            "issued": "2014-01-01",
             "keyword": [
                 "beaches",
                 "recreation",
@@ -24525,38 +24536,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2013-02-13",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bill Kramer, U.S. EPA Office of Water (OW) - Office of Science and Technology (OST)",
-                "hasEmail": "mailto:kramer.bill@epa.gov"
-            },
-            "identifier": "{F1EA07EA-7243-49F1-A50E-682B90DF4741}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7BF1EA07EA-7243-49F1-A50E-682B90DF4741%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7BF1EA07EA-7243-49F1-A50E-682B90DF4741%7D"
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
+            "title": "National List of Beaches"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Drinking Water State Revolving Fund",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The Drinking Water State Revolving Fund (DWSRF) National Information Management System collects information that provide a record of progress and accountability for the program.  Reports on DWSRF activity are currently available for state fiscal years (July-June) 1996 through 2010.",
+            "identifier": "{1A9B6384-B900-4E31-A6B1-16FC45402E16}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "srf",
@@ -24569,38 +24580,38 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2009-07-30",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{1A9B6384-B900-4E31-A6B1-16FC45402E16}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B1A9B6384-B900-4E31-A6B1-16FC45402E16%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B1A9B6384-B900-4E31-A6B1-16FC45402E16%7D"
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
+            "title": "Drinking Water State Revolving Fund"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Drinking Water Maximum Contaminant Levels (MCLs)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "National Primary Drinking Water Regulations (NPDWRs or primary standards) are legally enforceable standards that apply to public water systems. Primary standards protect public health by limiting the levels of contaminants in drinking water.",
+            "identifier": "{801C993D-B195-4B7A-97B6-17B299ED1E95}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "sdwa",
@@ -24614,38 +24625,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2009-05-01",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{801C993D-B195-4B7A-97B6-17B299ED1E95}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B801C993D-B195-4B7A-97B6-17B299ED1E95%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B801C993D-B195-4B7A-97B6-17B299ED1E95%7D"
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
+            "title": "Drinking Water Maximum Contaminant Levels (MCLs)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Distribution (State Allotment) of Drinking Water State Revolving Fund Appropriation from the American Recovery and Reinvestment Act of 2009 (ARRA)",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "The ARRA appropriation for the DWSRF program is $2,000,000,000. DWSRF allotments are based on percentages derived from the 2003 Drinking Water Infrastructure Needs Survey. For general and government-wide ARRA information, please visit EPA's Recovery site or RECOVERY.gov. This ARRA appropriation is in addition to the DWSRF appropriation for FY 2009",
+            "identifier": "{2CE25440-7393-406C-B21E-45D378344FB2}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "arra",
@@ -24661,38 +24672,38 @@
                 "united states",
                 "environment"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2009-07-29",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline, U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{2CE25440-7393-406C-B21E-45D378344FB2}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B2CE25440-7393-406C-B21E-45D378344FB2%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B2CE25440-7393-406C-B21E-45D378344FB2%7D"
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
+            "title": "Distribution (State Allotment) of Drinking Water State Revolving Fund Appropriation from the American Recovery and Reinvestment Act of 2009 (ARRA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Contaminant Candidate List 3",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "CCL 3 is a list of contaminants that are currently not subject to any proposed or promulgated national primary drinking water regulations, that are known or anticipated to occur in public water systems, and which may require regulation under the Safe Drinking Water Act (SDWA). The list includes, among others, pesticides, disinfection byproducts, chemicals used in commerce, waterborne pathogens, pharmaceuticals, and biological toxins. The Agency considered the best available data and information on health effects and occurrence to evaluate thousands of unregulated contaminants. EPA used a multi-step process to select 116 candidates for the final CCL 3. The final CCL 3 includes 104 chemicals or chemical groups and 12 microbiological contaminants.",
+            "identifier": "{756BBB59-7208-459A-A008-C64107182AAC}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "sdwa",
@@ -24707,38 +24718,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2009-10-08",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{756BBB59-7208-459A-A008-C64107182AAC}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B756BBB59-7208-459A-A008-C64107182AAC%7D",
                 "https://edg.epa.gov/metadata/rest/document?id=%7B756BBB59-7208-459A-A008-C64107182AAC%7D"
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
+            "title": "Contaminant Candidate List 3"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Contaminant Candidate List 2",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
             "description": "CCL 2 is a list of contaminants that are currently not subject to any proposed or promulgated national primary drinking water regulations, that are known or anticipated to occur in public water systems, and which may require regulation under the Safe Drinking Water Act (SDWA). The list includes, among others, pesticides, disinfection byproducts, chemicals used in commerce, waterborne pathogens, pharmaceuticals, and biological toxins. The Agency considered the best available data and information on health effects and occurrence to evaluate thousands of unregulated contaminants.",
+            "identifier": "{479F758A-F9B6-4330-9E0F-933822232A28}",
+            "issued": "2014-01-01",
             "keyword": [
                 "drinking water",
                 "sdwa",
@@ -24753,38 +24764,38 @@
                 "united states",
                 "health"
             ],
+            "license": "https://edg.epa.gov/EPA_Data_License.html",
             "modified": "2005-02-24",
-            "issued": "2014-01-01",
+            "programCode": [
+                "020:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. EPA Office of Water (OW) - Office of Ground Water and Drinking Water (OGWDW)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Safe Drinking Water Hotline",
-                "hasEmail": "mailto:safewater@epa.gov"
-            },
-            "identifier": "{479F758A-F9B6-4330-9E0F-933822232A28}",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
             "references": [
                 "https://edg.epa.gov/metadata/rest/document?id=%7B479F758A-F9B6-4330-9E0F-933822232A28%7D",
                 "https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid=%7B479F758A-F9B6-4330-9E0F-933822232A28%7D"
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
+            "title": "Contaminant Candidate List 2"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Contaminant Candidate List 1",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "020:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Safe Drinking Water Hotline",
+                "hasEmail": "mailto:safewater@epa.gov"
+            },
+            "dataQuality": false,
```

